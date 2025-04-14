from ..libs.blender_utils import (
  add_scene_custom_prop, 
  get_selected_pose_bones, 
  get_object_, 
  get_collection,
  get_data, 
  create_collection,
  set_mode
)
from os.path import dirname, abspath, join
from ..const import wgt_collection_name
from ..widget_strategies import rotation_strategies, scale_strategies, translation_strategies

template_path = join(dirname(abspath(__file__)), '../assets/wgt/wgts.blend')
wgt_prefix = 'bone_widget_'

def get_widget (collection, shape):
  widget_name = wgt_prefix + shape
  widget = get_object_(widget_name)

  # 不存在则导入
  if not widget:
    with get_data().libraries.load(template_path, link = False) as (data_from, data_to):
      for name in data_from.objects:
        if name == shape:
          data_to.objects.append(name)

          break

    widget = data_to.objects[0]
    widget.name = widget_name
    widget['type'] = shape
    collection.objects.link(widget)

  return widget

def update_rotation (pose_bone, custom_shape):
  strategy_name = custom_shape['type']
  pose_bone.custom_shape_rotation_euler = rotation_strategies[strategy_name]

def update_scale_xyz (pose_bone, custom_shape):
  factor_x = pose_bone.length / custom_shape.dimensions[0]
  factor_y = factor_x / 5
  strategy_name = custom_shape['type']
  xyz = scale_strategies[strategy_name](factor_x, factor_y, factor_y)
  pose_bone.custom_shape_scale_xyz = xyz

def update_translation (pose_bone, custom_shape):
  l = pose_bone.length
  w = l / 5
  strategy_name = custom_shape['type']
  x, y, z = translation_strategies[strategy_name]
  _x = w * x * 0.01
  _y = l * y * 0.01
  _z = w * z * 0.01
  pose_bone.custom_shape_translation = (_x, _y, _z)

def on_update (self, context):
  pose_bones = get_selected_pose_bones() or []

  if not len(pose_bones):
    return
  
  collection = get_collection(wgt_collection_name)
  if not collection:
    collection = create_collection(wgt_collection_name)
    collection.hide_render = True
    collection.hide_viewport = True
  
  widget = get_widget(collection, self.shape)

  for pose_bone in pose_bones:
    custom_shape = pose_bone.custom_shape

    if custom_shape:
      if widget != custom_shape:
        pose_bone.custom_shape = widget
      else:
        continue
    else:
      pose_bone.use_custom_shape_bone_size = False
      pose_bone.custom_shape = widget
      self.show_wire = self.show_wire
      self.wire_width = self.wire_width
    
    update_scale_xyz(pose_bone, widget)
    update_rotation(pose_bone, widget)
    update_translation(pose_bone, widget)

def add_shape ():
  add_scene_custom_prop(
    'shape', 
    'Enum', 
    'Cube', 
    # TODO: 根据文件生成
    items = [
      # 务必通过旋转操作保证 x 是最长的边
      ('Chest', 'Chest', ''),
      ('Cuboid', 'Cuboid', ''),
      ('Circle', 'Circle', ''),
      ('Cube', 'Cube', ''),
      ('Cube_Mini', 'Cube_Mini', ''),
      ('FK Limb 1', 'FK Limb 1', ''),
      ('FK Limb 2', 'FK Limb 2', ''),
      ('Gear Complex', 'Gear Complex', ''),
      ('Gear Simple', 'Gear Simple', ''),
      ('Line', 'Line', ''),
      ('Paddle', 'Paddle', ''),
      ('Roll', 'Roll', ''),
      ('Roll 2', 'Roll 2', ''),
      ('Root', 'Root', ''),
      ('Sphere', 'Sphere', '')
    ],
    update = on_update
  )
