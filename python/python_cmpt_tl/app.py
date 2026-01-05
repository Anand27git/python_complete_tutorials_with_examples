i = 1
while i <= 5:
    print('*'*i)
    i=i+1
    txt = "anand kumar"[::-1]
    print(txt)

    a = [8, 3, 5, 1, 9, 0,12]

    # Find the smallest number
    smallest = min(a) #smallest
    largest = max(a) #largest number
    print(smallest)
    print(largest)

    def my_function(x):
        return x[::-1]


    mytxt = my_function("I wonder how this text looks like backwards")
    print(mytxt)

