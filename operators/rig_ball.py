from ..libs.blender_utils import (
  set_mode,
  get_operator,
  report_error,
  get_edit_bone,
  active_object_
)

from ..bones_roll import init_bones_roll
from ..constraints import init_bone_constraints
from ..bones.init_ball_bones import init_ball_bones
from ..bones_roll.ball_roll_map import init_ball_roll
from ..colors.init_ball_colors import init_ball_color
from ..widgets.init_ball_widgets import init_ball_widgets
from ..collections.init_ball_collections import init_ball_collections
from ..constraints.init_ball_constraints import init_ball_constraints_config

class OBJECT_OT_rig_ball (get_operator()):
  bl_idname = 'object.rig_ball'
  bl_label = 'Rig Ball'

  def execute(self, context):
    scene = context.scene
    armature = scene.ball_armature
    active_object_(armature)
    set_mode('EDIT')
    init_bones_roll(init_ball_roll(scene))
    ball_config = init_ball_bones(scene)
    init_bone_constraints(init_ball_constraints_config())
    init_ball_widgets(ball_config, scene)
    init_ball_collections(ball_config, scene)
    init_ball_color(scene)

    return {'FINISHED'}
