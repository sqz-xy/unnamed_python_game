from Engine.Scenes.Scene import Scene

class MainMenuScene(Scene):
    scene_manager = None

    def __init__(self, p_scene_manager):
        self.scene_manager = p_scene_manager
        self.scene_manager.title = "Main Menu"
        self.scene_manager.renderer = self.render
        self.scene_manager.updater = self.update
        self.scene_manager.event = self.event
        self.initialize()

    def initialize(self):
        self.scene_manager.input_manager.initialize_binds()

    def event(self, p_event):
        self.scene_manager.input_manager.check_input(self.scene_manager, p_event)

    def render(self, p_canvas):
        p_canvas.fill((255, 255, 255))

    def update(self, p_canvas):
        pass

    def close(self):
        self.scene_manager.input_manager.clear_binds()
        pass
