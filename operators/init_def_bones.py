from ..libs.blender_utils import (
  get_operator
)
from ..bones.init_org_bones import init_org_bones
from ..constraints import def_bone_add_copy_transforms

class OBJECT_OT_init_def_bones (get_operator()):
  bl_idname = "object.init_def_bones"
  bl_label = "Init Def Bones"

  def execute(self, context):
    init_org_bones()
    def_bone_add_copy_transforms()

    return {'FINISHED'}
