from functools import lru_cache
from dynaconf import Dynaconf
from pydantic_settings import BaseSettings
from typing import List

import logging

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
        env_name=dynaconf_settings.get("ENV_FOR_DYNACONF", "production"),
        debug=dynaconf_settings.get("debug", False),
        log_level=dynaconf_settings.get("log_level", 'INFO'),
        DJANGO_DEBUG=dynaconf_settings.get("DJANGO_DEBUG", False),
        DJANGO_SECRET_KEY=dynaconf_settings.get("DJANGO_SECRET_KEY", '!There is no DJANGO_SECRET_KEY in settings files! Check it!'),
        DJANGO_ALLOWED_HOSTS=dynaconf_settings.get("DJANGO_ALLOWED_HOSTS", ['!There is no DJANGO_ALLOWED_HOSTS in settings files! Check it!'])
    )

    log_format = '[%(name)s] %(levelname)s: %(message)s' if result.env_name != 'production' else '%(asctime)s [%(name)s] %(levelname)s: %(message)s'
    logging.basicConfig(
        format=log_format,
        datefmt='%d-%b-%y %H:%M:%S',
        level=getattr(logging, result.log_level.upper(), logging.INFO)
    )

    logger = logging.getLogger(__name__)

    logger.info(f'Loading settings for: {result.env_name}')
    logger.info(f'  debug: {result.debug}')
    logger.info(f'  log_level: {result.log_level}')
    logger.info(f'  DJANGO_DEBUG: {result.DJANGO_DEBUG}')
    logger.info(f'  DJANGO_SECRET_KEY: {result.DJANGO_SECRET_KEY}')
    logger.info(f'  DJANGO_ALLOWED_HOSTS: {result.DJANGO_ALLOWED_HOSTS}')

    # print(f'Loading settings for: {result.env_name}')
    # print(f'  debug: {result.debug}')
    # print(f'  log_level: {result.log_level}')
    # print(f'  DJANGO_DEBUG: {result.DJANGO_DEBUG}')
    # print(f'  DJANGO_SECRET_KEY: {result.DJANGO_SECRET_KEY}')
    # print(f'  DJANGO_ALLOWED_HOSTS: {result.DJANGO_ALLOWED_HOSTS}')

    logger.setLevel(result.log_level)

    return result

if __name__ == '__main__':
    settings = get_settings()
