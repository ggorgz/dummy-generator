from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel


class PostgresSettings(BaseSettings):
    ENGINE: str = "django.db.backends.postgresql"
    NAME: str
    HOST: str
    PORT: str
    USER: str
    PASSWORD: str
    model_config: SettingsConfigDict = SettingsConfigDict(
        env_prefix="POSTGRES_",
        case_sensitive=True,
        env_file=".env",
        env_file_encoding="utf-8",
    )


class Databases(BaseModel):
    default: PostgresSettings

    @classmethod
    def build_model(cls, **kwargs):
        return cls(default=PostgresSettings(), **kwargs)

    @classmethod
    def build_model_dict(cls, **kwargs):
        return cls.build_model(**kwargs).model_dump()
