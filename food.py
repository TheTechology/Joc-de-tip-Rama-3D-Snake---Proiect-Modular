from OpenGL.GL import *
from OpenGL.GLU import *
import random
from settings import *

class Food:
    def __init__(self, walls, snake_positions):
        self.position = self.generate_position(walls, snake_positions)
        self.rotation = 0
        
    def generate_position(self, walls, snake_positions):
        while True:
            pos = (
                random.randint(-10, 10),
                random.randint(-10, 10),
                random.randint(-10, 10)
            )
            if pos not in walls and pos not in snake_positions:
                return pos
    
    def draw(self, delta_time):
        self.rotation += delta_time * 50  # Rotire continuă
        
        x, y, z = self.position
        size = GRID_SIZE / 2
        
        glPushMatrix()
        glTranslatef(x * GRID_SIZE, y * GRID_SIZE, z * GRID_SIZE)
        glRotatef(self.rotation, 1, 1, 1)  # Rotire pe toate axele
        
        # Culori alternante pentru efect 3D
        glColor3f(*COLORS['food'][0])
        
        # Desenează cubul de mâncare
        glBegin(GL_QUADS)
        # ... (cod similar cu cel din Snake pentru desenare cub)
        glEnd()
        
        glPopMatrix()
