from ..libs.blender_utils import register_classes, unregister_classes
from .add_bone_colors import add_bone_colors
from .add_armature_name import add_armature_name
from .add_mesh_name import add_mesh_name
from .add_pole_target_normal import add_pole_target_normal
from .add_rotation_mode import add_rotation_mode
from .add_foot_ctrl import add_foot_ctrl
from .add_soft_body_config import add_soft_body_config
from .add_dynamic_parent import add_dynamic_parent

classes = ()

def register():
  # register_classes(classes)
  add_armature_name()
  add_mesh_name()
  add_pole_target_normal()
  add_rotation_mode()
  add_foot_ctrl()
  add_soft_body_config()
  add_bone_colors()
  add_dynamic_parent()
  
def unregister():
  # unregister_classes(classes)
  pass
