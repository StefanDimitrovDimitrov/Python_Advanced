def get_primes(arg):


    for num in arg:
        the_number_is_prime = True
        if num >= 2:
            for num_2 in range(2, num):
                if num % num_2 == 0:
                    the_number_is_prime = False
                    break
            if the_number_is_prime:
                yield num




print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))