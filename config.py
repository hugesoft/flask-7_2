import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    
    @staticmethod
    def init_app(app):
        print 'mmx'
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    print 'hugesofg'

config = {
    'development':DevelopmentConfig,
    'default':DevelopmentConfig
}
