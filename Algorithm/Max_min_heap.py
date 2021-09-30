class Max_heap:

    def __init__(self):
        self.data = [None]

    def plus(self, value):
        self.data.append(value)
        x = len(self.data)
        while x // 2 > 0:
            if self.data[x] > self.data[x // 2]:
                self.data[x], self.data[x // 2] = self.data[x // 2], self.data[x]
            else:
                break
            x = x // 2

    def remove(self):
        x = len(self.data)
        if x > 1:
            value = self.data.pop()
            self.data[1] = value
            self.max_heapify(1)

    def max_heapify(self, i):
        left = i * 2
        right = i * 2 + 1
        biggest = i

        if left < len(self.data) and self.data[left] > self.data[biggest]:
            smallest = left
        if right < len(self.data) and self.data[right] > self.data[biggest]:
            smallest = right
        if biggest != i:
            self.data[i], self.data[biggest] = self.data[biggest], self.data[i]
            self.max_heapify(biggest)