def duplicate_number(arr):
    correct_sum = 0
    invalid_sum = 0
    for i in range(len(arr) - 1):
        correct_sum += i
    
    for i in arr:
        invalid_sum += i
    
    return invalid_sum - correct_sum

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    output = duplicate_number(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr = [0, 1, 5, 4, 3, 2, 0]
solution = 0
test_case = [arr, solution]
test_function(test_case)

arr = [0, 0]
solution = 0
test_case = [arr, solution]
test_function(test_case)

arr = [0, 2, 3, 1, 4, 5, 3]
solution = 3
test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 5, 4, 3, 2, 0]
solution = 0
test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 5, 5, 3, 2, 4]
solution = 5
test_case = [arr, solution]
test_function(test_case)