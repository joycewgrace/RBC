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





