import pygame

from Engine.Scenes.Scene import SceneType


class InputManager:
    key_binds = None
    mouse_binds = None

    def __init__(self):
        self.initialize_binds()

    def initialize_binds(self):
        self.key_binds = dict()
        self.mouse_binds = dict()
        self.key_binds.update({pygame.K_w: "START_GAME"})   #Default bind, remove at some point, replace with bind script

    def check_input(self, p_scene_manager, p_event):
        if p_event.type == pygame.KEYDOWN:
            for key in self.key_binds:
                if key == p_event.key:
                    self.handle_input(self.key_binds[key], p_scene_manager)

    def handle_input(self, p_action, p_scene_manager):
        match p_action:
            case "START_GAME":
                p_scene_manager.change_scene(SceneType.SceneGame)

    def clear_binds(self):
        self.key_binds = dict()
        self.mouse_binds = dict()
