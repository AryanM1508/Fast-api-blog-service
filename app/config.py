from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int  # ✅ matches .env


    class Config:
        env_file = ".env"

settings= Settings()