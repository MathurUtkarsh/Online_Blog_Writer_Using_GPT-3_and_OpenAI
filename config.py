# -*- coding: utf-8 -*-

##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}