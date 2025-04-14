from ..libs.blender_utils import (
  set_mode,
  get_operator,
  report_error,
  active_object_,
)

from ..bones_roll import init_bones_roll
from ..constraints import init_bone_constraints
from ..bones.init_bow_bones import init_bow_bones
from ..bones_roll.bow_roll_map import init_bow_roll
from ..colors.init_bow_colors import init_bow_color
from ..widgets.init_bow_widgets import init_bow_widgets
from ..collections.init_bow_collections import init_bow_collections
from ..constraints.init_bow_constraints import init_bow_constraints_config

class OBJECT_OT_rig_bow (get_operator()):
  bl_idname = 'object.rig_bow'
  bl_label = 'Rig Bow'

  def invoke(self, context, event):
    scene = context.scene
    bowstring = scene.bowstring
    bow_limb = scene.bow_limb
    bow_limb_upper = scene.bow_limb_upper
    bow_limb_lower = scene.bow_limb_lower

    if (
      not bowstring.startswith('def_') or
      not bow_limb.startswith('def_') or
      not bow_limb_upper.startswith('def_') or
      not bow_limb_lower.startswith('def_')
    ):
      report_error(self, '除 bow root 外存在不以 def_ 开头的骨骼')
      return {'CANCELLED'}
    else:
      return self.execute(context)

  def execute(self, context):
    scene = context.scene
    armature = scene.bow_armature
    active_object_(armature)
    set_mode('EDIT')
    init_bones_roll(init_bow_roll(scene))
    bow_config = init_bow_bones(scene)
    init_bone_constraints(init_bow_constraints_config(scene))
    init_bow_widgets(bow_config, scene)
    init_bow_collections(bow_config, scene)
    init_bow_color(scene)

    return {'FINISHED'}
