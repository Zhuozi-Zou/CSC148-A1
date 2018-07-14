"""
module for GameState class
"""
from typing import Any


class GameState:
    """The game state for a two-player, sequential move, zero-sum,
    perfect-information game.

    current_player - the player that is about to play at the point
    """
    current_player: str

    def __init__(self, current_player: str) -> None:
        """Initialize a new game state

        >>> s = GameState('p2')
        >>> s.current_player
        'p2'
        """
        self.current_player = current_player

    def __str__(self) -> str:
        """Return a string representation of self
        """
        raise NotImplementedError('Subclass needed')

    def __eq__(self, other: Any) -> bool:
        """Return whether GameState self is equivalent to other
        """
        raise NotImplementedError('Subclass needed')

    def get_current_player_name(self) -> str:
        """Return the current player's name

        >>> a = GameState('p2')
        >>> a.get_current_player_name()
        'p2'
        """
        return self.current_player

    def get_possible_moves(self) -> list:
        """Return all possible moves
        """
        raise NotImplementedError('Subclass needed')

    def is_valid_move(self, move_to_make: str) -> bool:
        """Return whether move_to_make is a valid move
        """
        raise NotImplementedError('Subclass needed')

    def make_move(self, move: int) -> Any:
        """Apply the valid move
        """
        raise NotImplementedError('Subclass needed')


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
