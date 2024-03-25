# landscape_gen.py
import pygame
import random


# Initialize pygame
pygame.init()

def generate_terrain(screen, grass_images, tree_images, rock_images, seed=None):
    # Set the seed
    if seed is not None:
        random.seed(seed)

    # Set up constants for grid dimensions
    grid_width, grid_height = 100, 50  # Adjust as needed

    # Calculate dynamic tile size based on screen dimensions
    tile_size = min(screen.get_width() // grid_width, screen.get_height() // grid_height)  # Adjust as needed

    grass_images = [pygame.image.load(image_path).convert_alpha() for image_path in grass_images]
    tree_images = [pygame.image.load(image_path).convert_alpha() for image_path in tree_images]
    rock_images = [pygame.image.load(image_path).convert_alpha() for image_path in rock_images]

    terrain = [[None for _ in range(grid_height)] for _ in range(grid_width)]

    # Generate terrain
    for x in range(grid_width):
        for y in range(grid_height):
            terrain[x][y] = random.choice(grass_images)

    # Add trees and rocks
    for x in range(grid_width):
        for y in range(grid_height):
            if terrain[x][y] in grass_images and random.random() < 0.1:
                terrain[x][y] = random.choice(tree_images)
            elif terrain[x][y] in tree_images and random.random() < 0.1:
                terrain[x][y] = random.choice(rock_images)

    # Render terrain
    for x in range(grid_width):
        for y in range(grid_height):
            # Calculate the position to center the image within the grid square
            image = terrain[x][y]
            image_rect = image.get_rect()
            x_pos = x * tile_size + (tile_size - image_rect.width) // 2
            y_pos = y * tile_size + (tile_size - image_rect.height) // 2
            
            # Adjust the y position for trees to center them vertically within the square
            if image in tree_images:
                y_pos += (tile_size - image_rect.height) // 4  # Adjust as needed for better visual alignment
            
            screen.blit(image, (x_pos, y_pos))


    pygame.display.flip()  # Update the display

    return terrain