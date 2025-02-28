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

    results = []
    for l, r in queries:
        # Step 2: Find the range of indices for the size range [l, r]
        start = binary_search_left(sorted_sizes, l)  # First index where size >= l
        end = binary_search_right(sorted_sizes, r)  # First index where size > r

        # Step 3: Calculate the sum of healths in the range [start, end)
        health_sum = sum(sorted_healths[start:end])
        results.append(health_sum)

    return results


# Example Input
n = 3
health = [3, 4, 1, 2, 5]
size = [1, 2, 4, 3, 5]
queries = [(2, 4), (1, 5)]  # Example queries: [l, r]

n=3
size = [1,1,1]
health = [4,5,6]
query =[[1,3],[2,4]]

n= 3
size = [1,2,3]
health= [2,3,4]
query = [[1,3],[2,3]]



# Output
print(setupDataCenter(health, size, queries))
