"""
you are tasked with decoding a message for the government.
 you notice that the text in the message can be translated into sequence of digits.
 The digit sequence you notice is peculiar, it is string of digits S with no spaces.
 but if you add spaces at the right places, it will be sequence numbers that are incremented by one for each consecutive number except that there is skipped number. the skipped number is key to decoding and a set of such skipped numbers gives you the decoded message. your task is to implement a function that returns skipped number, given the sequence of digits
"""

def find_missing_number(s):
    def is_valid_sequence(start, length):
        current = start
        i = 0
        missing = None
        while i < len(s):
            expected = str(current)
            if s[i:i+len(expected)] != expected:
                if missing is not None:
                    return None
                missing = current
                current += 1
                continue
            i += len(expected)
            current += 1
        return missing if i == len(s) else None

    for length in range(1, 7):  # Try lengths from 1 to 6 digits
        start = int(s[:length])
        missing = is_valid_sequence(start, length)
        if missing is not None:
            return missing

    return -1  # No valid sequence found

# Test the function
test_cases = ["313234",
    "89101113",
    "9899101102",
    "123567",
    "12345678910",
    "98999100101103104105"
]

for case in test_cases:
    result = find_missing_number(case)
    print(f"Input: {case}")
    print(f"Missing number: {result}")
    print()
