import dotenv

from functools import lru_cache
from typing import Type, TypeVar

from pydantic_settings import BaseSettings, SettingsConfigDict

Tsettings = TypeVar("Tsettings", bound=BaseSettings)

@lru_cache
def get_settings(cls: Type[Tsettings]) -> Tsettings:
    dotenv.load_dotenv()
    return cls()


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(str_strip_whitespace=True, env_prefix="database_")

    host: str
    port: int
    user: str
    password: str
    name: str
    
    @property
    def url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"

class JWTSettings(BaseSettings):
    model_config = SettingsConfigDict(str_strip_whitespace=True, env_prefix="jwt_")
    
    secret_key: str
    algorithm: str
