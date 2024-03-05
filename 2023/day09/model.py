def is_all_zero(lst: list[int]) -> bool:
    for num in lst:
        if num != 0:
            return False
    return True


class History:
    def __init__(self, lst):
        self.history_list = lst
        self.analyze_result = None
        self.analyze_complete = False

    def analyze(self):
        if self.analyze_complete:
            return

        current_history = self.history_list
        self.analyze_result = [current_history]

        while not is_all_zero(current_history):
            next_history = []
            for i in range(1, len(current_history)):
                next_history.append(current_history[i] - current_history[i - 1])

            self.analyze_result.append(next_history)
            current_history = next_history

        self.analyze_complete = True

    def predict(self) -> int:
        if not self.analyze_complete:
            raise Exception("should be analyzed before predict")
        ret = 0
        for row in self.analyze_result:
            ret += row[-1]

        return ret
