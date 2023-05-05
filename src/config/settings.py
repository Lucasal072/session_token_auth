from src.config.mongo_config import ConfigurationMongoDB

mongo_config = ConfigurationMongoDB

EXPIRATION_SESSION_TOKEN_IN_SECONDS = 3600
DEBUG = True
MONGO_URI = f'mongodb://{mongo_config.host}:{mongo_config.port}/{mongo_config.database}'