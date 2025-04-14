from ..libs.blender_utils import get_panel, get_active_object

from ..const import bl_category
from ..operators import OBJECT_OT_rig_weapon
from ..operators.rig_bow import OBJECT_OT_rig_bow
from ..operators.rig_human import OBJECT_OT_rig_human
from ..operators.bone_wiggle import OBJECT_OT_bone_wiggle
from ..operators.init_location import OBJECT_OT_init_location

def init_rig_human_ui (scene, layout):
  box = layout.box()
  row = box.row()
  row.label(text = 'Armature ')
  row.prop(scene, 'armature', text = '')

  if not scene.armature:
    return
  
  box = layout.box()
  row = box.row()
  row.label(text = 'Arm subdiv bones')
  row.prop(scene, 'arm_tweak_bone_number', text = '')

  arm_tweak_bone_number = scene.arm_tweak_bone_number
  if arm_tweak_bone_number:
    for i in range(0, arm_tweak_bone_number):
      row = box.row()
      row.label(text = f'Arm subdiv bone { i + 1 } influence')
      row.prop(scene, f'arm_influence_{ i }', text = '')

  row = box.row()
  row.label(text = 'Forearm subdiv bones')
  row.prop(scene, 'forearm_tweak_bone_number', text = '')

  forearm_tweak_bone_number = scene.forearm_tweak_bone_number
  if forearm_tweak_bone_number:
    for i in range(0, forearm_tweak_bone_number):
      row = box.row()
      row.label(text = f'Forearm subdiv bone { i + 1 } influence')
      row.prop(scene, f'arm_influence_{ i }', text = '')

  row = box.row()
  row.label(text = 'Leg subdiv bones')
  row.prop(scene, 'leg_tweak_bone_number', text = '')

  leg_tweak_bone_number = scene.leg_tweak_bone_number
  if leg_tweak_bone_number:
    for i in range(0, leg_tweak_bone_number):
      row = box.row()
      row.label(text = f'Leg subdiv bone { i + 1 } influence')
      row.prop(scene, f'arm_influence_{ i }', text = '')

  row = box.row()
  row.label(text = 'Shin subdiv bones')
  row.prop(scene, 'shin_tweak_bone_number', text = '')

  shin_tweak_bone_number = scene.shin_tweak_bone_number
  if shin_tweak_bone_number:
    for i in range(0, shin_tweak_bone_number):
      row = box.row()
      row.label(text = f'Shin subdiv bone { i + 1 } influence')
      row.prop(scene, f'arm_influence_{ i }', text = '')

  box = layout.box()
  row = box.row()
  row.operator(
    OBJECT_OT_init_location.bl_idname, 
    text = 'Set foot roll side 1 pos'
  ).type = 'side_01'
  row.operator(
    OBJECT_OT_init_location.bl_idname, 
    text = 'Set foot roll side 2 pos'
  ).type = 'side_02'
  row = box.row()
  row.operator(
    OBJECT_OT_init_location.bl_idname, 
    text = 'Set heel pos'
  ).type = 'heel'
  row.operator(
    OBJECT_OT_init_location.bl_idname, 
    text = 'Set Tiptoe pos'
  ).type = 'foot_tip'
  
  box = layout.box()
  row = box.row()
  row.operator(OBJECT_OT_rig_human.bl_idname, text = 'Rig')

def init_rig_bow_ui (scene, layout):
  box = layout.box()
  row = box.row()
  row.label(text = 'Armature ')
  row.prop(scene, 'bow_armature', text = '')

  if not scene.bow_armature:
    return
  
  box = layout.box()
  row = box.row()
  row.label(text = 'Bowstring max distance ')
  row.prop(scene, 'bowstring_max_distance', text = '')
  row = box.row()
  row.label(text = 'Bow limb max angle ')
  row.prop(scene, 'bow_limb_max_angle', text = '')
  box = layout.box()
  row = box.row()
  row.operator(OBJECT_OT_rig_bow.bl_idname, text = 'Rig bow')

def init_rig_weapon_ui (scene, layout):
  box = layout.box()
  row = box.row()
  row.label(text = 'Weapon')
  armature = get_active_object()
  data = armature.data
  row.prop_search(scene, 'weapon', data, 'bones', text = '')
  box = layout.box()
  row = box.row()
  row.operator(OBJECT_OT_rig_weapon.bl_idname, text = 'Rig Weapon')

def init_rig_physical_ui (scene, layout):
  box = layout.box()
  row = box.row()
  row.label(text = 'Custom prop')
  row.prop(scene, 'wiggle_prop', text = '')
  row = box.row()
  row.label(text = 'Influence ')
  row.prop(scene, 'wiggle_influence', text = '')
  box = layout.box()
  row = box.row()
  row.operator(OBJECT_OT_bone_wiggle.bl_idname, text = 'Bone Wiggle')

class VIEW3D_PT_auto_rig (get_panel()):
  bl_region_type = 'UI'
  bl_space_type = 'VIEW_3D'
  bl_category = bl_category
  bl_label = 'Auto Rig'
  bl_idname = 'VIEW3D_PT_auto_rig'

  def draw(self, context):
    layout = self.layout
    scene = context.scene
    box = layout.box()
    row = box.row()
    row.label(text = 'Rig type ')
    row.prop(scene, 'rig_type', text = '')
    rig_type = scene.rig_type

    if rig_type == 'human':
      init_rig_human_ui(scene, layout)
    elif rig_type == 'bow':
      init_rig_bow_ui(scene, layout)
    elif rig_type == 'weapon':
      init_rig_weapon_ui(scene, layout)
    elif  rig_type == 'bone wiggle':
      init_rig_physical_ui(scene, layout)
