
from frenetic.lib import *

def hub(network):
    network.install_policy(flood)

    for switch in network.switch_joins:
        print "Add switch: %s" % switch
        
start(hub)
