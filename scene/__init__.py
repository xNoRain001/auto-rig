from ..libs.blender_utils import register_classes, unregister_classes, add_scene_custom_prop

# classes = ()

def register():
  # register_classes(classes)
  add_scene_custom_prop('armature_name', 'String', '荧_arm')
  add_scene_custom_prop('friction', 'Float', 10)
  add_scene_custom_prop('mass', 'Float', 0.1)
  add_scene_custom_prop('goal_min', 'Float', 0.4)
  add_scene_custom_prop('friction', 'Float', 10)


def unregister():
  # unregister_classes(classes)
  pass
