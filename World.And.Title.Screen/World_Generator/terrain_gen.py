# terrain_generator.py
import random
import numpy as np
from . import noise


def save_seed(seed):
    with open("seed.txt", "w") as file:
        file.write(str(seed))

def create_seed():
    seed = random.seed()
    save_seed(seed)  # Save the seed to a file
    return seed

def load_seed():
    try:
        with open("seed.txt", "r") as file:
            seed = file.read().strip()  # Remove leading/trailing whitespace
            print(seed)
        return seed
    except FileNotFoundError:
        seed = create_seed()  # Generate and save new seed if the file doesn't exist
        return seed

def generate_terrain(width, height, seed):
    scale = 100.0  # Adjust the scale as needed
    octaves = 6
    persistence = 0.5
    lacunarity = 2.0

    terrain = np.zeros((height, width))

    for y in range(height):
        for x in range(width):
            noise_val = noise.noise2(x / scale, y / scale, octaves, persistence, lacunarity, seed=seed)
            terrain[y][x] = noise_val * 50

    return terrain
