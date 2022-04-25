"""     Adrian SZKLARSKI, 12.2021r,
          Sum and Average value:

Numbers program: the user specifies the length of an array,
then fills it with numbers, and the program returns their
sum and average value

    Returns:      array, sum & average of element's array
    Parameters:   number of elements in the array
                  the values of the elements in the array
    Error:        ValueError or NameError
"""


def numbers(n):

    var = 0
    numbers_list = []
    while var < n:
        print(var, end=": ")
        while True:
            try:
                my_no = (int(input('Specify the value of an array element: ')))
                break
            except Exception:
                print("You should have given either an int")
        numbers_list.append(my_no)
        var += 1

    if sum(numbers_list) > (sum(numbers_list) / n):
        print(f'The sum is greater than the average!')
    else:
        print(f'The sum is not greater than the average')
    return numbers_list


if __name__ == '__main__':
    while True:
        try:
            n = int(input("How many numbers you want to enter?: "))
            print(' ')
            break
        except ValueError or NameError:
            print("You should have given either an int")
            print(' ')

result = (numbers(n))
print(' ')
print('List of elements: ', result)
print('Sum of elements in the list:', sum(result))
print('Average value of electives on the list:', sum(result) / n)

