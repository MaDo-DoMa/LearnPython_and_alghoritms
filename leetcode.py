from multiprocessing.managers import Array

#you get two sequences A and B
#you have to create a new sequence C
#in sequence C must be all numbers from A
#excpect those which are in B p times, where p is a primary number

def ifFirstNumber(number):
    if number == 1:
        return False
    for i in range(2,number):
        if number % i == 0:
            return False

    return True

def sequence_c(A,B):
    freq = {}
    for b in B:
        if b in freq:
            freq[b] += 1
        else:
            freq[b] = 1

    Array = []

    for a in A:
        if a not in freq or not ifFirstNumber(freq[a]):
            Array.append(a)


    return Array

A = [2,3,9,2,5,1,3,7,10]
B = [2,1,3,4,3,10,6,6,1,7,10,10,10]
C = sequence_c(A,B)
print(C)