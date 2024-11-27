class FenwickTree:
    def __init__(self, n):
        self.tree = [0] * n
        self.n = n
    def add(self, index, value):
        while index < self.n:
            self.tree[index] += value
            index |= index + 1
    def prefix_sum(self, index):
        result = 0
        while index >= 0:
            result += self.tree[index]
            index = (index & (index + 1)) - 1
        return result
    def range_sum(self, left, right):
        return self.prefix_sum(right - 1) - self.prefix_sum(left - 1)

n = int(input())
Array = list(map(int, input().split()))
k = int(input())
fenwick = FenwickTree(n)
for i in range(n):
    fenwick.add(i, Array[i])
for _ in range(k):
    query = input().split()
    if query[0] == "Add":
        i = int(query[1])
        x = int(query[2])
        fenwick.add(i, x)
    elif query[0] == "FindSum":
        l = int(query[1])
        r = int(query[2])
        print(fenwick.range_sum(l, r))
