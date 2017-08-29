"""Main test class for all the FSM states
"""
import unittest
from external_lib.mock import Mock
from fsm.states import PlayingGameState


class TestPlayGameState(unittest.TestCase):
    """Unit test class for the play game state
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_initialize_PvsC_mode(self):
        game = Mock()
        gameOverState = Mock()
        gameWonState = Mock()
        playGameState = PlayingGameState(game, gameOverState, gameWonState)
        playGameState.mode = 1
        playGameState.initialize()
        self.assertEqual(playGameState.controller.p1.isComputer, False)
        self.assertEqual(playGameState.controller.p2.isComputer, True)

    def test_initialize_CvsC_mode(self):
        game = Mock()
        gameOverState = Mock()
        gameWonState = Mock()
        playGameState = PlayingGameState(game, gameOverState, gameWonState)
        playGameState.mode = 2
        playGameState.initialize()
        self.assertEqual(playGameState.controller.p1.isComputer, True)
        self.assertEqual(playGameState.controller.p2.isComputer, True)

if __name__ == '__main__':
    unittest.main()