-- migrate:up
CREATE TABLE "role"
(
   id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
   name varchar not null,
   created_at timestamp not null default CURRENT_TIMESTAMP

);

-- migrate:down
DROP TABLE "role"