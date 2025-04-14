def init_bow_parent_config (scene):
  root = scene.bow_root
  org_bowstring = scene.bowstring.replace('def_', 'org_')
  org_bow_limb = scene.bow_limb.replace('def_', 'org_')
  org_bow_limb_upper = scene.bow_limb_upper.replace('def_', 'org_')
  org_bow_limb_lower = scene.bow_limb_lower.replace('def_', 'org_')

  return [
    [org_bowstring, root, False],
    [org_bow_limb, root, False],
    [org_bow_limb_upper, root, False],
    [org_bow_limb_lower, root, False]
  ]
