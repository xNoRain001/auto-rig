from ..libs.blender_utils import register_classes, unregister_classes
from .add_bone_colors import add_bone_colors
from .add_armature import add_armature
from .add_mesh import add_mesh
from .add_pole_target_normal import add_pole_target_normal
from .add_rotation_mode import add_rotation_mode
from .add_foot_ctrl import add_foot_ctrl
from .add_soft_body_config import add_soft_body_config
from .add_dynamic_parent import add_dynamic_parent
from .add_wiggle_config import add_wiggle_config
from .add_line_width import add_line_width
from .add_weapon_props import add_weapon_props
from .add_def_bones import add_def_bones
from .add_tweak_bone_number import add_tweak_bone_number

classes = ()

def register():
  # register_classes(classes)
  add_armature()
  add_mesh()
  add_pole_target_normal()
  add_rotation_mode()
  add_foot_ctrl()
  add_soft_body_config()
  add_bone_colors()
  add_dynamic_parent()
  add_wiggle_config()
  add_line_width()
  # add_weapon_props()
  add_def_bones()
  add_tweak_bone_number()
  
def unregister():
  # unregister_classes(classes)
  pass
