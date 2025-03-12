from ..libs.blender_utils import register_classes, unregister_classes
from .init_rig import OBJECT_OT_init_rig
from .init_bone_widgets import OBJECT_OT_init_bone_widgets
from .reload_addon import OBJECT_OT_reload_addon
from .init_bone_collections import OBJECT_OT_init_bone_collection
from .snap_utils import OBJECT_OT_snap_utils
from .soft_body import OBJECT_OT_soft_body
from .init_location import OBJECT_OT_init_location
from .rig_weapon import OBJECT_OT_rig_weapon
from .add_target import OBJECT_OT_add_target
from .remove_target import OBJECT_OT_remove_target
from .add_wiggle import OBJECT_OT_add_wiggle
from .init_def_bones import OBJECT_OT_init_def_bones
from .refresh_weapon import OBJECT_OT_refresh_weapon

classes = (
  OBJECT_OT_init_rig,
  OBJECT_OT_init_bone_widgets,
  OBJECT_OT_reload_addon,
  OBJECT_OT_init_bone_collection,
  OBJECT_OT_snap_utils,
  OBJECT_OT_soft_body,
  OBJECT_OT_init_location,
  OBJECT_OT_rig_weapon,
  OBJECT_OT_add_target,
  OBJECT_OT_remove_target,
  OBJECT_OT_add_wiggle,
  OBJECT_OT_init_def_bones,
  OBJECT_OT_refresh_weapon
)

def register():
  register_classes(classes)

def unregister():
  unregister_classes(classes)
