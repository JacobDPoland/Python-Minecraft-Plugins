from mcpi.minecraft import Minecraft
mc = Minecraft.create()
print(tuple(mc.player.getTilePos()))