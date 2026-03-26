import pygame
from Setting import *


class Menu:
    def __init__(self):
        pygame.font.init()
        self.title_font = pygame.font.SysFont(None, 100)
        self.button_font = pygame.font.SysFont(None, 50)

        button_width = 200
        button_height = 50
        center_x = WindowWidth / 2 - button_width / 2

        self.start_rect = pygame.Rect(center_x, 300, button_width, button_height)
        self.score_rect = pygame.Rect(center_x, 400, button_width, button_height)

        self.current_state = "MENU"

    def draw(self, screen):

        screen.fill((0, 0, 0))

        # --- Draw Title ---
        title_text = self.title_font.render('MAZE RUNNER', True, (255, 50, 50))
        screen.blit(title_text, (WindowWidth / 2 - title_text.get_width() / 2, 100))

        # --- Draw Start Button ---
        pygame.draw.rect(screen, (40, 40, 40), self.start_rect)
        start_text = self.button_font.render('START', True, (255, 255, 255))
        screen.blit(start_text, (self.start_rect.x + 45, self.start_rect.y + 10))

        # --- Draw Scores Button ---
        # this part is in progress so the color i set to be a but off
        pygame.draw.rect(screen, (20, 20, 20), self.score_rect)
        score_text = self.button_font.render('SCORES', True, (100, 100, 100))
        screen.blit(score_text, (self.score_rect.x + 30, self.score_rect.y + 10))


        # TODO: Add a "Settings" or "Quit" button render here later if needed

    def draw_win_screen(self, screen):
        screen.fill((0, 0, 0))

        # --- Draw "YOU WIN" Text ---
        win_text = self.title_font.render('YOU WIN!', True, (50, 255, 50))  # Nice bright green
        screen.blit(win_text, (WindowWidth / 2 - win_text.get_width() / 2, 150))

        # --- Draw Scores
        # TODO: Read from a saved text/json file and display the fastest times here
        score_text = self.button_font.render('SCORES: [To be implemented]', True, (255, 255, 255))
        screen.blit(score_text, (WindowWidth / 2 - score_text.get_width() / 2, 300))

        return_text = self.button_font.render('Press N to Return to Menu', True, (100, 100, 100))
        screen.blit(return_text, (WindowWidth / 2 - return_text.get_width() / 2, 450))

    def update(self, events):
        self.current_state = "MENU"

        for event in events:

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if self.start_rect.collidepoint(mouse_pos):
                    self.current_state = "PLAY"

                elif self.score_rect.collidepoint(mouse_pos):
                    # TODO: Implement reading the score file here
                    # TODO: Change self.current_state to "SCORE_SCREEN" once built
                    print("Scores button clicked! (Score system not yet implemented)")

        return self.current_state