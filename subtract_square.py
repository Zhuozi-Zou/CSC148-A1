"""module for SubtractSquare class
"""
from typing import Any
from game import Game
from subtract_square_state import SubtractSquareState


class SubtractSquare(Game):
    """A subtract sqaure game
    """
    current_value: int
    current_state: SubtractSquareState

    def __init__(self, is_p1_turn: bool) -> None:
        """Initialize a new subtract sqaure game

        Extends Game.__init__

        ===New Attributes===
        current_value - the current value of a subtract square game
        current_state - an instance of SubtractSquareState class

        Assume starting_value is a non-negative whole number
        """
        super().__init__(is_p1_turn)
        self.current_value = int(input("Type a non-negative whole number " +
                                       "as the starting value of the game: "))
        self.current_state = SubtractSquareState(self.current_player,
                                                 self.current_value)

    def __str__(self) -> str:
        """Return a string representation of current_state of self

        Overrides Game.__str__
        """
        return str(self.current_state)

    def __eq__(self, other: Any) -> bool:
        """Return whether SubtractSquare self is equivalent to other

        Overrides Game.__eq__
        """
        return (type(self) == type(other)
                and self.current_value == other.current_value
                and self.current_player == other.current_player
                and self.current_state == other.current_state)

    def get_instructions(self) -> str:
        """Return instructions of the subtract square game

        Overrides Game.get_instructions
        """
        return ("A subtract square game is played as follows: \n" +
                "A non-negative whole number is chosen as the " +
                "starting value by some\nneutral entity. Players take " +
                "turns subtracting square values (such\nas 1, 4, 9, ...) " +
                "from the current value, provided the chosen square\nis not" +
                "larger. When no moves are possible, whoever is about to " +
                "play\nat that point loses!")

    def is_over(self, current_state: SubtractSquareState) -> bool:
        """Return whether self is over from the information provided by
        current_state

        Overrides Game.is_over
        """
        return current_state.current_value == 0

    def is_winner(self, player: str) -> bool:
        """Return whether player is the winner in the subtract square game

        Overrides Game.is_winner

        Assume player is either "p1" or "p2"
        """
        if self.is_over(self.current_state):
            return not self.current_state.current_player == player
        return False

    def str_to_move(self, move: str) -> int:
        """Return move as an integer

        Overrides Game.str_to_move
        """
        try:
            return int(move)
        except ValueError as ve:
            print(ve)
            print("Your move must be an integer")


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
