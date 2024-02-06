-- Add migration script here
CREATE TABLE subjects (
  id uuid PRIMARY KEY,
  name varchar,
  assistant_id varchar,
  owner uuid,
  created_at timestamptz
);

CREATE TABLE users (
  id uuid PRIMARY KEY,
  email varchar unique,
  username varchar,
  active boolean,
  hashed_password varchar,
  role varchar,
  created_at timestamptz
);

CREATE TABLE threads (
  id uuid PRIMARY KEY,
  thread_id varchar,
  subject_id uuid,
  created_at timestamptz
);

-- ALTER TABLE subjects ADD FOREIGN KEY (ownwer) REFERENCES users (id);

ALTER TABLE threads ADD FOREIGN KEY (subject_id) REFERENCES subjects (id);