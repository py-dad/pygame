from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


# create instance of Ursina app                
app = Ursina()
grass_texture = load_texture('assets/grass_block.png')

class Voxel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5,
            texture = grass_texture,
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



# create voxels
for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x,0,z))

player = FirstPersonController()

app.run()