from .reload_addon import VIEW3D_PT_reload_auto_rig_addon
from .auto_rig import VIEW3D_PT_auto_rig
from ..libs.blender_utils import register_classes, unregister_classes, add_scene_custom_prop
from .custom_props import VIEW3D_PT_custom_props
from .snap_utils import VIEW3D_PT_snap_utils
from .rig_layers import VIEW3D_PT_rig_layers
from .soft_body import VIEW3D_PT_soft_body
from .dynamic_parent import VIEW3D_PT_dynamic_parent, Armature_Targets
from .add_wiggle import VIEW3D_PT_add_wiggle
from .helper import VIEW3D_PT_helper

classes = (
  VIEW3D_PT_reload_auto_rig_addon,
  VIEW3D_PT_auto_rig,
  VIEW3D_PT_custom_props, 
  VIEW3D_PT_snap_utils, 
  VIEW3D_PT_rig_layers,
  # VIEW3D_PT_soft_body,
  # VIEW3D_PT_dynamic_parent,
  # Armature_Targets,
  VIEW3D_PT_add_wiggle,
  VIEW3D_PT_helper,
)

def register():
  register_classes(classes)

def unregister():
  unregister_classes(classes)
