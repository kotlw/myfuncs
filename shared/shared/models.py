from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    my_env_var: str
