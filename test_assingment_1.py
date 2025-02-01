# 1. Approximation Algorithm 
def approx_method(x0, tol):
    iter = 0
    diff = x0
    x = x0

    print(f"{iter}: {x}")

    while diff >= tol:
        iter += 1
        y = x

        x = (x / 2) + (1 / x)

        print(f"{iter}: {x}")

        diff = abs(x - y)

    print(f"\nConverged after {iter} iterations\n")

# example usage of code 1
approx_method(1.5, 0.000001)

# 2. The bisection Method 
def f(x):
    return x**3 + 4*x**2 - 10

def bisection_method(a, b, tol, max_iter, f):
    left = a
    right = b
    i = 0

    while abs(right - left) > tol and i < max_iter:
        i += 1
        p = (left + right) / 2

        if (f(left) < 0 and f(p) > 0) or (f(left) > 0 and f(p) < 0):
            right = p
        else:
            left = p

    return p

#example of running code 2
p = bisection_method(1,2, .001, 100, f)
print(p)
print("")


# 3. The fixed-point iteration 
def iteration_method(g, p0, tol, max_iter):
    i = 1
    while i <= max_iter:
        p = g(p0)
        
        if abs(p - p0) < tol:
            print(f"Root found at: {p}")
            print("SUCCESS\n")
            return p
        
        i += 1
        p0 = p
    
    print("FAILURE")
    return None

# example usage of code 3
def g(x):
    return (x+2/x)/2
result = iteration_method(g, 1.5, .0001, 100)

# 4. The Newton-Raphson method 
def newton_method(pprev, tol, max_iter, fprime, f):
    i = 1
    while i < max_iter:
        if abs(fprime(pprev)) != 0:  
            pnext = pprev - f(pprev) / fprime(pprev)
            
            if (abs(pnext - pprev) < tol):  
                print(f"iteration found at: {i}")
                print("SUCCESS\n")
                return pnext
                
            
            i += 1
            pprev = pnext  
        
        else:
            print("FAILURE: Derivative is zero")
            return None

    print("FAILURE: Max iterations reached")
    return None
 
# example usage of code 4
def f(x):
    return x**3 - x**2 + 4
def fprime(x):
    return 3*x**2 - 2*x 
newton_method(1, .001, 20, fprime, f)