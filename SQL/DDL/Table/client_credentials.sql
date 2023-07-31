-- Drop table

-- DROP TABLE clientschema.client_credentials;

CREATE TABLE clientschema.client_credentials (
	client_id serial4 NOT NULL,
	created_on timestamp NOT NULL,
	encrypted_clientname bytea NULL,
	encrypted_password bytea NULL,
	encrypted_email bytea NULL,
	CONSTRAINT client_credentials_pkey PRIMARY KEY (client_id)
);
