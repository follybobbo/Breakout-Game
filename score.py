class Score:


    def __init__(self):
        self.total_score = 0


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
        pass



    """Take in index of rect as parameter, and add score accourding to index of rect collide."""