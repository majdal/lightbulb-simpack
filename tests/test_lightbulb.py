import unittest
import sys
from os.path import dirname, realpath

cwd = dirname(dirname(dirname(realpath(__file__))))
sys.path.append(cwd)

import lightbulb_simpack
from lightbulb_simpack.lightbulb.lightbulb import People, Lamps #, Intervention
from lightbulb_simpack.state import State
import garlicsim

# Here's our "unit tests".
class LightbulbCase(unittest.TestCase):
    def setUp(self):
        lamps = Lamps()
        people = People(250)
        interventions = []
        data = {'Incandescent': [],
                'CFL': [],
                'Halogen': [],
                'LED': [],
                'time': []
        }
        self.state = State.create_root(lamps, people, interventions, data)        

    def test_init(self):
        garlicsim.simulate(self.state, 5)

    def test_project(self):
        project = garlicsim.Project(lightbulb_simpack)
        root = project.root_this_state(self.state)
        project.begin_crunching(root, 4)
        print project.sync_crunchers()
        print project.sync_crunchers()
        print project.tree
        (path,) = project.tree.all_possible_paths()
        print path

if __name__ == '__main__':
    unittest.main()