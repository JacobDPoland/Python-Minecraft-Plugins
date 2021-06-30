from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = [0, 1, 0]  # (0, 4, 0) in game coords 

mc.player.setTilePos(*pos)
