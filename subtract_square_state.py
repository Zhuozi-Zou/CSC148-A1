"""module for SubtractSquareState class
"""
from typing import Any
from game_state import GameState


class SubtractSquareState(GameState):
    """The current state of a subtract sqaure game
    """
    current_value: int

    def __init__(self, current_player: str, current_value: int) -> None:
        """Initialize a new state of a subtract square game

        Extends GameState.__init__

        ===New Attributes===
        current_value - the current value of a subtract square game

        >>> s = SubtractSquareState('p1', 27)
        >>> s.current_player
        'p1'
        >>> s.current_value
        27
        """
        super().__init__(current_player)
        self.current_value = current_value

    def __str__(self) -> str:
        """Return a string representation of current_player and current_value
        of self

        Overrides GameState.__str__

        >>> s = SubtractSquareState('p2', 28)
        >>> print(s)
        The current player is Player 2 and the current value is 28
        """
        player = 2
        if self.current_player == 'p1':
            player = 1
        return ("The current player is Player {} and the current value " +
                "is {}").format(player, self.current_value)

    def __eq__(self, other: Any) -> bool:
        """Return whether SubtractSquareState self is equivalent to other

        Overrides GameState.__eq__

        >>> a = SubtractSquareState('p2', 28)
        >>> a == 78
        False
        >>> a == SubtractSquareState('p2', 27)
        False
        >>> a == SubtractSquareState('p2', 28)
        True
        """
        return (type(self) == type(other)
                and self.current_value == other.current_value
                and self.current_player == other.current_player)

    def get_possible_moves(self) -> list:
        """Return all possible moves for the subtract square game

        Overrides GameState.get_possible_moves

        >>> a = SubtractSquareState('p2', 28)
        >>> a.get_possible_moves()
        [1, 4, 9, 16, 25]
        >>> b = SubtractSquareState('p1', 0)
        >>> b.get_possible_moves()
        []
        """
        possible_base = 1
        result = []
        while possible_base ** 2 <= self.current_value:
            result.append(possible_base ** 2)
            possible_base += 1
        return result

    def is_valid_move(self, move_to_make: int) -> bool:
        """Return whether move_to_make is a valid move

        Overrides GameState.is_valid_move

        >>> a = SubtractSquareState('p2', 25)
        >>> a.is_valid_move(25)
        True
        >>> a.is_valid_move(7)
        False
        >>> a.is_valid_move(36)
        False
        >>> a.is_valid_move(-25)
        False
        """
        return move_to_make in self.get_possible_moves()

    def make_move(self, move: int) -> 'SubtractSquareState':
        """Apply the valid move

        Overrides GameState.make_move

        >>> a = SubtractSquareState('p2', 28)
        >>> b = a.make_move(16)
        >>> b == SubtractSquareState('p1', 12)
        True
        """
        current_player = 'p2'
        if self.current_player == 'p2':
            current_player = 'p1'
        current_value = self.current_value - move
        return SubtractSquareState(current_player, current_value)


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
