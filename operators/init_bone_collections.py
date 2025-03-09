from collections import defaultdict
from ..libs.blender_utils import (
  set_mode, 
  get_edit_bone, 
  select_bone, 
  deselect, 
  get_active_object, 
  get_context, 
  get_armature, 
  get_operator,
  get_edit_bones,
  get_pose_bones,
  active_object_,
  get_object_,
  get_bone_collections
)
from .add_wiggle import check_armature

def add_org_bone (bones, map):
  for bone in bones:
    bone_name = bone.name

    if bone_name.startswith('org_'):
      map['org'].add(bone)
    elif bone_name.startswith('def_'):
      map['def'].add(bone)
    elif bone_name.startswith('mch_'):
      map['mch'].add(bone)

def add_root (map):
  map['root'].add(get_edit_bone('root'))

def add_prosp (map):
  map['props'].add(get_edit_bone('props'))

def add_torso (map):
  map['torso'].update([
    get_edit_bone('hips'),
    get_edit_bone('chest'),
    get_edit_bone('torso'),
    get_edit_bone('neck'),
    get_edit_bone('head'),
    get_edit_bone('shoulder.l'),
    get_edit_bone('shoulder.r'),
  ])
  map['torso_fk'].update([
    get_edit_bone('fk_hips'),
    get_edit_bone('fk_spine_01'),
    get_edit_bone('fk_spine_02'),
    get_edit_bone('fk_chest'),
  ])
  map['tweak_torso'].update([
    get_edit_bone('tweak_hips'),
    get_edit_bone('tweak_spine_01'),
    get_edit_bone('tweak_spine_02'),
    get_edit_bone('tweak_chest'),
    get_edit_bone('tweak_neck'),
    get_edit_bone('tweak_head'),
    get_edit_bone('tweak_top_head'),
  ])

def add_arm (map):
  map['arm_fk.l'].update([
    get_edit_bone('fk_arm.l'),
    get_edit_bone('fk_forearm.l'),
    get_edit_bone('fk_hand.l'),
  ])
  map['arm_ik.l'].update([
    get_edit_bone('ik_hand.l'),
    get_edit_bone('arm_pole.l'),
    get_edit_bone('vis_arm_pole.l'),
  ])
  map['tweak_arm.l'].update([
    get_edit_bone('tweak_arm.l'),
    get_edit_bone('tweak_forearm.l'),
    get_edit_bone('tweak_hand.l'),
    get_edit_bone('tweak_tip_hand.l'),
    get_edit_bone('tweak_arm_01.l'),
    get_edit_bone('tweak_arm_02.l'),
    get_edit_bone('tweak_arm_03.l'),
    get_edit_bone('tweak_arm_04.l'),
    get_edit_bone('tweak_forearm_01.l'),
    get_edit_bone('tweak_forearm_02.l'),
    get_edit_bone('tweak_forearm_03.l'),
    get_edit_bone('tweak_forearm_04.l'),
  ])
  map['arm_fk.r'].update([
    get_edit_bone('fk_arm.r'),
    get_edit_bone('fk_forearm.r'),
    get_edit_bone('fk_hand.r'),
  ])
  map['arm_ik.r'].update([
    get_edit_bone('ik_hand.r'),
    get_edit_bone('arm_pole.r'),
    get_edit_bone('vis_arm_pole.r'),
  ])
  map['tweak_arm.r'].update([
    get_edit_bone('tweak_arm.r'),
    get_edit_bone('tweak_forearm.r'),
    get_edit_bone('tweak_hand.r'),
    get_edit_bone('tweak_tip_hand.r'),
    get_edit_bone('tweak_arm_01.r'),
    get_edit_bone('tweak_arm_02.r'),
    get_edit_bone('tweak_arm_03.r'),
    get_edit_bone('tweak_arm_04.r'),
    get_edit_bone('tweak_forearm_01.r'),
    get_edit_bone('tweak_forearm_02.r'),
    get_edit_bone('tweak_forearm_03.r'),
    get_edit_bone('tweak_forearm_04.r'),
  ])

def add_leg (map):
  map['leg_fk.l'].update([
    get_edit_bone('fk_leg.l'),
    get_edit_bone('fk_shin.l'),
    get_edit_bone('fk_foot.l'),
  ])
  map['leg_ik.l'].update([
    get_edit_bone('ik_foot.l'),
    get_edit_bone('leg_pole.l'),
    get_edit_bone('vis_leg_pole.l'),
    get_edit_bone('foot_heel.l')
  ])
  map['tweak_leg.l'].update([
    get_edit_bone('tweak_leg.l'),
    get_edit_bone('tweak_shin.l'),
    get_edit_bone('tweak_foot.l'),
  ])
  map['leg_fk.r'].update([
    get_edit_bone('fk_leg.r'),
    get_edit_bone('fk_shin.r'),
    get_edit_bone('fk_foot.r'),
  ])
  map['leg_ik.r'].update([
    get_edit_bone('ik_foot.r'),
    get_edit_bone('leg_pole.r'),
    get_edit_bone('vis_leg_pole.r'),
    get_edit_bone('foot_heel.r')
  ])
  map['tweak_leg.r'].update([
    get_edit_bone('tweak_leg.r'),
    get_edit_bone('tweak_shin.r'),
    get_edit_bone('tweak_foot.r'),
  ])

  toes = get_edit_bone('org_toes.l')

  if toes:
    map['leg_fk.l'].add(get_edit_bone('fk_toes.l'))
    map['leg_ik.l'].add(get_edit_bone('ik_toes.l'))
    map['tweak_leg.l'].update([
      get_edit_bone('tweak_toes.l'),
      get_edit_bone('tweak_tip_toes.l')
    ])
    map['leg_fk.r'].add(get_edit_bone('fk_toes.r'))
    map['leg_ik.r'].add(get_edit_bone('ik_toes.r'))
    map['tweak_leg.r'].update([
      get_edit_bone('tweak_toes.r'),
      get_edit_bone('tweak_tip_toes.r')
    ])
  else:
    map['tweak_leg.l'].update([get_edit_bone('tweak_tip_foot.l')])
    map['tweak_leg.r'].update([get_edit_bone('tweak_tip_foot.r')])

def add_hand (map):
  map['hand.l'].update([
    get_edit_bone('thumb_01.l'),
    get_edit_bone('thumb_02.l'),
    get_edit_bone('thumb_03.l'),
    get_edit_bone('finger_a_01.l'),
    get_edit_bone('finger_a_02.l'),
    get_edit_bone('finger_a_03.l'),
    get_edit_bone('finger_b_01.l'),
    get_edit_bone('finger_b_02.l'),
    get_edit_bone('finger_b_03.l'),
    get_edit_bone('finger_c_01.l'),
    get_edit_bone('finger_c_02.l'),
    get_edit_bone('finger_c_03.l'),
    get_edit_bone('finger_d_01.l'),
    get_edit_bone('finger_d_02.l'),
    get_edit_bone('finger_d_03.l'),
  ])
  map['tweak_hand.l'].update([
    get_edit_bone('tweak_thumb_01.l'),
    get_edit_bone('tweak_thumb_02.l'),
    get_edit_bone('tweak_thumb_03.l'),
    get_edit_bone('tweak_tip_thumb_03.l'),
    get_edit_bone('tweak_finger_a_01.l'),
    get_edit_bone('tweak_finger_a_02.l'),
    get_edit_bone('tweak_finger_a_03.l'),
    get_edit_bone('tweak_tip_finger_a_03.l'),
    get_edit_bone('tweak_finger_b_01.l'),
    get_edit_bone('tweak_finger_b_02.l'),
    get_edit_bone('tweak_finger_b_03.l'),
    get_edit_bone('tweak_tip_finger_b_03.l'),
    get_edit_bone('tweak_finger_c_01.l'),
    get_edit_bone('tweak_finger_c_02.l'),
    get_edit_bone('tweak_finger_c_03.l'),
    get_edit_bone('tweak_tip_finger_c_03.l'),
    get_edit_bone('tweak_finger_d_01.l'),
    get_edit_bone('tweak_finger_d_02.l'),
    get_edit_bone('tweak_finger_d_03.l'),
    get_edit_bone('tweak_tip_finger_d_03.l'),
  ])
  map['hand.r'].update([
    get_edit_bone('thumb_01.r'),
    get_edit_bone('thumb_02.r'),
    get_edit_bone('thumb_03.r'),
    get_edit_bone('finger_a_01.r'),
    get_edit_bone('finger_a_02.r'),
    get_edit_bone('finger_a_03.r'),
    get_edit_bone('finger_b_01.r'),
    get_edit_bone('finger_b_02.r'),
    get_edit_bone('finger_b_03.r'),
    get_edit_bone('finger_c_01.r'),
    get_edit_bone('finger_c_02.r'),
    get_edit_bone('finger_c_03.r'),
    get_edit_bone('finger_d_01.r'),
    get_edit_bone('finger_d_02.r'),
    get_edit_bone('finger_d_03.r'),
  ])
  map['tweak_hand.r'].update([
    get_edit_bone('tweak_thumb_01.r'),
    get_edit_bone('tweak_thumb_02.r'),
    get_edit_bone('tweak_thumb_03.r'),
    get_edit_bone('tweak_tip_thumb_03.r'),
    get_edit_bone('tweak_finger_a_01.r'),
    get_edit_bone('tweak_finger_a_02.r'),
    get_edit_bone('tweak_finger_a_03.r'),
    get_edit_bone('tweak_tip_finger_a_03.r'),
    get_edit_bone('tweak_finger_b_01.r'),
    get_edit_bone('tweak_finger_b_02.r'),
    get_edit_bone('tweak_finger_b_03.r'),
    get_edit_bone('tweak_tip_finger_b_03.r'),
    get_edit_bone('tweak_finger_c_01.r'),
    get_edit_bone('tweak_finger_c_02.r'),
    get_edit_bone('tweak_finger_c_03.r'),
    get_edit_bone('tweak_tip_finger_c_03.r'),
    get_edit_bone('tweak_finger_d_01.r'),
    get_edit_bone('tweak_finger_d_02.r'),
    get_edit_bone('tweak_finger_d_03.r'),
    get_edit_bone('tweak_tip_finger_d_03.r'),
  ])

def add_other (map, bones):
  for bone in bones:
    unassign = True

    for value in map.values():
      if bone in value:
        unassign = False

        break
    
    if unassign:
      map['other'].add(bone)

def gen_color_map (map, scene):
  torso_color = scene.torso_color
  fk_ik_l_color = scene.fk_ik_l_color
  fk_ik_r_color = scene.fk_ik_r_color
  tweak_color = scene.tweak_color
  color_map = defaultdict(list)

  for collection_name in map.keys():
    if collection_name.startswith('tweak_'):
      color_map[tweak_color].append(collection_name)
    elif collection_name.endswith(('ik.l', 'fk.l', 'hand.l')):
      color_map[fk_ik_l_color].append(collection_name)
    elif collection_name.endswith(('ik.r', 'fk.r', 'hand.r')):
      color_map[fk_ik_r_color].append(collection_name)
    elif (
      collection_name == 'torso' or 
      collection_name == 'torso_fk' or
      collection_name == 'root'
    ):
      color_map[torso_color].append(collection_name)

  return color_map

def assign_collection (map, color_map, armature):
  pose_bones = get_pose_bones()
  visible = ['root', 'torso', 'arm_ik.l', 'arm_ik.r', 'hand.l', 'hand.r', 'leg_ik.l', 'leg_ik.r']
  # not_visible = ['def', 'org', 'mch', 'props']
  bone_collections = get_bone_collections(armature)

  for collection_name in map.keys():
    color = None

    for c, collection_names in color_map.items():
      if collection_name in collection_names:
        color = c

        break

    bones = map[collection_name]

    for bone in bones:
      if bone:
        select_bone(bone)

        if color:
          pose_bones[bone.name].color.palette = color

    if collection_name not in bone_collections:
      get_armature().collection_create_and_assign(name = collection_name)
    else:
      get_armature().collection_assign(name = collection_name)

    deselect()

  get_armature().collection_show_all()

  for collection in bone_collections:
    collection_name = collection.name
    
    if collection_name not in visible:
      bone_collections[collection_name].is_visible = False

def init_map (map, bones):
  add_org_bone(bones, map)
  add_root(map)
  add_prosp(map)
  add_torso(map)
  add_arm(map)
  add_leg(map)
  add_hand(map)
  add_other(map, bones)

def init_collection (scene):
  armature = scene.armature
  set_mode('EDIT')
  # 使用 set，而不使用 list，为了在寻找没有被分配的骨骼时节省时间
  map = defaultdict(set)
  active_object_(armature)
  bones = get_edit_bones()
  init_map(map, bones)
  color_map = gen_color_map(map, scene)
  assign_collection(map, color_map, armature)


def run_checker (
  self,
  armature
):
  passing = True
  checkers = [
    check_armature
  ]
  params = [
    [self, armature],
  ]

  for index, checker in enumerate(checkers):
    passing = checker(*params[index])

    if not passing:
      passing = False

      break

  return passing

class OBJECT_OT_init_bone_collection (get_operator()):
  bl_idname = 'object.init_bone_collection'
  bl_label = 'Init Bone Collection'

  def execute(self, context):
    scene = context.scene
    armature = scene.armature
    passing = run_checker(self, armature)

    if passing:
      init_collection(scene)

    return {'FINISHED'}
