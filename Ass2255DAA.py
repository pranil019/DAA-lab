class Item:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit
    
    def ratio(self):
        return self.profit / self.weight


def fractional_knapsack(items, capacity):
    """
    Solves the fractional knapsack problem using a greedy approach.
    
    Args:
        items: List of Item objects
        capacity: Maximum capacity of the knapsack
    
    Returns:
        Maximum profit achievable
    """
    # Sort items by profit-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio(), reverse=True)
    
    total_profit = 0.0
    remaining_capacity = capacity
    
    for item in items:
        if remaining_capacity >= item.weight:
            # Take the entire item
            remaining_capacity -= item.weight
            total_profit += item.profit
        else:
            # Take a fraction of the item
            total_profit += item.profit * (remaining_capacity / item.weight)
            break
    
    return total_profit


if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    
    items = []
    for i in range(n):
        weight, profit = map(int, input(f"Enter weight and profit of item {i + 1}: ").split())
        items.append(Item(weight, profit))
    
    capacity = int(input("Enter maximum capacity: "))
    
    max_profit = fractional_knapsack(items, capacity)
    
    print(f"Maximum Profit = {max_profit}")

