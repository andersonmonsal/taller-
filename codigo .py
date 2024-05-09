class Frame:
    def __init__(self):
        self.rolls = []

    def add_roll(self, pins):
        self.rolls.append(pins)

    def is_strike(self):
        return len(self.rolls) == 1 and self.rolls[0] == 10

    def is_spare(self):
        return len(self.rolls) == 2 and sum(self.rolls) == 10


class Game:
    def __init__(self):
        self.frames = [Frame() for _ in range(10)]
        self.current_frame = 0

    def roll(self, pins):
        frame = self.frames[self.current_frame]
        frame.add_roll(pins)
        if frame.is_strike() or len(frame.rolls) == 2:
            self.current_frame += 1

    def calculate_score(self):
        score = 0
        frame_index = 0
        for frame in self.frames:
            score += sum(frame.rolls)
            if frame.is_strike():
                if frame_index < 9:
                    next_frame = self.frames[frame_index + 1]
                    score += sum(next_frame.rolls[:2])
                    if next_frame.is_strike() and frame_index < 8:
                        score += self.frames[frame_index + 2].rolls[0]
                elif frame_index == 9:
                    score += sum(frame.rolls)  # strike in last frame
            elif frame.is_spare():
                if frame_index < 9:
                    score += self.frames[frame_index + 1].rolls[0]
                elif frame_index == 9:
                    score += self.frames[frame_index].rolls[2]  # spare in last frame
            frame_index += 1
        return score

