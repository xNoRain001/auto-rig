from ..libs.blender_utils import (
  get_operator, 
  get_selected_bones,
  set_mode,
  get_edit_bone,
  get_mode,
  report_warning,
  is_pose_mode,
  get_selected_pose_bones,
  get_armature,
  select_bone,
  deselect,
  get_bone_collections,
  get_bone_chain_names,
  deselect_bones,
  report_error,
  get_active_object
)
from ..bone_patch.add_custom_props import _add_custom_props
from ..bones.init_org_bones import init_org_bones
from ..constraints import def_bone_add_copy_transforms
from ..bones import _init_bones
from ..bones.init_parent import _init_parent
from ..constraints import _init_constraints
from ..drivers import _init_drivers

def get_bone_names ():
  # 可能在 POSE 模式下选中骨骼
  set_mode('EDIT')
  bones = get_selected_bones()
  bone_names = []

  for bone in bones:
    bone_names.append(bone.name)

  for bone_name in bone_names:
    if bone_name.startswith('def_'):
      init_org_bones()
      def_bone_add_copy_transforms()

      break

  for index, bone_name in enumerate(bone_names):
    if bone_name.startswith('def_'):
      bone_names[index] = bone_name.replace('def_', 'org_')

  return bone_names

def check_armature (self, armature):
  passing = True

  if not armature:
    passing = False
    report_warning(self, 'Armature 不能为空')

  return passing

def check_wiggle_prop (self, wiggle_prop):
  passing = True

  if not wiggle_prop:
    passing = False
    report_warning(self, '控制摆动强度的自定义属性不能为空')

  return passing

def check_selected_bones (self):
  passing = True
  selected_bones = get_selected_pose_bones() if is_pose_mode() else get_selected_bones()
  print(selected_bones)

  # OBJECT 模式下 selected_bones 为 None
  if not selected_bones or not len(selected_bones):
    passing = False
    report_warning(self, '没有选中骨骼')
  else:
    for selected_bone in selected_bones:
      if not selected_bone.name.startswith(('def_', 'org_')):
        passing = False
        report_warning(self, '选中的骨骼中存在名称不以 def_ 或 org_ 开头的骨骼')

        break

  return passing

def run_checker (self, context):
  scene = context.scene
  armature = scene.armature
  wiggle_prop = scene.wiggle_prop
  passing = True
  checkers = [
    check_armature,
    check_wiggle_prop, 
    check_selected_bones
  ]
  params = [
    [self, armature],
    [self, wiggle_prop],
    [self]
  ]

  for index, checker in enumerate(checkers):
    passing = checker(*params[index])

    if not passing:
      passing = False

      break

  return passing

def create_bone_collections (names, bone_collections):
  deselect()

  for name in names:
    if not bone_collections.get(name):
      get_armature().collection_create_and_assign(name = name)

def assign_collection (bone_config, armature):
  set_mode('EDIT')
  bone_collections = get_bone_collections(armature)
  # create_bone_collections(['phy', 'mch', 'def', 'org'], bone_collections)

  for item in bone_config:
    bone_name = item['name']
    bone = get_edit_bone(bone_name)
    select_bone(bone)

    if bone_name.startswith('phy_'):
      get_armature().collection_unassign_named(name = 'other', bone_name = bone_name)
      get_armature().collection_assign(name = 'phy')
    elif bone_name.startswith('mch_'):
      get_armature().collection_unassign_named(name = 'other', bone_name = bone_name)
      get_armature().collection_assign(name = 'mch')
    elif bone_name.startswith('def_'):
      get_armature().collection_unassign_named(name = 'other', bone_name = bone_name)
      get_armature().collection_assign(name = 'def')
    elif bone_name.startswith('org_'):
      get_armature().collection_unassign_named(name = 'other', bone_name = bone_name)
      get_armature().collection_assign(name = 'org')

    deselect()

def init_wiggle (scene):
  bone_config = []
  parent_config = []
  constraint_config = []
  driver_config = []
  selected_bone_names = get_bone_names()
  wiggle_prop = scene.wiggle_prop
  wiggle_influence = scene.wiggle_influence
  # TODO: 分配集合

  set_mode('EDIT')

  for selected_bone_name in selected_bone_names:
    bone = get_edit_bone(selected_bone_name)
    root = bone.parent.name
    bone_names = get_bone_chain_names(bone)

    if len(bone_names) == 1:
      continue

    for index, bone_name in enumerate(bone_names):
      # fk bone 的父级是 mch bone，mch bone 的父级是 mch int bone,
      # 每一个 mch int bone 复制对应的 phy bone 的变换，
      # 当 phy bone 变换时，所有骨骼都会有相同的变换
      # mch int bone 的父级是上一个 fk bone，mch bone 复制上一个 fk_bone 的变换，
      # 当 fk bone 变换时，其他 fk bone 也会变换并且带有过渡效果
      tweak_bone_name = bone_name.replace('org_', 'tweak_')
      fk_bone_name = bone_name.replace('org_', 'fk_')
      mch_bone_name = bone_name.replace('org_', 'mch_')
      mch_int_bone_name = bone_name.replace('org_', 'mch_int_')
      phy_bone_name = bone_name.replace('org_', 'phy_')
      prev_bone_name = bone_names[index - 1]
      prev_fk_bone = prev_bone_name.replace('org_', 'fk_') if index else None
      prev_phy_bone = prev_bone_name.replace('org_', 'phy_') if index else None

      if prev_phy_bone:
        parent_config.append([phy_bone_name, prev_phy_bone, False])
        constraint_config.append({
          'name': prev_phy_bone,
          'target': phy_bone_name,
          'type': 'DAMPED_TRACK',
          'config': {
            'influence': wiggle_influence
          }
        })
        driver_config.append({
          'name': prev_phy_bone,
          'index': -1,
          'config': {
            'name': 'influence',
            'type': 'AVERAGE',
            'vars': [
              {
                'name': wiggle_prop,
                'targets': [
                  {
                    'id_type': 'OBJECT',
                    'data_path': f'pose.bones["props"]["{ wiggle_prop }"]'
                  }
                ]
              }
            ]
          }
        })
      else:
        parent_config.append([phy_bone_name, root, False])

      if prev_fk_bone:
        parent_config.append([mch_int_bone_name, prev_fk_bone, False])
        constraint_config.extend([
          {
            'name': mch_int_bone_name,
            'target': phy_bone_name,
            'type': 'COPY_TRANSFORMS',
            'config': {
              'target_space': 'LOCAL', 
              'owner_space': 'LOCAL'
            }
          },
          {
            'name': mch_bone_name,
            'target': prev_fk_bone,
            'type': 'COPY_TRANSFORMS',
            'config': {
              'target_space': 'LOCAL', 
              'owner_space': 'LOCAL'
            }
          },
          {
            'name': bone_names[index - 1],
            'target': tweak_bone_name,
            'type': 'STRETCH_TO',
          }
        ])
      else:
        # mch_int_bone_name 父级设置为 phy_bone_name 会比设置为 root 效果更好
        parent_config.append([mch_int_bone_name, phy_bone_name, False])

      parent_config.extend([
        [bone_name, tweak_bone_name, False],
        [tweak_bone_name, fk_bone_name, False],
        [fk_bone_name, mch_bone_name, False],
        [mch_bone_name, mch_int_bone_name, False]
      ])

      bone_config.extend([
        {
          'name': tweak_bone_name,
          'source': bone_name,
          'operator': 'copy',
          'operator_config': {
            'scale_factor': 0.5
          }
        },
        {
          'name': fk_bone_name,
          'source': bone_name,
          'operator': 'copy',
          'operator_config': {
            'scale_factor': 1
          }
        },
        {
          'name': mch_bone_name,
          'source': bone_name,
          'operator': 'copy',
          'operator_config': {
            'scale_factor': 0.25
          }
        },
        {
          'name': mch_int_bone_name,
          'source': bone_name,
          'operator': 'copy',
          'operator_config': {
            'scale_factor': 0.1
          }
        },
        {
          'name': phy_bone_name,
          'source': bone_name,
          'operator': 'copy',
          'operator_config': {
            'scale_factor': 1
          }
        },
      ])

  # TODO: fix performance
  _init_bones(bone_config)
  _init_parent(parent_config)
  _init_constraints(constraint_config)
  _init_drivers(driver_config)

  return bone_config

class OBJECT_OT_bone_wiggle (get_operator()):
  bl_idname = "object.bone_wiggle"
  bl_label = "Bone Wiggle"

  def invoke(self, context, event):
    passing = run_checker(self, context)
  
    if passing:
      return self.execute(context)
    else:
      return {'CANCELLED'}
      
  def execute(self, context):
    scene = context.scene
    wiggle_prop = scene.wiggle_prop
    wiggle_influence = scene.wiggle_influence
    _add_custom_props(get_active_object(), [{
      'prop_name': wiggle_prop,
      'config': {
        'min': 0,
        'max': 1,
        'default': wiggle_influence
      }
    }])
    bone_config = init_wiggle(scene)
    # assign_collection(bone_config, armature)

    return {'FINISHED'}
