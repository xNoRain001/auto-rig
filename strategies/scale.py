def scale_1 (x, y, z):
  return (x, y, z)

def scale_2 (x, y, z):
  return (x, x, x)

def scale_3 (x, y, z):
  return (x, x / 2, x / 2)

def scale_4 (x, y, z):
  return (y, y, y)

def scale_5 (x, y, z):
  return (x / 2, x / 2, x / 2)

scale_strategies = {
  'Cube': scale_2,
  'Cube_Mini': scale_4,
  'Cuboid': scale_3,
  # 'Cuboid_Mini': scale_1,
  'Circle': scale_2,
  'Chest': scale_2,
  'FK Limb 1': scale_5,
  'FK Limb 2': scale_5,
  'Gear Complex': scale_2,
  'Gear Simple': scale_2,
  'Line': scale_2,
  'Paddle': scale_2,
  'Roll': scale_2,
  'Root': scale_2,
  'Sphere': scale_2
}
