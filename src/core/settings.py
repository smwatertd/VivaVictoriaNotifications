from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    name: str = 'notifications'
    host: str = '0.0.0.0'
    port: int = 8000

    model_config = SettingsConfigDict(
        env_file='.env',
        env_prefix='APP_',
    )


app_settings = AppSettings()
