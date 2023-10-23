
class Move:
    def __init__(self, initial, final):
        self.initial = initial
        self.final = final
        # note these are squares not tuples

    def __str__(self):
        s = ''
        s += f'({self.initial.row}, {self.initial.col})'
        s += f' -> ({self.final.row}, {self.final.col})'
        return s
    
    def __eq__(self, other):
        return self.initial == other.initial and self.final == other.final
    
    def init_eq_final(self):
        if self.initial == self.final:
            return True
        else:
            return False