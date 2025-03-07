from ..libs.blender_utils import (
  get_edit_bone,
  extrude_bone,
)

def gen_props_bone ():
  props_bone = get_edit_bone('props')

  if not props_bone:
    head = get_edit_bone('org_head')
    extrude_bone(
      head, 
      'tail', 
      (0, 0, head.length), 
      name = 'props',
      parent = get_edit_bone('root'), 
      parent_connect = False
    )
