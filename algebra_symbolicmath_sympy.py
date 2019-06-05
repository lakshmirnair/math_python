#factoring and expanding expression 5
from sympy import Symbol,factor,pprint,simplify,solve,init_printing
x = Symbol('x')
x=1
print(x + x + 1)
x = Symbol('x')
y= Symbol('y')
print(x*y+y*x)
p=(x+2)*(x+3)
print(p.expand())
exp=x**2-y**2
print(factor(exp))
print(factor(x+y+x*y))
#pretty prenting use of pprint
pprint(x+y+x*y)

#printing series x+x^2/2+x^3/3+x^4/4
def print_series(n):

 init_printing(order='rev-lex')
 x = Symbol('x')
 series = x
 for i in range(2, n+1):
  series = series + (x**i)/i
 pprint(series)
if __name__ == '__main__':
 n = 4
 print_series(int(n))

#substituting values
exp=x**2+x*y+y**2
res=exp.subs({x:1,y:2})
print(res)
r=exp.subs({x:1-y})
print(simplify(r))

#solving expression
from sympy import Symbol
x=Symbol('x')
ex=x-5-7
print(solve(ex))

#solving Quadratic Equation
from sympy import solve
x = Symbol('x')
expr = x**2 + 5*x + 4
print(solve(expr, dict=True))

expr = x**2 + x + 1
print(solve(expr, dict=True))

#Solving one variable in terms of another
x=Symbol('x')
a=Symbol('a')
b=Symbol('b')
c=Symbol('c')
ex=a*x**2+b*x+c
print(solve(ex,x,dict=True))

#Solving a system of linear equation
x=Symbol('x')
y=Symbol('y')
e1=2*x+3*y-6
e2=3*x+2*y-12
soln=solve((e1,e2),dict=True)
print(solve((e1,e2),dict=True))

#to verify whether given no's are solution or not
soln = soln[0]
print(e1.subs({x:soln[x], y:soln[y]}))

#plotting using sympy
from sympy.plotting import plot
from sympy import Symbol
x=Symbol('x')
plot((2*x+3),(x,-5,5),title='A line',xlabel='x',ylabel='2*x+3')

#plotting multiple function
from sympy.plotting import plot
from sympy import Symbol
x=Symbol('x')
pl=plot(2*x+3,3*x+1,legend=True,show=False)
pl[0].line_color='b'
pl[1].line_color='r'
pl.show()

