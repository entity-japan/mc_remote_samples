from mc_remote.minecraft import Minecraft
import param_mc_remote as param
from param_mc_remote import PLAYER_ORIGIN as PO
from param_mc_remote import block
mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
mc.setPlayer(param.PLAYER_NAME, PO.x, PO.y, PO.z)


#def set_pyramid(mc, x0=0, y0=param.Y_SEA + 30, z0=0, height=3, block_id=block.GOLD_BLOCK):
#    for y in range(height):
#        d = height - y - 1
#        for x in range(-d, d + 1):
#            for z in range(-d, d + 1):
#                mc.setBlock(x0 + x, y0 + y, z0 + z, block_id)
                

#mc.postToChat("Building three pyramids...")
"set_pyramid(mc, x0=5, z0=5, height=5)"
"set_pyramid(mc, x0=10, y0=param.Y_SEA + 3, z0=-10, block_id=block.IRON_BLOCK)"
#set_pyramid(mc, x0=-20, z0=-10, height=15, block_id=block.DIAMOND_BLOCK)

def set_pyramid1(mc, x0=0, y0=param.Y_SEA + 10, z0=0, height=3, block_id=block.GOLD_BLOCK):
    for y in range(height):
        d = height - y - 1
        for x in range(-d, d + 1):
            for z in range(-d, d + 1):
                mc.setBlock(x0 + x, y0 + y, z0 + z, block_id)

mc.postToChat("Building three pyramids...")
set_pyramid1(mc, x0=-20, z0=-10, height=10, block_id=block.DIAMOND_BLOCK)