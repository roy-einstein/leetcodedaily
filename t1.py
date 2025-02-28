from http.cookiejar import cut_port_re


def find_skipped_number(s):
    n = len(s)
    for length in range(1, len(s) // 2 + 1):  # Length of the first number
        skipped = -1
        i = 0
        current_number = int(s[:length])  # First number
        valid = True

        while i < n:
            # Determine the next number to expect
            expected = str(current_number)
            expected_length = len(expected)
            if s[i:i+expected_length] != expected:
                if skipped != -1:
                    valid = False
                    break
                else:
                    skipped = current_number
                    current_number +=1
                    continue
            i += len(str(current_number))
            current_number +=1

        if valid:
            return skipped if skipped != -1 else -1  # Return skipped number or -1
    return -1


def find_skipped_number(s):
    n = len(s)
    for length in range(1, len(s) // 2 + 1):  # Length of the first number
        skipped = -1
        i = length
        current_number = int(s[:length])  # First number
        valid = True

        while i < n:
            # Determine the next number to expect
            expected = str(current_number + 1) if skipped == -1 else str(current_number + 2)
            expected_length = len(expected)

            # If we can't match the next number, break
            if i + expected_length > n or s[i:i + expected_length] != expected:
                if skipped == -1:  # Allow one skip
                    skipped = current_number + 1
                    current_number += 1
                else:
                    valid = False
                    break
            else:
                current_number += 1
            i += expected_length

        if valid:
            return skipped if skipped != -1 else -1  # Return skipped number or -1
    return -1


# # Input
# s = input("Enter the string: ")
#
# # Output
# print(find_skipped_number(s))

# # Test the function
test_cases = ["313234",
    "89101113",
    "9899101102",
    "123567",
    "12345678910",
    "98999100101103104105"
]

for case in test_cases:
    result = find_skipped_number(case)
    print(f"Input: {case}")
    print(f"Missing number: {result}")
    print()
