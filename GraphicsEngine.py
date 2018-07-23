import pygame

class GraphicsEngine:
    def __init__(self):
        pass

    def init(self):
        self.window = pygame.display.set_mode((1000, 1000))

    def display(self, players, map):
        self.window.blit(map, (0,0))
        for p in players:
            pygame.draw.circle(self.window, p.color, (int(p.position.x), int(p.position.y)), 2)

        pygame.display.flip()
