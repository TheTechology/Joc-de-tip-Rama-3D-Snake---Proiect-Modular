import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from settings import *

class Snake:
    def __init__(self):
        self.positions = [(0, 0, 0)]
        for i in range(1, INITIAL_LENGTH):
            self.positions.append((-i, 0, 0))
        self.direction = (1, 0, 0)
        self.last_move_time = 0
        self.grow = False
        
    def change_direction(self, new_dir):
        # Previntre inversarea directiei
        if (new_dir[0] * -1, new_dir[1] * -1, new_dir[2] * -1) != self.direction:
            self.direction = new_dir
    
    def move(self, current_time):
        if current_time - self.last_move_time >= MOVE_INTERVAL:
            head = self.positions[0]
            new_head = (
                head[0] + self.direction[0],
                head[1] + self.direction[1],
                head[2] + self.direction[2]
            )
            
            self.positions.insert(0, new_head)
            if not self.grow:
                self.positions.pop()
            else:
                self.grow = False
                
            self.last_move_time = current_time
            return True
        return False
    
    def draw(self):
        for i, pos in enumerate(self.positions):
            # Culori alternante pentru efect 3D
            color = COLORS['snake'][i % 2]
            self.draw_cube(pos, color)
    
    def draw_cube(self, pos, color):
        x, y, z = pos
        size = GRID_SIZE / 2
        
        glPushMatrix()
        glTranslatef(x * GRID_SIZE, y * GRID_SIZE, z * GRID_SIZE)
        glColor3f(*color)
        
        # Desenează cubul
        glBegin(GL_QUADS)
        # Fațetele cubului (sus, jos, față, spate, stânga, dreapta)
        # ... (cod pentru desenare cub OpenGL)
        glEnd()
        
        glPopMatrix()
    
    def check_collision(self, walls):
        head = self.positions[0]
        # Coliziune cu pereții
        if head in walls:
            return True
        # Coliziune cu sine
        if head in self.positions[1:]:
            return True
        return False
