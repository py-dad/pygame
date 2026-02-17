from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

grass_texture = load_texture('assets/gras_block.png')

class Voxel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block.obj',
            origin_y = 0.5,
            texture = 'grass',
            color = color.color(0,0,random.uniform(0.9,1)),
            highlight_color = color.lime
        )

    def input(self, key): # create voxel with mouse button
        if self.hovered:
            if key == "left mouse down":
                voxel = Voxel(position = self.position + mouse.normal)

            # destroy voxel with mouse button
            if key == "right mouse down":
                destroy(self)

# create instance of Ursina app                
app = Ursina()

# create voxels
for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x,0,z))

player = FirstPersonController()

app.run()