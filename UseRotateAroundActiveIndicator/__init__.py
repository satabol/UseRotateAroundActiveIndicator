bl_info = {
    "name": "Use rotate around active Indicator",
    "description" : "Settings -> Navigation -> Orbit Around Selection", 
    "author": "satabol",
    "version": (1,0,1),
    "blender": (2,90,0),
    "location": "View3D",
    "category": "3D View",
}
def register():
    from .addon.register import register_addon
    register_addon()
    pass

def unregister():
    from .addon.register import unregister_addon
    unregister_addon()
    pass