-- migrate:up
CREATE TABLE "role_operation"
(
   id integer generated always as identity primary key,
   name varchar not null,
   module varchar not null,
   role_id integer not null,

   CONSTRAINT fk_role_id FOREIGN KEY (role_id) REFERENCES "role"(id) ON DELETE CASCADE

);

-- migrate:down
DROP TABLE "role_operation"