"""Steps:
            1 - Print the vector, values and position -> if is empty, return -1
            2 - Add values in the vector until your max capacity, return message when is already full
            3 - Search element inside the vector, return the position of him, return -1 if not exists
            4 - Remove element inside the vector, relocate positions for the remains elements from the
            empty position until the last, in case exist duplicates, search for all elements and remove them.
            Update the last position everytime that removes some element."""

import numpy as np


class NotOrderedVector:

    def __init__(self, capacity):
        self._capacity = capacity
        self._lastPosition = -1
        self._values = np.empty(self._capacity, dtype=int)

    def printer(self):
        if self._lastPosition == -1:
            print('Vector is empty!')
        else:
            for i in range(self._lastPosition + 1):
                print(f'Position: {i} - Element: {self._values[i]}')

    def insert(self, element):
        if self._lastPosition == len(self._values) - 1:
            print('Vector is full, max capacity reached!')
        else:
            self._lastPosition += 1
            self._values[self._lastPosition] = element

    def search(self, element):
        for i in range(self._lastPosition + 1):
            if self._values[i] == element:
                return i
        return -1

    def remove(self, element):
        position = self.search(element)
        if position == -1:
            return -1
        else:
            for i in range(position, self._lastPosition):
                self._values[i] = self._values[i + 1]
            self._lastPosition -= 1


if __name__ == '__main__':
    Vector = NotOrderedVector(5)
    Vector.printer()
    print("---")
    Vector.insert(10)
    Vector.insert(20)
    Vector.insert(30)
    Vector.insert(40)
    Vector.insert(50)
    Vector.printer()
    print("---")
    Vector.remove(10)
    Vector.printer()
    print("---")
    Vector.remove(40)
    Vector.printer()
