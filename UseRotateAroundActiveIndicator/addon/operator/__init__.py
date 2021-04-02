import bpy

from .RotateAroundSelectionIndcator import URAA_OP_use_rotate_around_active

classes = (
    URAA_OP_use_rotate_around_active,
)

def draw_button(self, context):
    user_preferences = context.preferences
    if context.region.alignment == 'RIGHT':
        layout = self.layout
        row = layout.row(align=True)
        if bpy.context.preferences.inputs.use_rotate_around_active==True:
            layout.operator(
                    "URAA.use_rotate_around_active", icon="PROP_CON",
                    text="Object",
                )
        else:
            layout.operator(
                    "URAA.use_rotate_around_active", icon="SNAP_NORMAL",
                    text="Mouse"
                )

        return{'FINISHED'}

def register_operators():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls);
    bpy.types.TOPBAR_HT_upper_bar.prepend(draw_button)


def unregister_operators():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls);
    bpy.types.TOPBAR_HT_upper_bar.remove(draw_button)