import pygame as pg
import tilemap
import time
import os
import math
import settings
from pygame.math import Vector2 as vec

# def spawn(game, s_pos, path):
#     enemies = []
#     enemies.append(Enemy(game, s_pos, path))
#     # for i in range(s_amount):
#     #     enemies.append(Enemy(s_pos, path))
#     #     time.sleep(s_interval)
#     return enemies

class Enemy(pg.sprite.Sprite):
    def __init__(self, game, pos, waypoints):
        self.groups = game.all_sprites, game.enemies_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load("assets/imgs/enemies/Guy_green.png").convert_alpha()
        self.original_image = self.image
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        self.rect.center = self.pos
        self.vel = vec(0, 0)
        self.max_speed = 5
        self.rot = 0
        self.waypoints = waypoints
        self.waypoint_index = 0
        self.target = self.waypoints[self.waypoint_index]
        self.target_radius = 10
        self.health = 99 # Change depending on which enemey it is
    
    def update(self):
        # A vector pointing from self to the target.
        heading = self.target - self.pos
        distance = heading.length()  # Distance to the target.
        heading.normalize_ip()
        if distance <= 2:  # We're closer than 2 pixels.
            if self.waypoint_index >= 0 and self.waypoint_index < len(self.waypoints) - 1:
                # Increment the waypoint index to swtich the target.
                self.waypoint_index = (self.waypoint_index + 1)
                self.target = self.waypoints[self.waypoint_index]
                # Rotate enemy
                self.rot = (self.target - self.pos).angle_to(vec(1, 0))
                self.image = pg.transform.rotate(self.original_image, self.rot)
                self.rect = self.image.get_rect()
            else:
                # Enemy is in goal take away som health and despawn the enemy.
                self.kill()
                print("dead enemy")
        if distance <= self.target_radius:
            # If we're approaching the target, we slow down.
            self.vel = heading * (distance / self.target_radius * self.max_speed)
        else:
            # Otherwise move with max_speed.
            self.vel = heading * self.max_speed

        self.pos += self.vel
        self.rect.center = self.pos

        # Check health
        if self.health <= 0:
            self.kill()
            print("dead enemy")
        
    def draw_health(self):
        if self.health > 60:
            health_color = settings.GREEN
        elif self.health > 30:
            health_color = settings.YELLOW
        else:
            health_color = settings.RED
        width = int(self.rect.width * self.health / 100)
        self.health_bg = pg.Rect(self.pos[0], self.pos[1], (self.rect.width * 100 / 100), 7)
        self.health_bar = pg.Rect(self.pos[0], self.pos[1], width, 7)
        if self.health < 100:
            pg.draw.rect(self.game.screen, (200, 214, 229), self.health_bg)
            pg.draw.rect(self.game.screen, health_color, self.health_bar)