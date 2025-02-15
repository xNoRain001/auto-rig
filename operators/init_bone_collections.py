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
  get_edit_bones
)

def assign_collection ():
  set_mode('EDIT')

  obj = {}

  for value in group.values():
    for collection_names in value:
      for collection_name in collection_names:
        obj[collection_name] = []

  bones = get_edit_bones()

  for bone in bones:
    bone_name = bone.name

    if bone_name.startswith('org_'):
      obj['org'].append(bone)
    elif bone_name.startswith('def_'):
      obj['def'].append(bone)
    elif bone_name.startswith('mch_'):
      obj['mch'].append(bone)

  obj['root'].append(get_edit_bone('root'))
  obj['props'].append(get_edit_bone('props'))
  obj['torso'].extend([
    get_edit_bone('hips'),
    get_edit_bone('chest'),
    get_edit_bone('torso'),
    get_edit_bone('neck'),
    get_edit_bone('head'),
    # get_edit_bone('org_shoulder.l'),
    # get_edit_bone('org_shoulder.r'),
  ])
  obj['torso_fk'].extend([
    get_edit_bone('fk_hips'),
    get_edit_bone('fk_spine_01'),
    get_edit_bone('fk_spine_02'),
    get_edit_bone('fk_chest'),
  ])
  obj['torso_tweak'].extend([
    get_edit_bone('tweak_hips'),
    get_edit_bone('tweak_spine_01'),
    get_edit_bone('tweak_spine_02'),
    get_edit_bone('tweak_chest'),
    get_edit_bone('tweak_neck'),
    get_edit_bone('tweak_head'),
    get_edit_bone('tweak_top_head'),
  ])
  obj['arm_fk.l'].extend([
    get_edit_bone('fk_arm.l'),
    get_edit_bone('fk_forearm.l'),
    get_edit_bone('fk_hand.l'),
  ])
  obj['arm_ik.l'].extend([
    get_edit_bone('ik_hand.l'),
    get_edit_bone('arm_pole.l'),
    get_edit_bone('vis_arm_pole.l'),
  ])
  obj['arm_tweak.l'].extend([
    get_edit_bone('tweak_arm.l'),
    get_edit_bone('tweak_forearm.l'),
    get_edit_bone('tweak_hand.l'),
    get_edit_bone('tweak_tip_hand.l'),
  ])
  obj['arm_fk.r'].extend([
    get_edit_bone('fk_arm.r'),
    get_edit_bone('fk_forearm.r'),
    get_edit_bone('fk_hand.r'),
  ])
  obj['arm_ik.r'].extend([
    get_edit_bone('ik_hand.r'),
    get_edit_bone('arm_pole.r'),
    get_edit_bone('vis_arm_pole.r'),
  ])
  obj['arm_tweak.r'].extend([
    get_edit_bone('tweak_arm.r'),
    get_edit_bone('tweak_forearm.r'),
    get_edit_bone('tweak_hand.r'),
    get_edit_bone('tweak_tip_hand.r'),
  ])

  obj['leg_fk.l'].extend([
    get_edit_bone('fk_leg.l'),
    get_edit_bone('fk_shin.l'),
    get_edit_bone('fk_foot.l'),
  ])
  obj['leg_ik.l'].extend([
    get_edit_bone('ik_foot.l'),
    get_edit_bone('leg_pole.l'),
    get_edit_bone('vis_leg_pole.l'),
    get_edit_bone('foot_heel.l')
  ])
  obj['leg_tweak.l'].extend([
    get_edit_bone('tweak_leg.l'),
    get_edit_bone('tweak_shin.l'),
    get_edit_bone('tweak_foot.l'),
  ])
  obj['leg_fk.r'].extend([
    get_edit_bone('fk_leg.r'),
    get_edit_bone('fk_shin.r'),
    get_edit_bone('fk_foot.r'),
  ])
  obj['leg_ik.r'].extend([
    get_edit_bone('ik_foot.r'),
    get_edit_bone('leg_pole.r'),
    get_edit_bone('vis_leg_pole.r'),
    get_edit_bone('foot_heel.r')
  ])
  obj['leg_tweak.r'].extend([
    get_edit_bone('tweak_leg.r'),
    get_edit_bone('tweak_shin.r'),
    get_edit_bone('tweak_foot.r'),
  ])

  toes = get_edit_bone('org_toes.l')

  if toes:
    obj['leg_fk.l'].append(get_edit_bone('fk_toes.l'))
    obj['leg_ik.l'].append(get_edit_bone('ik_toes.l'))
    obj['leg_tweak.l'].extend([
      get_edit_bone('tweak_toes.l'),
      get_edit_bone('tweak_tip_toes.l')
    ])
    obj['leg_fk.r'].append(get_edit_bone('fk_toes.r'))
    obj['leg_ik.r'].append(get_edit_bone('ik_toes.r'))
    obj['leg_tweak.r'].extend([
      get_edit_bone('tweak_toes.r'),
      get_edit_bone('tweak_tip_toes.r')
    ])
  else:
    obj['leg_tweak.l'].extend([get_edit_bone('tweak_tip_foot.l')])
    obj['leg_tweak.r'].extend([get_edit_bone('tweak_tip_foot.r')])
  
  obj['hand.l'].extend([
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
  obj['hand_tweak.l'].extend([
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
  obj['hand.r'].extend([
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
  obj['hand_tweak.r'].extend([
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

  for collection_name, bones in obj.items():
    if len(bones):
      # tweak.l | tweak.r | torso_tweak
      tweak_collection = (
        collection_name.endswith('tweak.r') or 
        collection_name.endswith('tweak.l') or 
        collection_name.endswith('tweak')
      )
      # torso | torso_fk
      torso_collection = collection_name == 'torso' or collection_name == 'torso_fk'
      # fk.l | ik.l
      ik_or_fk_collection_l = (
        collection_name.endswith('ik.l') or
        collection_name.endswith('fk.l')
      )
      # fk.r | ik.r
      ik_or_fk_collection_r = (
        collection_name.endswith('ik.r') or
        collection_name.endswith('fk.r')
      )

      palettes = ['THEME09', 'THEME04', 'THEME01', 'THEME03']
      collections_with_color = [
        tweak_collection, 
        torso_collection, 
        ik_or_fk_collection_l,
        ik_or_fk_collection_r
      ]

      index = None
      for _index, value in enumerate(collections_with_color):
        if value:
          index = _index

          break

      if index != None:
        # pose_bones = context.object.pose.bones
        pose_bones = get_edit_bones()

        for bone in bones:
          pose_bones[bone.name].color.palette = palettes[index]
        
      for bone in bones:
        select_bone(bone)
        
      # set_mode('OBJECT')
      # context.view_layer.update()
      # set_mode('EDIT')
      get_armature().collection_create_and_assign(name = collection_name)
      deselect()

class OBJECT_OT_init_bone_collection (get_operator()):
  bl_idname = 'object.init_bone_collection'
  bl_label = 'Init Bone Collection'

  def execute(self, context):
    assign_collection()

    return {'FINISHED'}
