from Menu import *
import pygame
from Setting import *
from Map import *
from Player import *
from Rays import *
from Raycaster import*
pygame.init()
#Set window size, need to make this adjustable later
clock = pygame.time.Clock()
Screen = pygame.display.set_mode((WindowWidth, WindowHeight))

map = Map()
player = Player(map)
raycaster = Raycaster(player,map)
game_menu = Menu()
current_state = "MENU"

while True:
    clock.tick(100)
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1 or event.key == pygame.K_m:
                pygame.quit()
                exit()

            if event.key == pygame.K_n:
                current_state = "MENU"
                map = Map()
                player = Player(map)
                raycaster = Raycaster(player, map)

    # --- STATE: MAIN MENU ---
    if current_state == "MENU":
        pygame.event.set_grab(False)
        pygame.mouse.set_visible(True)
        game_menu.draw(Screen)
        old_state = current_state
        current_state = game_menu.update(events)
        if current_state == "PLAY" and old_state == "MENU":
            start_time = pygame.time.get_ticks()



    # --- STATE: LEADERBOARD SCORES ---
    elif current_state == "SCORES":
        pygame.event.set_grab(False)
        pygame.mouse.set_visible(True)
        game_menu.draw_score_screen(Screen)


    # --- STATE: PLAYING-----
    elif current_state == "PLAY":

        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)
        Screen.fill((0, 0, 0))

        has_won = player.update()

        if has_won:
            current_state = "WIN"
            final_time = (pygame.time.get_ticks() - start_time) / 1000.0
            game_menu.save_score(final_time)
            current_state = "WIN"
        if current_state == "PLAY":
            raycaster.Castallrays(Screen)
            raycaster.render_25D(Screen)

    # --- STATE: WINNING-----
    elif current_state == "WIN":
        pygame.event.set_grab(False)
        pygame.mouse.set_visible(True)
        game_menu.draw_win_screen(Screen)


    pygame.display.update()




