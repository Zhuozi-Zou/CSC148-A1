"""module for ChopsticksState class
"""
from typing import Any, Dict, List
from game_state import GameState


class ChopsticksState(GameState):
    """The current state of a chopsticks game
    """
    current_value: Dict[str, List[int]]
    p1_left: int
    p1_right: int
    p2_left: int
    p2_right: int

    def __init__(self, current_player: str, p1_state: List[int],
                 p2_state: List[int]) -> None:
        """Initialize a new state of a chopsticks game

        Extends GameState.__init__

        ===New Attributes===
        current_value - the current value of a chopsticks game
        p1_left - the value of the left hand of player 1
        p1_right - the value of the right hand of player 1
        p2_left - the value of the left hand of player 2
        p2_right - the value of the right hand of player 2

        >>> s = ChopsticksState('p2', [1, 1], [2, 1])
        >>> s.current_value
        {'p1': [1, 1], 'p2': [2, 1]}
        >>> s.current_player
        'p2'
        >>> s.p2_left
        2
        """
        self.current_value = {'p1': p1_state[:], 'p2': p2_state[:]}
        self.p1_left = p1_state[0]
        self.p1_right = p1_state[1]
        self.p2_left = p2_state[0]
        self.p2_right = p2_state[1]
        super().__init__(current_player)

    def __str__(self) -> str:
        """Return a string representation of current_value
        of self

        Overrides GameState.__str__

        >>> s = ChopsticksState('p2', [1, 3], [2, 4])
        >>> print(s)
        Player 1: Left 1 - 3 Right; Player 2: Left 2 - 4 Right
        """
        return ("Player 1: Left {} - {} Right; Player 2: " +
                "Left {} - {} Right").format(self.p1_left, self.p1_right,
                                             self.p2_left, self.p2_right)

    def __eq__(self, other: Any) -> bool:
        """Return whether ChopsticksState self is equivalent to other

        Overrides GameState.__eq__

        >>> s = ChopsticksState('p2', [1, 3], [2, 4])
        >>> s == '22'
        False
        >>> s == ChopsticksState('p2', [1, 3], [2, 3])
        False
        >>> s == ChopsticksState('p2', [1, 3], [2, 4])
        True
        """
        return (type(self) == type(other)
                and self.current_value == other.current_value
                and self.current_player == other.current_player)

    def get_possible_moves(self) -> list:
        """Return all possible moves for a chopsticks game

        Overrides GameState.get_possible_moves

        >>> a = ChopsticksState('p2', [1, 3], [2, 0])
        >>> a.get_possible_moves()
        ['ll', 'lr']
        >>> b = ChopsticksState('p1', [1, 3], [2, 0])
        >>> b.get_possible_moves()
        ['ll', 'rl']
        >>> c = ChopsticksState('p1', [1, 3], [0, 0])
        >>> c.get_possible_moves()
        []
        """
        result = []
        if self.current_player == 'p1':
            if self.p1_left % 5 != 0:
                if self.p2_left % 5 != 0:
                    result.append('ll')
                if self.p2_right % 5 != 0:
                    result.append('lr')
            if self.p1_right % 5 != 0:
                if self.p2_left % 5 != 0:
                    result.append('rl')
                if self.p2_right % 5 != 0:
                    result.append('rr')
        else:
            if self.p2_left % 5 != 0:
                if self.p1_left % 5 != 0:
                    result.append('ll')
                if self.p1_right % 5 != 0:
                    result.append('lr')
            if self.p2_right % 5 != 0:
                if self.p1_left % 5 != 0:
                    result.append('rl')
                if self.p1_right % 5 != 0:
                    result.append('rr')
        return result

    def is_valid_move(self, move_to_make: str) -> bool:
        """Return whether move_to_make is a valid move

        Overrides GameState.is_valid_move

        >>> b = ChopsticksState('p1', [1, 3], [2, 0])
        >>> b.is_valid_move('lr')
        False
        >>> b.is_valid_move('rl')
        True
        >>> b.is_valid_move('rm')
        False
        """
        return move_to_make in self.get_possible_moves()

    def make_move(self, move: str) -> 'ChopsticksState':
        """Apply the valid move

        Overrides GameState.make_move

        >>> b = ChopsticksState('p1', [4, 3], [2, 0])
        >>> c = b.make_move('ll')
        >>> c.current_value
        {'p1': [4, 3], 'p2': [1, 0]}
        >>> c.current_player
        'p2'
        """
        if self.current_player == 'p2':
            if move[0] == 'r':
                if move[1] == 'r':
                    p1_right = (self.p1_right + self.p2_right) % 5
                    return ChopsticksState('p1', [self.p1_left, p1_right],
                                           self.current_value['p2'])
                p1_left = (self.p1_left + self.p2_right) % 5
                return ChopsticksState('p1', [p1_left, self.p1_right],
                                       self.current_value['p2'])
            else:
                if move[1] == 'r':
                    p1_right = (self.p1_right + self.p2_left) % 5
                    return ChopsticksState('p1', [self.p1_left, p1_right],
                                           self.current_value['p2'])
                p1_left = (self.p1_left + self.p2_left) % 5
                return ChopsticksState('p1', [p1_left, self.p1_right],
                                       self.current_value['p2'])
        else:
            if move[0] == 'r':
                if move[1] == 'r':
                    p2_right = (self.p1_right + self.p2_right) % 5
                    return ChopsticksState('p2', self.current_value['p1'],
                                           [self.p2_left, p2_right])
                p2_left = (self.p1_right + self.p2_left) % 5
                return ChopsticksState('p2', self.current_value['p1'],
                                       [p2_left, self.p2_right])
            else:
                if move[1] == 'r':
                    p2_right = (self.p1_left + self.p2_right) % 5
                    return ChopsticksState('p2', self.current_value['p1'],
                                           [self.p2_left, p2_right])
                p2_left = (self.p1_left + self.p2_left) % 5
                return ChopsticksState('p2', self.current_value['p1'],
                                       [p2_left, self.p2_right])


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
