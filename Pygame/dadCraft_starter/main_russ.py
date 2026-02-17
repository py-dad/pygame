#import the ursina library
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise
import random

noise = PerlinNoise(octaves=3,seed=random.randint(1,1000000))

#create an instance of the Ursina app
app = Ursina()

#define game variables
selected_block = "grass"

sky_texture =load_texture('assets/skybox.png')
#create player
player=FirstPersonController(
  mouse_sensitivity=Vec2(100, 100),
  position=(0, 5, 0)
  )

block_textures = {
  "grass": load_texture("assets/grass_block.png"),
  "dirt": load_texture("assets/dirt_block.png"),
  "stone": load_texture("assets/stone_block.png"),
  "bedrock": load_texture("assets/brick_block.png"),
  "snow": load_texture('assets/snow.png'),
  "wood": load_texture('assets/wood.png')
  
}

class Block(Entity):
  def __init__(self, position, block_type):
    super().__init__(
      position=position,
      model="assets/block",
      scale=0.5,
      origin_y=-0.5,
      texture=block_textures.get(block_type),
      collider="box"
      )
    self.block_type = block_type

mini_block = Entity(
  parent=camera,
  model="assets/models/block_model",
  #texture=block_textures.get(selected_block),
  texture="axe",
  scale=0.2,
  position=(0.35, -0.25, 0.5),
  rotation=(-15, -30, -5)
  )

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 150,
            double_sided = True
            
        )


#create world
min_height = -5
for x in range(-10, 10):
  for z in range(-10, 10):
    height = noise([x * .02,z * .02])
    height = math.floor(height * 7.5)
    for y in range(height, min_height - 1, -1):
      if y == min_height:
        block = Block((x, y + min_height, z), "bedrock")
      elif y == height:
        block = Block((x, y + min_height, z), "grass")
      elif height - y > 2:
        block = Block((x, y + min_height, z), "stone")
      else:
        block = Block((x, y + min_height, z), "dirt")

def input(key):
  global selected_block
  #place block
  if key == 'left mouse down':
    hit_info = raycast(camera.world_position, camera.forward, distance=10)
    if hit_info.hit:
      block = Block(hit_info.entity.position + hit_info.normal, selected_block)
  #delete block
  if key == 'right mouse down' and mouse.hovered_entity:
    if not mouse.hovered_entity.block_type == "bedrock":
      destroy(mouse.hovered_entity)
  #change block type
  if key == '1':
    selected_block = "grass"
  if key == '2':
    selected_block = "dirt"
  if key == '3':
    selected_block = "stone"
  if key == '4':
      selected_block = "snow"
  if key == '5':
    selected_block = "wood"



def update():
  mini_block.texture=block_textures.get(selected_block)

sky = Sky()

#run the app
app.run()