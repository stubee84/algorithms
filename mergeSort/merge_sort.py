from typing import List

class merge_sort:
    def __init__(self, num: int, strings: List[str]):
        self.num = num
        self.strings = strings

        for i in range(self.num):
            print(self.sort(strings=self.strings[i].split(" ")))
    
    def sort(self, strings: List[str]) -> list:
        if len(strings) > 1:
            mid = len(strings)//2

            left = strings[:mid]
            right = strings[mid:]

            self.sort(strings=left)
            self.sort(strings=right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if len(left[i]) < len(right[j]):
                    strings[k] = left[i]
                    i += 1
                elif len(left[i]) > len(right[j]):
                    strings[k] = right[j]
                    j += 1
                else:
                    strings[k] = left[i]
                    i += 1
                k += 1
            
            while i < len(left) or j < len(right):
                if i < len(left):
                    strings[k] = left[i]
                    i += 1
                elif j < len(right):
                    strings[k] = right[j]
                    j += 1
                k += 1
        return strings

if __name__ == "__main__":
    merge_sort(num=3, strings=[
        "ab cd e j asd ljffg df",
        "a a b b c c",
        "xy yx zxy zx xzy xxx",
    ])