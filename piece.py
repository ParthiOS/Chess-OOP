import os
class Piece: 

    def __init__(self, name, color, value, texture= None, texture_rect=None):
        self.name = name
        self.color = color
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        self.texture = texture
        self.set_texture()
        self.moves = []
        self.moved = False
        self.texture_rect = texture_rect
    def set_texture(self, size = 80):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png'
        )
    def add_move(self, move):
        self.moves.append(move)

    def clear_moves(self):
        self.moves = []
        

    def print_moves(self):
        """
        Method to print the list of moves stored in self.moves.
        """
        print(f"List of moves for {self.name} ({self.color}):")
        for move in self.moves:
            print(move)

    def check_final(self, tuple):
            
            for move in self.moves:
                if move.final.row == tuple[0] and move.final.col == tuple[1]:
                    return True
                else: 
                    return False
class Pawn(Piece):
    def __init__(self, color):
        self.dir = -1 if color == 'white' else 1
        super().__init__('pawn', color, 1.0)


class Knight(Piece):
    def __init__(self, color):
        super().__init__('knight',color,3.0)

class Bishop(Piece):
    def __init__(self, color):
        super().__init__('bishop',color,3.00001)

class Rook(Piece):
    def __init__(self, color):
        super().__init__('rook',color,5.0)

class Queen(Piece):
    def __init__(self, color):
        super().__init__('queen',color,9.0)

class King(Piece):
    def __init__(self, color):
        self.left_rook = None
        self.right_rook = None
        super().__init__('king',color,100000.0)