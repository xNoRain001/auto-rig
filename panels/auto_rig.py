from ..libs.blender_utils import get_panel, add_row_with_operator
from ..operators.init_rig import OBJECT_OT_init_rig
from ..operators.init_bone_collections import OBJECT_OT_init_bone_collection
from ..operators.init_bone_widgets import OBJECT_OT_init_bone_widgets
from ..operators.init_location import OBJECT_OT_init_location
from ..operators.rig_weapon import OBJECT_OT_rig_weapon
from ..const import bl_category

class VIEW3D_PT_auto_rig (get_panel()):
  bl_label = "Auto Rig"
  bl_idname = "VIEW3D_PT_auto_rig"
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = bl_category

  def draw(self, context):
    layout = self.layout
    scene = context.scene
    row = layout.row()
    row.prop(scene, 'torso_color', text = 'Torso')
    row = layout.row()
    row.prop(scene, 'fk_ik_l_color', text = 'L Ctrl')
    row = layout.row()
    row.prop(scene, 'fk_ik_r_color', text = 'R Ctrl')
    row = layout.row()
    row.prop(scene, 'tweak_color', text = 'Tweaker')
    row = layout.row()
    row.prop(scene, 'mesh_name', text = 'mesh 名称')
    row = layout.row()
    row.prop(scene, 'armature_name', text = '骨架名称')
    row = layout.row()
    row.prop(scene, 'rotation_mode', text = '旋转模式')
    row = layout.row()
    row.prop(scene, 'arm_pole_normal', text = '手臂极向方向')
    row = layout.row()
    row.prop(scene, 'leg_pole_normal', text = '腿极向方向')
    row = layout.row()
    row.operator(OBJECT_OT_init_location.bl_idname, text = '滚动骨 1').type = 'side_01'
    row.prop(scene, 'side_01_head_location', text = '')
    row = layout.row()
    row.operator(OBJECT_OT_init_location.bl_idname, text = '滚动骨 2').type = 'side_02'
    row.prop(scene, 'side_02_head_location', text = '')
    row = layout.row()
    row.operator(OBJECT_OT_init_location.bl_idname, text = '脚后跟').type = 'heel'
    row.prop(scene, 'heel_location', text = '')
    row = layout.row()
    row.operator(OBJECT_OT_init_location.bl_idname, text = '脚尖').type = 'foot_tip'
    row.prop(scene, 'foot_tip_location', text = '')
    add_row_with_operator(layout, OBJECT_OT_init_rig.bl_idname, '绑定（请检查轴向）')
    add_row_with_operator(layout, OBJECT_OT_init_bone_widgets.bl_idname, '自定义骨骼')
    add_row_with_operator(layout, OBJECT_OT_init_bone_collection.bl_idname, '分配集合')
    add_row_with_operator(layout, OBJECT_OT_rig_weapon.bl_idname, '绑定武器')
