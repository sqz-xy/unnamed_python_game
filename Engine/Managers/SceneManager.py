from Engine.Managers.InputManager import InputManager
from Game.Scenes.GameScene import *
import pygame
from pygame.locals import *

from Game.Scenes.MainMenuScene import MainMenuScene

class SceneManager:
    title = ""
    renderer = None
    updater = None
    event = None
    current_scene = None
    canvas = None
    input_manager = None

    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(self.title)
        self.canvas = pygame.display.set_mode((500, 500))
        self.input_manager = InputManager()

    def run(self, p_start_scene):
        close = False

        self.current_scene = p_start_scene

        while not close:
            self.renderer(self.canvas)
            self.updater(self.canvas)
            for event in pygame.event.get():
                self.event(event)
                if event.type == pygame.QUIT:
                    close = True
            pygame.display.update()

        self.current_scene.close()

    def change_scene(self, p_new_scene):
        self.current_scene.close()
        self.current_scene = p_new_scene

        pygame.display.set_caption(self.title)
