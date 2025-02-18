from ..libs.blender_utils import (
  get_pose_bone, get_context, get_active_object, get_ops, get_props, get_operator,
  get_bone_collections
)

def snap (source, target):
  source_bone_matrix = source.bone.matrix_local
  target_bone_matrix = target.bone.matrix_local
  offset_matrix = source_bone_matrix.inverted() @ target_bone_matrix
  source_world_matrix = source.matrix
  target.matrix = source_world_matrix @ offset_matrix

def snap_func (fk_or_ik, leg_or_arm, side):
  props = get_pose_bone('props')
  leg = leg_or_arm == 'leg'
  prop = f"{ 'leg' if leg else 'arm' }_fk_to_ik.{ side }"
  value = props[prop]
  is_fk = fk_or_ik == 'fk'
  is_ik = fk_or_ik == 'ik'

  # 处理 ik 切换到 ik 或者 fk 切换到 fk
  if (is_fk and not value) or (is_ik and value):
    return
  
  context = get_context()
  props[prop] = False if is_fk else True
  bones = [props]
  ik_collection = None
  fk_collection = None
  props_collection = props.bone.collections[0]

  if is_fk:
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
    bones.extend([fk_arm, fk_forearm, fk_hand])
    ik_collection = ik_hand.bone.collections[0]
    fk_collection = fk_arm.bone.collections[0]
  else:
    fk_hand = get_pose_bone(f"fk_{ 'foot' if leg else 'hand'}.{ side }")
    mch_ik_fk_arm_pole = get_pose_bone(f"mch_ik_fk_{ 'leg' if leg else 'arm'}_pole.{ side }")
    ik_hand = get_pose_bone(f"ik_{ 'foot' if leg else 'hand'}.{ side }")
    ik_pole = get_pose_bone(f"{ 'leg' if leg else 'arm'}_pole.{ side }")
    snap(fk_hand, ik_hand)
    context.view_layer.update()
    snap(mch_ik_fk_arm_pole, ik_pole)
    context.view_layer.update()
    bones.extend([ik_hand, ik_pole])
    ik_collection = ik_hand.bone.collections[0]
    fk_collection = fk_hand.bone.collections[0]

  get_ops().pose.select_all(action='DESELECT')
  # 骨骼必须可见才能插帧
  props_collection.is_visible = True
  ik_collection.is_visible = True
  fk_collection.is_visible = True

  for pbone in bones:
    get_active_object().data.bones.active = pbone.bone

    if get_context().scene.tool_settings.use_keyframe_insert_auto:
      get_ops().anim.keyframe_insert_menu(type='Available')

  if is_fk:
    ik_collection.is_visible = False
  else:
    fk_collection.is_visible = False

  props_collection.is_visible = False

class OBJECT_OT_snap_utils (get_operator()):
    bl_idname = 'object.snap_utils'
    bl_label = 'Snap Utils'
    param: get_props().StringProperty()

    def execute(self, context):
      fk_or_ik, leg_or_arm, side = self.param.split('-')
      snap_func(fk_or_ik, leg_or_arm, side)

      return {'FINISHED'}
