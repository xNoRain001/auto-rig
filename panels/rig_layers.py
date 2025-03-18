from ..libs.blender_utils import get_bone_collections, get_panel, get_active_object
from ..const import bl_category
from .custom_props import show_panel

rig_layer_map = {
  'visible': [
    ['root'],
    ['torso', 'torso_fk', 'tweak_torso'],
    ['arm_fk.l', 'arm_fk.r'],
    ['arm_ik.l', 'arm_ik.r'],
    ['tweak_arm.l', 'tweak_arm.r'],
    ['hand.l', 'hand.r'],
    ['tweak_hand.l', 'tweak_hand.r'],
    ['leg_fk.l', 'leg_fk.r'],
    ['leg_ik.l', 'leg_ik.r'],
    ['tweak_leg.l', 'tweak_leg.r']
  ],
  'not_visible': [
    ['def'],
    ['org'],
    ['mch'],
    ['props']
  ]
}

class VIEW3D_PT_rig_layers (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = bl_category
  bl_label = "Rig Layers"
  bl_idname = "VIEW3D_PT_rig_layers"

  @classmethod
  def poll(cls, context):
    return show_panel(context)

  def draw(self, context):
    armature = get_active_object()
    layout = self.layout
    box = layout.box()

    bone_collections = get_bone_collections(armature)

    for visible_collection in rig_layer_map['visible']:
      row = box.row()

      for visible_collection_name in visible_collection:
        if visible_collection_name in bone_collections:
          row.prop(
            bone_collections[visible_collection_name], 
            'is_visible', 
            toggle = True, 
            text = visible_collection_name
          )
