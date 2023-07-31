--delete from clientSchema.client_credentials;
insert into clientSchema.client_credentials
SELECT client_id, 
created_on,
pgp_sym_encrypt(clientname, 'RBC$Security') as encrypted_clientname,
pgp_sym_encrypt(password, 'RBC$Security') as encrypted_password,
pgp_sym_encrypt(email, 'RBC$Security') as encrypted_email
from clientSchema.client_credentials_load
