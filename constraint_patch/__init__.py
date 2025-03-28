from .fix_ik_pole_angle import fix_ik_pole_angle

constraint_patchs = {
  'mch_ik_shin.l': fix_ik_pole_angle,
}
