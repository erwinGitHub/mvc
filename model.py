import pygame
from eventmanager import *

class GameEngine(object):
    """
    Tracks the game state.
    """

    def __init__(self, evManager):
        """
        evManager (EventManager): Allows posting messages to the event queue.
        Attributes:
        running (bool): True while the engine is online. Changed via QuitEvent().
        """
            
        self.evManager = evManager
        evManager.RegisterListener(self)
        self.running = False
        self.currentKey = None

    def notify(self, event):
        """
        Called by an event in the message queue. 
        """

        if isinstance(event, QuitEvent):
            self.running = False
        elif isinstance(event, InputEvent):
            self.currentKey = event.char

    def run(self):
        """
        Starts the game engine loop.
        This pumps a Tick event into the message queue for each loop.
        The loop ends when this object hears a QuitEvent in notify(). 
        """
        self.running = True
        self.evManager.Post(InitializeEvent())
        newTick = TickEvent()
        while self.running:
            self.evManager.Post(newTick)
