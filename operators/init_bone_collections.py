from collections import defaultdict

from ..const import group
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
  get_object_
)

def gen_map ():
  map = {}

  for value in group.values():
    for collection_names in value:
      for collection_name in collection_names:
        map[collection_name] = []

  return map

def add_org_bone (bones, map):
  for bone in bones:
    bone_name = bone.name

    if bone_name.startswith('org_'):
      map['org'].append(bone)
    elif bone_name.startswith('def_'):
      map['def'].append(bone)
    elif bone_name.startswith('mch_'):
      map['mch'].append(bone)

def add_root (map):
  map['root'].append(get_edit_bone('root'))

def add_prosp (map):
  map['props'].append(get_edit_bone('props'))

def add_torso (map):
  map['torso'].extend([
    get_edit_bone('hips'),
    get_edit_bone('chest'),
    get_edit_bone('torso'),
    get_edit_bone('neck'),
    get_edit_bone('head'),
    get_edit_bone('shoulder.l'),
    get_edit_bone('shoulder.r'),
  ])
  map['torso_fk'].extend([
    get_edit_bone('fk_hips'),
    get_edit_bone('fk_spine_01'),
    get_edit_bone('fk_spine_02'),
    get_edit_bone('fk_chest'),
  ])
  map['torso_tweak'].extend([
    get_edit_bone('tweak_hips'),
    get_edit_bone('tweak_spine_01'),
    get_edit_bone('tweak_spine_02'),
    get_edit_bone('tweak_chest'),
    get_edit_bone('tweak_neck'),
    get_edit_bone('tweak_head'),
    get_edit_bone('tweak_top_head'),
  ])

def add_arm (map):
  map['arm_fk.l'].extend([
    get_edit_bone('fk_arm.l'),
    get_edit_bone('fk_forearm.l'),
    get_edit_bone('fk_hand.l'),
  ])
  map['arm_ik.l'].extend([
    get_edit_bone('ik_hand.l'),
    get_edit_bone('arm_pole.l'),
    get_edit_bone('vis_arm_pole.l'),
  ])
  map['arm_tweak.l'].extend([
    get_edit_bone('tweak_arm.l'),
    get_edit_bone('tweak_forearm.l'),
    get_edit_bone('tweak_hand.l'),
    get_edit_bone('tweak_tip_hand.l'),
  ])
  map['arm_fk.r'].extend([
    get_edit_bone('fk_arm.r'),
    get_edit_bone('fk_forearm.r'),
    get_edit_bone('fk_hand.r'),
  ])
  map['arm_ik.r'].extend([
    get_edit_bone('ik_hand.r'),
    get_edit_bone('arm_pole.r'),
    get_edit_bone('vis_arm_pole.r'),
  ])
  map['arm_tweak.r'].extend([
    get_edit_bone('tweak_arm.r'),
    get_edit_bone('tweak_forearm.r'),
    get_edit_bone('tweak_hand.r'),
    get_edit_bone('tweak_tip_hand.r'),
  ])

def add_leg (map):
  map['leg_fk.l'].extend([
    get_edit_bone('fk_leg.l'),
    get_edit_bone('fk_shin.l'),
    get_edit_bone('fk_foot.l'),
  ])
  map['leg_ik.l'].extend([
    get_edit_bone('ik_foot.l'),
    get_edit_bone('leg_pole.l'),
    get_edit_bone('vis_leg_pole.l'),
    get_edit_bone('foot_heel.l')
  ])
  map['leg_tweak.l'].extend([
    get_edit_bone('tweak_leg.l'),
    get_edit_bone('tweak_shin.l'),
    get_edit_bone('tweak_foot.l'),
  ])
  map['leg_fk.r'].extend([
    get_edit_bone('fk_leg.r'),
    get_edit_bone('fk_shin.r'),
    get_edit_bone('fk_foot.r'),
  ])
  map['leg_ik.r'].extend([
    get_edit_bone('ik_foot.r'),
    get_edit_bone('leg_pole.r'),
    get_edit_bone('vis_leg_pole.r'),
    get_edit_bone('foot_heel.r')
  ])
  map['leg_tweak.r'].extend([
    get_edit_bone('tweak_leg.r'),
    get_edit_bone('tweak_shin.r'),
    get_edit_bone('tweak_foot.r'),
  ])

  toes = get_edit_bone('org_toes.l')

  if toes:
    map['leg_fk.l'].append(get_edit_bone('fk_toes.l'))
    map['leg_ik.l'].append(get_edit_bone('ik_toes.l'))
    map['leg_tweak.l'].extend([
      get_edit_bone('tweak_toes.l'),
      get_edit_bone('tweak_tip_toes.l')
    ])
    map['leg_fk.r'].append(get_edit_bone('fk_toes.r'))
    map['leg_ik.r'].append(get_edit_bone('ik_toes.r'))
    map['leg_tweak.r'].extend([
      get_edit_bone('tweak_toes.r'),
      get_edit_bone('tweak_tip_toes.r')
    ])
  else:
    map['leg_tweak.l'].extend([get_edit_bone('tweak_tip_foot.l')])
    map['leg_tweak.r'].extend([get_edit_bone('tweak_tip_foot.r')])

def add_hand (map):
  map['hand.l'].extend([
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
  map['hand_tweak.l'].extend([
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
  map['hand.r'].extend([
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
  map['hand_tweak.r'].extend([
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

def gen_color_map (map):
  # TODO: UI 选择颜色
  color_map = defaultdict(list)

  for collection_name in map.keys():
    if collection_name.endswith(('tweak.r', 'tweak.l', 'tweak')):
      color_map['THEME04'].append(collection_name)
    elif collection_name.endswith(('ik.l', 'fk.l')):
      color_map['THEME01'].append(collection_name)
    elif collection_name.endswith(('ik.r', 'fk.r')):
      color_map['THEME03'].append(collection_name)
    elif collection_name == 'torso' or collection_name == 'torso_fk':
      color_map['THEME09'].append(collection_name)

  return color_map

def assign_collection (map, color_map):
  pose_bones = get_pose_bones()
  not_visible = ['def', 'org', 'mch', 'prop']
  collections_all = get_context().object.data.collections_all

  for collection_name in map.keys():
    color = color_map[collection_name] if collection_name in color_map else None
    bones = map[collection_name]

    for bone in bones:
      if bone:
        select_bone(bone)
      if color:
        pose_bones[bone.name].color.palette = color

    get_armature().collection_create_and_assign(name = collection_name)
    deselect()

    if collection_name in not_visible:
      collections_all[collection_name].is_visible = False

def init_collection (armature_name):
  set_mode('EDIT')
  map = gen_map()
  active_object_(get_object_(armature_name))
  bones = get_edit_bones()
  add_org_bone(bones, map)
  add_root(map)
  add_prosp(map)
  add_torso(map)
  add_arm(map)
  add_leg(map)
  add_hand(map)
  color_map = gen_color_map(map)
  assign_collection(map, color_map)

class OBJECT_OT_init_bone_collection (get_operator()):
  bl_idname = 'object.init_bone_collection'
  bl_label = 'Init Bone Collection'

  def execute(self, context):
    armature_name = context.scene.armature_name
    init_collection(armature_name)

    return {'FINISHED'}
