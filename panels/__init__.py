from .reload_addon import VIEW3D_PT_reload_auto_rig_addon
from .auto_rig import VIEW3D_PT_auto_rig
from ..libs.blender_utils import register_classes, unregister_classes, add_scene_custom_prop
from .custom_props import VIEW3D_PT_custom_props
from .snap_utils import VIEW3D_PT_snap_utils
from .rig_layer import VIEW3D_PT_rig_layer
from .soft_body import VIEW3D_PT_soft_body
from .dynamic_parent import VIEW3D_PT_dynamic_parent, Armature_Targets
from .wiggle import VIEW3D_PT_wiggle

classes = (
  VIEW3D_PT_reload_auto_rig_addon,
  VIEW3D_PT_auto_rig,
  VIEW3D_PT_custom_props, 
  VIEW3D_PT_snap_utils, 
  VIEW3D_PT_rig_layer,
  VIEW3D_PT_soft_body,
  VIEW3D_PT_dynamic_parent,
  Armature_Targets,
  VIEW3D_PT_wiggle
)

def register():
  register_classes(classes)

def unregister():
  unregister_classes(classes)
