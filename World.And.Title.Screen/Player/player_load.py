import time

player_path_idle_1 = 'Assets/Player/tile034.png'
player_path_idle_2 = 'Assets/Player/tile000.png'

class Player:
    def __init__(self, speed, speed_in_atk):
        self.speed = speed  # Moves 1 tile/sec
        self.speed_in_atk = speed_in_atk  # Moves 0.2 tiles/sec while attacking

def loadPlayer(pygame, screen):
    # Load player images
    player_idle_image_1 = pygame.image.load(player_path_idle_1)
    player_idle_image_2 = pygame.image.load(player_path_idle_2)
    
    # Display the player images
    screen.blit(player_idle_image_1, (100, 100))
    pygame.display.flip()
    time.sleep(0.7)
    screen.blit(player_idle_image_2, (100, 100))
    pygame.display.flip()
