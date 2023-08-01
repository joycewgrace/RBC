**Step 1**

PostgreSQL installation - follow the below link to install latest PostgreSQL on windows 

https://www.postgresql.org/download/windows/

**Step 2**

On PostgreSQL command prompt- execute the below script to create a DBadmin

https://github.com/joycewgrace/RBC/blob/main/SQL/DDL/User/dbAdmin.sql

**Step 3**

Log in as dbAdmin and execute the below scripts to create an sqluser and the ClientDB database

https://github.com/joycewgrace/RBC/blob/main/SQL/DDL/User/sqluser.sql
https://github.com/joycewgrace/RBC/blob/main/SQL/DDL/User/Database/ClientDB.sql

**Step 4**

Log in as sqluser and execute the below scripts to create the client_credentials_load and client_credentials tables

https://github.com/joycewgrace/RBC/blob/main/SQL/DDL/Table/client_credentials_load.sql
https://github.com/joycewgrace/RBC/blob/main/SQL/DDL/Table/client_credentials.sql

**Step 5**

Execute the below scripts to copy the data file into client_credentials_load table and encrypt the neccessary data into client_credentials table

https://github.com/joycewgrace/RBC/blob/main/SQL/DML/client_credentials_load.sql
https://github.com/joycewgrace/RBC/blob/main/SQL/DML/client_credentials.sql

**Step 9**

Save the below Python script (script of the python function that retrieves client details) into the local machine.

https://github.com/joycewgrace/RBC/blob/main/Scripts/RBC_Client_Credentials_Retrieval.py

Call the script as shown below: 

1st argument - Client_Id

2nd argument - Security_Key

![image](https://github.com/joycewgrace/RBC/assets/141069257/ddd4760e-f434-466a-93c8-1e819fb2ba57)

**Step 10**

Save the below Python script (script of the python function that updates client details) into the local machine.

https://github.com/joycewgrace/RBC/blob/main/Scripts/RBC_Client_Credentials_Update.py

Call the script and enter values for prompts as shown below: 

Argument - Client_Id

![image](https://github.com/joycewgrace/RBC/assets/141069257/0d70e645-daa7-4d5e-9827-858f15651de4)







