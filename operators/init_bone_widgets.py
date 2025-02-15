from ..libs.blender_utils import get_pose_bone, get_pose_bones, get_context, get_bone_widget, get_operator
from math import radians

def add_bone_widget (
  bone_name, 
  shape, 
  relative_size = True, 
  global_size = 1, 
  slide = 0,
  rotation = (0, 0, 0)
):
  # set_mode('POSE')
  x, y, z = rotation
  _rotation = (radians(x), radians(y), radians(z))
  pose_bone = get_pose_bone(bone_name)
  pose_bone.bone.select = True
  get_context().scene.widget_list = shape
  get_bone_widget().create_widget(
    relative_size = relative_size, 
    global_size = global_size, 
    slide = slide, 
    rotation = _rotation
  )
  pose_bone.bone.select = False

def init_bone_widget ():
  add_bone_widget('root', 'Root 1')
  add_bone_widget('props', 'Gear Complex', rotation = (90, 0, 0))
  add_bone_widget('head', 'Circle', slide = 1)
  add_bone_widget('neck', 'Circle', slide = 0.5)
  add_bone_widget('torso', 'Cube')
  add_bone_widget('chest', 'Chest', rotation = (90, 0, 0))
  add_bone_widget('hips', 'Chest', rotation = (90, 0, 0))
  add_bone_widget('fk_arm.l', 'FK Limb 2')
  add_bone_widget('fk_forearm.l', 'FK Limb 2')
  add_bone_widget('fk_hand.l', 'FK Limb 2')
  add_bone_widget('ik_hand.l', 'Cube')
  add_bone_widget('arm_pole.l', 'Sphere')
  add_bone_widget('vis_arm_pole.l', 'Line')
  add_bone_widget('thumb_01.l', 'Cube', global_size = 0.2, slide = 0.5)
  add_bone_widget('thumb_02.l', 'Cube', global_size = 0.2, slide = 0.5)
  add_bone_widget('thumb_03.l', 'Cube', global_size = 0.2, slide = 0.5)
  add_bone_widget('finger_a_01.l', 'Cube', global_size = 0.2, slide = 0.5)
  add_bone_widget('finger_a_02.l', 'Cube', global_size = 0.2, slide = 0.5)
  add_bone_widget('finger_a_03.l', 'Cube', global_size = 0.2, slide = 0.5)
  add_bone_widget('finger_b_01.l', 'Cube', global_size = 0.2, slide = 0.5)
  add_bone_widget('finger_b_02.l', 'Cube', global_size = 0.2, slide = 0.5)
  add_bone_widget('finger_b_03.l', 'Cube', global_size = 0.2, slide = 0.5)
  add_bone_widget('finger_c_01.l', 'Cube', global_size = 0.2, slide = 0.5)
  add_bone_widget('finger_c_02.l', 'Cube', global_size = 0.2, slide = 0.5)
  add_bone_widget('finger_c_03.l', 'Cube', global_size = 0.2, slide = 0.5)
  add_bone_widget('finger_d_01.l', 'Cube', global_size = 0.2, slide = 0.5)
  add_bone_widget('finger_d_02.l', 'Cube', global_size = 0.2, slide = 0.5)
  add_bone_widget('finger_d_03.l', 'Cube', global_size = 0.2, slide = 0.5)
  add_bone_widget('ik_foot.l', 'Cube', slide = 0.5)
  add_bone_widget('leg_pole.l', 'Sphere')
  add_bone_widget('vis_leg_pole.l', 'Line')
  add_bone_widget('foot_heel.l', 'Roll 1', slide = 0.5)
  add_bone_widget('ik_toes.l', 'Roll 3', global_size = 0.5, slide = 0.5)
  add_bone_widget('fk_leg.l', 'FK Limb 2')
  add_bone_widget('fk_shin.l', 'FK Limb 2')
  add_bone_widget('fk_foot.l', 'FK Limb 2')
  add_bone_widget('fk_toes.l', 'FK Limb 2')

  pose_bones = get_pose_bones()

  for pose_bone in pose_bones:
    bone_name = pose_bone.bone.name
    
    if bone_name.startswith('tweak_'):
      add_bone_widget(bone_name, 'Sphere')

  # 可能是 bone widget 插件 bug，只能手动对称
  # bpy.ops.pose.select_all(action='SELECT')
  # bonewidget.symmetrize_shape()
  # bpy.ops.pose.select_all(action='DESELECT')

class OBJECT_OT_init_bone_widgets (get_operator()):
  bl_idname = 'object.init_bone_widget'
  bl_label = 'Init Bone Widget'

  def execute(self, context):
    init_bone_widget()

    return {'FINISHED'}
