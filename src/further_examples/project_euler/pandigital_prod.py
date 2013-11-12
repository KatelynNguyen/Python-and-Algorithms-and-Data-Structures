#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


# very dumb version, need to be optimized 

'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

def is_pandigital(n):
    size = len(n)
    pan = set([x for x in range(1,size + 1)])
    for i in n:
        if int(i) in pan:
            pan = pan - {int(i)}
        else:
            return False
    return True
    
def find_multiples(n):
    multiples = set([1, n])
    for i in range(2, n):
        if n%i == 0:
            multiples.add(i)
            multiples.add(n//i)       
    return multiples
 

def find_pandigital():
    sum_pan = 0
  
    for i in range(10, 987654322):
        if i//10 == 0:
            continue
        digits = set(str(i))
        if len(digits) != len(str(i)):
            continue
        multiples = find_multiples(i)
        mult_set = set()
        for j in multiples:
            for c in str(j):
                if c in digits or int(c) == 0:
                    continue
            for c in str(j):
                mult_set.add(c)            
            k = i//j
            for c in str(k):
                if c in digits or int(c) == 0:
                    continue
            for c in str(k):
                mult_set.add(c)  
            if len(mult_set ) == 9:
                sum_pan += j + k + i               
    return sum_pan
        
    
   
def main():
    assert(is_pandigital('15234') == True )
    assert(is_pandigital('15233') == False ) 
    
    print(find_pandigital()) 
    
    print('Tests Passed!')
                   
if __name__ == '__main__':
    main()

