from ..libs.blender_utils import register_classes, unregister_classes
from .add_human_collections_color import add_human_collections_color
from .add_ball_collections_color import add_ball_collections_color
from .add_armature import add_armature
from .add_mesh import add_mesh
from .add_pole_target_normal import add_pole_target_normal
from .add_rotation_mode import add_rotation_mode
from .add_foot_ctrl import add_foot_ctrl
from .add_soft_body_config import add_soft_body_config
from .add_dynamic_parent import add_dynamic_parent
from .add_wiggle_config import add_wiggle_config
from .add_weapon_props import add_weapon_props
from .add_def_bones import add_def_bones
from .add_tweak_bone_number import add_tweak_bone_number
from .add_weapon import add_weapon
from .add_rotation import add_rotation
from .add_scale import add_scale
from .add_shape import add_shape
from .add_show_wire import add_show_wire
from .add_translation import add_translation
from .add_wire_width import add_wire_width
from .add_retarget_armature import add_retarget_armature
from .add_bow import add_bow
from .add_ball import add_ball
from .add_bow_collections_color import add_bow_collections_color

classes = ()

def register():
  # register_classes(classes)
  add_armature()
  add_mesh()
  add_pole_target_normal()
  add_rotation_mode()
  add_foot_ctrl()
  add_soft_body_config()
  add_human_collections_color()
  add_ball_collections_color()
  add_bow_collections_color()
  add_dynamic_parent()
  add_wiggle_config()
  # add_weapon_props()
  add_def_bones()
  add_tweak_bone_number()
  add_weapon()
  add_rotation()
  add_scale()
  add_shape()
  add_show_wire()
  add_translation()
  add_wire_width()
  add_retarget_armature()
  add_bow()
  add_ball()
  
def unregister():
  # unregister_classes(classes)
  pass
