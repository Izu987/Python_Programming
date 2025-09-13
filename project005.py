"""Build a Probability Calculator Project
"""
import random
import copy

class Hat:
    def __init__(self, **kwargs):
        """
        Initializes a Hat object.
        kwargs: key-value pairs representing color:count
        Example: Hat(red=5, blue=2)
        """
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        """
        Draw num_balls from the hat without replacement.
        Returns a list of drawn balls.
        """
        if num_balls >= len(self.contents):
            # If asking for more balls than available, return all
            drawn_balls = self.contents.copy()
            self.contents.clear()
            return drawn_balls
        
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Perform num_experiments trials, drawing num_balls_drawn balls
    from a copy of the hat each time, and estimate the probability
    of getting at least the expected_balls.
    """
    success_count = 0

    for _ in range(num_experiments):
        # Copy the hat so original isn't modified
        hat_copy = copy.deepcopy(hat)

        # Draw balls
        drawn = hat_copy.draw(num_balls_drawn)

        # Count occurrences of each color
        drawn_counts = {}
        for ball in drawn:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1

        # Check if drawn balls satisfy expected_balls
        success = True
        for color, count in expected_balls.items():
            if drawn_counts.get(color, 0) < count:
                success = False
                break

        if success:
            success_count += 1

    # Probability = successful outcomes / total experiments
    return success_count / num_experiments


# ---- Example Usage ----
if __name__ == "__main__":
    hat = Hat(blue=6, red=4, green=3)
    probability = experiment(
        hat=hat,
        expected_balls={"red": 2, "green": 1},
        num_balls_drawn=5,
        num_experiments=2000
    )
    print("Estimated Probability:", probability)