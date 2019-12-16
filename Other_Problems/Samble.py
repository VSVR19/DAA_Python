def sample_method(num1=1, num2=2):
    # print("Num 1 is: {0}.".format(num1))
    # print("Num 2 is: {0}.".format(num2))

    number_one = 19
    number_two = 33

    # s[left], s[right] = s[right], s[left]

    number_one, number_two = number_two, number_one

    print("Number One is: {0}.".format(number_one))
    print("Number Two is: {0}.".format(number_two))


sample_method(19, 20)