from ..libs.blender_utils import (
  get_operator, 
  get_selected_bone, 
  get_edit_bone, 
  copy_bone, 
  set_parent,
  set_mode, 
  get_pose_bone, 
  add_armature_constraint, 
  add_copy_transforms_constraint,
  get_active_object
)
from ..patch.add_custom_props import add_custom_props
from ..bones import _init_bones
from ..bones.init_parent import _init_parent
from ..constraints import _init_constraints
from ..drivers import _init_drivers
from ..patch.add_custom_props import _add_custom_props

def gen_custom_props_config (weapon_name):
  custom_props_config =[
    {
      'prop_name': f'{ weapon_name }_parent',
      'config': {
        'min': 0,
        'max': 2,
        'description': '0-root | 1-hand.l | 2-hand.r',
        'default': 0
      },
      'is_visible': True
    },
    {
      'prop_name': f'{ weapon_name }_to_master',
      'config': {
        'default': False
      },
      'is_visible': True
    },
    {
      'prop_name': f'{ weapon_name }_master_parent',
      'config': {
        'min': 0,
        'max': 1,
        'description': '0-root | 1-torso',
        'default': 0
      },
      'is_visible': True
    }
  ]

  return custom_props_config

def rig_weapon (weapon):
  _add_custom_props(gen_custom_props_config(weapon))

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
            'name': f'{ weapon }_to_master',
            'targets': [
              {
                'id_type': 'OBJECT',
                'data_path': f'pose.bones["props"]["{ weapon }_to_master"]'
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
            'name': f'{ weapon }_to_master',
            'targets': [
              {
                'id_type': 'OBJECT',
                'data_path': f'pose.bones["props"]["{ weapon }_to_master"]'
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
                'data_path': f'pose.bones["props"]["{ weapon }_master_parent"]'
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
            'name': f'{ weapon }_parent',
            'targets': [
              {
                'id_type': 'OBJECT',
                'data_path': f'pose.bones["props"]["{ weapon }_parent"]'
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
            'name': f'{ weapon }_to_master',
            'targets': [
              {
                'id_type': 'OBJECT',
                'data_path': f'pose.bones["props"]["{ weapon }_to_master"]'
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
    weapon_bone = get_selected_bone()
    rig_weapon(weapon_bone.name)

    return {'FINISHED'}
