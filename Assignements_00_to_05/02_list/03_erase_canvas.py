import pygame  

# Initialize Pygame
pygame.init()

# Define canvas dimensions
canvas_width = 500
canvas_height = 500
grid_size = 20  # Size of each cell in the grid

# Define colors
blue = (0, 0, 255)  # RGB for blue
white = (255, 255, 255)  # RGB for white
red = (255, 0, 0) # RGB for red - for the eraser

# Create the display surface (the window)
screen = pygame.display.set_mode((canvas_width, canvas_height))
pygame.display.set_caption("Canvas Eraser")

# Create a 2D list (grid) to represent the canvas state
# Initially, all cells are set to True (blue)
canvas_grid = [[True for _ in range(canvas_width // grid_size)] for _ in range(canvas_height // grid_size)]

# Function to draw the canvas
def draw_canvas():
    """
    This function draws the grid of blue/white cells on the screen
    """
    screen.fill(white)  # Start with a white background
    for row in range(canvas_height // grid_size):
        for col in range(canvas_width // grid_size):
            if canvas_grid[row][col]:  # If the cell is True (blue)
                pygame.draw.rect(screen, blue, (col * grid_size, row * grid_size, grid_size, grid_size))

# Function to "erase" cells
def erase_cells(eraser_rect):
    """
    This function "erases" cells (sets them to white) that overlap with the eraser rectangle.

    Args:
        eraser_rect (pygame.Rect): The rectangle representing the eraser's current position and size.
    """
    for row in range(canvas_height // grid_size):
        for col in range(canvas_width // grid_size):
            cell_rect = pygame.Rect(col * grid_size, row * grid_size, grid_size, grid_size)
            if eraser_rect.colliderect(cell_rect):  # Check for overlap
                canvas_grid[row][col] = False  # Set the cell to False (white)

# Game loop
running = True
erasing = False  # Flag to indicate if the eraser is active
eraser_size = 30  # Size of the square eraser
eraser_rect = pygame.Rect(0, 0, eraser_size, eraser_size) #initial position of eraser

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                erasing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                erasing = False
        elif event.type == pygame.MOUSEMOTION:
            if erasing:
                eraser_rect.center = event.pos  # Update eraser position
                erase_cells(eraser_rect)  # "Erase" overlapping cells

    # Draw everything
    draw_canvas()
    pygame.draw.rect(screen, red, eraser_rect) #draw the eraser
    pygame.display.flip()  # Update the display1234567890