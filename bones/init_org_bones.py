from ..libs.blender_utils import (
  select_bone,
  get_edit_bone,
  get_edit_bones,
  duplicate_bones,
  deselect_bones
)

# 选中所有 def 骨骼，包括隐藏的
def select_def_bones ():
  edit_bones = get_edit_bones()
  hide_def_bones = []
  selected_bones = []

  for edit_bone in edit_bones:
    name = edit_bone.name

    if name.startswith('def_'):
      org_bone = get_edit_bone(name.replace('def_', 'org_'))

      # 隐藏的骨骼也会被选中，但不会被复制，只有可见的骨骼才会被复制，因此让它显示，
      # 复制完成后再隐藏回去
      if not org_bone:
        collections = edit_bone.collections

        if collections:
          for collection in collections:
            collection.is_visible = True

        if edit_bone.hide == True:
          hide_def_bones.append(edit_bone)
          edit_bone.hide = False
          
        select_bone(edit_bone)
        selected_bones.append(edit_bone)

  return hide_def_bones, selected_bones

# def_hand.l -> org_hand.l
def rename_org_bones (selected_bones):
  for selected_bone in selected_bones:
    org_bone_name = selected_bone.name + '.001'
    org_bone = get_edit_bone(org_bone_name)
    if not org_bone:
      print(org_bone_name)
    org_bone.name = \
      org_bone_name.replace('def_', 'org_').replace('.001', '')

def restore_bone_visibility (hide_def_bones):
  for hide_def_bone in hide_def_bones:
    hide_def_bone.hide = True
      
def init_org_bones ():
  hide_def_bones, selected_bones = select_def_bones()
  duplicate_bones()
  # 复制完成后，def bones 不再被选中，复制后的骨骼，即 org bones 被选中
  rename_org_bones(selected_bones)
  restore_bone_visibility(hide_def_bones)
  deselect_bones()
  