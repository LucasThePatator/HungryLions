import pygame
from pygame.locals import *
from GraphicsEngine import *
from Players import Player

class GameEngine:
    def __init__(self):
        self.graphics = GraphicsEngine()
        
    def init_game(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.graphics.init()
        self.players = []
        self.players.append(Player.Player("Lucas"))
        self.players.append(Player.Player("Charlie"))
        self.players[0].position = pygame.math.Vector2(50, 50)
        self.players[1].position = pygame.math.Vector2(950, 950)

        self.map = pygame.image.load('F:\\Workspace\\Hungry Lions Battle\\testmap.png').convert()

    def start(self):
        self.play_round()
        pygame.quit()

    def update_player_positions(self):
        for p in self.players:
            p.update_position(self.map, self.players)

    def play_round(self):
        run_round = True
        while(run_round):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    run_round = False

            self.update_player_positions()
            self.graphics.display(self.players, self.map)
            self.clock.tick(30)


    