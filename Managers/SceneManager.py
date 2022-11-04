from Managers.InputManager import InputManager
from Scenes.GameScene import *
import pygame
from pygame.locals import *

from Scenes.MainMenuScene import MainMenuScene
from Scenes.Scene import SceneType


class SceneManager:
    title = None
    renderer = None
    updater = None
    event = None
    current_scene = None
    canvas = None
    input_manager = None

    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.canvas = pygame.display.set_mode((500, 500))
        self.input_manager = InputManager()
        self.current_scene = MainMenuScene(self)
        self.initialise()

    def initialise(self):
        pygame.display.set_caption(self.title)

    def run(self):
        close = False

        while not close:
            self.renderer(self.canvas)
            self.updater(self.canvas)
            for event in pygame.event.get():
                self.event(event)
                if event.type == pygame.QUIT:
                    close = True
            pygame.display.update()

        self.current_scene.close()

    def change_scene(self, p_scene_type):
        match p_scene_type:
            case SceneType.SceneMainMenu:
                self.current_scene.close()
                self.current_scene = MainMenuScene(self)
            case SceneType.SceneGame:
                self.current_scene.close()
                self.current_scene = GameScene(self)

        print("Scene Changed")
        self.initialise()
