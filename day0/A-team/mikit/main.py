import random

class NumberGuess:
    def __init__(self, ans: int) -> None:
        assert type(ans) is int and 0 < ans
        self.ans = ans
    
    def judgement(self, num: int) -> str:
        if not (type(num) is int and 0 < num):
            return 'invalid'
        if self.ans == num:
            return 'correct'
        else:
            return 'smaller' if num < self.ans else 'greater'

if __name__ == '__main__':
    game = NumberGuess(random.randint(1, 100))
    while True:
        res = game.judgement(int(input()))
        print(res)
        if res == 'correct':
            break
