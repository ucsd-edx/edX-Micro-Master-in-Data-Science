```python
#X1 = 1/3 + 0 + 1/6;
#X2 = 0 + 0 + 0;
#X3 = 1/6 + 0 + 1/3;

#Y1 = 1/3 + 0 + 1/6;
#Y2 = 0 + 0 + 0;
#Y3 = 1/6 + 0 + 1/3;

#E_X = 1*X1 + 2*X2 + 3*X3;
#E_Y = 1*Y1 + 2*Y2 + 3*Y3;
#E_XY = 1*1/3 + 2*0 + 3*1/6 + 2*0 + 4*0 + 6*0 + 3*1/6 + 6*0 + 9*1/3;
#COV_XY  = E_XY - E_X * E_Y;
#E_X2 = 1*X1 + 4*X2 + 9*X3;
#E_Y2 = 1*X1 + 4*X2 + 9*X3;
#STD_X = math.sqrt(E_X2 - E_X**2);
#STD_Y = math.sqrt(E_Y2 - E_Y**2);


solution1 = "1/3 + 0 + 1/6"
solution2 = "0 + 0 + 0"
solution3 = "1/6 + 0 + 1/3"
solution4 = "1/3 + 0 + 1/6"
solution5 = "0 + 0 + 0"
solution6 = "1/6 + 0 + 1/3"
solution7 = "0"
solution8 = "1"
solution9 = "1*({0})+2*({1})+3*({2})".format(solution1, solution2,solution3)#{"$E_X"}
solution10 = "1*({0})+2*({1})+3*({2})".format(solution4, solution5, solution6)#{"$E_Y"}
solution11 = "{0} + {1}".format(solution9, solution10)#{"$E_X + $E_Y"}
solution12 = "1*1/3 + 2*0 + 3*1/6 + 2*0 + 4*0 + 6*0 + 3*1/6 + 6*0 + 9*1/3"
solution13 = "1*1/3 + 2*0 + 3*1/6 + 2*0 + 4*0 + 6*0 + 3*1/6 + 6*0 + 9*1/3 - (1*(1/3 + 0 + 1/6) + 2*(0 + 0 + 0) + 3*(1/6 + 0 + 1/3)) * (1*(1/3 + 0 + 1/6) + 2*(0 + 0 + 0) + 3*(1/6 + 0 + 1/3))"
solution14 = "({0})/(sqrt(1*(1/3 + 0 + 1/6) + 4*(0 + 0 + 0) + 9*(1/6 + 0 + 1/3) - (1*(1/3 + 0 + 1/6) + 2*(0 + 0 + 0) + 3*(1/6 + 0 + 1/3))^2)*sqrt(1*(1/3 + 0 + 1/6) + 4*(0 + 0 + 0) + 9*(1/6 + 0 + 1/3) - (1*(1/3 + 0 + 1/6) + 2*(0 + 0 + 0) + 3*(1/6 + 0 + 1/3))^2))".format(solution13) #{"($COV_XY)/(($STD_X)*($STD_Y))"}
solution15 = "1"#{"0"}

solutions = [solution1, solution2, solution3, solution4, solution5, solution6, solution7, solution8, solution9, solution10, solution11, solution12, solution13, solution14, solution15]
```
<table>
<tr>
   <th></th>
   <th>X=1</th>
   <th>X=2</th>
   <th>X=3</th>
 </tr>
 <tr>
   <td>Y=1</td>
   <td>1/3</td>
   <td>0</td>
   <td>1/6</td>
 </tr>
 <tr>
    <td>Y=2</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
 </tr>
 <tr>
    <td>Y=3</td>
    <td>1/6</td>
    <td>0</td>
    <td>1/3</td>
 </tr>
</table>

(1) The marginal distribution of \\\(X\\\) is

\\\(P(X=1)=\\\)

[_]

\\\(P(X=2)=\\\)

[_]

\\\(P(X=3)=\\\)

[_]

(2) The marginal distribution of \\\(Y\\\) is

\\\(P(Y=1)=\\\)

[_]

\\\(P(Y=2)=\\\)

[_]

\\\(P(Y=3)=\\\)

[_]

(3) Are \\\(X\\\) and \\\(Y\\\) independent? (1=independent, 0=dependent)

[_]

(4) Are \\\(X\\\)  and \\\(Y\\\)  identically distributed? (0=no, 1=yes)

[_]

(5) \\\(E(X) =\\\)

[_]

(6) \\\(E(Y) =\\\)

[_]

(7) \\\(E(X+Y) =\\\)

[_]

(8) \\\(E(XY) = \\\)

[_]

(9) \\\(Cov(X,Y) =\\\)

[_]

(10) The correlation coefficient between \\\(X\\\) and \\\(Y\\\) is

[_]

(11) Are \\\(X\\\) and \\\(Y\\\) correlated (1=Correlated, 0=uncorrelated, -1=anticorrelated)

[_]
