from beamline.controller.MinerController import MinerController
from beamline.miners.DiscoveryMiner import DiscoveryMiner

MinerController.miners.append(DiscoveryMiner())
print("done")