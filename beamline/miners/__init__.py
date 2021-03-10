from beamline.web.controllers import MinerController
from beamline.miners.DiscoveryMiner import DiscoveryMiner

MinerController.miners.append(DiscoveryMiner().serialize())
print("done")