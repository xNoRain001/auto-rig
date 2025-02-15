import bpy

from ..libs.blender_utils import get_pose_bone, get_context

def snap (source, target):
  source_bone_matrix = source.bone.matrix_local
  target_bone_matrix = target.bone.matrix_local
  offset_matrix = source_bone_matrix.inverted() @ target_bone_matrix
  source_world_matrix = source.matrix
  target.matrix = source_world_matrix @ offset_matrix

def snap_func (type, leg_or_arm, side):
  props = get_pose_bone('props')
  leg = leg_or_arm == 'leg'
  prop = f"{ 'leg' if leg else 'arm' }_fk_to_ik.{ side }"
  value = props[prop]
  fk = type == 'fk'
  ik = type == 'ik'

  # 处理 ik 切换到 ik 或者 fk 切换到 fk
  if (fk and not value) or (ik and value):
    return
  
  context = get_context()
  
  if fk:
    fk_arm = get_pose_bone(f"fk_{ 'leg' if leg else 'arm'}.{ side }")
    fk_forearm = get_pose_bone(f"fk_{ 'shin' if leg else 'forearm'}.{ side }")
    fk_hand = get_pose_bone(f"fk_{ 'foot' if leg else 'hand'}.{ side }")
    ik_arm =  get_pose_bone(f"mch_ik_{ 'leg' if leg else 'arm'}.{ side }")
    ik_forearm =  get_pose_bone(f"mch_ik_{ 'shin' if leg else 'forearm'}.{ side }")
    ik_hand =  get_pose_bone(f"ik_{ 'foot' if leg else 'hand'}.{ side }")
    
    snap(ik_arm, fk_arm)
    context.view_layer.update()
    snap(ik_forearm, fk_forearm)
    context.view_layer.update()
    snap(ik_hand, fk_hand)
    context.view_layer.update()

  else:
    fk_hand = get_pose_bone(f"fk_{ 'foot' if leg else 'hand'}.{ side }")
    mch_ik_fk_arm_pole = get_pose_bone(f"mch_ik_fk_{ 'leg' if leg else 'arm'}_pole.{ side }")
    ik_hand = get_pose_bone(f"ik_{ 'foot' if leg else 'hand'}.{ side }")
    ik_pole = get_pose_bone(f"{ 'leg' if leg else 'arm'}_pole.{ side }")

    snap(fk_hand, ik_hand)
    context.view_layer.update()
    snap(mch_ik_fk_arm_pole, ik_pole)
    context.view_layer.update()

  props[prop] = False if fk else True
  
def gen_custom_rig_ui ():
  armature_name = bpy.data.armatures[0].name

class OBJECT_OT_snap_utils (bpy.types.Operator):
    bl_idname = 'object.snap_utils'
    bl_label = 'Snap Utils'

    param: bpy.props.StringProperty()

    def execute(self, context):
      type, leg_or_arm, side = self.param.split('-')
      snap_func(type, leg_or_arm, side)

      return {'FINISHED'}
