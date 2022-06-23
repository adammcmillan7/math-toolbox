from random import randint
from datetime import datetime
from matplotlib import pyplot

""" Polynomials in standard form can be rewritten in nested form
        eg 1 + 2x + 3x^2 = 1 + x(2 + x(3))
    
    Rewriting in this form simplifies evaluating at any point x. 
    In this nested form, evaluating only requires n multiplications (n = highest power of x)
    
    In our algorithms, we take in a point x to evaluate a certain polynomial at.
    We also input a list of coefficients of the polynomial in order of lowest power to highest
        eg [1,2,3]  = 1 + 2x + 3x^2 
        
    This code compares the efficiency of the traditional polynomial algorithm and the nested algorithm.
    For polynomials of small degree, evaluation time is near instant for any efficient algorithm.
    However we can evaluate large degree polynomials exponentially faster using nested form instead of standard form."""

def trad(x,c):
    """ x is our x value.
        c is a list of coefficients
        returns tuple of (value, total time)"""
    start = datetime.now()
    pwr = 0;
    val = 0
    for i in range(len(c)):
        val += (x ** pwr) *(c[i])
        pwr += 1
    end = datetime.now()
    return (val, end-start)

def nest(x,c):
    """ x is our x value.
        c is a list of coefficients
        returns tuple of (value, total time)"""
    start = datetime.now()
    val = 0
    for i in range(len(c)-1,-1,-1):
        val *= x
        val += c[i]
    end = datetime.now()
    return (val, end-start)

def randompoly():
    """generates a random polynomial of degree <= 9999
        with coefficients between (-1000,1000) """
    deg = randint(0,10000)
    coeff = list()
    for i in range(0,deg):
        coeff.append(randint(-1000,1000))
    return coeff
    
def evaluate():
    """evaluates traditional and nested forms at a random x value at a randomly generated polynomials
        returns tuple of ( (len(poly),tradtime), (len(poly), nestedtime) )"""
    x = randint(-10000, 10000)
    poly = randompoly()
    tradtime = trad(x,poly)[1]
    nesttime = nest(x,poly)[1]
    return ( (len(poly), tradtime.total_seconds()) , (len(poly), nesttime.total_seconds()))


"""To compare the time efficiency of each algorithm, evaluate 1,000 different randomly generated polynomials
    of degree <= 9999 with integer coefficients between (-1000,1000). Evaluation point x is a random integer
    between (-10000, 10000).
    
    We plot points of evaluation time of each polynomial in a scatter plot to see the exponential time needed
    to evaluate a polynomial in traditional form vs the near constant time needed to evaluate that same polynomial
    as expressed in nested format. We include a scatterplot of only nested evaluation time to show evaluation time
    is not quite perfectly constant for nested format. """

tradplot = list()
nestplot = list()

for i in range(0,1000):
    eval = evaluate()
    tradplot.append(eval[0])
    nestplot.append(eval[1])
    
#combined scatterplot of both traditional and nested evaluations
pyplot.scatter(*zip(*tradplot), c='r', label="Traditional")
pyplot.scatter(*zip(*nestplot), c='g', label="Nested")
pyplot.legend(loc='upper left')
pyplot.xlabel("Length of Polynomial")
pyplot.ylabel("Evaluation Time in Seconds")
pyplot.title("Time Efficiency of Evaluating Polynomials in Traditional Form versus Nested Form")
pyplot.show()

#scatterplot of only nested evaluations
pyplot.scatter(*zip(*nestplot))
pyplot.xlabel("Length of Polynomial")
pyplot.ylabel("Evaluation Time in Seconds")
pyplot.title("Time Efficiency of Evaluating Polynomials in Nested Form")
pyplot.show()
