class Config:
    SECRET_KEY = 'Edsonmata432.'

class DevelopmentConfig(Config):
    DEBUG = True

config = {
        'development': DevelopmentConfig,
        'default': DevelopmentConfig

}