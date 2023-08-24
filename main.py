from Engine.Managers.SceneManager import SceneManager
from Game.Scenes.MainMenuScene import MainMenuScene

# TODO: Load in keybindings from file, separate binds per scene

game = SceneManager()
game.run(MainMenuScene(game))
