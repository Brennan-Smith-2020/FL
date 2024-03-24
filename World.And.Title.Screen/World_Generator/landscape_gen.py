# landscape_gen.py
import pygame
import random
from World_Generator.terrain_gen import load_seed, create_seed, generate_terrain


def generate_landscape(screen, grass_images, tree_images, rock_images, seed=None):
    if seed is None:
        seed = load_seed()  # Load seed from file if not provided
    if seed is None:
        seed = create_seed()  # Generate and save new seed if none exists

    random.seed(seed)  # Set the seed for random module

    # Set up constants for grid dimensions
    grid_width, grid_height = 100, 50  # Adjust as needed

    # Calculate dynamic tile size based on screen dimensions
    tile_size = 16  # Adjust as needed

    # Generate terrain heights using Perlin noise
    terrain_heights = generate_terrain(grid_width, grid_height, seed)

    # Load grass, tree, and rock images
    grass_images = [pygame.image.load(image_path).convert_alpha() for image_path in grass_images]
    tree_images = [pygame.image.load(image_path).convert_alpha() for image_path in tree_images]
    rock_images = [pygame.image.load(image_path).convert_alpha() for image_path in rock_images]

    # Generate landscape based on terrain heights
    for row in range(grid_height):
        for col in range(grid_width):
            height = terrain_heights[row][col]

            # Render grass
            if height < 10:
                grass_image = random.choice(grass_images)
                screen.blit(grass_image, (col * tile_size, row * tile_size))
            # Render trees
            elif height < 30:
                tree_image = random.choice(tree_images)
                screen.blit(tree_image, (col * tile_size, row * tile_size))
            # Render rocks
            elif height < 50:
                rock_image = random.choice(rock_images)
                screen.blit(rock_image, (col * tile_size, row * tile_size))

    # Update display
    pygame.display.flip()