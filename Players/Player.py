import pygame.math

class Player:
    def __init__(self, name):
        self.name = name
        self.traits = []
        self.speed = pygame.math.Vector2(1,1)
        self.position = pygame.math.Vector2()
        self.color = [255, 0, 0]

        #Behaviour
        self.goal = pygame.math.Vector2(500, 500)

    def init(self):
       self.goal = pygame.math.Vector2(500, 500)
        
    def update_position(self, map, other_players):
        direction = (self.goal - self.position).normalize()
        new_position = self.position + self.speed.elementwise() * direction

        map_color_at_new_pos = map.get_at((int(self.position.x), int(self.position.y)))
        if map_color_at_new_pos == (255, 255, 255):
            self.position = new_position
        
