from ..libs.blender_utils import get_operator, set_mode, active_object_, get_edit_bones

from ..hooks import rename_bones_for_mixamo, rename_bones_for_gi
from ..bones_roll import init_bones_roll
from ..bones_roll.human_roll_map import init_human_roll
from ..parent import init_bones_parent
from ..parent.init_human_parent import init_human_parent_config
from ..operators.rig_human import symmetrize_bones

def init_roll_map (retarget_armature):
  active_object_(retarget_armature)
  set_mode('EDIT')
  bones = get_edit_bones()
  roll_map = {}

  for bone in bones:
    roll_map[bone.name] = bone.roll

  return roll_map

def init_boll_roll (roll_map):
  bones = get_edit_bones()

  for bone in bones:
    bone_name = bone.name

    if bone_name in roll_map:
      bone.roll = roll_map[bone_name]
    
class OBJECT_OT_retarget_to_cascadeur (get_operator()):
  bl_idname = 'object.retarget_to_cascadeur'
  bl_label = 'Retarget To Cascadeur'

  def execute(self, context):
    scene = context.scene
    armature = scene.armature
    active_object_(armature)
    set_mode('EDIT')
    rename_bones_for_gi()
    init_bones_roll(init_human_roll())
    init_bones_parent(init_human_parent_config())
    rename_bones_for_mixamo()
    
    return {'FINISHED'}
