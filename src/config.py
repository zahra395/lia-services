from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    MONGO_CONNECTION_STRING: str = "mongodb://mongodb:27017"
    MONGO_DATABASE: str = "MarketDB"
    ORIGINS: str = "*"
    VERSION: str = "0.0.1"
    SWAGGER_TITLE: str = "Lia Service"


settings = Setting()
