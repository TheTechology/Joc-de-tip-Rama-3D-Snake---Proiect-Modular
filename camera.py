from OpenGL.GL import *
from OpenGL.GLU import *
import pygame

class Camera:
    def __init__(self):
        self.angle_x = 30
        self.angle_y = -45
        self.distance = 50
        
    def update(self):
        glLoadIdentity()
        gluPerspective(45, (800/600), 0.1, 1000)
        
        # Poziționare cameră
        glTranslatef(0, 0, -self.distance)
        glRotatef(self.angle_x, 1, 0, 0)
        glRotatef(self.angle_y, 0, 1, 0)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:  # Drag cu butonul stâng
                self.angle_y += event.rel[0] * 0.5
                self.angle_x -= event.rel[1] * 0.5
                
        elif event.type == pygame.MOUSEWHEEL:
            self.distance = max(10, min(self.distance - event.y * 5, 200))
