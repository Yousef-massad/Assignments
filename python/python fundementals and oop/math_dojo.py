class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self

md = MathDojo()

x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)

md2 = MathDojo()

test1 = md2.add(5).add(10, 20).add(1, 2, 3, 4).result
print(test1)

md3 = MathDojo()

test2 = md3.add(100).subtract(20).subtract(10, 5).subtract(1, 2, 3).result
print(test2)