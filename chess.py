from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        row, col = self.position
        if self.color == "white":
            moves = [
                (row + 1, col + 0), (row + 2, col + 0),
            ]

        elif self.color == "black":
            moves = [
                (row - 1, col + 0), (row - 2, col + 0),
            ]

        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves
    
    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 1, col + 1), (row + 1, col - 1),
            (row + 2, col + 2), (row + 2, col - 2),
            (row + 3, col + 3), (row + 3, col - 3),
            (row + 4, col + 4), (row + 4, col - 4),
            (row + 5, col + 5), (row + 5, col - 5),
            (row + 6, col + 6), (row + 6, col - 6),
            (row + 7, col + 7), (row + 7, col - 7),
            (row - 1, col + 1), (row - 1, col - 1),
            (row - 2, col + 2), (row - 2, col - 2),
            (row - 3, col + 3), (row - 3, col - 3),
            (row - 4, col + 4), (row - 4, col - 4),
            (row - 5, col + 5), (row - 5, col - 5),
            (row - 6, col + 6), (row - 6, col - 6),
            (row - 7, col + 7), (row - 7, col - 7)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves
    
    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 0, col + 1), (row + 0, col - 1),
            (row + 0, col + 2), (row + 0, col - 2),
            (row + 0, col + 3), (row + 0, col - 3),
            (row + 0, col + 4), (row + 0, col - 4),
            (row + 0, col + 5), (row + 0, col - 5),
            (row + 0, col + 6), (row + 0, col - 6),
            (row + 0, col + 7), (row + 0, col - 7),
            (row + 1, col + 0), (row - 1, col + 0),
            (row + 2, col + 0), (row - 2, col + 0),
            (row + 3, col + 0), (row - 3, col + 0),
            (row + 4, col + 0), (row - 4, col + 0),
            (row + 5, col + 0), (row - 5, col + 0),
            (row + 6, col + 0), (row - 6, col + 0),
            (row + 7, col + 0), (row - 7, col + 0)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves
    
    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 0, col + 1), (row + 0, col - 1),
            (row + 0, col + 2), (row + 0, col - 2),
            (row + 0, col + 3), (row + 0, col - 3),
            (row + 0, col + 4), (row + 0, col - 4),
            (row + 0, col + 5), (row + 0, col - 5),
            (row + 0, col + 6), (row + 0, col - 6),
            (row + 0, col + 7), (row + 0, col - 7),
            (row + 1, col + 0), (row - 1, col + 0),
            (row + 2, col + 0), (row - 2, col + 0),
            (row + 3, col + 0), (row - 3, col + 0),
            (row + 4, col + 0), (row - 4, col + 0),
            (row + 5, col + 0), (row - 5, col + 0),
            (row + 6, col + 0), (row - 6, col + 0),
            (row + 7, col + 0), (row - 7, col + 0),
            (row + 1, col + 1), (row + 1, col - 1),
            (row + 2, col + 2), (row + 2, col - 2),
            (row + 3, col + 3), (row + 3, col - 3),
            (row + 4, col + 4), (row + 4, col - 4),
            (row + 5, col + 5), (row + 5, col - 5),
            (row + 6, col + 6), (row + 6, col - 6),
            (row + 7, col + 7), (row + 7, col - 7),
            (row - 1, col + 1), (row - 1, col - 1),
            (row - 2, col + 2), (row - 2, col - 2),
            (row - 3, col + 3), (row - 3, col - 3),
            (row - 4, col + 4), (row - 4, col - 4),
            (row - 5, col + 5), (row - 5, col - 5),
            (row - 6, col + 6), (row - 6, col - 6),
            (row - 7, col + 7), (row - 7, col - 7)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves
    
    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 1, col - 1), (row - 1, col - 1),
            (row + 1, col + 1), (row - 1, col + 1),
            (row + 1, col + 0), (row - 1, col + 0),
            (row - 1, col + 1), (row - 1, col - 1),
            (row + 1, col + 1), (row + 1, col - 1),
            (row + 0, col + 1), (row + 0, col - 1)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'

if __name__ == "__main__":
    piece = Knight("black", (1, 2))
    print(piece)
    print(piece.possible_moves())