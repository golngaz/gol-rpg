from src.Config.ConfigParserFacade import ConfigParserFacade
from src.Game.Game import Game

config = ConfigParserFacade('conf.ini', 'dev')

game = Game(config)

game.run()
