from abc import ABC, abstractmethod

class Scene(ABC):

    @property
    @abstractmethod
    def scene_manager(self):
        pass

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def event(self, p_event):
        pass

    @abstractmethod
    def render(self, p_canvas):
        pass

    @abstractmethod
    def update(self, p_canvas):
        pass

    @abstractmethod
    def close(self):
        pass
