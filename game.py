import pygame
from const import *
from board import Board
from dragger import Dragger
class Game:

    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
        self.next_player = 'white'
        self.hovered_sqr = None
    def show_background(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (120, 119, 118)
                else:
                    color = (86, 85, 84)

                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    if piece is not self.dragger.piece:
                        piece.set_texture(size = 80)
                        img = pygame.image.load(piece.texture)
                        img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE //2 
                        piece.texture_rect = img.get_rect(center = img_center)
                        surface.blit(img, piece.texture_rect)

    def show_moves(self, surface):
        
        if self.dragger.dragging:
            piece = self.dragger.piece
            
            for move in piece.moves:
                color = '#C86464' if (move.final.row + move.final.col) % 2 == 0 else '#C84646'
                
                rect = (move.final.col * SQSIZE, move.final.row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)

    def if_mate_show_winner(self, surface, player_color):
        color = '#121212' if player_color == 'white' else '#FFFFFF'
        for row in range(ROWS):
            for col in range(COLS):
                
                rect = (col* SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)
                
    def show_last_move(self, surface):
        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final
            for pos in [initial, final]:
                color = (244, 247, 116) if (pos.row + pos.col % 2) == 0 else (172, 195, 51)

                rect = (pos.col * SQSIZE, pos.row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)

    def show_hover(self,surface):
        if self.hovered_sqr:
            color = (180,180,180)

            rect = (self.hovered_sqr.col * SQSIZE, self.hovered_sqr.row * SQSIZE, SQSIZE, SQSIZE)
            pygame.draw.rect(surface, color, rect, width = 6)

    def set_hover(self, row, col):
        self.hovered_sqr = self.board.squares[row][col]
    
    def next_turn(self):
        self.next_player = 'white' if self.next_player == 'black' else 'black'

    def reset(self):
        self.__init__()