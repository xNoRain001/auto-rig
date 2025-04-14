def init_ball_parent_config (scene):
  root = scene.ball_root
  deformation = scene.deformation
  
  return [
    [deformation, 'rotation', False],
    ['rotation', 'mch_squash_stretch', False],
    ['mch_squash_stretch', 'squash_bottom', False],
    ['squash_bottom', root, False],
    ['squash_top', root, False]
  ]
