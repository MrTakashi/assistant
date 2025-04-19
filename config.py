from functools import lru_cache
from dynaconf import Dynaconf
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    env_name: str
    debug: bool
    DJANGO_DEBUG: bool


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
        env_name=dynaconf_settings.get("env_name", "default"),
        debug=dynaconf_settings.get("debug", False),
        DJANGO_DEBUG=dynaconf_settings.get("DJANGO_DEBUG", False),
    )

    print(f'Loading settings for: {result.env_name}')
    print(f'  debug: {result.debug}')
    print(f'  DJANGO_DEBUG: {result.DJANGO_DEBUG}')

    return result

if __name__ == '__main__':
    settings = get_settings()
