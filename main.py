import pygame
import sys
import random

# Inicialización de PyGame
pygame.init()

# Dimensiones de la pantalla
screen_width = 800
screen_height = 600

# Crear la ventana del juego
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('KODLAND TP TUTOR - REARTE')

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)  # Color para resaltar la opción seleccionada

# Definir el personaje
player_size = 50
player_color = GREEN
player_x = 10  # Posición X del personaje ajustada a 10
player_y = screen_height // 2  # Posición Y del personaje en el centro vertical
player_speed = 0.5  # Velocidad del personaje ajustada a 0.5

# Definir la bala
bullet_width = 10
bullet_height = 5
bullet_color = BLUE
bullet_speed = 1  # Velocidad de la bala ajustada a 1
bullets = []
max_bullets = 5  # Número máximo de balas que puede disparar el jugador

class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, bullet_width, bullet_height)

    def update(self):
        self.rect.x += bullet_speed

    def draw(self):
        pygame.draw.rect(screen, bullet_color, self.rect)

# Definir el enemigo
enemy_size = 50

class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, enemy_size, enemy_size)

    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)

def create_enemies(num_enemies):
    enemies = []
    start_x = screen_width - 50  # Posición inicial en el eje X
    for _ in range(num_enemies):
        y_position = random.randint(0, screen_height - enemy_size)  # Posición Y aleatoria dentro de la pantalla
        enemies.append(Enemy(start_x, y_position))
    return enemies

# Funciones personalizadas
def show_main_menu():
    font = pygame.font.Font(None, 74)
    text = font.render('Presiona Enter para jugar', True, BLACK)  # Texto en blanco
    screen.blit(text, (100, 250))
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False

def show_enemy_menu():
    font = pygame.font.Font(None, 74)
    font_selected = pygame.font.Font(None, 100)
    text = font.render('Selecciona cantidad de enemigos:', True, BLACK)  # Texto en blanco
    screen.blit(text, (50, 100))

    font_small = pygame.font.Font(None, 50)
    options = ['1', '2', '3', '4', '5']
    selected = 1
    while True:
        screen.fill(WHITE)  # Limpiar pantalla
        screen.blit(text, (50, 100))
        
        for i, option in enumerate(options):
            color = LIGHT_BLUE if i + 1 == selected else BLACK
            font_to_use = font_selected if i + 1 == selected else font_small
            text_option = font_to_use.render(option, True, color)
            screen.blit(text_option, (50 + i * 60, 300))
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and selected > 1:
                    selected -= 1
                if event.key == pygame.K_RIGHT and selected < len(options):
                    selected += 1
                if event.key == pygame.K_RETURN:
                    return selected

def draw_player(x, y):
    pygame.draw.rect(screen, player_color, (x, y, player_size, player_size))

def check_collisions(bullets, enemies, enemies_kill):
    for bullet in bullets[:]:
        for enemy in enemies:
            if bullet.rect.colliderect(enemy.rect):
                bullets.remove(bullet)
                enemies.remove(enemy)
                enemies_kill += 1
    return enemies_kill

def draw_stats(num_bullets, enemies_kill):
    font = pygame.font.Font(None, 36)
    bullets_text = font.render(f'Munición gastada: {num_bullets}', True, BLACK)
    enemies_text = font.render(f'Enemigos matados: {enemies_kill}', True, BLACK)
    screen.blit(bullets_text, (10, 10))
    screen.blit(enemies_text, (10, 40))

def game_loop(num_enemies):
    global player_x, player_y
    num_bullets = 0
    enemies_kill = 0
    bullets = []
    
    while True:
        enemies = create_enemies(num_enemies)
        game_running = True
        
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and len(bullets) < max_bullets:
                        bullets.append(Bullet(player_x + player_size, player_y + player_size // 2))
                        num_bullets += 1

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                player_y -= player_speed
            if keys[pygame.K_DOWN]:
                player_y += player_speed

            # Asegurar que el personaje no se mueva fuera de la pantalla
            if player_y < 0:
                player_y = 0
            if player_y > screen_height - player_size:
                player_y = screen_height - player_size

            # Actualizar las balas
            for bullet in bullets[:]:
                bullet.update()
                if bullet.rect.x > screen_width:
                    bullets.remove(bullet)

            # Comprobar colisiones entre balas y los enemigos
            enemies_kill = check_collisions(bullets, enemies, enemies_kill)
            
            # Comprobar si quedan enemigos
            if not enemies:
                game_running = False
                show_main_menu()  # Mostrar menú de inicio después de eliminar todos los enemigos

            screen.fill(WHITE)
            for enemy in enemies:
                enemy.draw()
            draw_player(player_x, player_y)
            for bullet in bullets:
                bullet.draw()
            draw_stats(num_bullets, enemies_kill)  # Mostrar estadísticas en pantalla
            pygame.display.flip()

if __name__ == '__main__':
    num_enemies = show_enemy_menu()
    game_loop(num_enemies)
