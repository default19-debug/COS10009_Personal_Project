import json
import os


class ScoreSystem:
    def __init__(self, filename="scores.json"):
        self.filename = filename
        self.scores = self.load_scores()

    def merge_sort(self, arr):
        """Recursively divides the array in half, sorts, and merges them back."""
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]
            # Recursively call merge_sort on both halves
            self.merge_sort(left_half)
            self.merge_sort(right_half)
            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

        return arr



    def load_scores(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except:
                return []

        return []

    def add_score(self, new_time_in_seconds):

        self.scores.append(new_time_in_seconds)

        self.scores = self.merge_sort(self.scores)

        self.scores = self.scores[:5]

        self.save_scores()

    def save_scores(self):

        with open(self.filename, 'w') as file:
            json.dump(self.scores, file)

    def get_top_scores(self):
        return self.scores


