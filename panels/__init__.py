from ..libs.blender_utils import register_classes, unregister_classes

from .helper import VIEW3D_PT_helper
from .auto_rig import VIEW3D_PT_auto_rig
from .soft_body import VIEW3D_PT_soft_body
from .extra_rig import VIEW3D_PT_extra_rig
from .rig_layers import VIEW3D_PT_rig_layers
from .bone_widget import VIEW3D_PT_bone_widget
from .custom_props import VIEW3D_PT_custom_props
from .ik_fk_snap_utils import VIEW3D_PT_ik_fk_snap_utils
from .reload_addon import VIEW3D_PT_reload_auto_rig_addon
from .dynamic_parent import VIEW3D_PT_dynamic_parent, Armature_Targets
from .retarget_to_mixamo import VIEW3D_PT_retarget_to_mixamo
from .rig_bow import VIEW3D_PT_rig_bow

classes = (
  VIEW3D_PT_reload_auto_rig_addon,
  VIEW3D_PT_auto_rig,
  VIEW3D_PT_custom_props, 
  VIEW3D_PT_ik_fk_snap_utils, 
  VIEW3D_PT_rig_layers,
  # VIEW3D_PT_soft_body,
  # VIEW3D_PT_dynamic_parent,
  # Armature_Targets,
  VIEW3D_PT_extra_rig,
  VIEW3D_PT_helper,
  VIEW3D_PT_bone_widget,
  VIEW3D_PT_retarget_to_mixamo,
  VIEW3D_PT_rig_bow
)

def register():
  register_classes(classes)

def unregister():
  unregister_classes(classes)
