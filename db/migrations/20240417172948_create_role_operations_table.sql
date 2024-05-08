-- migrate:up
CREATE TABLE "role_operation"
(
   id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
   name varchar not null,
   module varchar not null,
   role_id UUID not null,

   CONSTRAINT fk_role_id FOREIGN KEY (role_id) REFERENCES "role"(id) ON DELETE CASCADE

);

-- migrate:down
DROP TABLE "role_operation"