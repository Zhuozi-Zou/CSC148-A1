"""module for Chopsticks class
"""
from typing import Any
from game import Game
from chopstick_state import ChopsticksState


class Chopsticks(Game):
    """A chopsticks game
    """
    current_state: ChopsticksState

    def __init__(self, is_p1_turn: bool) -> None:
        """Initialize a new chopsticks game

        Extends Game.__init__

        ===New Attributes===
        current_state - an instance of ChopsticksState class

        >>> a = Chopsticks(False)
        >>> a.current_player
        'p2'
        """
        super().__init__(is_p1_turn)
        self.current_state = ChopsticksState(self.current_player, [1, 1],
                                             [1, 1])

    def __str__(self) -> str:
        """Return a string representation of current_state of self

        Overrides Game.__str__

        >>> a = Chopsticks(False)
        >>> print(a)
        Player 1: Left 1 - 1 Right; Player 2: Left 1 - 1 Right
        """
        return str(self.current_state)

    def __eq__(self, other: Any):
        """Return whether SubtractSquare self is equivalent to other

        Overrides Game.__eq__

        >>> a = Chopsticks(False)
        >>> a == 32
        False
        >>> a == Chopsticks(False)
        True
        >>> a == Chopsticks(True)
        False
        """
        return (type(self) == type(other)
                and self.current_player == other.current_player
                and self.current_state == other.current_state)

    def get_instructions(self) -> str:
        """Return instructions of the chopsticks game

        >>> a = Chopsticks(True)
        >>> b = a.get_instructions()
        >>> "Players take turns" == b[:18]
        True

        Overrides Game.get_instructions
        """
        return ("Players take turns adding the value of one of their " +
                "hands\nto the value of one of their opponents' hands " +
                "(module 5).\nA hand with a value of 5 (or 0; 5 module " +
                "5) is considered\n'dead'. The first player to have both" +
                " hands dead losses the\ngame.")

    def is_over(self, current_state: ChopsticksState) -> bool:
        """Return whether self is over from the information provided by
        current_state

        Overrides Game.is_over

        >>> a = ChopsticksState('p1', [0, 1], [1, 0])
        >>> b = Chopsticks(True)
        >>> b.is_over(a)
        False
        >>> c = ChopsticksState('p2', [0, 1], [0, 0])
        >>> b.is_over(c)
        True
        """
        return (current_state.current_value['p1'] == [0, 0]
                or current_state.current_value['p2'] == [0, 0])

    def is_winner(self, player: str) -> bool:
        """Return whether player is the winner in the chopsticks game

        Overrides Game.is_winner

        Assume player is in form "p1" or "p2"

        >>> a = ChopsticksState('p1', [0, 1], [1, 0])
        >>> c = ChopsticksState('p2', [0, 1], [0, 0])
        >>> b = Chopsticks(True)
        >>> b.current_state = a
        >>> b.is_winner('p2')
        False
        >>> b.current_state = c
        >>> b.is_winner('p2')
        False
        >>> b.is_winner('p1')
        True
        """
        if self.is_over(self.current_state):
            return not self.current_state.current_player == player
        return False

    def str_to_move(self, move: str) -> str:
        """Return move as a string

        Overrides Game.str_to_move

        >>> b = Chopsticks(True)
        >>> b.str_to_move('ll')
        'll'
        >>> b.str_to_move('wrr')
        'wrr'
        """
        return move


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
