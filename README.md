# erp-dev-security

ERP security module

## Installation

- Docker installed on your machine ([Install Docker](https://docs.docker.com/get-docker/))

- Python virtual env
1. Open a terminal and create with:
    ```bash
    pyenv virtaulenv 3.12.2 env-name 
    ```
2. Install dependencies from requirements.txt
    ```bash
    cd erp-dev-security-1
    pyenv activate env-name
    pip install -r requirements.txt
    pip install --upgrade pip
    ```
    Replace `env-name` with your desired virtual env name.

## Environment Variables

Add and set .env with vars to use database:

#### Set Database credentials
- `APP_ENVIRONMENT`: development.
- `DB_PORT`: Port of postgresql database (5432).
- `DB_HOST`: Host of database.
- `DB_USER`: User of database.
- `DB_PASSWORD`: Password of database.
- `DB_NAME`: Name of database.


#### Set for postgresql database docker image
- `POSTGRES_DB="{DB_NAME}"`
- `POSTGRES_USER="{DB_USER}"`
- `POSTGRES_PASSWORD="{DB_PASSWORD}"`

#### Set postgresql database uri
- `DATABASE_URL="postgresql://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}"`

#### Set bearer vars
- `AUTH_SECRET_KEY=your-secret-key`
- `AUTH_ALGORITHM=your-algorithm`
- `ACCESS_TOKEN_EXPIRE_MINUTES=token-expiration`

#### Set docker image name
- `IMAGE_NAME=your-img-name`

## Building the Docker containers

Follow the next steps to build the python and db containers:

1. Open a terminal.
2. Navigate to the directory of the project.
3. Run the following command:

    ```bash
    docker compose build --no-cache
    docker compose up -d 
    ```

    You can remove flag `-d` to show in terminal logs while container is running.

Now you can run the api on your localhost: http://localhost:55

Test
