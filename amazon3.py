from typing import List
import bisect


def getMinConnectionCost(warehouseCapacity: List[int], additionalHubs: List[List[int]]) -> List[int]:
    n = len(warehouseCapacity)
    results = []

    # Central hub is always at position n-1 (0-indexed)
    main_hub_capacity = warehouseCapacity[-1]

    # Process each query
    for hubA, hubB in additionalHubs:
        # Convert to 0-indexed positions
        hubA -= 1
        hubB -= 1

        total_cost = 0

        # Precompute the cost of connecting to the main hub
        for i in range(n):
            # Calculate the minimum cost of connecting the warehouse to one of the hubs
            cost_to_hubA = warehouseCapacity[hubA] - warehouseCapacity[i] if i <= hubA else float('inf')
            cost_to_hubB = warehouseCapacity[hubB] - warehouseCapacity[i] if i <= hubB else float('inf')
            cost_to_main_hub = main_hub_capacity - warehouseCapacity[i]

            total_cost += min(cost_to_hubA, cost_to_hubB, cost_to_main_hub)

        # Store the result for the current query
        results.append(total_cost)

    return results


# Example Input
warehouseCapacity = [2, 6, 8, 14]
additionalHubs = [[1, 2]]  # Query: Two additional hubs at positions 1 and 2

# Output
print(getMinConnectionCost(warehouseCapacity, additionalHubs))  # Expected Output: [6]
