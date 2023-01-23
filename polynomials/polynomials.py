from numbers import Number
from numbers import Integral


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other):
        
        if isinstance(other, Number):
            return Polynomial((self.coefficients[0]-other,) + self.coefficients[1:])
        
        elif isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1  
            coefs = tuple( a-b for a,b in zip(self.coefficients[:common], other.coefficients[:common]))
            if self.degree() >= other.degree():
                coefs += self.coefficients[common:]
                return Polynomial(coefs)
            elif self.degree() < other.degree():
                coefs += tuple([-1* a for a in other.coefficients[common:]])
                return Polynomial(coefs)
            
        else:
            return NotImplemented
    
    def __rsub__(self, other):
        poly = self-other
        inv_poly = tuple([-1 * a for a in poly.coefficients])
        return Polynomial(inv_poly)

 
    def __mul__(self, other):
        
        if isinstance(other, Number):
            coef = tuple(other*i for i in self.coefficients)
            return Polynomial(coef)
        elif isinstance(other, Polynomial):
            mul_coe = [0]*(self.degree()+other.degree()+1)
            for s_pow,s_coe in enumerate(list(self.coefficients)):
                for o_pow,p_coe in enumerate(list(other.coefficients)):
                    mul_coe[s_pow+o_pow] += s_coe*p_coe
            return Polynomial(tuple(mul_coe))  
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self*other   


    def __pow__(self,other):
        
        if isinstance(other, Integral) and other >0 :
            new = self*self
            for i in range(other-2):
                new = self*new
            return new

    
    def __call__(self ,other):
        n=0
        if isinstance(other, Number):
            for power,val in enumerate(list(self.coefficients)):
                n += val*(other**power)
            return n

    def dx(self):
        
        if self.degree() == 0 :
            return Polynomial((0,))
        elif self.degree() :
            coef = [0]* self.degree()    
            coef[0] = self.coefficients[1]

            for power,val in enumerate(list(self.coefficients[2:]),start=2):
                coef[power-1] += val*power
            return Polynomial(tuple(coef))


def derivative(poly):
    return poly.dx()






