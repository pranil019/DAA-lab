from queue import Queue

class Node:
    def __init__(self, level, profit, weight):
        self.level = level
        self.profit = profit
        self.weight = weight

def bound(node, n, W, profit, weight):
    if node.weight >= W:
        return 0

    result = node.profit
    j = node.level + 1
    totweight = node.weight

    while j < n and totweight + weight[j] <= W:
        totweight += weight[j]
        result += profit[j]
        j += 1

    if j < n:
        result += (W - totweight) * profit[j] / weight[j]

    return result


# -------- FIFO --------
def knapsack_fifo(W, profit, weight, n):
    Q = Queue()
    Q.put(Node(-1, 0, 0))
    maxProfit = 0

    while not Q.empty():
        u = Q.get()

        if u.level == n - 1:
            continue

        v = Node(u.level + 1, u.profit, u.weight)

        # include item
        v.weight += weight[v.level]
        v.profit += profit[v.level]

        if v.weight <= W and v.profit > maxProfit:
            maxProfit = v.profit

        if bound(v, n, W, profit, weight) > maxProfit:
            Q.put(v)

        # exclude item
        v2 = Node(u.level + 1, u.profit, u.weight)

        if bound(v2, n, W, profit, weight) > maxProfit:
            Q.put(v2)

    return maxProfit


# -------- LIFO --------
def knapsack_lifo(W, profit, weight, n):
    stack = []
    stack.append(Node(-1, 0, 0))
    maxProfit = 0

    while stack:
        u = stack.pop()

        if u.level == n - 1:
            continue

        v = Node(u.level + 1, u.profit, u.weight)

        # include item
        v.weight += weight[v.level]
        v.profit += profit[v.level]

        if v.weight <= W and v.profit > maxProfit:
            maxProfit = v.profit

        if bound(v, n, W, profit, weight) > maxProfit:
            stack.append(v)

        # exclude item
        v2 = Node(u.level + 1, u.profit, u.weight)

        if bound(v2, n, W, profit, weight) > maxProfit:
            stack.append(v2)

    return maxProfit


# -------- USER INPUT --------
n = int(input("Enter number of items: "))

profit = []
weight = []

print("Enter profits:")
for i in range(n):
    profit.append(int(input()))

print("Enter weights:")
for i in range(n):
    weight.append(int(input()))

W = int(input("Enter maximum capacity: "))


# -------- OUTPUT --------
print("\nMaximum Profit using FIFO:", knapsack_fifo(W, profit, weight, n))
print("Maximum Profit using LIFO:", knapsack_lifo(W, profit, weight, n))