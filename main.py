import sys
from PyQt5 import QtWidgets, uic
from mancala import Mancala


class GameUi(QtWidgets.QMainWindow):
    def __init__(self):
        self.__mancala = Mancala()
        super(GameUi, self).__init__()
        uic.loadUi(r'cw3_ui.ui', self)
        self.a_studnia.mousePressEvent = self.clicked_studnia_a
        self.a_0.mousePressEvent = self.clicked_a0
        self.a_1.mousePressEvent = self.clicked_a1
        self.a_2.mousePressEvent = self.clicked_a2
        self.a_3.mousePressEvent = self.clicked_a3
        self.a_4.mousePressEvent = self.clicked_a4
        self.a_5.mousePressEvent = self.clicked_a5

        self.b_studnia.mousePressEvent = self.clicked_studnia_b
        self.b_0.mousePressEvent = self.clicked_b0
        self.b_1.mousePressEvent = self.clicked_b1
        self.b_2.mousePressEvent = self.clicked_b2
        self.b_3.mousePressEvent = self.clicked_b3
        self.b_4.mousePressEvent = self.clicked_b4
        self.b_5.mousePressEvent = self.clicked_b5

        self.start_game.mousePressEvent = self.start_new_game

    def start_new_game(self, event):
        self.__mancala = Mancala()
        self.__renew_game_state()
        self.info.setText("Game")

    def clicked_studnia_a(self, event):
        print("clicked studnia a")
        #self.__mancala.step_player(6, 'a')

    def clicked_a0(self, event):
        print("clicked a0")
        self.__mancala.step_player(0, 'a')
        self.__renew_game_state()

    def clicked_a1(self, event):
        print("clicked a1")
        self.__mancala.step_player(1, 'a')
        self.__renew_game_state()

    def clicked_a2(self, event):
        print("clicked a2")
        self.__mancala.step_player(2, 'a')
        self.__renew_game_state()

    def clicked_a3(self, event):
        print("clicked a3")
        self.__mancala.step_player(3, 'a')
        self.__renew_game_state()

    def clicked_a4(self, event):
        print("clicked a4")
        self.__mancala.step_player(4, 'a')
        self.__renew_game_state()

    def clicked_a5(self, event):
        print("clicked a5")
        self.__mancala.step_player(5, 'a')
        self.__renew_game_state()

    def clicked_studnia_b(self, event):
        print("clicked studnia b")
        #self.__mancala.step_player(6, 'b')

    def clicked_b0(self, event):
        print("clicked b0")
        self.__mancala.step_player(0, 'b')
        self.__renew_game_state()

    def clicked_b1(self, event):
        print("clicked b1")
        self.__mancala.step_player(1, 'b')
        self.__renew_game_state()

    def clicked_b2(self, event):
        print("clicked b2")
        self.__mancala.step_player(2, 'b')
        self.__renew_game_state()

    def clicked_b3(self, event):
        print("clicked b3")
        self.__mancala.step_player(3, 'b')
        self.__renew_game_state()

    def clicked_b4(self, event):
        print("clicked b4")
        self.__mancala.step_player(4, 'b')
        self.__renew_game_state()

    def clicked_b5(self, event):
        print("clicked b5")
        self.__mancala.step_player(5, 'b')
        self.__renew_game_state()

    def __renew_game_state(self):
        self.a_studnia.setText(str(self.__mancala.player_a.containers[6].num_stones))
        self.a_0.setText(str(self.__mancala.player_a.containers[0].num_stones))
        self.a_1.setText(str(self.__mancala.player_a.containers[1].num_stones))
        self.a_2.setText(str(self.__mancala.player_a.containers[2].num_stones))
        self.a_3.setText(str(self.__mancala.player_a.containers[3].num_stones))
        self.a_4.setText(str(self.__mancala.player_a.containers[4].num_stones))
        self.a_5.setText(str(self.__mancala.player_a.containers[5].num_stones))

        self.b_studnia.setText(str(self.__mancala.player_b.containers[6].num_stones))
        self.b_0.setText(str(self.__mancala.player_b.containers[0].num_stones))
        self.b_1.setText(str(self.__mancala.player_b.containers[1].num_stones))
        self.b_2.setText(str(self.__mancala.player_b.containers[2].num_stones))
        self.b_3.setText(str(self.__mancala.player_b.containers[3].num_stones))
        self.b_4.setText(str(self.__mancala.player_b.containers[4].num_stones))
        self.b_5.setText(str(self.__mancala.player_b.containers[5].num_stones))

        if self.__mancala.finish:
            print("finish game")
            winner = "Player A" if self.__mancala.player_a.containers[-1].num_stones > self.__mancala.player_b.containers[-1].num_stones else "Player B"
            self.info.setText("{} wins".format(winner))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = GameUi()
    widget.show()
    app.exec_()

