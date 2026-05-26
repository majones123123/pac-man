import pygame as pg
from constants import *
from board import Board
from pacman import PacMan
from ghosts import *

pg.init()
board = Board()
vindu = pg.display.set_mode(board.window_size())
clock = pg.time.Clock()


pacman = PacMan(3, 4, board)
red_ghost = Red(3, 4, board)

frame = 0

running = True
while running:
    
    frame += 1
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
    
    # Tegn bakgrunn: (En slags "reset" av hele vinduet vårt)
    vindu.fill(BLACK)

    # Tegn brettet først, og pacman og andre ting "oppå":
    board.draw(vindu)

    # TODO: Oppdater objektene våre:


    # Tegn objektene våre:
    pacman.oppdater()
    pacman.draw(vindu)
    
    red_ghost.draw(vindu)
    
    red_ghost.ghost_oppdater()
    


    # Har alltid disse med til slutt:
    pg.display.flip()
    clock.tick(FPS)


# While running er slutt: Avslutt pygame på en "ryddig måte":
pg.quit()
