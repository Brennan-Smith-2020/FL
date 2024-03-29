## setup file for game

import warnings

# Ignore libpng warnings about incorrect sRGB profile
warnings.filterwarnings("ignore", category=UserWarning, message=".*iCCP: known incorrect sRGB profile.*")

# Set player pos
x = 100
y = 100