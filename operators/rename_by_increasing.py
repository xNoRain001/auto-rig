import re
import sys
from ..libs.blender_utils import get_operator, get_bone_chain, get_selected_bones
 
class Rename_By_Increasing (get_operator()):
  bl_idname = "object.rename_by_increasing"
  bl_label = "Rename By Increasing"

  def execute(self, context):
    selected_bones = get_selected_bones()

    for selected_bone in selected_bones:
      bone_name = selected_bone.name
      # a_b_01.l a_b_01 a_b_01.r
      # a_b_01_01.l a_b_01_01 a_b_01_01.r
      match = re.search(r'(\d+)(\.l|\.r|$)', bone_name)
      bones = get_bone_chain(selected_bone)

      if match and bones:
        n = match.group(1)
        number = int(n)
        suffix = match.group(2)
        prefix = bone_name[:-(len(n + suffix))]

        for bone in bones:
          number = number + 1
          # :02d 是格式说明符，表示如何格式化表达式的结果
          # 0 表示用零填充
          # 2 表示结果应至少为两位数
          # d 表示结果应格式化为十进制整数
          bone.name = f"{ prefix }{ number:02d}{ suffix }"

    return {'FINISHED'}
