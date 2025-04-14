from . import init_bones_widget

def init_main_bone_widgets (bone_config, scene):
  patch_config = [
    {
      'name': scene.bow_root,
      'widget': 'Root'
    },
    {
      'name': scene.bowstring.replace('def_', 'org_'),
      'widget': 'Sphere'
    }
  ]

  init_bones_widget(patch_config, scene)

def init_bow_widgets (bone_config, scene):
  init_main_bone_widgets(bone_config, scene)
  