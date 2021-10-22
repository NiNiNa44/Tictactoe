import unittest
import tictactoe


class MyTestCase(unittest.TestCase):


    def test_max(self):
        X = tictactoe.X
        O = tictactoe.O
        EMPTY = tictactoe.EMPTY

        board = [[X, X, EMPTY], [], []]

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
