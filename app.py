def myrange():
    for i in range(1,100):
        try:
            x=20
            z= int("30")
            if z is None:
                raise Exception("Z cannot be None")
            j=440
        except:
            return 43
        finally:
            return 20


def calculate_average(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum / len(numbers)


