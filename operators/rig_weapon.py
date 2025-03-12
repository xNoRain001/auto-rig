from ..libs.blender_utils import (
  get_operator, 
  get_selected_bone, 
  get_pose_bone, 
  get_mode,
  set_mode
)
from ..bones import _init_bones
from ..bones.init_parent import _init_parent
from ..constraints import _init_constraints
from ..drivers import _init_drivers
from ..patch.add_custom_props import _add_custom_props
from ..scene.add_weapon_props import add_weapon_props
import json
from ..const import weapon_custom_prop_prefix

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

def rig_weapon (weapon_bone, armature):
  weapon = weapon_bone.name
  update_weapons(weapon)
  custom_prop_config = gen_custom_props_config(weapon)
  _add_custom_props(custom_prop_config)
  add_weapon_props([weapon])
  mch_parent_weapon = f'mch_parent_{ weapon }'
  mch_parent_weapon_to_master = f'mch_parent_{ weapon }_to_master'
  weapon_master = f'{ weapon }_master'
  mch_parent_weapon_master = f'mch_parent_{ weapon }_master'
  # 新创建的
  mch_parent_ik_to_master_l = 'mch_parent_ik_to_master.l'
  mch_parent_ik_to_master_r = 'mch_parent_ik_to_master.r'
  # 原本就存在的
  mch_parent_ik_hand_l = 'mch_parent_ik_hand.l'
  mch_parent_ik_hand_r = 'mch_parent_ik_hand.r'

  bone_config = [
    {
      'name': mch_parent_weapon,
      'source': weapon,
      'operator': 'copy',
      'operator_config': {
        'scale': 0.5
      }
    },
    {
      'name': mch_parent_weapon_to_master,
      'source': weapon,
      'operator': 'copy',
      'operator_config': {
        'scale': 0.5
      }
    },
    {
      'name': weapon_master,
      'source': weapon,
      'operator': 'copy',
      'operator_config': {
        'scale': 0.5
      }
    },
    {
      'name': mch_parent_weapon_master,
      'source': weapon,
      'operator': 'copy',
      'operator_config': {
        'scale': 0.5
      }
    },
    {
      'name': mch_parent_ik_to_master_l,
      'source': weapon,
      'operator': 'copy',
      'operator_config': {
        'scale': 0.5
      }
    },
    {
      'name': mch_parent_ik_to_master_r,
      'source': weapon,
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
      'target': ['root', 'torso'],
      'type': 'ARMATURE',
    },
    {
      'name': mch_parent_weapon,
      'target': ['root', 'org_hand.l', 'org_hand.r'],
      'type': 'ARMATURE',
    },
    {
      'name': mch_parent_weapon,
      'target': mch_parent_weapon_to_master,
      'type': 'COPY_TRANSFORMS',
    },
    {
      'name': mch_parent_ik_hand_l,
      'target': mch_parent_ik_to_master_l,
      'type': 'COPY_TRANSFORMS',
    },
    {
      'name': mch_parent_ik_hand_r,
      'target': mch_parent_ik_to_master_r,
      'type': 'COPY_TRANSFORMS',
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
  
  _init_bones(bone_config)
  _init_parent(parent_config)
  _init_constraints(constraint_config)
  _init_drivers(driver_config)

class OBJECT_OT_rig_weapon (get_operator()):
  bl_idname = "object.rig_weapon"
  bl_label = "Rig Weapon"

  # def invoke(self, context, event):
  #   passing = run_checker(self, context)
  
  #   if passing:
  #     return self.execute(context)
  #   else:
  #     return {'CANCELLED'}

  def execute(self, context):
    # 编辑模式下
    mode = get_mode()
    if mode == 'POSE':
      set_mode('EDIT')

    weapon_bone = get_selected_bone()
    rig_weapon(weapon_bone, context.scene.armature)

    return {'FINISHED'}
