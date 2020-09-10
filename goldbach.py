#the goal of this program is to piggy back off of goldbach's conjecture which is:
#is every even number the sum of 2 prime numbers?
#this program will ask for input an even number, and return the two prime numbers that sum up to it
#ex: 6 returns 3 + 3

user_input = int(input("Please enter an even number: "))

#we could just compute a list of the primes for the number, then iterate through the list of primes and subtract the current iteration
#from the input, and see if the leftover result is in the list of primes < user_input
#so ex: user_input = 112, we want to compute a list of all prime numbers between 1 and 112:
#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109]
#actually notice that there is not always a unique pair of primes, either I can return just one pair, or return all pairs
#how would i return all pairs?

#first let's worry about how we will return a list of all primes < user_input
#we will use the sieve of eratosthenes
#say we have a list of numbers [2, user_input] -> [2, 16] -> [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#first we consider the first element to be unmarked, which is 2, and we move down the list of numbers and mark off/remove all the elements that are 
#a multiple of 2 and we will get -> [2, 3, 5, 7, 9, 11]
#now we move the cursor to the element after 2, which is 3 and repeat the same process and we will get -> [2, 3, 5, 7, 11]
#if we continued the process for the remaining elements of the list, we'd get -> [2, 3, 5, 7, 11]
def sieve(n):
    # the blueprint for this algorithm is to fill an array of booleans that is the size of n + 1
    # each index is a correspondence with the naturals 1 -> n
    # false is not prime
    # true is prime
    # by default all values will be true
    # as we mark the naturals/sieve through the naturals, we mark the values as false
    bool_list = [True]*(n+1)
    result = []
    # we can remove all the even numbers (except 2) since they are composite
    for i in range(4, n+1, 2):
        bool_list[i] = False
    for comparee in range(3, n+1):
        for compared in range(comparee**2, n+1):
            if compared%comparee == 0:
                bool_list[compared] = False
    for i in range(2, n+1):
        if bool_list[i]: 
            result.append(i)
    return result


primes = sieve(user_input)
# print(primes)

answers = []

for prime in primes:
    difference = user_input - prime
    pair = []
    if difference in primes and prime <= user_input/2:
        pair.append(prime)
        pair.append(difference)
        answers.append(pair)

print(answers)
