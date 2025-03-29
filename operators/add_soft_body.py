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
  get_collection,
  get_bone_chain_names,
  add_damped_track_constraint,
  add_copy_location_constraint,
  active_object_,
  get_selected_bone,
  childof_set_inverse
)

def gen_simulation_point (vector, collection, bone_name):
  set_mode('OBJECT')
  mesh = get_mesh()
  mesh.primitive_cube_add()
  cube = get_selected_object()
  cube.name = 'soft_body_' + bone_name
  set_mode('EDIT')
  mesh.select_all(action='SELECT')
  mesh.merge(type='CENTER')
  cube.location = vector
  collection.objects.link(cube)

  return cube

def gen_vertex_group (vertex_group):
  obj = get_selected_object()
  # 创建顶点组
  vertex_group = obj.vertex_groups.new(name = vertex_group)
  # 分配顶点到顶点组并设置权重
  set_mode('OBJECT')
  vertex_group.add([0], 1, 'REPLACE')

def add_soft_body_modifier (point, friction, mass, goal_min):
  get_object().modifier_add(type='SOFT_BODY')
  soft_body_modifier = point.modifiers['软体']
  soft_body_modifier.settings.friction = friction
  soft_body_modifier.settings.mass = mass
  # soft_body_modifier.settings.bend = 0.6
  soft_body_modifier.settings.goal_min = goal_min

def get_vectors (selected_bone):
  vectors = []
  vectors.append(selected_bone.head.copy())
  # for damp track
  # vectors.append(selected_bone.tail.copy())

  return vectors

def add_child_of_constraint (subtarget, armature):
  o = get_selected_object()
  constraint = o.constraints.new(type='CHILD_OF')
  constraint.target = armature
  constraint.subtarget = subtarget
  childof_set_inverse(constraint)
  active_object_(armature)

def get_soft_body_collection ():
  collection_name = 'Soft_Body'
  collection = get_collection(collection_name)

  return collection if collection else create_collection(collection_name)

def add_soft_body (friction, mass, goal_min):
  set_mode('EDIT')
  armature = get_object_(get_active_object().name)
  collection = get_soft_body_collection()
  selected_bone = get_selected_bone()
  vectors = get_vectors(selected_bone)
  subtarget = selected_bone.parent.name
  bone_name = selected_bone.name
  vertex_group = bone_name.replace('org_', 'phy_')
  simulation_point = gen_simulation_point(vectors[0], collection, bone_name)
  gen_vertex_group(vertex_group)
  add_soft_body_modifier(simulation_point, friction, mass, goal_min)
  add_child_of_constraint(subtarget, armature)
  set_mode('POSE')
  add_copy_location_constraint(bone_name, vertex_group, target = simulation_point)
  # TODO: 再创造一个模拟点，骨骼尾部对它进行 damp track 

class OBJECT_OT_add_soft_body (get_operator()):
  bl_idname = "object.add_soft_body"
  bl_label = "Add Soft Body"

  def execute(self, context):
    scene = context.scene
    friction = scene.friction
    # 质量越大，抖动强度越大
    mass = scene.mass
    goal_min = scene.goal_min

    add_soft_body(friction, mass, goal_min)

    return {'FINISHED'}
