<details>
<summary>RBC Data Engineer Assigment</summary>
<ul>
<details>
<summary>Steps</summary>
<ul>
  
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


Once the above set up is completed, you can list the users and check if proper roles are assigned.

![image](https://github.com/joycewgrace/RBC/assets/141069257/a22a0050-316b-4e04-8b2a-0eebf36b0bb3)

**Step 6**

Save the below Python script (script of the python function that retrieves client details) into the local machine.

https://github.com/joycewgrace/RBC/blob/main/Scripts/RBC_Client_Credentials_Retrieval.py

Call the script as shown below: Client_Id as argument

```
python3 RBC_Client_Credentials_Retrieval.py 1
```
![image](https://github.com/joycewgrace/RBC/assets/141069257/fe1194fa-d8ef-4b1e-98dd-9c06c03f4a72)


**Step 7**

Save the below Python script (script of the python function that updates client details) into the local machine.

https://github.com/joycewgrace/RBC/blob/main/Scripts/RBC_Client_Credentials_Update.py

Call the script and enter values for prompts as shown below: Client_Id as argument

```
python3 RBC_Client_Credentials_Update.py 1
```
![image](https://github.com/joycewgrace/RBC/assets/141069257/6fa91a94-0b70-413f-bd4f-1d270ecfc8b9)
</ul>
</details>
<details>
<summary>Issues Faced</summary>
<ul>

**1) File data copy**

Error:
SQL Error [42501]: ERROR: must be superuser or have privileges of the pg_read_server_files role to COPY from a file
Hint: Anyone can COPY to stdout or from stdin. psql's \copy command also works for anyone.

Solution:
```
grant pg_read_server_files to sqluser;
```

**2) File permission**

Error: 
Permission denied 
HINT: COPY FROM instructs the PostgreSQL server process to read a file. You may want a client-side facility such as psql's \copy. SQL state: 42501

Solution:

Go to Properties of that particular file by right clicking on it. Then, go to Security tab of the displayed Properties dialog box. 
Click on Edit option. Permissions dialog box appears, then click on Add button. Type 'Everyone' (without apostrophes) in the "Enter the object names to select" description box and click on OK button. 
Then, make sure all the checkboxes of "Permissions for Everyone" are selected by just ticking the "Full Control" check box to allow the control access without any restriction.
Then, Apply and OK all the tabs to apply all the changes done.

**3)Data issue - comma**

Error:
SQL Error [22P04]: ERROR: extra data after last expected column
Where: COPY client_credentials, line 18: "16,Kristin, Sanders,!4lZ5%m4,bellmichael@example.org,2021-03-16 08:49:42"

Solution:

Removed ","(comma) from the clientname column(Kristin, Sanders)
  
**4) Encrypt column - bytea**

Faced issue while decrypting the encrypted columns 

Solution:

Encrypted columns need to be stored in bytea data type instead of varchar.

</ul>
</details>

<details>
<summary>Handling Encryption key</summary>
<ul>
In this solution, I have given the Encryption key as an environment variable, but in case of Enterprise level solution, we can have the vaiable in an environment file, and assign only the execute permission to the python job/business user similar to the below:
  
[![image](https://github.com/joycewgrace/RBC/assets/141069257/e690d23b-42e5-46a8-adf0-581007aa2631)](https://imgur.com/a/usfjp6x)

</ul>
</details>

</ul>
</details>
