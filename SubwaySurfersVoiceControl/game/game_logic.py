import pygame

class GameLogic:
    def __init__(self):
        self.player_x = 100
        self.player_y = 100
        self.policeman_x = 200
        self.policeman_y = 200

    def move_left(self):
        self.player_x -= 10

    def move_right(self):
        self.player_x += 10

    def jump(self):
        self.player_y -= 20

    def duck(self):
        self.player_y += 20

    def update(self):
        # Update game state here
        pass