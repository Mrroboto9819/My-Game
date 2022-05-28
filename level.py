from re import I
import pygame
from settings import TILESIZE, WORLD_MAP
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprite = YSortCamaraGroup()
        self.obstacles_sprite = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for rowIndex,row in enumerate(WORLD_MAP):
            for colIndex,col in enumerate(row):
                x = colIndex * TILESIZE
                y = rowIndex * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprite,self.obstacles_sprite])
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprite], self.obstacles_sprite)
                print(colIndex)
                print(col)

    def run(self):
        self.visible_sprite.custom_draw(self.player)
        self.visible_sprite.update()
        # debug(self.player.direction)


class YSortCamaraGroup(pygame.sprite.Group):
    def __init__(self):
        
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery- self.half_height

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_rect = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_rect)
        