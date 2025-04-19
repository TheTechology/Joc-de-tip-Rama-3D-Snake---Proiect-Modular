import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from snake import Snake
from food import Food
from camera import Camera
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF|OPENGL)
        pygame.display.set_caption("Rama 3D")
        
        self.clock = pygame.time.Clock()
        self.camera = Camera()
        self.snake = Snake()
        self.walls = self.generate_walls()
        self.food = Food(self.walls, self.snake.positions)
        self.score = 0
        self.game_over = False
        
    def generate_walls(self):
        # Generează pereții în formă de cub
        walls = []
        wall_size = 15
        for x in range(-wall_size, wall_size+1):
            for y in range(-wall_size, wall_size+1):
                for z in range(-wall_size, wall_size+1):
                    if (abs(x) == wall_size or 
                        abs(y) == wall_size or 
                        abs(z) == wall_size):
                        walls.append((x, y, z))
        return walls
    
    def draw_walls(self):
        for wall in self.walls:
            self.draw_cube(wall, COLORS['wall'][0])
    
    def draw_cube(self, pos, color):
        # ... (similar cu metoda din Snake)
        pass
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if not self.game_over:
                    if event.key == pygame.K_RIGHT:
                        self.snake.change_direction((1, 0, 0))
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction((-1, 0, 0))
                    elif event.key == pygame.K_UP:
                        self.snake.change_direction((0, 1, 0))
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction((0, -1, 0))
                    elif event.key == pygame.K_w:
                        self.snake.change_direction((0, 0, 1))
                    elif event.key == pygame.K_s:
                        self.snake.change_direction((0, 0, -1))
            
            self.camera.handle_event(event)
        
        return True
    
    def update(self):
        if not self.game_over:
            current_time = pygame.time.get_ticks() / 1000
            if self.snake.move(current_time):
                # Verifică coliziuni
                if self.snake.check_collision(self.walls):
                    self.game_over = True
                
                # Verifică dacă a mâncat mâncarea
                if self.snake.positions[0] == self.food.position:
                    self.snake.grow = True
                    self.score += 10
                    self.food = Food(self.walls, self.snake.positions)
    
    def render(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)
        
        self.camera.update()
        
        # Desenează elementele jocului
        self.draw_walls()
        self.snake.draw()
        self.food.draw(self.clock.get_time() / 1000)
        
        # Afișează scorul
        pygame.display.set_caption(f"Rama 3D - Scor: {self.score}")
        
        pygame.display.flip()
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)
        
        pygame.quit()
