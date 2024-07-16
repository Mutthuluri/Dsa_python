import random

# Define the initial prices and demand function
prices = [100, 150, 200, 250]  # Initial prices for products


def demand(price):
    return 1000 - 5 * price  # Example demand function


def calculate_revenue(prices):
    return sum(price * demand(price) for price in prices)


def get_neighbors(prices):
    neighbors = []
    for i in range(len(prices)):
        for change in [-10, 10]:  # Adjust prices by ±10
            new_prices = prices.copy()
            new_prices[i] += change
            neighbors.append(new_prices)
    return neighbors


# Hill climbing algorithm
current_solution = prices
current_revenue = calculate_revenue(current_solution)
while True:
    neighbors = get_neighbors(current_solution)
    neighbor_revenues = [calculate_revenue(neighbor) for neighbor in neighbors]
    best_neighbor_index = neighbor_revenues.index(max(neighbor_revenues))
    best_neighbor = neighbors[best_neighbor_index]
    best_neighbor_revenue = neighbor_revenues[best_neighbor_index]

    if best_neighbor_revenue > current_revenue:
        current_solution = best_neighbor
        current_revenue = best_neighbor_revenue
    else:
        break

print("Optimal prices:", current_solution)
print("Maximum revenue:", current_revenue)