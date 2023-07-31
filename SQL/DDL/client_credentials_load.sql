-- Drop table

-- DROP TABLE clientschema.client_credentials_load;

CREATE TABLE clientschema.client_credentials_load (
	client_id serial4 NOT NULL,
	clientname varchar(50) NOT NULL,
	"password" varchar(50) NOT NULL,
	email varchar(255) NOT NULL,
	created_on timestamp NOT NULL,
	CONSTRAINT client_credentials_load_pkey PRIMARY KEY (client_id)
);
