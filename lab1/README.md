# Lab1
In this repository is present a possibile solution for the set covering problem. I worked with my collegue Luca Marcellino (292950) in order to to find a best solution.
The code print the sum of number of elements inside the lists (W). In the code the unit_cost is setted to the len of the list that the code will add, but in this case the computation time will increase exponentially when also the N increase. When we try to explore N=100 we can't find a good solution in a reasonable time.
If we change the unit_cost to one we obtain the results here below. The results are not optiamal but the time to achive them is very good. we thought that this could be an optimal trade-off between (difference between optimal solution and found solution) and (computational time).


Problem with N=5
A* W=5; bloat=0%
Done in 0.019455671310424805 seconds


Problem with N=10
A* W=12; bloat=20%
Done in 0.0029790401458740234 seconds


Problem with N=20
A* W=32; bloat=60%
Done in 0.002991199493408203 seconds


Problem with N=100
A* W=183; bloat=83%
Done in 0.06474566459655762 seconds


Problem with N=500
A* W=1361; bloat=172%
Done in 2.228945255279541 seconds


Problem with N=1000
A* W=2997; bloat=200%
Done in 7.1089537143707275 seconds
