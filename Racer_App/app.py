# Black Jackal
# louw.reyneke.otto@gmail.com


class AlcornRacer:
    def __init__(self):
        self.actual = []
        self.predictions = {}
        self.scores = {}

    # Create Score Logic Function
    def _calculate_player_score(self, predicted: list[str, str, str]) -> int:
        """
        Calculate points based on a player's prediction and the actual results.

        :param predicted: The player's predicted top 3 finishers.

        :return: The total points awarded to the player based on prediction accuracy.
        """
        points = 0
        # Define the base points for each position
        point_values = {0: 5, 1: 4, 2: 3}

        for i, predicted_finisher in enumerate(predicted):
            if predicted_finisher in self.actual:
                # Find the actual position of the predicted finisher
                actual_position = self.actual.index(predicted_finisher)

                # Calculate points with penalty
                points += max(point_values[i] - abs(i - actual_position), 0)

        return points

    def _order_by_rank(self) -> list:
        """
        Orders Predictions by score in list
        :return: a list with a tuple containing the score and username
        """
        return sorted(self.scores.items(), key=lambda x: x[1], reverse=True)

    def get_scores(self) -> list:
        """
        Calculates scores based on prediction accuracy.
        :return: Nothing
        """
        for username, predictions in self.predictions.items():
            self.scores[username] = self._calculate_player_score(predictions)

        return self._order_by_rank()

    def add_prediction(self) -> None:
        print("\n===== Prediction Entry ====")

        # Username
        username = str(input("Username:         "))
        print("Please be sure to enter names correctly.")

        # Predictions
        first = str(input("First:            "))
        second = str(input("Second:           "))
        third = str(input("Third:            "))

        self.predictions[username] = [first, second, third]
        print(f"\nPredictions added for {username}.")

        del username, first, second, third

    def show_predictions(self) -> None:
        print("\n======= Predictions =======")
        for username, predictions in self.predictions.items():
            prediction_rank = 1
            print(f"\n{username}")
            for prediction in predictions:
                print(f"    {prediction_rank} {prediction}")
                prediction_rank += 1

        return self.predictions

    def add_actual(self, ) -> None:
        print("\n=========== Actual ==========")
        # Predictions
        first = str(input("First:             "))
        second = str(input("Second:            "))
        third = str(input("Third:             "))

        # Update Actual
        self.actual = [first, second, third]

        show_score = input("Show scores? [y/n] ")

        if show_score.lower() == "y":
            self.get_scores()
            self.show_rankings()

    def show_rankings(self):
        place = 1
        for username, score in self._order_by_rank():
            print(f"\n{place:0>3} {username+': ':<40}{score}")

        return self._order_by_rank()

    def run(self):
        while True:

            # Show Menu
            print("\n========== Alcorn Racer ==========")
            print("1    Add Prediction")
            print("2    Show Predictions")
            print("3    Add Actual")
            print("4    Show Rankings")
            print("5    Quit")

            # Get Command
            command = int(input("\nEnter command:     "))

            if command == 1:
                self.add_prediction()
            elif command == 2:
                self.show_predictions()
            elif command == 3:
                self.add_actual()
                self.get_scores()
            elif command == 4:
                self.show_rankings()
            elif command == 5:
                break


if __name__ == "__main__":
    AlcornRacer().run()
