from ..libs.blender_utils import register_classes, unregister_classes
from .rig_human import OBJECT_OT_rig_human
from .reload_addon import OBJECT_OT_reload_addon
from .ik_fk_snap_utils import OBJECT_OT_ik_fk_snap_utils
from .add_soft_body import OBJECT_OT_add_soft_body
from .init_location import OBJECT_OT_init_location
from .rig_weapon import OBJECT_OT_rig_weapon
from .add_target import OBJECT_OT_add_target
from .remove_target import OBJECT_OT_remove_target
from .bone_wiggle import OBJECT_OT_bone_wiggle
from .init_def_bones import OBJECT_OT_init_def_bones
from .refresh_weapon import OBJECT_OT_refresh_weapon
from .clear_bone_widget import OBJECT_OT_clear_bone_widget
from .clear_unused_widget import OBJECT_OT_clear_unused_bone_widget
from .reset_transform import OBJECT_OT_reset_transform
from .retarget_to_mixamo import OBJECT_OT_retarget_to_mixamo
from .rig_bow import OBJECT_OT_rig_bow
from .retarget_to_cascadeur import OBJECT_OT_retarget_to_cascadeur
from .rig_ball import OBJECT_OT_rig_ball

classes = (
  OBJECT_OT_rig_human,
  OBJECT_OT_reload_addon,
  OBJECT_OT_ik_fk_snap_utils,
  OBJECT_OT_add_soft_body,
  OBJECT_OT_init_location,
  OBJECT_OT_rig_weapon,
  OBJECT_OT_add_target,
  OBJECT_OT_remove_target,
  OBJECT_OT_bone_wiggle,
  OBJECT_OT_init_def_bones,
  OBJECT_OT_refresh_weapon,
  OBJECT_OT_clear_bone_widget,
  OBJECT_OT_clear_unused_bone_widget,
  OBJECT_OT_reset_transform,
  OBJECT_OT_retarget_to_mixamo,
  OBJECT_OT_rig_bow,
  OBJECT_OT_retarget_to_cascadeur,
  OBJECT_OT_rig_ball
)

def register():
  register_classes(classes)

def unregister():
  unregister_classes(classes)
