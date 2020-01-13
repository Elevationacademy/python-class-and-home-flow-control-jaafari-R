def fizz_buzz(n):
    if n < 1:
        raise ValueError("n should be bigger than zero")
    if type(n) != int:
        raise TypeError("n should be an integer")
    for i in range(1, n + 1):
        check_fizz = False # checks if n is a multiple of 3
        check_buzz = False # checks if n is a multiple of 5

        if i % 3 == 0:
            print("fizz", end="")
            check_fizz = True
        if i % 5 == 0:
            print("buzz", end="")
            check_buzz = True
        if not (check_fizz or check_buzz):
            print(i, end="")
        print()


if __name__ == "__main__":
   fizz_buzz(15)