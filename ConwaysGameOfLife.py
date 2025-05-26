Shruthi.p/1AY24AI104/o Sec
import random
import time
import os

WIDTH = 40
HEIGHT = 20

def create_grid():
    return [[random.choice([0, 1]) for _ in range(WIDTH)] for _ in range(HEIGHT)]

def display_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears the terminal
    for row in grid:
        print(''.join(['■' if cell else ' ' for cell in row]))

def get_neighbors(grid, x, y):
    neighbors = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            nx, ny = x + i, y + j
            if 0 <= nx < HEIGHT and 0 <= ny < WIDTH:
                neighbors += grid[nx][ny]
    return neighbors

def next_generation(grid):
    new_grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for i in range(HEIGHT):
        for j in range(WIDTH):
            neighbors = get_neighbors(grid, i, j)
            if grid[i][j] == 1:
                if neighbors in [2, 3]:
                    new_grid[i][j] = 1
            else:
                if neighbors == 3:
                    new_grid[i][j] = 1
    return new_grid

def main():
    grid = create_grid()
    try:
        while True:
            display_grid(grid)
            grid = next_generation(grid)
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("\nSimulation stopped.")

if __name__ == "__main__":
    main()
