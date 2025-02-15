from ..libs.blender_utils import (
  get_operator, get_object_, get_edit_bone, get_object_, set_mode, 
  active_object_, get_props, snap_cursor, snap_selected_to_cursor, deselect,
  snap_cursor_to_selected
)

class OBJECT_OT_init_location (get_operator()):
  bl_idname = "object.init_location"
  bl_label = "Reload Addon"
  type: get_props().EnumProperty(
    default = 'side_01', 
    items = [
      ('side_01', "side_01", ""),
      ('side_02', "side_02", ""),
      ('heel', "heel", ""),
      ('foot_tip', "foot_tip", "")
    ]
  )

  def execute(self, context):
    scene = context.scene
    type = self.type

    # bm = bmesh.from_edit_mesh(mesh.data)
    # for v in bm.verts:
    #   if v.select:
    #     if type == 'side_01':
    #       scene.side_01_head_location = v.co
    #     elif type == 'side_02':
    #       scene.side_02_head_location = v.co
    #     elif type == 'heel':
    #       scene.heel_location = v.co
    #     else:
    #       scene.foot_tip_location = v.co
    #     break

    location = snap_cursor_to_selected()

    if type == 'side_01':
      scene.side_01_head_location = location
    elif type == 'side_02':
      scene.side_02_head_location = location
    elif type == 'heel':
      scene.heel_location = location
    else:
      scene.foot_tip_location = location

    return {'FINISHED'}
