from PyQt5.QtWidgets import *
from PyQt5 import uic
from app import AlcornRacer


class AlcornGUI(QMainWindow):
    def __init__(self):
        super(AlcornGUI, self).__init__()
        uic.loadUi('gui/alcorn.ui', self)
        self.show()

        self.racer = AlcornRacer()

        # Add Prediction Button
        self.submit_prediction.clicked.connect(self._submit_prediction)

        # Lock Prediction Button
        self.lock_preds.clicked.connect(self._lock_predictions)

        # Score Players Button
        self.score_players.clicked.connect(self._score_players)

    def _submit_prediction(self):
        self.racer.predictions[self.username.text()] = [
            self.pred_1.text(),
            self.pred_2.text(),
            self.pred_3.text(),
        ]

    def _lock_predictions(self):
        # Disable Entries
        self.username.setEnabled(False)
        self.pred_1.setEnabled(False)
        self.pred_2.setEnabled(False)
        self.pred_3.setEnabled(False)
        self.submit_prediction.setEnabled(False)
        self.lock_preds.setEnabled(False)

        # Enable Actual Results
        self.actual_1.setEnabled(True)
        self.actual_2.setEnabled(True)
        self.actual_3.setEnabled(True)
        self.score_players.setEnabled(True)

    def _score_players(self):
        self.racer.actual = [self.actual_1.text(), self.actual_2.text(), self.actual_3.text()]
        scores = self.racer.get_scores()

        for user, score in scores:
            self.display_content.append(f'{user+" ":-<23} {score}')


def main():
    app = QApplication([])
    window = AlcornGUI()
    window.setWindowTitle("Alcorn Racer")

    window.setFixedSize(580, 375)

    app.exec_()


if __name__ == '__main__':
    main()
