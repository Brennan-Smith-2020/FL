import pygame
import random

def generate_D0A0(screen, dungeonFloor, dungeonDoor):
    # Load dungeon floor images
    dungeonFloor_imgs = [pygame.image.load(image_path).convert_alpha() for image_path in dungeonFloor]

    # Set up constants for grid dimensions
    grid_width, grid_height = 550, 250  # Adjust as needed

    # Calculate dynamic tile size based on screen dimensions
    tile_size = min(4, 4)

    # Setup terrain
    terrain = [[None for _ in range(grid_height)] for _ in range(grid_width)]

    # Define coordinates to blit the dungeon floor image
    blitmapX = [2, 3, 4, 5, 6, 7,
                2, 3, 4, 5, 6, 7,
                2, 3, 4, 5, 6, 7,
                2, 3, 4, 5, 6, 7,
                2, 3, 4, 5, 6, 7,
                2, 3, 4, 5, 6, 7,
                0, 1, 8, 9,
                0, 1, 8, 9,
                0, 1, 8, 9,
                0, 1, 8, 9,
                0, 1, 8, 9,
                0, 1, 8, 9,
]
    blitmapY = [2, 2, 2, 2, 2, 2,
                3, 3, 3, 3, 3, 3,
                4, 4, 4, 4, 4, 4,
                5, 5, 5, 5, 5, 5,
                6, 6, 6, 6, 6, 6,
                7, 7, 7, 7, 7, 7,
                0, 0, 0, 0,
                1, 1, 1, 1,
                2, 2, 2, 2,
                3, 3, 3, 3,
                4, 4, 4, 4,
                5, 5, 5, 5,
] # Adjust as needed

    for x in range(len(blitmapX)):  # Use len(blitmapX) instead of grid_width
        for y in range(len(blitmapY)):  # Use len(blitmapY) instead of grid_height
            if x < grid_width and y < grid_height:  # Add this condition to prevent accessing out-of-range indices
                if x == blitmapX[x] and y == blitmapY[y]:
                    terrain[x][y] = random.choice(dungeonFloor_imgs)
                    screen.blit(terrain[x][y], (blitmapX[x], blitmapY[y]))
