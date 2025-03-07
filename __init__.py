bl_info = {
  "name": "Auto Rig",
  'author': 'xNoRain001',
  'version': (0, 0, 0),
  'blender': (4, 1, 0),
  "category": "Rigging",
  'location': 'View3D > Sidebar > Auto Rig',
  'description': 'Blender auto rig addon.',
  'doc_url': 'https://github.com/xNoRain001/auto-rig',
  'tracker_url': 'https://github.com/xNoRain001/auto-rig/issues'
}

from .libs.blender_utils import register as utils_register, unregister as utils_unregister
from .panels import register as panels_register, unregister as panels_unregister
from .operators import (
  register as operators_register, 
  unregister as operators_unregister
)
from .scene import (
  register as scene_register, 
  unregister as scene_unregister
)

def register():
  utils_register()
  operators_register()
  panels_register()
  scene_register()

def unregister():
  utils_unregister()
  panels_unregister()
  operators_unregister()
  scene_unregister()

if __name__ == "__main__":
  register()
