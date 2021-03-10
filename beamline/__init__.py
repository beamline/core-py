from beamline.web.Beamline import Beamline
import beamline.miners

b = Beamline()

if __name__ == "__main__":
    b.serve()