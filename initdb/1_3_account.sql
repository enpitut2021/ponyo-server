CREATE TABLE accounts (
    id TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL DEFAULT '',
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL DEFAULT '',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT current_timestamp,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT current_timestamp,
    CONSTRAINT user_pkey PRIMARY KEY(id)
);
INSERT INTO accounts(id, email)
VALUES('example-user-id', 'hoge@example.com');
