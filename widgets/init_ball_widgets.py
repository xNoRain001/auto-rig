from . import init_bones_widget

def init_main_bone_widgets (bone_config, scene):
  patch_config = [{
    'name': scene.ball_root,
    'widget': 'Root',
    'widget_config': {
      'scale': (4, 4, 4)
    }
  }]

  init_bones_widget(patch_config, scene)
  init_bones_widget(bone_config, scene)

def init_ball_widgets (bone_config, scene):
  init_main_bone_widgets(bone_config, scene)
  