def binary_search_left(array, target):
    """Find the first index where array[index] >= target."""
    low, high = 0, len(array)
    while low < high:
        mid = (low + high) // 2
        if array[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low


def binary_search_right(array, target):
    """Find the first index where array[index] > target."""
    low, high = 0, len(array)
    while low < high:
        mid = (low + high) // 2
        if array[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return low


def setupDataCenter(health, size, queries):
    # Step 1: Pair and sort servers by size
    servers = sorted(zip(size, health))  # [(size, health)]
    sorted_sizes = [s[0] for s in servers]  # Extract sorted sizes
    sorted_healths = [s[1] for s in servers]  # Extract healths corresponding to sorted sizes

    # Step 2: Precompute prefix sums of healths
    prefix_sum = [0] * (len(sorted_healths) + 1)
    for i in range(len(sorted_healths)):
        prefix_sum[i + 1] = prefix_sum[i] + sorted_healths[i]

    results = []
    for l, r in queries:
        # Step 3: Find the range of indices for the size range [l, r]
        start = binary_search_left(sorted_sizes, l)  # First index where size >= l
        end = binary_search_right(sorted_sizes, r)  # First index where size > r

        # Step 4: Calculate the sum of healths using the prefix sum array
        health_sum = prefix_sum[end] - prefix_sum[start]
        results.append(health_sum)

    return results


# Example Input
n = 5
health = [3, 4, 1, 2, 5]
size = [1, 2, 4, 3, 5]
queries = [(2, 4), (1, 5), (6, 10)]  # Example queries: [l, r]

# Output
print(setupDataCenter(health, size, queries))
