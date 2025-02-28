# const
# int
# n = (int)
# charge.size();
# int
# mx = charge[0];
# long
# long
# sumeven = 0, sumodd = 0;
# for (int i = 0; i < n;i++){
#     mx = max(mx, charge[i]);
# if (i % 2 == 0)
# sumeven += max(charge[i], 0);
# else
# sumodd += max(charge[i], 0);
#
# }
# return sumeven == 0 & & sumodd == 0? mx: max(sumeven, sumodd);


def getMaximumCharge(charge):
    n = len(charge)
    mx= charge[0]
    sumEven, sumOdd=0,0
    for i in range(n):
        mx= max(mx,charge[i])
        if i%2 ==0:
            sumEven +=max(charge[i],0)
        else:
            sumOdd += max(charge[i],0)
    return mx if sumEven == 0 and sumOdd ==0 else max(sumEven, sumOdd)


def max_final_charge(charge):
    n = len(charge)
    dp = [[0] * n for _ in range(n)]

    # Initialize dp with single element subarrays
    for i in range(n):
        dp[i][i] = charge[i]

    # Fill dp table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            # Calculate charge when removing first element
            left_removal = (charge[i] if i == 0 else 0) + dp[i + 1][j]

            # Calculate charge when removing last element
            right_removal = dp[i][j - 1] + (charge[j] if j == n - 1 else 0)

            # Calculate max charge for all possible removals in between
            max_middle_removal = max(
                dp[i][k - 1] + dp[k + 1][j] + charge[k]
                for k in range(i + 1, j)
            ) if j > i + 1 else float('-inf')

            # Update dp with max of all possible removals
            dp[i][j] = max(left_removal, right_removal, max_middle_removal)

    return dp[0][n - 1]


def getMaximumCharge(charge):
    while len(charge) > 1:
        max_gain = float('-inf')
        remove_index = -1

        # Iterate through the array to find the best system to remove
        for i in range(1, len(charge) - 1):
            gain = charge[i - 1] + charge[i + 1] - charge[i]
            if gain > max_gain:
                max_gain = gain
                remove_index = i

        # Remove the best system
        if remove_index != -1:
            charge[remove_index - 1] += charge[remove_index + 1]
            charge.pop(remove_index + 1)
            charge.pop(remove_index)
        else:
            break

    return max(charge)

# Example usage
charge = [-2, 4, 3, -2, 1]
result = max_final_charge(charge)
print(result)

charge = [-2,4,3,-2,1]
print(getMaximumCharge(charge))