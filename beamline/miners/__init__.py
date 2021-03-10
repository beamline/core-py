from beamline.web.Beamline import Beamline
from beamline.miners.DiscoveryMiner import DiscoveryMiner

Beamline.miners.append(DiscoveryMiner())
