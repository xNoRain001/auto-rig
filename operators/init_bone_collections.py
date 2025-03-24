from collections import defaultdict
from ..libs.blender_utils import (
  set_mode, 
  get_edit_bone, 
  select_bone, 
  deselect_bones, 
  get_armature, 
  get_operator,
  get_edit_bones,
  get_pose_bones,
  active_object_,
  get_bone_collections,
  get_active_object,
  update_view,
  get_pose_bone
)
from .bone_wiggle import check_armature

def add_org_bone (bones, map):
  for bone in bones:
    bone_name = bone.name

    if bone_name.startswith('org_'):
      map['org'].add(bone_name)
    elif bone_name.startswith('def_'):
      map['def'].add(bone_name)
    elif bone_name.startswith('mch_'):
      map['mch'].add(bone_name)

def add_root (map):
  map['root'].add('root')

def add_prosp (map):
  map['props'].add('props')

def add_torso (map):
  map['torso'].update([
    'hips',
    'chest',
    'torso',
    'neck',
    'head',
    'shoulder.l',
  ])
  map['torso_fk'].update([
    'fk_hips',
    'fk_spine_01',
    'fk_spine_02',
    'fk_chest',
  ])
  map['tweak_torso'].update([
    'tweak_hips',
    'tweak_spine_01',
    'tweak_spine_02',
    'tweak_chest',
    'tweak_neck',
    'tweak_head',
    'tweak_top_head',
  ])

def add_arm (map):
  map['arm_fk.l'].update([
    'fk_arm.l',
    'fk_forearm.l',
    'fk_hand.l',
  ])
  map['arm_ik.l'].update([
    'ik_hand.l',
    'arm_pole.l',
    'vis_arm_pole.l',
  ])
  map['tweak_arm.l'].update([
    'tweak_arm.l',
    'tweak_forearm.l',
    'tweak_hand.l',
    'tweak_tip_hand.l',
    'tweak_arm_01.l',
    'tweak_arm_02.l',
    'tweak_arm_03.l',
    'tweak_arm_04.l',
    'tweak_forearm_01.l',
    'tweak_forearm_02.l',
    'tweak_forearm_03.l',
    'tweak_forearm_04.l',
  ])

def add_leg (map):
  map['leg_fk.l'].update([
    'fk_leg.l',
    'fk_shin.l',
    'fk_foot.l',
  ])
  map['leg_ik.l'].update([
    'ik_foot.l',
    'leg_pole.l',
    'vis_leg_pole.l',
    'foot_heel.l'
  ])
  map['tweak_leg.l'].update([
    'tweak_leg.l',
    'tweak_shin.l',
    'tweak_foot.l',
  ])

  toes = get_edit_bone('org_toes.l')

  if toes:
    map['leg_fk.l'].add('fk_toes.l')
    map['leg_ik.l'].add('ik_toes.l')
    map['tweak_leg.l'].update([
      'tweak_toes.l',
      'tweak_tip_toes.l'
    ])
  else:
    map['tweak_leg.l'].update(['tweak_tip_foot.l'])

def add_hand (map):
  map['hand.l'].update([
    'thumb_01.l',
    'thumb_02.l',
    'thumb_03.l',
    'finger_a_01.l',
    'finger_a_02.l',
    'finger_a_03.l',
    'finger_b_01.l',
    'finger_b_02.l',
    'finger_b_03.l',
    'finger_c_01.l',
    'finger_c_02.l',
    'finger_c_03.l',
    'finger_d_01.l',
    'finger_d_02.l',
    'finger_d_03.l',
  ])
  map['tweak_hand.l'].update([
    'tweak_thumb_01.l',
    'tweak_thumb_02.l',
    'tweak_thumb_03.l',
    'tweak_tip_thumb_03.l',
    'tweak_finger_a_01.l',
    'tweak_finger_a_02.l',
    'tweak_finger_a_03.l',
    'tweak_tip_finger_a_03.l',
    'tweak_finger_b_01.l',
    'tweak_finger_b_02.l',
    'tweak_finger_b_03.l',
    'tweak_tip_finger_b_03.l',
    'tweak_finger_c_01.l',
    'tweak_finger_c_02.l',
    'tweak_finger_c_03.l',
    'tweak_tip_finger_c_03.l',
    'tweak_finger_d_01.l',
    'tweak_finger_d_02.l',
    'tweak_finger_d_03.l',
    'tweak_tip_finger_d_03.l',
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

def gen_color_map (scene, bone_collections):
  torso_color = scene.torso_color
  fk_ik_l_color = scene.fk_ik_l_color
  fk_ik_r_color = scene.fk_ik_r_color
  tweak_color = scene.tweak_color
  color_map = {}

  for bone_collection in bone_collections:
    collection_name = bone_collection.name

    if collection_name.startswith('tweak_'):
      color_map[collection_name] = tweak_color
    elif collection_name.endswith(('ik.l', 'fk.l', 'hand.l')):
      color_map[collection_name] = fk_ik_l_color
    elif collection_name.endswith(('ik.r', 'fk.r', 'hand.r')):
      color_map[collection_name] = fk_ik_r_color
    elif (
      collection_name == 'torso' or 
      collection_name == 'torso_fk' or
      collection_name == 'root'
    ):
      color_map[collection_name] = torso_color

  return color_map

def assign_bone_to_collection (collection_name, bone_collections):
  if collection_name not in bone_collections:
    get_armature().collection_create_and_assign(name = collection_name)
  else:
    get_armature().collection_assign(name = collection_name)

  deselect_bones()

def assign_collection (map, bone_collections):
  visible = [
    'root', 'torso', 'arm_ik.l', 'arm_ik.r', 'hand.l', 'hand.r', 'leg_ik.l', 
    'leg_ik.r'
  ]
  # not_visible = ['def', 'org', 'mch', 'props']

  for collection_name, bone_names in map.items():
    for bone_name in bone_names:
      bone = get_edit_bone(bone_name)

      if bone:
        select_bone(bone)

    assign_bone_to_collection(collection_name, bone_collections)

    if collection_name.endswith('.l'):
      mirror_collection_name = collection_name.replace('.l', '.r')

      for bone_name in bone_names:
        if bone_name.endswith('.l'):
          mirror_bone = get_edit_bone(bone_name.replace('.l', '.r'))

          if mirror_bone:
            select_bone(mirror_bone)

      assign_bone_to_collection(mirror_collection_name, bone_collections)

  get_armature().collection_show_all()

  for collection in bone_collections:
    collection_name = collection.name
    
    if collection_name not in visible:
      bone_collections[collection_name].is_visible = False

def init_map ():
  bones = get_edit_bones()
  # 使用 set，而不使用 list，为了在寻找没有被分配的骨骼时节省时间
  map = defaultdict(set)
  add_org_bone(bones, map)
  add_root(map)
  add_prosp(map)
  add_torso(map)
  add_arm(map)
  add_leg(map)
  add_hand(map)
  # add_other(map, bones)

  return map

def init_bone_colors (scene, bone_collections):
  set_mode('POSE')
  pose_bones = get_pose_bones()
  color_map = gen_color_map(scene, bone_collections)

  for pose_bone in pose_bones:
    collections = pose_bone.bone.collections

    if not len(collections):
      continue

    collection_name = collections[0].name
    color = color_map.get(collection_name)

    if color:
      pose_bone.color.palette = color

def init_bone_collections (scene):
  armature = scene.armature
  set_mode('EDIT')
  active_object_(armature)
  map = init_map()
  bone_collections = get_bone_collections(armature)
  assign_collection(map, bone_collections)
  init_bone_colors(scene, bone_collections)

def run_checker (
  self,
  armature
):
  passing = True
  checkers = [check_armature]
  params = [[self, armature]]

  for index, checker in enumerate(checkers):
    passing = checker(*params[index])

    if not passing:
      passing = False

      break

  return passing

class OBJECT_OT_init_bone_collections (get_operator()):
  bl_idname = 'object.init_bone_collections'
  bl_label = 'Init Bone Collections'

  # def invoke(self, context, event):
  #   armature = context.scene.armature
  #   passing = run_checker(self, armature)
  
  #   if passing:
  #     return self.execute(context)
  #   else:
  #     return {'CANCELLED'}

  def execute(self, context):
    init_bone_collections(context.scene)

    return {'FINISHED'}
