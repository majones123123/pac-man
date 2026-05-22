import pygame as pg
from constants import *




class Board:
    def __init__(self):
        font = pg.font.SysFont("Arial", 30)
        self.score = 0
        self.grid = [
            "#################",
            "#...##.....##...#",
            "#.#.###.###.#.#.#",
            "#.#...........#.#",
            "#.#.###.#.###.#.#",
            "#.....#...#.....#",
            "###.#.#####.#.####",
            ".....................",
            "###.#.#####.#.####",
            "#.....#...#.....#",
            "#.#.###.#.###.#.#",
            "#.#...........#.#",
            "#.#.###.###.#.#.#",
            "#...##.....##...#",
            "#################",
        ]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        self.poeng_tekst = font.render(str(self.score), True, WHITE)

    def window_size(self):
        return self.cols*TILE_SIZE, self.rows*TILE_SIZE

    def draw(self, surface):
        """Tegn brettet på den gitte pygame-flaten."""
        for y, row in enumerate(self.grid):
            for x, tile in enumerate(row):
                rect = pg.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                food = pg.Rect(x * TILE_SIZE + TILE_SIZE / 2 - 2, y * TILE_SIZE + TILE_SIZE / 2 - 2, 4, 4)
                if tile == '#':
                    pg.draw.rect(surface, DARK_BLUE, rect, border_radius=5)
                
                if tile == '.':
                    pg.draw.rect(surface, ORANGE, food, border_radius=10)
            surface.blit(self.poeng_tekst, (TILE_SIZE, 0))
    def is_road(self, x: int, y: int) -> bool:
        """Returnerer True hvis posisjonen er fri for vegg."""
        if x < 0 or x >= self.cols or y < 0 or y >= self.rows:
            return False
        return self.grid[y][x] != '#'
