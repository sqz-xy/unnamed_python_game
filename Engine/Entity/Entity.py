from Engine.Entity.EngineComponents import Component

class Entity():
    components = None
    name = None
    guid = None
    max_guid = 0

    
    def __init__(self, p_name):
        self.name = p_name
        self.components = list()
        self.guid = Entity.max_guid
        Entity.max_guid += 1

    def add_component(self, p_component: Component):
        self.components.append(p_component)
        
    def remove_component(self, p_component: Component):
        self.components.list.remove(p_component)
    
        