from pathlib import Path
import pygame as pg
from constants import *
from board import Board
from pacman import PacMan
import random as r


class Ghost:
    IMAGE_FILE = Path(__file__).parent / "sprites" / "pacman2.png"

    def getImageSpriteList(self, x_start, y_start, num_frames) -> list[pg.Surface]:
        full_image = pg.image.load(self.IMAGE_FILE)
        frame_width = 16
        
        # Dele opp bildet i frames, som lagres i en liste:
        frames = []
        for i in range(num_frames):
            # Bildene er kvadratiske - bruker frame widht både som høye og bredde:
            frame = full_image.subsurface(pg.Rect(x_start + i * frame_width, y_start, frame_width, frame_width))
            frames.append(frame)
        return frames

    def __init__(self, row, col, board):
        self.row = row
        self.col = col

        self.ghostx = col*TILE_SIZE
        self.ghosty = row*TILE_SIZE
        
        self.ghostretninger = ["høyre", "venstre", "opp", "ned"]
        
        self.ghostretning="høyre"
        self.ghostfremtid_retning="opp"

        self.board=board
        
        self.frames_spøkelse = self.getImageSpriteList(0, 64, 8)
        
        # Bildet vi skal vise til å starte med er idle:
        # Om vi vil ha animasjon som går gjennom frames:
        self.current_frame = 0

        # Om vi vil speile bildet:
        self.venstre = True
    
    def draw(self, surface):

        # Få bildet fra en liste av bilder (om du vil bruke animasjon/sprites):
        current_frame_image = self.frames_spøkelse[self.current_frame//5+RETNINGER_FRAMES[self.ghostretning]]
        
        # Speiler bildet hvis det trengs:
        if self.venstre:
            current_frame_image = pg.transform.flip(current_frame_image, True, False)

        # Sørg for at vi tegner midt i "Tile":
        mid = TILE_SIZE // 2
        rect = current_frame_image.get_rect()
        rect.center = (self.ghostx + mid , self.ghosty + mid)

        # Blit images på skjermen (der self.rect befinner seg):
        surface.blit(current_frame_image, rect)
        if self.ghostx <= -16:
            self.ghostx = 18*TILE_SIZE-2
        if self.ghostx >= 18*TILE_SIZE:
            self.ghostx = -14

    def advance_frame(self):
        if self.current_frame == 9:
            self.current_frame=0
        else:
            self.current_frame+=1
    
    def move(self):
        if RETNINGER[self.ghostretning][0] == -RETNINGER[self.ghostfremtid_retning][0] and RETNINGER[self.ghostretning][1] == -RETNINGER[self.ghostfremtid_retning][1]:
            self.ghostretning=self.ghostfremtid_retning
        if self.ghostx % TILE_SIZE == 0 and self.ghosty % TILE_SIZE == 0:
            self.col=self.ghostx//TILE_SIZE
            self.row=self.ghosty//TILE_SIZE
            if self.board.grid[self.row+RETNINGER[self.ghostfremtid_retning][0]][self.col+RETNINGER[self.ghostfremtid_retning][1]] != "#":
                self.ghostretning=self.ghostfremtid_retning
                print("nå")
        ghostxmove=RETNINGER[self.ghostretning][1]
        ghostYMove=RETNINGER[self.ghostretning][0]
        if self.ghostx % TILE_SIZE == 0 and self.ghosty % TILE_SIZE == 0:
            if self.board.grid[self.row+ghostYMove][self.col+ghostxmove] != "#":
                self.ghosty += ghostYMove*2
                self.ghostx += ghostxmove*2
                self.advance_frame()
        else:
            self.ghosty += ghostYMove*2
            self.ghostx += ghostxmove*2
            self.advance_frame()
        print(int(self.ghostx), int(self.ghosty))
        
    def ghost_oppdater(self):
        
        
        self.ghostfremtid_retning = r.choice(self.ghostretninger)
        
        self.move()
        

class Red(Ghost):
    def __init__(self, row, col, board):
        super().__init__(row, col, board)
        
        self.frames_spøkelse = self.getImageSpriteList(0, 64, 8)
        