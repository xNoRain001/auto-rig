def init_arm ():
  config = []
  org_bone_names = ['org_arm.l', 'org_forearm.l', 'org_hand.l']
  no_mch_prefix_set = set(['org_hand.l'])
  last_index = len(org_bone_names) - 1

  for index, org_bone_name in enumerate(org_bone_names):
    config.extend([
      # mch switch bone
      {
        'name': org_bone_name.replace('org_', 'mch_switch_'),
        'source': org_bone_name,
        'operator': 'copy',
        'operator_config': {
          'scale_factor': 1
        }
      },
      # fk bone
      {
        'name': org_bone_name.replace('org_', 'fk_'),
        'source': org_bone_name,
        'operator': 'copy',
        'operator_config': {
          'scale_factor': 1
        }
      },
      # (mch) ik bone
      {
        'name': org_bone_name.replace(
          'org_', 
          f'{ "" if org_bone_name in no_mch_prefix_set else "mch_" }ik_'
        ),
        'source': org_bone_name,
        'operator': 'copy',
        'operator_config': {
          'scale_factor': 1
        }
      },
      # tweak bone
      {
        'name': org_bone_name.replace('org_', 'tweak_'),
        'source': org_bone_name,
        'operator': 'copy',
        'operator_config': {
          'scale_factor': 0.5
        }
      }
    ])

    # mch tweak bone
    if index > 0: # tweak_arm 不需要 mch_tweak_leg 处理缩放
      config.append({
        'name': org_bone_name.replace('org_', 'mch_tweak_'),
        'source': org_bone_name,
        'operator': 'copy',
        'operator_config': {
          'scale_factor': 0.25
        }
      })

    # tweak tip
    if index == last_index:
      config.append({
        'name': org_bone_name.replace('org_', 'tweak_tip_'),
        'source': org_bone_name,
        'operator': 'extrude',
        'operator_config': {
          'head_or_tail': 'tail',
          'scale_factor': (0, 0.5, 0)
        }
      })

  config.extend([
    # 生成极向目标的临时骨骼，它将沿着 mch_ik_arm.l 的法向移动
    {
      'name': 'mch_ik_arm.l.001',
      'source': 'mch_ik_arm.l',
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 1
      },
      # 标识类型
      'pole_target_type': 'arm',
    },
    # pole bone
    {
      'name': 'arm_pole.l',
      'source': 'mch_ik_arm.l.001',
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'tail',
        'scale_factor': (0, 0.1, 0)
      }
    },
    # ik 动态父级时，arm_pole.l 将复制 mch_parent_arm_pole.l 的变换
    {
      'name': 'mch_parent_arm_pole.l',
      'source': 'arm_pole.l',
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5
      }
    },
    # mch_ik_arm.l 到 arm_pole.l 之间的一条直线
    {
      'name': 'vis_arm_pole.l',
      'source': 'mch_ik_arm.l',
      'operator': 'extrude',
      'operator_config': {
        'target': 'arm_pole.l',
        'head_or_tail': 'tail',
        'target_head_or_tail': 'tail'
      }
    },
    # fk_arm.l 的 pole，当 fk 切换到 ik 时，ik 的 pole 会修改位置为 fk 的 pole
    {
      'name': 'mch_ik_fk_arm_pole.l',
      'source': 'arm_pole.l',
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.25
      }
    },
    # 用于实现 ik_hand.l 动态父级
    {
      'name': 'mch_parent_ik_hand.l',
      'source': 'ik_hand.l',
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5
      }
    },
  ])

  org_tweak_bone_names = [
    'org_arm_01.l', 'org_arm_02.l', 'org_arm_03.l', 'org_arm_04.l',
    'org_forearm_01.l', 'org_forearm_02.l', 'org_forearm_03.l', 'org_forearm_04.l'
  ]

  for org_tweak_bone_name in org_tweak_bone_names:
    config.append({
      'name': org_tweak_bone_name.replace('org_', 'tweak_'),
      'source': org_tweak_bone_name,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5
      }
    })

  # twist bones
  config.extend([
    {
      'name': 'mch_arm.l',
      'source': 'org_arm.l',
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'head',
        'scale_factor': (0, 0, 0.25)
      }
    },
    {
      'name': 'mch_int_arm.l',
      'source': 'mch_arm.l',
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5
      }
    },
    {
      'name': 'mch_twist_arm.l',
      'source': 'org_arm.l',
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'head',
        'scale_factor': (0, 0, -0.25)
      }
    }
  ])

  return config
