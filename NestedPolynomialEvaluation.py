from random import randint

""" Polynomials in this standard form can be rewritten in nested form
        eg 1 + 2x + 3x^2 = 1 + x(2 + x(3))
    
    Rewriting in this form simplifies evaluating at any point x. 
    In this nested form, evaluating only requires n multiplications (n = highest power of x)
    
    In our algorithms, we take in a point x to evaluate a certain polynomial at.
    We also input a list of coefficients of the polynomial in order of lowest power to highest
        eg [1,2,3]  = 1 + 2x + 3x^2 """

def trad(x,c):
    """ x is our x value.
        c is a list of coefficients"""
    #todo param validation
    
    pwr = 0;
    val = 0
    for i in range(len(c)):
        val += (x ** pwr) *(c[i])
        pwr += 1
    return val

def nest(x,c):
    """ x is our x value.
        c is a list of coefficients"""
    #todo param validation
    val = 0
    for i in range(len(c)-1,-1,-1):
        val *= x
        val += c[i]
    return val

def randompoly():
    """generates a random polynomial of degree <= 99
        with coefficients between [-1000,1000] """
    deg = randint(0,100)
    coeff = list()
    for i in range(0,deg):
        coeff.append(randint(-1000,1000))
    return coeff

#test fn
def algo_test(n=100000):
    """tests that both algorithms return the same result for any polynomial.
        tests n different polynomials, defaults to 100,000"""
    for i in range(0,n):
        poly= randompoly()
        x = randint(-1000,1000)
        if (trad(x,poly) != nest(x,poly)):
            print("failed")
            return(x,poly)
    print("success")