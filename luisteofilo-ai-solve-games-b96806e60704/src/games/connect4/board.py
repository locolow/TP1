import random


class Piece:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.color

class PieceSet:
    def __init__(self):
        self.__pieces = [
            Piece('BL'), Piece('BL'), Piece('BL'), Piece('BL'), Piece('BL'), Piece('BL'), Piece('BL'), Piece('BL'),
            Piece('BK'), Piece('BK'), Piece('BK'), Piece('BK'), Piece('BK'), Piece('BK'), Piece('BK'), Piece('BK'),
            Piece('GR'), Piece('GR'), Piece('GR'), Piece('GR'), Piece('GR'), Piece('GR'), Piece('GR'), Piece('GR'),
            Piece('RE'), Piece('RE'), Piece('RE'), Piece('RE'), Piece('RE'), Piece('RE'), Piece('RE'), Piece('RE'),
            Piece('WH'), Piece('WH'), Piece('WH'), Piece('WH'), Piece('WH'), Piece('WH'), Piece('WH'), Piece('WH'),
            Piece('SP'), Piece('SP'), Piece('SP')
        ]
        
    def shuffle_pieces(self):
        random.shuffle(self.__pieces)
        return self.__pieces

    def get_piece(self):
        if len(self.__pieces) == 0:
            return None
        return self.__pieces.pop()