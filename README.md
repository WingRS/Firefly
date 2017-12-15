# This is implementation of FireFly algorithm
This is basic FA algorithm based on  is a metaheuristic research by Xin-She Yang and inspired by the flashing behaviour of fireflies.
This algorithm also is used for optimization of global minimum, maximum functions. In this current example Schwefel's function 7

# Description:
Schwefel's function [Sch81] is deceptive in that the global minimum is geometrically distant, over the parameter space, from the next best local minima. Therefore, the search algorithms are potentially prone to convergence in the wrong direction.

function definition:



  f7(x)=sum(-x(i)·sin(sqrt(abs(x(i))))), i=1:n; -500<=x(i)<=500.
global minimum:

  f(x)=-n·418.9829; x(i)=420.9687, i=1:n. 
This function is implemented in objfun7.

