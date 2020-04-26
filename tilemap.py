import pygame as pg
import pytmx
import settings
from tower_foundation import TowerFoundation

class Map:
    def __init__(self, game, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm
        self.game = game
        self.path = []
        self.tower_foundations_pos = []
        self.tower_foundations = []
    
    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))
        for tile_object in self.tmxdata.objects:
            if tile_object.type == "waypoint":
                # Minus with 16 on the x and y to get the center position of the 32x32 objects and add that as a waypoint to get path list.
                self.path.append(((tile_object.x - 16), (tile_object.y - 16)))
            elif tile_object.type == "Tower_foundation":
                self.tower_foundations.append(TowerFoundation(self.game, ((tile_object.x), (tile_object.y))))
    
    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface

    def draw_map(self, surface, map_img, pos):
        surface.blit(map_img, pos)