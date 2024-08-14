

from config.api_doc_config import ApiDocConfig
from config.db_config import DbConfig
from config.jwt_config import JwtConfig


class Config(ApiDocConfig, DbConfig, JwtConfig):
    PROPAGATE_EXCEPTIONS = True
