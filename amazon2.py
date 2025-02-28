def binary_search_left(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

def getMinConnectionCost(warehouseCapacity, queries):
    n = len(warehouseCapacity)
    # Precompute prefix sums for the warehouse capacities
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + warehouseCapacity[i]

    results = []

    for hubA, hubB in queries:
        # Convert 1-based index to 0-based index
        hubA -= 1
        hubB -= 1

        min_total_cost = 0

        for i in range(n):
            if i <= hubA:
                cost_to_hubA = warehouseCapacity[hubA] - warehouseCapacity[i]
            else:
                cost_to_hubA = float('inf')

            if i <= hubB:
                cost_to_hubB = warehouseCapacity[hubB] - warehouseCapacity[i]
            else:
                cost_to_hubB = float('inf')

            cost_to_central = warehouseCapacity[-1] - warehouseCapacity[i]

            min_cost = min(cost_to_hubA, cost_to_hubB, cost_to_central)
            min_total_cost += min_cost

        results.append(min_total_cost)

    return results

# Example usage
warehouseCapacity = [5, 10, 15, 20, 25]
queries = [(2, 4), (1, 3)]
print(getMinConnectionCost(warehouseCapacity, queries))
