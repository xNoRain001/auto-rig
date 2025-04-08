from ..libs.blender_utils import get_operator, set_mode, active_object_, get_edit_bones

from ..hooks import rename_bones_for_mixamo, rename_bones_for_gi

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
    
class OBJECT_OT_retarget_to_mixamo (get_operator()):
  bl_idname = 'object.retarget_to_mixamo'
  bl_label = 'Retarget To Mixamo'

  def execute(self, context):
    scene = context.scene
    armature = scene.armature
    retarget_armature = scene.retarget_armature
    roll_map = init_roll_map(retarget_armature)
    active_object_(armature)
    rename_bones_for_gi()
    rename_bones_for_mixamo()
    init_boll_roll(roll_map)
    
    return {'FINISHED'}
