import pygame
from eventmanager import *

class InputDevice:
    """
    Handles keyboard and mouse input.
    """

    def __init__(self, evManager):
        """
        evManager (EventManager): Allows posting messages to the event queue.
        """
        self.evManager = evManager
        evManager.RegisterListener(self)

    def notify(self, event):
        """
        Receive events posted to the message queue. 
        """

        if isinstance(event, TickEvent):
            # Called for each game tick. We check our keyboard/mouse presses here.
            for current_event in pygame.event.get():
                # handle window manager closing our window
                if current_event.type == pygame.QUIT:
                    self.evManager.Post(QuitEvent())
                # handle key down events
                if current_event.type == pygame.KEYDOWN:
                    if current_event.key == pygame.K_ESCAPE:
                        self.evManager.Post(QuitEvent())
                    else:
                        # post any other keys to the message queue for everyone else to see
                        self.evManager.Post(InputEvent(current_event.unicode, None, None))
                # handle key up events
                if current_event.type == pygame.KEYUP:
                    # post that key was up to the message queue for everyone else to see
                    self.evManager.Post(InputEvent(None, None, None))
                # handle mousebuttondown events
                if current_event.type == pygame.MOUSEBUTTONDOWN:
                    # post that mouse button was klicked to the message queue for everyone else to see
                    self.evManager.Post(InputEvent(None, pygame.mouse.get_pos(), pygame.mouse.get_pressed()))
