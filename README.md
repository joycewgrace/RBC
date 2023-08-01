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

![du](https://github.com/joycewgrace/RBC/assets/141069257/de96e693-fe80-42cc-a522-fa8df012fb9b)

**Step 6**

Save the below Python script (script of the python function that retrieves client details) into the local machine.

https://github.com/joycewgrace/RBC/blob/main/Scripts/RBC_Client_Credentials_Retrieval.py

Call the script as shown below: Client_Id as argument

```
python3 RBC_Client_Credentials_Retrieval.py 1
```
![Retrieval](https://github.com/joycewgrace/RBC/assets/141069257/63341bb7-f0b0-4831-b95a-391ee7b0e3e5)


**Step 7**

Save the below Python script (script of the python function that updates client details) into the local machine.

https://github.com/joycewgrace/RBC/blob/main/Scripts/RBC_Client_Credentials_Update.py

Call the script and enter values for prompts as shown below: Client_Id as argument

```
python3 RBC_Client_Credentials_Update.py 1
```
![Update](https://github.com/joycewgrace/RBC/assets/141069257/eef79474-5167-42ed-b64f-1c00fa13aa53)
</ul>
</details>
<details>
<summary>Issues Faced</summary>
<ul>

**1) File data copy**

_Error:
SQL Error [42501]: ERROR: must be superuser or have privileges of the pg_read_server_files role to COPY from a file
Hint: Anyone can COPY to stdout or from stdin. psql's \copy command also works for anyone._

**Solution:**
```
grant pg_read_server_files to sqluser;
```

**2) File permission**

_Error: 
Permission denied 
HINT: COPY FROM instructs the PostgreSQL server process to read a file. You may want a client-side facility such as psql's \copy. SQL state: 42501_

**Solution:**
Go to Properties of that particular file by right clicking on it. Then, go to Security tab of the displayed Properties dialog box. 
Click on Edit option. Permissions dialog box appears, then click on Add button. Type 'Everyone' (without apostrophes) in the "Enter the object names to select" description box and click on OK button. 
Then, make sure all the checkboxes of "Permissions for Everyone" are selected by just ticking the "Full Control" check box to allow the control access without any restriction.
Then, Apply and OK all the tabs to apply all the changes done.

**3)Data issue - comma**

_Error:
SQL Error [22P04]: ERROR: extra data after last expected column
Where: COPY client_credentials, line 18: "16,Kristin, Sanders,!4lZ5%m4,bellmichael@example.org,2021-03-16 08:49:42"_

**Solution:**
Removed ","(comma) from the clientname column(Kristin, Sanders)
  
**4) Encrypt column - bytea**

_Faced issue while decrypting the encrypted columns_

**Solution:**
Encrypted columns need to be stored in bytea data type instead of varchar.

</ul>
</details>

<details>
<summary>Handling Encryption key</summary>
<ul>
In this solution, I have given the Encryption key as an environment variable, but in case of Enterprise level solution, we can have the vaiable in an environment file, and assign only the execute permission to the python job/business user similar to the below:
  
![CHmod](https://github.com/joycewgrace/RBC/assets/141069257/efe747ad-11fc-4d13-b7db-20eb5b22270d)

</ul>
</details>

</ul>
</details>
