import sys
import psycopg2
import os

# This function will retrieve the client details using the client_id and encryption key
def retrieve_clientdetails(client_id, encryption_key):
    # Connection details for the PostgreSQL database
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="clientdb",
            user="sqluser",
            password="pwd4sqluser"
        )
    except Exception as exp:
        print("Error: Unable to connect to the database.")
        print(exp)
        return None



    # Retrieve the client details using the client_id
    query = """
        SELECT
            pgp_sym_decrypt(encrypted_clientname::bytea, %s) AS clientname,
            pgp_sym_decrypt(encrypted_password::bytea, %s) AS password,
            pgp_sym_decrypt(encrypted_email::bytea, %s) AS email,
            created_on AS created_on
        FROM clientschema.client_credentials
        WHERE client_id = %s
    """

    # Executing the above query to fetch the decrypted data from the database
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, (encryption_key, encryption_key, encryption_key, client_id))
            decrypted_data = cursor.fetchone()
    except Exception as exp:
        print("Error: Query execution failed.")
        print(exp)
        connection.close()
        return None


    # Return the decrypted client details
    connection.close()
    return {
        "clientname": decrypted_data[0],
        "password": decrypted_data[1],
        "email": decrypted_data[2],
        "created_on": decrypted_data[3]
    }

# Main
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Argument list invalid")
        sys.exit(1)
    
    encryption_key = os.environ.get("ENCRYPTION_KEY")
    client_id = int(sys.argv[1])

    retrieved_client_details = retrieve_clientdetails(client_id, encryption_key)

    if retrieved_client_details:
        print("Client Details:")
        print("Client ID:", client_id)
        print("Client Name:", retrieved_client_details["clientname"])
        print("Password:", retrieved_client_details["password"])
        print("Email:", retrieved_client_details["email"])
        print("Created On:",retrieved_client_details["created_on"])
