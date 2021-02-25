from src.Config.ConfigParserFacade import ConfigParserFacade
from src.Editor.Editor import Editor

config = ConfigParserFacade('conf.ini', 'dev', root_directory='..')

editor = Editor(config)
editor.run()
