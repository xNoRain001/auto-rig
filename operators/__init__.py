from .init_rig import OBJECT_OT_init_rig
from .init_bone_widgets import OBJECT_OT_init_bone_widgets
from .reload_addon import OBJECT_OT_reload_addon
from .init_bone_collections import OBJECT_OT_init_bone_collection
from .snap_utils import OBJECT_OT_snap_utils
from .soft_body import OBJECT_OT_soft_body
from .init_location import OBJECT_OT_init_location
from ..libs.blender_utils import register_classes, unregister_classes

classes = (
  OBJECT_OT_init_rig,
  OBJECT_OT_init_bone_widgets,
  OBJECT_OT_reload_addon,
  OBJECT_OT_init_bone_collection,
  OBJECT_OT_snap_utils,
  OBJECT_OT_soft_body,
  OBJECT_OT_init_location
)

def register():
  register_classes(classes)

def unregister():
  unregister_classes(classes)
