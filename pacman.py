from pathlib import Path
import pygame as pg
from constants import *
from board import Board

class PacMan:
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

        self.x = col*TILE_SIZE
        self.y = row*TILE_SIZE

        self.retning=RETNINGER_FRAMES["start"]
        self.fremtid_retning=None

        self.board=board

        frames_start = self.getImageSpriteList(32, 0, 1)
        frames_høyre = self.getImageSpriteList(0,16,2)
        frames_venstre = self.getImageSpriteList(0,32,2)
        frames_opp = self.getImageSpriteList(0,48,2)
        frames_ned = self.getImageSpriteList(0,64,2)
        
        # Bildet vi skal vise til å starte med er idle:
        self.frames = frames_start*2+frames_høyre+frames_venstre+frames_opp+frames_ned
        # Om vi vil ha animasjon som går gjennom frames:
        self.current_frame = 0

        # Om vi vil speile bildet:
        self.venstre = False



    def draw(self, surface):

        # Få bildet fra en liste av bilder (om du vil bruke animasjon/sprites):
        current_frame_image = self.frames[self.current_frame%2+self.retning]
        
        # Speiler bildet hvis det trengs:
        if self.venstre:
            current_frame_image = pg.transform.flip(current_frame_image, True, False)

        # Sørg for at vi tegner midt i "Tile":
        mid = TILE_SIZE // 2
        rect = current_frame_image.get_rect()
        rect.center = (self.x + mid , self.y + mid)

        # Blit images på skjermen (der self.rect befinner seg):
        surface.blit(current_frame_image, rect)
        if self.current_frame%2 == 0:
            self.current_frame+=1
        else:
            self.current_frame-=1
    
    def move(self):
        xmove=RETNINGER[self.retning][1]
        ymove=RETNINGER[self.retning][0]
        if self.x % TILE_SIZE == 0 and self.y % TILE_SIZE == 0:
            self.col=self.x//TILE_SIZE
            self.row=self.y//TILE_SIZE
            if self.board[self.row+xmove][self.col+ymove] != "#":
                self.y += ymove
                self.x += xmove
        else:
            self.y += ymove
            self.x += xmove
