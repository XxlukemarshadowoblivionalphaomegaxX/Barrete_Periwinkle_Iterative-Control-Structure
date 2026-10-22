def getSum(limit):
    total = 0
    for i in range(1, limit+1):
        total += i
    return total

def output_verification(limit):
    sum = limit * (limit + 1) // 2
    return sum


while True:
    try:
        limit = int(input("Hi there! Please enter your age: "))

        if limit > 0:
            break
        else:
            print ("Invalid input. Please enter a positive whole number greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a positive whole number greater than 0.")


if output_verification(limit) == getSum(limit):
    print ("Expected sum is", getSum(limit))
    print ("After calling the function getSum, the sum of all numbers from 1 to", limit, "is:", output_verification(limit))
    print ("Output verified.")