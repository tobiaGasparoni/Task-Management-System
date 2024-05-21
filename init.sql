CREATE TABLE users (
	user_pk SERIAL primary key,
	first_name VARCHAR(50) not null,
	last_name VARCHAR(50) not null,
	email VARCHAR(50) not null unique,
	password VARCHAR(500) not null,
	created_at TIMESTAMP not null default NOW(),
	updated_at TIMESTAMP not null default NOW()
);

CREATE TABLE tasks (
	task_pk SERIAL primary key,
	title VARCHAR(255) not null,
	description VARCHAR(1000) not null,
	status VARCHAR(50) not null default 'TO DO',
	deleted INT not null default 0,
	user_fk BIGINT not null,
	created_at TIMESTAMP not null default NOW(),
	updated_at TIMESTAMP not null default NOW()
);