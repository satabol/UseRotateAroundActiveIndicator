import bpy

class URAA_OP_use_rotate_around_active(bpy.types.Operator):
    '''Use rotate around active'''
    bl_idname = "uraa.use_rotate_around_active"
    bl_label = "Use rotate around active indicator"
    bl_options = {'REGISTER', 'UNDO', 'BLOCKING',}

    @classmethod
    def poll(self, context):
        # Активировать можно всегда, независимо от режима работы редактора
        res = True
        return res

    def execute(self, context):
        bpy.context.preferences.inputs.use_rotate_around_active = not(bpy.context.preferences.inputs.use_rotate_around_active)
        return {'FINISHED'}