class Score:


    def __init__(self):
        self.total_score = 0
        self.best_score = 0


    #assigns different scores to different rows of blocks.
    def update_score(self, index):
        score = 0
        if index <= 15:
            score = 5
        elif 15 < index <= 31:
            score = 4
        elif 31 < index <= 47:
            score = 3
        elif index > 47:
            score = 2

        self.total_score += score

    def write_score_to_file(self):
        score_to_write = self.total_score
        with open("files/score_saver", mode="w") as file:
            file.write(f"score, {str(score_to_write)}")

    def read_score(self):
        with open("files/score_saver", mode="r") as file:
            read = file.readline()
            l = read.split(",")
            best_score = l[1].strip()

            self.best_score = best_score



    """Take in index of rect as parameter, and add score accourding to index of rect collide."""