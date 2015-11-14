import mcpi.minecraft as minecraft
import mcpi.block as block
import random

while True:
    mc = minecraft.Minecraft.create()
    pos = mc.player.getTilePos()

    # make a tower of random blocks above you
    # CHECK THE BLOCK IDs FOR VALID RANGE
    for a in range(1,10) :
        mc.setBlock(pos.x, pos.y+a, pos.z, random.randint(1,100))
    
