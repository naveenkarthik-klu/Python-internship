# 1 EXERCISE
l_1 = [4001, 4002, 4003, 4004, 4005]
l_2 = ["Naveen", "Siva", "Sailesh", "Dhananj", "Hari"]
l_3 = l_3 = list(zip(l_1, l_2))

print(l_3)
print()

# 2 EXERCISE

list_1 = ["Naveen", "Madhesh", "Roshan", "Livingstan",
          "Gowtham", "Antony", "John", "Since2000"]
range = list(range(1, 8))
lst = list(zip(list_1, range))
print(lst)
print()

# 3 EXERCISE

list = [98, 1, 53, 21, 4, 65, 2]
list.sort()
print("The sorted list is", list)
print()

# 4 EXERCISE

numbers = [1, 2, 4, 5, 7, 8, 10, 11]


def filterOddNum(num):

    if(num % 2) == 0:
        return False
    else:
        return True


oddfilter = filter(filterOddNum, numbers)
print("The odd numbers in the list are: ", list(oddfilter))
