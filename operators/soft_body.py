from ..libs.blender_utils import (
  get_operator, 
  get_ops, 
  set_mode, 
  get_context, 
  get_mesh,
  get_active_object,
  get_pose_bone,
  get_edit_bone,
  get_selected_object,
  get_object_,
  get_object,
  get_selected_bones,
  create_collection,
  get_collection
)

def gen_point (vector, collection, bone_name):
  set_mode('OBJECT')
  mesh = get_mesh()
  # 创建一个立方体
  mesh.primitive_cube_add()
  cube = get_selected_object()
  cube.name = 'soft_body_' + bone_name
  set_mode('EDIT')
  
  # 选择所有顶点
  mesh.select_all(action='SELECT')
  # 合并顶点到中心  
  mesh.merge(type='CENTER')
  get_ops().transform.translate(value = vector)
  cube.location = (0, 0, 0)
  collection.objects.link(cube)
  # cube.hide_set(True)

  return cube.name

def gen_vertex_group (bone):
  obj = get_selected_object()
  # 创建顶点组
  vertex_group = obj.vertex_groups.new(name = bone.replace('org_', 'phy_'))
  # 分配顶点到顶点组并设置权重
  set_mode('OBJECT')
  vertex_group.add([0], 1, 'REPLACE')

def add_cloth_modifier (cube_name, friction, mass, goal_min):
  obj = get_object_(cube_name)
  get_object().modifier_add(type='SOFT_BODY')
  # 获取布料模拟
  soft_body_modifier = obj.modifiers['软体']
  soft_body_modifier.settings.friction = friction
  soft_body_modifier.settings.mass = mass
  # soft_body_modifier.settings.bend = 0.6
  soft_body_modifier.settings.goal_min = goal_min

def get_vector (bone):
  vector_list = []

  while len(bone.children) > 0:
    bone = bone.children[0]
    vector_list.append(bone.head.copy())

  vector_list.append(bone.tail.copy())

  return vector_list

def get_children_names (bone):
  children_names = [bone.name]

  while len(bone.children) > 0:
    bone = bone.children[0]
    children_names.append(bone.name)

  return children_names

def add_child_of_constraint (bone, arm_name):
  obj = get_selected_object()
  # 添加子级约束
  constraint = obj.constraints.new(type='CHILD_OF')
  constraint.target = get_object_(arm_name)
  context = get_context()
  context.view_layer.objects.active = get_object_(arm_name)
  set_mode('EDIT')
  name = get_edit_bone(bone).parent.name
  constraint.subtarget = name
  context.view_layer.objects.active = obj
  # 设置反向
  get_ops().constraint.childof_set_inverse(constraint='子级', owner='OBJECT')
  context.view_layer.objects.active = get_object_(arm_name)

def add_dampled_track (item, cube_name):
  set_mode('POSE')
  bone = get_pose_bone(item)
  if bone:
    constraint = bone.constraints.new('DAMPED_TRACK')
    constraint.target = get_object_(cube_name)
    constraint.subtarget = item.replace('org_', 'phy_')
    constraint.track_axis = 'TRACK_Y'
    constraint.influence = 1.0
  set_mode('EDIT')

def soft_body (friction, mass, goal_min):
  arm_name = get_active_object().name
  collection_name = 'Soft_Body'
  collection = get_collection(collection_name)
  collection = collection if collection else create_collection(collection_name)
  selected_bone_names = []

  for select_bone in get_selected_bones():
    selected_bone_names.append(select_bone.name)

  for selected_bone_name in selected_bone_names:
    bone = get_edit_bone(selected_bone_name)
    vector_list = get_vector(bone)
    children_names = get_children_names(bone)
  
    for index, value in enumerate(vector_list):
      cube_name = gen_point(value, collection, children_names[index])
      gen_vertex_group(children_names[index])
      add_cloth_modifier(cube_name, friction, mass, goal_min)
      add_child_of_constraint(children_names[index], arm_name)
      add_dampled_track(children_names[index], cube_name)

class Soft_Body (get_operator()):
  bl_idname = "object.soft_body"
  bl_label = "Soft Body"

  def execute(self, context):
    scene = context.scene
    soft_body(scene.friction, scene.mass, scene.goal_min)

    return {'FINISHED'}
