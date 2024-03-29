import time
from World_Generator.generate_world import generate_terrain
from World_Generator.dungeonSpawnA1 import generate_D0A0

# Define the paths to grass, tree, and rock images
grass_images = [
    "Assets/Grass And Road Tiles/Grass And Road Tiles/Tiles/Grass0 - 0.png",
    "Assets/Grass And Road Tiles/Grass And Road Tiles/Tiles/Grass0 - 1.png",
    "Assets/Grass And Road Tiles/Grass And Road Tiles/Tiles/Grass0 - 2.png",
    "Assets/Grass And Road Tiles/Grass And Road Tiles/Tiles/Grass0 - 3.png",
    "Assets/Grass And Road Tiles/Grass And Road Tiles/Tiles/Grass0 - 4.png",
]

rock_images = [
    "Assets/Grass And Road Tiles/Grass And Road Tiles/Tiles/Rock - 0.png",
    "Assets/Grass And Road Tiles/Grass And Road Tiles/Tiles/Rock - 1.png",
]

tree_images = [
    "Assets/Grass And Road Tiles/Grass And Road Tiles/Tiles/Tree - 0.png",
    "Assets/Grass And Road Tiles/Grass And Road Tiles/Tiles/Tree - 1.png",
]

player_path_idle_1 = 'Assets/Player/tile034.png'
player_path_idle_2 = 'Assets/Player/tile000.png'

class Player:
    def __init__(self, speed, speed_in_atk):
        self.speed = speed  # Moves 1 tile/sec
        self.speed_in_atk = speed_in_atk  # Moves 0.2 tiles/sec while attacking

def loadPlayer(pygame, screen, x, y):
    # Load player images
    player_idle_image_1 = pygame.image.load(player_path_idle_1)
    player_idle_image_2 = pygame.image.load(player_path_idle_2)
    
    # Display the player images
    screen.blit(player_idle_image_1, (x, y))
    pygame.display.flip()