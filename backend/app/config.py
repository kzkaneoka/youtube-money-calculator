import os
from typing import List, Type

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    CONFIG_NAME = "base"
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
    DEVELOPER_KEY = os.environ["DEVELOPER_KEY"]
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"


class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = "dev"
    DEBUG = True
    TESTING = False


class TestingConfig(BaseConfig):
    CONFIG_NAME = "test"
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    CONFIG_NAME = "prod"
    DEBUG = False
    TESTING = False


EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig,
    TestingConfig,
    ProductionConfig
]

config_names = {config.CONFIG_NAME: config for config in EXPORT_CONFIGS}
