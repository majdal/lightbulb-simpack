import unittest


# Here's our "unit tests".
class LightbulbCase(unittest.TestCase):

    def test_init(self):
        import sys
        from os.path import dirname, realpath
        cwd = dirname(dirname(dirname(realpath(__file__))))

        sys.path.append(cwd)

        from lightbulb.lightbulb import People, Lamps#, Intervention
        import lightbulb_simpack.State
        import garlicsim

        lamps = Lamps()
        people = People(250)
        interventions = []
        data = {'Incandescent': [],
                'CFL': [],
                'Halogen': [],
                'LED': [],
                'time': []
        }
        state = lightbulb_simpack.State.create_root(Lamps, people, interventions, data)
        garlicsim.simulate(state, 5)


if __name__ == '__main__':
    unittest.main()