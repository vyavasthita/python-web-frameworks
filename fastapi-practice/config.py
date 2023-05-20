from pydantic import BaseSettings


class Settings(BaseSettings):
    api_host: str
    api_port: int
    reload: bool = False

settings = Settings()