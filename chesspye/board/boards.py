'''
Created on Jun 20, 2013

@author: nick
'''

from pieces import Pawn, Knight, Bishop, Rook, Queen, King, colors
from chesspye.utils import ctl, letter_to_number

class Board(object):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pieces = {}
        self.clear_board()
    
    def __str__(self):
        s = u'\n'
        for i in range(self.height - 1, -1, -1): #row
            s += '%s ' % (i + 1)
            for j in range(self.width): #col
                if self.pieces[(i,j)] is not None:
                    s += '| %s ' % self.pieces[(i,j)].__unicode__()
                else:
                    s += '|   '
            s += '|\n  --'
            s += '----' * self.width
            s += '\n'
        s += '  '
        for i in range(self.height):
            s += '| %s ' % ctl(i)
        s += '\n'
        return s.encode('UTF-8')
    
    def __repr__(self):
        s = 'Board(width=%s,height=%s) Contents:\n' % (self.width, self.height)
        for piece in self.pieces.viewitems():
            if piece[1] is not None:
                s += '%s at %s\n' % (repr(piece[1]), piece[0])
        return s
    
    def coordinate_to_algebraic_move(self, to_sq, from_sq):
        alg = str(from_sq[1])
        if to_sq[1] is not None:
            alg += 'x'
        alg += '%s%s' % (ctl(to_sq[0][1]), to_sq[0][0] + 1)
        return alg
    
    def coordinate_to_algebraic_square(self, square):
        return '%s%s' % (ctl(square[1]), square[0]+1)
    
    def algebraic_to_coordinate_square(self, algebraic):
        return (int(algebraic[1:]) - 1, letter_to_number(algebraic[0]))
    
    def get_coordinate_piece_tuple(self, r, c):
        return ((r,c), self.pieces[(r,c)])
    
    def clear_board(self):
        for i in range(self.height):
            for j in range(self.width):
                self.pieces[(i,j)] = None
                
    def square_is_on_board(self, square):
        return square[0] < self.width and square[0] >= 0 and square[1] < self.height and square[1] >= 0
    
    def set_square_to_piece(self, algebraic, piece):
        square = self.algebraic_to_coordinate_square(algebraic)
        if self.square_is_on_board(square):
            self.pieces[square] = piece
            return True
        return False
    
    def get_square(self, algebraic):
        square = self.algebraic_to_coordinate_square(algebraic)
        if self.square_is_on_board(square):
            return self.pieces[square]
        return None

class ClassicBoard(Board):
    
    def __init__(self):
        super(ClassicBoard, self).__init__(8,8)
        self.pieces[(0,0)] = Rook(colors.WHITE) #Fischer Random will look so much cleaner
        self.pieces[(0,1)] = Knight(colors.WHITE)
        self.pieces[(0,2)] = Bishop(colors.WHITE)
        self.pieces[(0,3)] = Queen(colors.WHITE)
        self.pieces[(0,4)] = King(colors.WHITE)
        self.pieces[(0,5)] = Bishop(colors.WHITE)
        self.pieces[(0,6)] = Knight(colors.WHITE)
        self.pieces[(0,7)] = Rook(colors.WHITE)
        self.pieces[(7,0)] = Rook(colors.BLACK)
        self.pieces[(7,1)] = Knight(colors.BLACK)
        self.pieces[(7,2)] = Bishop(colors.BLACK)
        self.pieces[(7,3)] = Queen(colors.BLACK)
        self.pieces[(7,4)] = King(colors.BLACK)
        self.pieces[(7,5)] = Bishop(colors.BLACK)
        self.pieces[(7,6)] = Knight(colors.BLACK)
        self.pieces[(7,7)] = Rook(colors.BLACK)
        for i in range(self.width):
            self.pieces[(1,i)] = Pawn(colors.WHITE)
            self.pieces[(6,i)] = Pawn(colors.BLACK)
        