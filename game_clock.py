import pygame

class GameClock:
    def __init__(self, fps=10):
        self.clock = pygame.time.Clock()
        self.fps = fps

    def tick(self):
        self.clock.tick(self.fps)
