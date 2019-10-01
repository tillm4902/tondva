import random
from typing import List

class Minesweeper:
    """
    Big ol' docstring baybeee
    """
    _board: List[List[str]]
    _size: int

    _emotes = {0:'||:zero:||', 1:'||:one:||', 2:'||:two:||', 3:'||:three:||',
              4:'||:four:||', 5:'||:five:||', 6:'||:six:||', 7:'||:seven:||',
              8:'||:eight:||'}

    def __init__(self, size:int) -> None:
        """
        40 >= size >= 3
        """
        self._board = []
        self._size = size

        for x in range(size):
            self._board.append([])

            for y in range(size):
                self._board[x].append('')

    def place_mines(self) -> None:
        """
        """
        num_mines = int((self._size**2)/6.4)

        while num_mines > 0:
            x = random.randint(0,self._size - 1)
            y = random.randint(0,self._size - 1)
            if self._board[y][x] != '||:bomb:||':
                self._board[y][x] = '||:bomb:||'
                num_mines -= 1

    def place_nums(self) -> None:
        """
        """
        for y in range(self._size):
            if y == 0:
                y_range = [0,2]
            elif y == self._size - 1:
                y_range = [-1,1]
            else:
                y_range = [-1,2]
            for x in range(self._size):
                if self._board[y][x] != '||:bomb:||':
                    adj_bombs = 0
                    if x == 0:
                        x_range = [0,2]
                    elif x == self._size - 1:
                        x_range = [-1,1]
                    else:
                        x_range = [-1,2]

                    for i in range(y + y_range[0], y + y_range[1]):
                        for j in range(x + x_range[0], x + x_range[1]):
                            if self._board[i][j] == '||:bomb:||':
                                adj_bombs += 1

                    self._board[y][x] = self._emotes[adj_bombs]

    def msg_board(self) -> str:
        """
        """
        msg = ''

        self.place_mines()
        self.place_nums()

        for row in self._board:
            for char in row:
                msg += char
            msg += '\n'

        return msg
