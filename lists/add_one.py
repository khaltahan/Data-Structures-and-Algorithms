def add_one(arr):
    string = ''
    for i in arr:
        string += str(i)
    new_string = str(int(string) + 1)
    return [int(digit) for digit in new_string]

print(add_one([1, 2, 3]))