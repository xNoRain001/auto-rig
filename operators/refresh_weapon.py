from ..libs.blender_utils import (
  get_operator
)
from ..scene.add_weapon_props import add_weapon_props

class OBJECT_OT_refresh_weapon (get_operator()):
  bl_idname = "object.refresh_weapon"
  bl_label = "Refresh Weapon"

  def execute(self, context):
    add_weapon_props()

    return {'FINISHED'}
