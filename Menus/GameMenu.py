import pygame
import Utils
import sys
import WorldMap
from pygame.locals import *

__author__ = "Jasmine Oliveira"
__date__ = "05/02/2016"


class GameMenu:
    """
    Defines and runs the main menu
    Displayed when the application starts
    Calls to the WorldMap to run the game
    """
    def __init__(self, screen, bg_color=(0, 0, 0), font=None, font_size=30,
                 font_color=(255, 255, 255)):
        """
        Initializes the GameMenu
        :param screen: the screen to draw on
        :param bg_color: background color, default white
        :param font: default None
        :param font_size: default 30
        :param font_color: default black
        """
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height

        self.bg_color = bg_color
        self.image = pygame.image.load("Resources/terrain/map2.png")       # background image
        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color

    def run(self):
        """
        Runs the main menu until the user selects either to begin the game or to quit
        :return: void
        """
        while True:
            # set title caption
            pygame.display.set_caption('Game Menu')

            # Redraw the background
            self.screen.fill(self.bg_color)

            # blit scaled cover
            cover = pygame.image.load("Resources/eco_sim_cover.png")
            cover = pygame.transform.scale(cover, (self.scr_width, self.scr_height))
            cover_rect = Rect((0,0), Utils.screen_size)
            Utils.screen.blit(cover, cover_rect)

            #begin menu
            menu_on = True

            # make buttons
            buttons = make_buttons(self)
            while menu_on:

                button_pressed = mouse_monitor(buttons)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            if not Utils.screen.get_flags() == FULLSCREEN:
                                pygame.display.set_mode(Utils.screen_size, pygame.FULLSCREEN)
                            else:
                                pygame.display.set_mode(Utils.screen_size)
                            cover = pygame.image.load("Resources/eco_sim_cover.png")
                            cover = pygame.transform.scale(cover, (self.scr_width, self.scr_height))
                            cover_rect = Rect((0, 0), Utils.screen_size)
                            Utils.screen.blit(cover, cover_rect)
                            pygame.display.flip()
                # If button 0, "Start" calls WorldMap
                # If button 1, "Quit" calls sys.exit()
                if button_pressed == 0:
                    WorldMap.display_map()
                    menu_on = False
                elif button_pressed == 1:
                    sys.exit()
                pygame.display.flip()


# makes start & quit buttons
def make_buttons(self):
    """
    Creates the list of buttons in the menu and blits them to the screen
    0: Start
    1: Quit
    :param self: GameMenu
    :return: the list of buttons
    """
    buttons = []

    # make a start button, Rect creates the rectangle to draw the button in
    start_button = pygame.image.load("Resources/buttons/startnormal.png")
    start_button_rect = Rect(((self.scr_width / 2)-200, (self.scr_height / 2)+210), (200, 100))

    # make a quit button, Rect creates the rectangle to draw the button in
    quit_button = pygame.image.load("Resources/buttons/quitnormal.png")
    quit_button_rect = Rect(((self.scr_width / 2) + 50, (self.scr_height / 2)+210), (200, 100))

    start_button_rect.right = Utils.screen.get_rect().centerx - 10
    quit_button_rect.left = Utils.screen.get_rect().centerx + 10
    # add buttons to the list
    buttons.append((start_button, start_button_rect))
    buttons.append((quit_button, quit_button_rect))

    # blit- puts stuff on the screen
    # blit terrain and buttons
    # flip just refreshes screen to display blits since last flip
    for button in buttons:
        Utils.screen.blit(button[0], button[1])
    pygame.display.flip()

    return buttons


def mouse_monitor(buttons):
    """
    Watches the mouse to detect hovering over and selection of buttons
    :param buttons: the buttons to watch
    :return: option (which buttons selected)
    """
    mouse = pygame.mouse    # our mouse from now on
    mouse_pos = mouse.get_pos()     # the position of the mouse
    option=-1
    for button in buttons:
        # while the mouse is within the bounds of any button in the button list
        while (button[1].left < mouse_pos[0] < button[1].right and
                button[1].top < mouse_pos[1] < button[1].bottom):
            # button[0] = start
            if buttons.index(button) == 0:
                # change to highlighted deer button
                start_button = pygame.image.load("Resources/buttons/startselected.png")
                Utils.screen.blit(start_button, button[1])
                pygame.display.flip()
                # waits for click to select deer button
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        option = 0
                        # button[1] = quit
            elif buttons.index(button) == 1:
                # change to highlighted wolf button
                stop_button = pygame.image.load("Resources/buttons/quitselected.png")
                Utils.screen.blit(stop_button, button[1])
                pygame.display.flip()
                # waits for click to select wolf button
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        option = 1
            # update position for while loop
            mouse_pos = mouse.get_pos()

    # return buttons to normal
    for button in buttons:
        Utils.screen.blit(button[0], button[1])
    pygame.display.flip()
    return option


def startGameMenu():
    """
    Entry point to the game menu. Call to run main menu.
    :return: void
    """
    # Start Game Menu
    pygame.display.set_caption('Game Menu')
    gm = GameMenu.GameMenu(Utils.screen)
    gm.run()
