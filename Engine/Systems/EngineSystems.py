from abc import ABC, abstractmethod

class System(ABC):
    
    @property
    @abstractmethod
    def system(self):
        pass
    
    @abstractmethod 
    def on_action(p_delta_time, p_entity_manager):
        pass
    
class SystemRender(System):
    def on_action(p_delta_time, p_entity_manager):
        pass