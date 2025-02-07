from .reload_addon import Reload_Addon
from .auto_rig import Auto_Rig
from .rename_by_increasing import Rename_By_Increasing
from ..libs.blender_utils import register_classes, unregister_classes
from .custom_props import Custom_Props
from .snap_utils import Snap_Utils
from .rig_layer import Rig_Layer
from .soft_body import Soft_Body

classes = (
  Reload_Addon,
  Auto_Rig,
  Rename_By_Increasing,
  Rig_Layer, 
  Custom_Props, 
  Snap_Utils,
  Soft_Body
)

def register():
  register_classes(classes)

def unregister():
  unregister_classes(classes)
