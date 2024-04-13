-- migrate:up
CREATE TABLE "role"
(
   id integer generated always as identity primary key,
   name varchar not null,
   created_at timestamp not null default CURRENT_TIMESTAMP

);

-- migrate:down
DROP TABLE "role"