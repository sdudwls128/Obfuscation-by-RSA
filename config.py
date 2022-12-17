# config.py
import obfuscation
import deobfuscation


class Config:
    APP_NAME = obfuscation.encrypt('myapp')
    SECRET_KEY = obfuscation.encrypt('secret-key-of-myapp')
    ADMIN_NAME = obfuscation.encrypt('administrator')

    AWS_DEFAULT_REGION = obfuscation.encrypt('ap-northeast-2')

    STATIC_PREFIX_PATH = obfuscation.encrypt('static')
    ALLOWED_IMAGE_FORMATS = ['jpg', 'jpeg', 'png', 'gif']
    MAX_IMAGE_SIZE = 5242880  # 5MB


class DevelopmentConfig(Config):
    DEBUG = True

    AWS_ACCESS_KEY_ID = obfuscation.encrypt('aws-access-key-for-dev')
    AWS_SECERT_ACCESS_KEY = obfuscation.encrypt('aws-secret-access-key-for-dev')
    AWS_S3_BUCKET_NAME = obfuscation.encrypt('aws-s3-bucket-name-for-dev')

    DATABASE_URI = obfuscation.encrypt('database-uri-for-dev')


class TestConfig(Config):
    DEBUG = True
    TESTING = True

    AWS_ACCESS_KEY_ID = obfuscation.encrypt('aws-access-key-for-test')
    AWS_SECERT_ACCESS_KEY = obfuscation.encrypt('aws-secret-access-key-for-test')
    AWS_S3_BUCKET_NAME = obfuscation.encrypt('aws-s3-bucket-name-for-test')

    DATABASE_URI = obfuscation.encrypt('database-uri-for-test')


class ProductionConfig(Config):
    DEBUG = False

    AWS_ACCESS_KEY_ID = obfuscation.encrypt('aws-access-key-for-prod')
    AWS_SECERT_ACCESS_KEY = obfuscation.encrypt('aws-secret-access-key-for-prod')
    AWS_S3_BUCKET_NAME = obfuscation.encrypt('aws-s3-bucket-name-for-prod')

    DATABASE_URI = obfuscation.encrypt('database-uri-for-prod')


class CIConfig:
    SERVICE = obfuscation.encrypt('travis-ci')
    HOOK_URL = obfuscation.encrypt('web-hooking-url-from-ci-service')
