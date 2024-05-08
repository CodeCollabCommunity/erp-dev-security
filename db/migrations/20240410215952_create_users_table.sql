-- migrate:up
CREATE TABLE "user"
(
   id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
   email varchar(255) not null,
   password varchar(255) not null,
   role_id UUID,
   created_at timestamp not null default CURRENT_TIMESTAMP,
   updated_at timestamp not null default CURRENT_TIMESTAMP

);

-- migrate:down
DROP TABLE "user"