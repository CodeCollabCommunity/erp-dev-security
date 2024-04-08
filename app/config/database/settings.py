"""
Settings for database connections
"""
from app.config.common import AppSettings


class DatabaseSettings(AppSettings):
    """
    Database settings
    """
    host: str = "172.23.0.2"
    port: int = 27017
    password: str = "pass"
    user: str = "user"
    name: str = "security"

    @property
    def mongodb_uri(self):
        """
        Return the postgres uri
        """
        return self.database_url

    @property
    def database_url(self):
        """
        Return the database url
        """
        return f"mongodb://{self.host}:{self.port}/{self.name}"

    class Config:
        """ Subclasses of Config to set prefix """
        env_prefix = "db_"
