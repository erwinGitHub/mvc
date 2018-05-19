import eventmanager
import model
import view
import controller

def run():
    evManager = eventmanager.EventManager()
    gameModel = model.GameEngine(evManager)
    keyboard = controller.Keyboard(evManager)
    graphics = view.GraphicalView(evManager, gameModel)
    gameModel.run()

if __name__ == '__main__':
    run()
