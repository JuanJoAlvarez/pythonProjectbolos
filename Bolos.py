class Roll:
    def _init_(self, pins):
        self.pins = pins


class Frame:
    def _init_(self):
        self.rolls = []

    def is_strike(self):
        return len(self.rolls) == 1 and self.rolls[0].pins == 10

    def is_spare(self):
        return len(self.rolls) == 2 and sum(roll.pins for roll in self.rolls) == 10

    def is_open(self):
        return not self.is_strike() and not self.is_spare()

    def add_roll(self, roll):
        if len(self.rolls) < 2:
            self.rolls.append(roll)

    def score(self, next_frame1=None, next_frame2=None):
        total_score = sum(roll.pins for roll in self.rolls)

        if self.is_strike() and next_frame1:
            total_score += next_frame1.score()
            if next_frame1.is_strike() and next_frame2:
                total_score += next_frame2.rolls[0].pins

        elif self.is_spare() and next_frame1:
            total_score += next_frame1.rolls[0].pins

        return total_score


class Game:
    def _init_(self):
        self.frames = [Frame() for _ in range(10)]
        self.current_frame = 0

    def roll(self, pins):
        current_frame = self.frames[self.current_frame]

        if current_frame.is_open():
            current_frame.add_roll(Roll(pins))
        else:
            self.current_frame += 1
            if self.current_frame < 10:
                self.frames[self.current_frame].add_roll(Roll(pins))

    def score(self):
        total_score = 0
        for i in range(10):
            total_score += self.frames[i].score(self.frames[i + 1] if i + 1 < len(self.frames) else None,
                                                self.frames[i + 2] if i + 2 < len(self.frames) else None)
        return total_score



game = Game()
rolls = [10, 7, 3, 9, 1, 10, 10, 10, 2, 8, 5, 4, 7, 2, 10, 9, 1]

for pins in rolls:
    game.roll(pins)

print("Puntaje final:", game.score())