"""
module for Game class
"""
from typing import Any


class Game:
    """A a two-player, sequential move, zero-sum, perfect-information game.

    current_player - the player that is about to play at the point
    """
    current_player: str

    def __init__(self, is_p1_turn: bool) -> None:
        """Initialize a new game and specify which player moves first

         >>> s = Game(True)
         >>> s.current_player
         'p1'
        """
        self.current_player = 'p2'
        if is_p1_turn:
            self.current_player = 'p1'

    def __str__(self) -> str:
        """Return a string representation of self
        """
        raise NotImplementedError('Subclass needed')

    def __eq__(self, other: Any) -> bool:
        """Return whether Game self is equivalent to other
        """
        raise NotImplementedError('Subclass needed')

    def get_instructions(self) -> str:
        """Return instructions of self
        """
        raise NotImplementedError('Subclass needed')

    def is_over(self, current_state: Any) -> bool:
        """Return whether self is over from the information provided by
        current_state
        """
        raise NotImplementedError('Subclass needed')

    def is_winner(self, player: str) -> bool:
        """Return whether player is the winner in self

        Assume player is either "p1" or "p2"
        """
        raise NotImplementedError('Subclass needed')

    def str_to_move(self, move: str) -> Any:
        """Return the value of move in appropriate type
        """
        raise NotImplementedError('Subclass needed')


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
