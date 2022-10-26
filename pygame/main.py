import pygame

pygame.init()

screen_width = 500
screen_height = 500
background_color = (100, 100, 100)
player_size = (50, 50)
player_color = (255, 255, 255)
player_position = [screen_width / 2, screen_height / 2]

player = pygame.Surface(player_size)
player.fill(player_color)

screen = pygame.display.set_mode([screen_width, screen_height])
screen.fill(background_color)
screen.blit(player, player_position)

pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed_key = pygame.get_pressed();

    if pressed_key[pygame.KEY_UP]:
        player_position[1] -= 1


pygame.quit()




