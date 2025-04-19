from functools import lru_cache
from dynaconf import Dynaconf
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    env_name: str
    debug: bool
    log_level: str

    DJANGO_DEBUG: bool
    DJANGO_SECRET_KEY: str
    DJANGO_ALLOWED_HOSTS: List[str] = []

@lru_cache()
def get_settings() -> Settings:
    dynaconf_settings = Dynaconf(
        settings_files=[
            'config/.secrets.toml',
            'config/settings.toml',
        ],
        environments=True,
        load_dotenv=False,
        envvar_prefix="DYNACONF",
        env_switcher="ENV_FOR_DYNACONF",
    )

    result = Settings(
        env_name=dynaconf_settings.get("env_name", "production"),
        debug=dynaconf_settings.get("debug", False),
        log_level=dynaconf_settings.get("log_level", 'INFO'),
        DJANGO_DEBUG=dynaconf_settings.get("DJANGO_DEBUG", False),
        DJANGO_SECRET_KEY=dynaconf_settings.get("DJANGO_SECRET_KEY", '!There is no DJANGO_SECRET_KEY in settings files! Check it!'),
        DJANGO_ALLOWED_HOSTS=dynaconf_settings.get("DJANGO_ALLOWED_HOSTS", ['!There is no DJANGO_ALLOWED_HOSTS in settings files! Check it!'])
    )

    print(f'Loading settings for: {result.env_name}')
    print(f'  debug: {result.debug}')
    print(f'  log_level: {result.log_level}')
    print(f'  DJANGO_DEBUG: {result.DJANGO_DEBUG}')
    print(f'  DJANGO_SECRET_KEY: {result.DJANGO_SECRET_KEY}')
    print(f'  DJANGO_ALLOWED_HOSTS: {result.DJANGO_ALLOWED_HOSTS}')

    return result

if __name__ == '__main__':
    settings = get_settings()
