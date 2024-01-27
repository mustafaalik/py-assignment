
def count_unique_values(lst):
    unique_values = set(lst)
    count_dict = {value: lst.count(value) for value in unique_values}
    return count_dict


input_list = [1, 2, 3, 1, 2, 4, 5, 6, 4, 7, 8, 9, 9]
result_dict = count_unique_values(input_list)
print("Count of unique values:", result_dict)


def sum_of_numbers(n):
    numbers = [int(input("Enter number: ")) for _ in range(n)]
    total_sum = sum(numbers)
    return total_sum


n = int(input("Enter the value of n: "))
result = sum_of_numbers(n)
print("Sum of {} numbers is: {}".format(n, result))


def fibonacci_series(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series


n = int(input("Enter the number of terms in Fibonacci series: "))
result_series = fibonacci_series(n)
print("Fibonacci series:", result_series)


file_path = 'example.txt'  
with open(file_path, 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

print("Lines from the file:", lines)


source_file_path = 'source.txt'  
destination_file_path = 'destination.txt'  

with open(source_file_path, 'r') as source_file:
    content = source_file.read()

with open(destination_file_path, 'w') as destination_file:
    destination_file.write(content)

print("Contents copied from {} to {}".format(source_file_path, destination_file_path))


def create_alphabet_file(filename, letters_per_line):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    with open(filename, 'w') as file:
        for i in range(0, len(alphabet), letters_per_line):
            line = alphabet[i:i + letters_per_line]
            file.write(line + '\n')


file_name = 'alphabet.txt'  
letters_per_line = 5
create_alphabet_file(file_name, letters_per_line)
print("File '{}' created with alphabet listed.".format(file_name))
