import dotenv
import os

from typing import Any, Union

CONFIG_BOT_TOKEN = "MY_BOT_TOKEN"
CONFIG_VERSION = "VERSION"
MONGO_CONNECTION_STRING = "MONGO_CONNECT"

# set during runtime
CONFIG_STARTUP_TIME = "RUNTIME_STARTUP_TIME"

config = {
    **dotenv.dotenv_values(".env"), # load local variables
    **os.environ # override loaded variables above with os environment variables (os env vars take precedence)
}


def get(key: str, default: Any = None) -> Union[Any, None]:
    return config.get(key, default)


def set(key: str, value: Any):
    config[key] = value