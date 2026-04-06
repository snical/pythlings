# classes7
# Fix the program so it prints `Ada: best=12, average=9.0`.

# hint: This tracker needs a list of scores, the highest score, and the average score.
class ScoreTracker:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def record(self, score):
        self.scores.append(score)

    def best(self):
        return max(self.scores)

    def average(self):
        return sum(self.scores) / len(self.scores)

    def report(self):
        return self.name + ": best=" + str(self.best()) + ", average=" + str(round(self.average(), 1))


tracker = ScoreTracker("Ada")
for score in [8, 12, 7]:
    tracker.record(score)

print(tracker.report())
