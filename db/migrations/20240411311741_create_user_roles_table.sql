-- migrate:up
CREATE TABLE "user_role"
(
   id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
   user_id UUID not null,
   role_id UUID not null,
   created_at timestamp not null default CURRENT_TIMESTAMP,

   CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES "user"(id) ON DELETE CASCADE,
   CONSTRAINT fk_role_id FOREIGN KEY (role_id) REFERENCES "role"(id) ON DELETE CASCADE

);

-- migrate:down
DROP TABLE "user_role"