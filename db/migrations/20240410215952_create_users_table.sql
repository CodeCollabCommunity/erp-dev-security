-- migrate:up
CREATE TABLE "user"
(
   id integer generated always as identity primary key,
   email varchar(255) not null,
   password varchar(255) not null,
   role_id integer, 
   created_at timestamp not null default CURRENT_TIMESTAMP,
   updated_at timestamp not null default CURRENT_TIMESTAMP

);

-- migrate:down
DROP TABLE "user"