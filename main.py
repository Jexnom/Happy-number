
while True :
    n = int(input("Enter your number: "))
    perv_n = 0
    digit = 2
    while True :
        if n-perv_n !=0:
            n = n - perv_n
            if n == 1:
                print("That is a happy number.")
                break
            elif digit == 1:
                print("This is not a happy number")
                break
        perv_n = n
        string_n = str(n)
        digit = len(string_n)
        mylist = list(string_n)
        int_mylist = list(map(int, mylist))
        for i in range (digit):
            n =  n + int_mylist[i] ** 2

