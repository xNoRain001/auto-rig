import json
from ..libs.blender_utils import (
  set_mode,
  get_operator, 
  report_error,
  get_pose_bone
)

from ..bones import init_bones
from ..parent import init_bones_parent
from ..drivers import _init_drivers
from ..constraints import init_bone_constraints
from ..bone_patch.add_custom_props import _add_custom_props
from ..scene.add_weapon_props import add_weapon_props
from ..hooks.init_bone_collections import move_bones_to_collection
from ..const import (
  mch_collection,
  weapons_collection,
  weapon_custom_prop_prefix,
)

def update_weapons (weapon_name):
  props_bone = get_pose_bone('props')

  if 'weapons' not in props_bone:
    props_bone['weapons'] = '[]'

  weapons = json.loads(props_bone['weapons'])
  weapons.append(weapon_name)
  props_bone['weapons'] = json.dumps(weapons)

def gen_custom_props_config (weapon_name):
  custom_props_config =[
    {
      'prop_name': f'{ weapon_custom_prop_prefix }{ weapon_name }_parent',
      'config': {
        'min': 0,
        'max': 2,
        'description': json.dumps(['root', 'ik_hand.l', 'ik_hand.r']),
        'default': 0
      }
    },
    {
      'prop_name': f'{ weapon_custom_prop_prefix }{ weapon_name }_to_master',
      'config': {
        'default': False
      }
    },
    {
      'prop_name': f'{ weapon_custom_prop_prefix }{ weapon_name }_master_parent',
      'config': {
        'min': 0,
        'max': 1,
        'description': json.dumps(['root', 'torso']),
        'default': 0,
      }
    }
  ]

  return custom_props_config

def rig_weapon (weapon):
  update_weapons(weapon)
  custom_prop_config = gen_custom_props_config(weapon)
  _add_custom_props(custom_prop_config)
  mch_parent_weapon = f'mch_parent_{ weapon }'
  mch_parent_weapon_to_master = f'mch_parent_{ weapon }_to_master'
  weapon_master = f'{ weapon }_master'
  mch_parent_weapon_master = f'mch_parent_{ weapon }_master'
  # 新创建的
  mch_parent_ik_to_master_l = f'mch_parent_ik_to_{ weapon }_master.l'
  mch_parent_ik_to_master_r = f'mch_parent_ik_to_{ weapon }_master.r'
  # 原本就存在的
  mch_parent_ik_hand_l = 'mch_parent_ik_hand.l'
  mch_parent_ik_hand_r = 'mch_parent_ik_hand.r'

  bone_config = [
    {
      'name': mch_parent_weapon,
      'source': weapon,
      'collection': mch_collection,
      'operator': 'copy',
      'operator_config': {
        'scale': 0.5
      }
    },
    {
      'name': mch_parent_weapon_to_master,
      'source': weapon,
      'collection': mch_collection,
      'operator': 'copy',
      'operator_config': {
        'scale': 0.5
      }
    },
    {
      'name': weapon_master,
      'source': weapon,
      'collection': weapons_collection,
      'operator': 'copy',
      'operator_config': {
        'scale': 0.5
      }
    },
    {
      'name': mch_parent_weapon_master,
      'source': weapon,
      'collection': mch_collection,
      'operator': 'copy',
      'operator_config': {
        'scale': 0.5
      }
    },
    {
      'name': mch_parent_ik_to_master_l,
      'source': weapon,
      'collection': mch_collection,
      'operator': 'copy',
      'operator_config': {
        'scale': 0.5
      }
    },
    {
      'name': mch_parent_ik_to_master_r,
      'source': weapon,
      'collection': mch_collection,
      'operator': 'copy',
      'operator_config': {
        'scale': 0.5
      }
    }
  ]
  parent_config = [
    [mch_parent_ik_to_master_l, weapon_master, False],
    [mch_parent_ik_to_master_r, weapon_master, False],
    [weapon, mch_parent_weapon, False],
    [mch_parent_weapon_to_master, weapon_master, False],
    [weapon_master, mch_parent_weapon_master, False]
  ]
  constraint_config = [
    {
      'name': mch_parent_weapon_master,
      'type': 'ARMATURE',
      'config': {
        'subtarget': ['root', 'torso']
      }
    },
    {
      'name': mch_parent_weapon,
      'type': 'ARMATURE',
      'config': {
        'subtarget': ['root', 'org_hand.l', 'org_hand.r']
      }
    },
    {
      'name': mch_parent_weapon,
      'type': 'COPY_TRANSFORMS',
      'config': {
        'subtarget': mch_parent_weapon_to_master
      }
    },
    {
      'name': mch_parent_ik_hand_l,
      'type': 'COPY_TRANSFORMS',
      'config': {
        'subtarget': mch_parent_ik_to_master_l
      }
    },
    {
      'name': mch_parent_ik_hand_r,
      'type': 'COPY_TRANSFORMS',
      'config': {
        'subtarget': mch_parent_ik_to_master_r
      }
    }
  ]
  driver_config = [
    {
      'name': mch_parent_ik_hand_l,
      'index': -1,
      'config': {
        'name': 'influence',
        'type': 'AVERAGE',
        'vars': [
          {
            'name': f'{ weapon_custom_prop_prefix + weapon }_to_master',
            'targets': [
              {
                'id_type': 'OBJECT',
                'data_path': f'pose.bones["props"]["{ weapon_custom_prop_prefix + weapon }_to_master"]'
              }
            ]
          }
        ]
      }
    },
    {
      'name': mch_parent_ik_hand_r,
      'index': -1,
      'config': {
        'name': 'influence',
        'type': 'AVERAGE',
        'vars': [
          {
            'name': f'{ weapon_custom_prop_prefix + weapon }_to_master',
            'targets': [
              {
                'id_type': 'OBJECT',
                'data_path': f'pose.bones["props"]["{ weapon_custom_prop_prefix + weapon }_to_master"]'
              }
            ]
          }
        ]
      }
    },
    {
      'name': mch_parent_weapon_master,
      'index': 0,
      'config': {
        'name': 'weight',
        'type': 'SCRIPTED',
        'vars': [
          {
            'name': 'master_parent',
            'targets': [
              {
                'id_type': 'OBJECT',
                'data_path': f'pose.bones["props"]["{ weapon_custom_prop_prefix + weapon }_master_parent"]'
              }
            ]
          }
        ]
      }
    },
    {
      'name': mch_parent_weapon,
      'index': 0,
      'config': {
        'name': 'weight',
        'type': 'SCRIPTED',
        'vars': [
          {
            'name': f'{ weapon_custom_prop_prefix + weapon }_parent',
            'targets': [
              {
                'id_type': 'OBJECT',
                'data_path': f'pose.bones["props"]["{ weapon_custom_prop_prefix + weapon }_parent"]'
              }
            ]
          }
        ]
      }
    },
    {
      'name': mch_parent_weapon,
      'index': -1,
      'config': {
        'name': 'influence',
        'type': 'AVERAGE',
        'vars': [
          {
            'name': f'{ weapon_custom_prop_prefix + weapon }_to_master',
            'targets': [
              {
                'id_type': 'OBJECT',
                'data_path': f'pose.bones["props"]["{ weapon_custom_prop_prefix + weapon }_to_master"]'
              }
            ]
          }
        ]
      }
    },
  ]
  
  init_bones(bone_config)
  init_bones_parent(parent_config)
  init_bone_constraints(constraint_config)
  _init_drivers(driver_config)
  add_weapon_props([weapon])

  return bone_config

def common_move_bones_to_collection (bone_config):
  for config in bone_config:
    bone_name = config['name']
    collection = config['collection']
    move_bones_to_collection(collection, bone_name)

def assign_collection (bone_config, weapon):
  move_bones_to_collection(weapons_collection, weapon)
  common_move_bones_to_collection(bone_config)

def check_weapon (self, weapon):
  passing = True

  if not weapon:
    passing = False
    report_error(self, 'weapon 不存在')
    
  return passing
  
def run_checker (self, context):
  scene = context.scene
  weapon = scene.weapon
  passing = True
  checkers = [check_weapon]
  params = [[self, weapon]]

  for index, checker in enumerate(checkers):
    passing = checker(*params[index])

    if not passing:
      passing = False

      break

  return passing

class OBJECT_OT_rig_weapon (get_operator()):
  bl_idname = "object.rig_weapon"
  bl_label = "Rig Weapon"

  def invoke(self, context, event):
    passing = run_checker(self, context)
  
    if passing:
      return self.execute(context)
    else:
      return {'CANCELLED'}

  def execute(self, context):
    set_mode('EDIT')
    weapon = context.scene.weapon
    bone_config = rig_weapon(weapon)
    assign_collection(bone_config, weapon)

    return {'FINISHED'}
