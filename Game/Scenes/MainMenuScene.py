import pygame as pygame

from pygame.math import *

from Engine.Entity.Entity import *
from Engine.Scenes.Scene import *
from Engine.Entity.EngineComponents import *

class MainMenuScene(Scene):
    scene_manager = None
    e1 = None

    def __init__(self, p_scene_manager):
        self.scene_manager = p_scene_manager
        self.scene_manager.title = "Main Menu"
        self.scene_manager.renderer = self.render
        self.scene_manager.updater = self.update
        self.scene_manager.event = self.event
        self.initialize()

    def initialize(self):
        self.scene_manager.input_manager.initialize_binds()
        
        self.e1 = Entity("deez")
        self.e1.add_component(ComponentTransform(Vector2(0.0, 0.0), Vector2(1.0, 1.0), 0.0, 0.0))
        self.e1.add_component(ComponentTexture(pygame.image.load("Game/Resources/randy.jpg")))

    def event(self, p_event):
        self.scene_manager.input_manager.check_input(self.scene_manager, p_event)

    def render(self, p_canvas):
        p_canvas.fill((255, 255, 255))
        
        ctr = ComponentTransform(Vector2(0.0, 0.0), Vector2(1.0, 1.0), 0.0, 0.0)
        ctx = ComponentTexture(pygame.image.load("Game/Resources/randy.jpg"))
                               
        self.scene_manager.canvas.blit(ctx.tex, (ctr.pos.x, ctr.pos.y))

    def update(self, p_canvas):
        pass

    def close(self):
        self.scene_manager.input_manager.clear_binds()
        pass
