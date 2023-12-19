from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    name: str = 'notifications'
    host: str = '0.0.0.0'
    port: int = 8000

    model_config = SettingsConfigDict(
        env_file='.env',
        env_prefix='APP_',
    )


class MessageBrokerSettings(BaseSettings):
    host: str = 'localhost'
    port: int = 5672
    virtual_host: str = '/'
    exchange: str = 'notifications'

    model_config = SettingsConfigDict(
        env_file='.env',
        env_prefix='MESSAGE_BROKER_',
    )


app_settings = AppSettings()
message_broker_settings = MessageBrokerSettings()
