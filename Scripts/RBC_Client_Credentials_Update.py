import sys
import psycopg2
import os


# This function will update a specific client's details 
def update_clientdetails(client_id, field_to_update, new_value, encryption_key):
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
        return False

    # Update the specified client details for the specified client_id
    query = f"""
        UPDATE clientschema.client_credentials
        SET encrypted_{field_to_update} = pgp_sym_encrypt(%s, %s)
        WHERE client_id = %s
    """

    # Executing the above query to update the encrypted field
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, (new_value, encryption_key, client_id))
            connection.commit()
    except Exception as exp:
        print("Error: Query execution failed.")
        print(exp)
        connection.rollback()
        connection.close()
        return False


    connection.close()
    return True

# Main
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Argument list invalid>")
        sys.exit(1)

    client_id_to_update = int(sys.argv[1])
    field_to_update = input("Enter the field to update (e.g., clientname, password, email): ")
    new_value = input("Enter the new value: ")
    encryption_key = os.environ.get("ENCRYPTION_KEY")

    success = update_clientdetails(client_id_to_update, field_to_update, new_value, encryption_key)

    if success:
        print("Client field updated successfully.")
    else:
        print("Failed to update client field.")
