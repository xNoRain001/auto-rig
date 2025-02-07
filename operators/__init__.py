from .init_rig import Init_Rig
from .init_bone_widgets import Init_Bone_Widgets
from .reload_addon import Reload_Addon
from .rename_by_increasing import Rename_By_Increasing
from .init_bone_collections import Init_Bone_Collections
from .snap_utils import Snap_Utils
from .soft_body import Soft_Body
from ..libs.blender_utils import register_classes, unregister_classes

classes = (
  Init_Rig,
  Rename_By_Increasing,
  Init_Bone_Widgets,
  Init_Bone_Collections,
  Reload_Addon,
  Snap_Utils,
  Soft_Body
)

def register():
  register_classes(classes)

def unregister():
  unregister_classes(classes)
