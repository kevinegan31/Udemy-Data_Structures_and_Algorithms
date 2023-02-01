def fizzBuzz(n):
    # Write your code here
    for n_int in range(1, n+1):
        if n_int % 3 == 0 and n_int % 5 == 0:
            print('FizzBuzz')
        elif n_int % 3 == 0:
            print('Fizz')
        elif n_int % 5 == 0:
            print('Buzz')
        else:
            print(str(n_int))
# print "\n".join(fizzBuzz(n) for n in range(1,n))
fizzBuzz(15)