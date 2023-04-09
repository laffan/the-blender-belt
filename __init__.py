# Blender Add-on Template
# Contributor(s): Aaron Powell (aaron@lunadigital.tv)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
        "name": "The Blender Belt",
        "description": "Tools that help Nate make things in blenderland.",
        "author": "Nate Laffan",
        "version": (1, 0),
        "blender": (3, 4, 1),
        "location": "Sidebar",
        "warning": "", # used for warning icon and text in add-ons panel
        "wiki_url": "http://my.wiki.url",
        "tracker_url": "http://my.bugtracker.url",
        "support": "COMMUNITY",
        "category": "Tools"
        }

import bpy
import importlib

# Import functions and reload them so they aren't cached by mistake.

def import_and_reload_functions(function_names):
    imported_functions = {}
    
    for function_name in function_names:
        module_name = f"scripts.{function_name}"
        if module_name in globals():
            importlib.reload(globals()[module_name])
        else:
            globals()[module_name] = importlib.import_module(f".{module_name}", __package__)
        
        imported_functions[function_name] = getattr(globals()[module_name], function_name)
    
    return imported_functions

# List of function names matching their file names
function_names = ["connectBakeNodes", "exportTheGLTF", "applyAllTransforms", "connectBSDF", "rebakeAll"]

# Import and reload functions
imported_functions = import_and_reload_functions(function_names)

connectBakeNodes = imported_functions["connectBakeNodes"]
exportTheGLTF = imported_functions["exportTheGLTF"]
applyAllTransforms = imported_functions["applyAllTransforms"]
connectBSDF = imported_functions["connectBSDF"]
rebakeAll = imported_functions["rebakeAll"]

class SimplePanel(bpy.types.Panel):
    bl_idname = "VIEW3D_PT_simple_panel"
    bl_label = "Blender Belt"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "++ Belt ++"

    def draw(self, context):
        layout = self.layout
        layout.operator("script.run_script1")
        layout.operator("script.run_script2")
        layout.operator("script.run_script3")
        layout.operator("script.run_script4")
        layout.operator("script.run_script5")

class Button1(bpy.types.Operator):
    bl_idname = "script.run_script1"
    bl_label = "Connect Bake Nodes"

    def execute(self, context):
        materials = bpy.data.materials
        connectBakeNodes(materials)
        return {'FINISHED'}

class Button2(bpy.types.Operator):
    bl_idname = "script.run_script2"
    bl_label = "Connect BSDF"

    def execute(self, context):
        materials = bpy.data.materials
        connectBSDF(materials)
        return {'FINISHED'}

class Button3(bpy.types.Operator):
    bl_idname = "script.run_script3"
    bl_label = "Export GLTF"

    def execute(self, context):
        exportTheGLTF()
        return {'FINISHED'}

class Button4(bpy.types.Operator):
    bl_idname = "script.run_script4"
    bl_label = "Rebake All"

    def execute(self, context):
        rebakeAll()
        return {'FINISHED'}

class Button5(bpy.types.Operator):
    bl_idname = "script.run_script5"
    bl_label = "Apply Transforms"

    def execute(self, context):
        applyAllTransforms()
        return {'FINISHED'}

def register():
    bpy.utils.register_class(SimplePanel)
    bpy.utils.register_class(Button1)
    bpy.utils.register_class(Button2)
    bpy.utils.register_class(Button3)
    bpy.utils.register_class(Button4)
    bpy.utils.register_class(Button5)

def unregister():
    bpy.utils.unregister_class(SimplePanel)
    bpy.utils.unregister_class(Button1)
    bpy.utils.unregister_class(Button2)
    bpy.utils.unregister_class(Button3)
    bpy.utils.unregister_class(Button5)

if __name__ == "__main__":
    register()