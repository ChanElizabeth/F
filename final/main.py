# Import menus
from screens.mainMenu import mainMenu
from screens.subMenu import subMenu
from screens.game import game
from screens.gameOver import gameOver

# Import objects
from objects.button import Button
from objects.statarrow import Statarrow

mainMenu(Button, Statarrow, subMenu, game, gameOver)
