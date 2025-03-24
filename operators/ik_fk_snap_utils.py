from ..libs.blender_utils import (
  get_ops, 
  get_props, 
  update_view,
  get_operator,
  get_pose_bone, 
  select_pose_bone,
  get_active_object,
  deselect_pose_bones,
  get_selected_pose_bone,
  use_keyframe_insert_auto
)

from ..scene.add_weapon_props import get_world_matrix

def show_collection (ik_collection, fk_collection, props_collection):
  # 骨骼必须可见才能插帧，这其中就要求集合也可见
  props_collection.is_visible = True
  ik_collection.is_visible = True
  fk_collection.is_visible = True

def insert_keyframe (bones):
  selected_pose_bone = get_selected_pose_bone()
  deselect_pose_bones()

  for bone in bones:
    select_pose_bone(bone.bone)
    get_ops().anim.keyframe_insert_menu(type='Available')
  
  # 还原回之前选中的骨骼
  select_pose_bone(selected_pose_bone)

def update_collection_visible (
  is_fk, 
  old_value, 
  ik_collection, 
  fk_collection, 
  props_collection
):
  setattr(fk_collection if is_fk else ik_collection, 'is_visible', True)
  setattr(ik_collection if is_fk else fk_collection, 'is_visible', False)

  if old_value is not None:
    props_collection.is_visible = old_value

def update_matrix (source, target):
  target.matrix = get_world_matrix(get_active_object(), source)

  # source_bone_matrix = source.bone.matrix_local
  # target_bone_matrix = target.bone.matrix_local
  # offset_matrix = source_bone_matrix.inverted() @ target_bone_matrix
  # source_world_matrix = source.matrix
  # target.matrix = source_world_matrix @ offset_matrix

def ik_to_fk (is_leg, side):
  fk_arm = get_pose_bone(f"fk_{ 'leg' if is_leg else 'arm'}.{ side }")
  fk_forearm = get_pose_bone(f"fk_{ 'shin' if is_leg else 'forearm'}.{ side }")
  fk_hand = get_pose_bone(f"fk_{ 'foot' if is_leg else 'hand'}.{ side }")
  mch_ik_fk_arm_pole = \
    get_pose_bone(f"mch_ik_fk_{ 'leg' if is_leg else 'arm'}_pole.{ side }")
  ik_arm = get_pose_bone(f"mch_ik_{ 'leg' if is_leg else 'arm'}.{ side }")
  ik_forearm = \
    get_pose_bone(f"mch_ik_{ 'shin' if is_leg else 'forearm'}.{ side }")
  ik_hand = get_pose_bone(f"{ 'mch_' if is_leg else '' }ik_{ 'foot' if is_leg else 'hand'}.{ side }")
  ik_pole = get_pose_bone(f"{ 'leg' if is_leg else 'arm'}_pole.{ side }")
  update_matrix(ik_arm, fk_arm)
  update_view()
  # fk_arm 移动到 ik_arm 的位置时，pole 之间可能有微小的偏移，需要修复它
  update_matrix(ik_pole, mch_ik_fk_arm_pole)
  update_view()
  update_matrix(ik_forearm, fk_forearm)
  update_view()
  update_matrix(ik_hand, fk_hand)
  update_view()

  if is_leg:
    # fk_foot 更新后，mch_ik_fk_foot 也会随着更新，fk 切换回 ik 时，ik_foot 更新
    # 到 mch_ik_fk_foot 位置，如果不修正 mch_ik_fk_foot 位置，就会发生偏移
    mch_ik_fk_foot = get_pose_bone(f'mch_ik_fk_foot.{ side }')
    ik_foot = get_pose_bone(f'ik_foot.{ side }')
    update_matrix(ik_foot, mch_ik_fk_foot)
    update_view()

    fk_toes = get_pose_bone(f'fk_toes.{ side }')

    if fk_toes:
      ik_toes = get_pose_bone(f'ik_toes.{ side }')
      update_matrix(ik_toes, fk_toes)
      update_view()
  
  return [
    [fk_arm, fk_forearm, fk_hand],
    ik_pole.bone.collections[0],
    fk_arm.bone.collections[0]
  ]

def fk_to_ik (is_leg, side):
  fk_hand = get_pose_bone(f"fk_{ 'foot' if is_leg else 'hand'}.{ side }")
  mch_ik_fk_arm_pole = \
    get_pose_bone(f"mch_ik_fk_{ 'leg' if is_leg else 'arm'}_pole.{ side }")
  ik_hand = get_pose_bone(f"ik_{ 'foot' if is_leg else 'hand'}.{ side }")
  ik_pole = get_pose_bone(f"{ 'leg' if is_leg else 'arm'}_pole.{ side }")

  if is_leg:
    mch_ik_fk_foot = get_pose_bone(f'mch_ik_fk_foot.{ side }')
    update_matrix(mch_ik_fk_foot, ik_hand)
  else:
    update_matrix(fk_hand, ik_hand)

  update_view()
  update_matrix(mch_ik_fk_arm_pole, ik_pole)
  update_view()

  if is_leg:
    fk_toes = get_pose_bone(f'fk_toes.{ side }')
    
    if fk_toes:
      ik_toes = get_pose_bone(f'ik_toes.{ side }')
      update_matrix(fk_toes, ik_toes)
      update_view()

  return [
    [ik_hand, ik_pole],
    ik_pole.bone.collections[0],
    fk_hand.bone.collections[0]
  ]

def on_snap (fk_or_ik, leg_or_arm, side):
  props = get_pose_bone('props')
  is_leg = leg_or_arm == 'leg'
  prop = f"{ 'leg' if is_leg else 'arm' }_fk_to_ik_{ side }"
  value = props[prop]
  is_fk = fk_or_ik == 'fk'
  is_ik = not is_fk

  # 处理 ik 切换到 ik 或者 fk 切换到 fk
  if (is_fk and not value) or (is_ik and value):
    return
  
  props[prop] = False if is_fk else True
  bones, ik_collection, fk_collection = \
    ik_to_fk(is_leg, side) if is_fk else fk_to_ik(is_leg, side)
  props_collection = props.bone.collections[0]
  old_value = None
  
  if use_keyframe_insert_auto():
    old_value = props_collection.is_visible
    show_collection(ik_collection, fk_collection, props_collection)
    insert_keyframe(bones)
  
  update_collection_visible(
    is_fk, 
    old_value, 
    ik_collection, 
    fk_collection, 
    props_collection
  )

class OBJECT_OT_ik_fk_snap_utils (get_operator()):
    bl_idname = 'object.ik_fk_snap_utils'
    bl_label = 'IK FK Snap Utils'
    param: get_props().StringProperty()

    def execute(self, context):
      fk_or_ik, leg_or_arm, side = self.param.split('-')
      on_snap(fk_or_ik, leg_or_arm, side)

      return {'FINISHED'}
