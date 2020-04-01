import pygame as pg
import tilemap
import time
from pygame.math import Vector2

def spawn(s_pos, path):
    enemies = []
    enemies.append(Enemy(s_pos, path))
    # for i in range(s_amount):
    #     enemies.append(Enemy(s_pos, path))
    #     time.sleep(s_interval)
    return enemies

class Enemy():
    def __init__(self, pos, waypoints):
        self.image = pg.Surface((32,32))
        self.image.fill(pg.Color('dodgerblue'))
        self.rect = self.image.get_rect(center=pos)
        self.vel = Vector2(0, 0)
        self.max_speed = 5
        self.pos = Vector2(pos)
        self.waypoints = waypoints
        self.waypoint_index = 0
        self.target = self.waypoints[self.waypoint_index]
        self.target_radius = 10
    
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
            else:
                # enemy is in goal take away som health and despawn the enemy.
                print("dead")
        if distance <= self.target_radius:
            # If we're approaching the target, we slow down.
            self.vel = heading * (distance / self.target_radius * self.max_speed)
        else:  # Otherwise move with max_speed.
            self.vel = heading * self.max_speed

        self.pos += self.vel
        self.rect.center = self.pos
    
    def draw(self, surface):
        surface.blit(self.image, self.pos)