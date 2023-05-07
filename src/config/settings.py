from src.config.mongo_config import ConfigurationMongoDB
from src.config.redis_config import RedisConfig



mongo_config = ConfigurationMongoDB
redis_config = RedisConfig


EXPIRATION_SESSION_TOKEN_IN_SECONDS = 3600
DEBUG = True
MONGO_URI = f'mongodb://{mongo_config.host}:{mongo_config.port}/{mongo_config.database}'