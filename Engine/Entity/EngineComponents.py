
class Component:
    pass

class ComponentTransform(Component):
    pos = None
    scale = None
    rot = None
    layer = None
    
    def __init__(self, p_pos, p_scale, p_rot, p_layer):
        self.pos = p_pos
        self.scale = p_scale
        self.rot = p_rot
        self.layer = p_layer
        
class ComponentTexture(Component):
    tex = None
    
    def __init__(self, p_tex):
        self.tex = p_tex