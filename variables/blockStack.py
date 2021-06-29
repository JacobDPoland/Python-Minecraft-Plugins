from mcpi.minecraft import Minecraft
from mcpi import block
from mcpi.block import Block
mc = Minecraft.create()

pos = tuple(mc.player.getTilePos())
mc.setBlock(pos[0] - 1, pos[1] - 1, pos[2] - 1, block.AIR.id)

y_level = 0
m = 3
b = 2

red_wool = Block(block.WOOL.id)
red_wool.data = 14

blue_wool = Block(block.WOOL.id)
blue_wool.data = 11


# for x in range(-100, 100):
#     mc.setBlock(x, y_level, m*x + b, block.AIR.id)

def draw_axis():
    for t in range(0, 100):
        mc.setBlock(t, 0, 0, red_wool)
        mc.setBlock(0, 0, t, blue_wool)

    mc.setBlock(0, 0, 0, block.WOOL.id)


def clear():
    for i in range(-100, 100):
        for j in range(-100, 100):
            mc.setBlock(i, 0, j, block.AIR.id)


def draw_line(m, b):
    for x in range(-100, 100):
        mc.setBlock(m*x+b, 0, x, block.MELON.id)


clear()
draw_axis()
mc.player.setTilePos(0, 1, 0)

# control loop
while True:
    events = mc.events.pollChatPosts()
    if events:
        message = events[0].message
        if message[0] == "!" and message.lower().__contains__('x'):
            equation = message[1:]
            parts = equation.split('x')
            
            # check input and convert to int

            parts[0] = int(parts[0][:-1])
            parts[1] = int(parts[1])

            print(parts)
            draw_line(parts[0], parts[1])


            # try:
            #     parts[0] = int(parts[0][:-1])
            #     parts[1] = int(parts[1])

            #     print(len(parts))

            #     # if len(parts) > 2:
            #     #     raise Exception('Invalid equation format')

            #     # draw_line(parts[0], parts[1])
            # except:
            #     print(parts)
            #     mc.postToChat('Invalid equation. Please use "m*x+b"')

            
                