"""
module for strategies
"""
from typing import Union, Any
import random
from game import Game


def interactive_strategy(game: Game) -> Union[str, int]:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def random_strategy(game: Any) -> Union[str, int]:
    """
    Return a random valid move
    """
    possible_moves = game.current_state.get_possible_moves()
    move = random.choice(possible_moves)
    return move


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
