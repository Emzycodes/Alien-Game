import sys
import pygame #imports the pygame lib
from settings import Settings

class AlienInvasion :

    def __init__(self):
        """ Initialize the game, and create a game resource"""
        pygame.init()

        self.settings = Settings() 
        self.screen = pygame.display.set_mode((
            self.settings.screen_width,self.settings.screen_height
        ))
        pygame.display.set_caption("Alien Invasion")

        self.bg_color = (230,100,220)

    def run_game(self):
        # Set the background color 
        """ Start the main loop for the game"""
        while True:
            # Watch for mouse and keyboard events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # # Make the most recently drawn screen visible.        
            pygame.display.flip()
            
if __name__ == '__main__':
 # Make a game instance, and run the game.
     ai = AlienInvasion()
     ai.run_game()