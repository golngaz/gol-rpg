from configparser import ConfigParser
from Engine import Engine
from src.Config.ConfigParserFacade import ConfigParserFacade


config = ConfigParserFacade('./conf.ini', 'dev')

game = Engine(config)


game.run()

# game.debug()
