```python
#C11 = 1/16;
#C12 = 2/16;
#C13 = 1/16;
#C21 = 2/16;
#C22 = 4/16;
#C23 = 2/16;
#C31 = 1/16;
#C32 = 2/16;
#C33 = 1/16;

#X1 = C11 + C21 + C31;
#X2 = C12 + C22 + C32;
#X3 = C13 + C23 + C33;

#Y1 = C11 + C12 + C13;
#Y2 = C21 + C22 + C23;
#Y3 = C31 + C32 + C33;

#E_X = 1*X1 + 2*X2 + 3*X3;
#E_Y = 1*Y1 + 2*Y2 + 3*Y3;
#E_XY = 1*C11 + 2*C12 + 3*C13 + 2*C21 + 4*C22 + 6*C23 + 3*C31 + 6*C32 + 9*C33;
#COV_XY  = E_XY - E_X *E_Y;
#E_X2 = 1*X1 + 4*X2 + 9*X3;
#E_Y2 = 1*X1 + 4*X2 + 9*X3;
#STD_X = math.sqrt(E_X2 - E_X**2);
#STD_Y = math.sqrt(E_Y2 - E_Y**2);

solution1 = "1/16 + 2/16 + 1/16"
solution2 = "2/16 + 4/16 + 2/16"
solution3 = "1/16 + 2/16 + 1/16"
solution4 = "1/16 + 2/16 + 1/16"
solution5 = "2/16 + 4/16 + 2/16"
solution6 = "1/16 + 2/16 + 1/16"
solution7 = "1"
solution8 = "1"
solution9 = "1*(1+ 2 + 1)/16+2*(2 + 4 + 2)/16+3*(1 + 2 + 1)/16"#{"$E_X"}
solution10 = "1*(1 + 2 + 1)/16+2*(2 + 4 + 2)/16+3*(1 + 2 + 1)/16"#{"$E_Y"}
solution11 = "{0} + {1}".format(solution9, solution10)#{"$E_X + $E_Y"}
solution12 = "(1*1 + 2*2 + 3*1 + 2*2 + 4*4 + 6*2 + 3*1 + 6*2 + 9*1)/16"#{"$E_XY"}
solution13 = "1*1/16 + 2*2/16 + 3*1/16 + 2*2/16 + 4*4/16 + 6*2/16 + 3*1/16 + 6*2/16 + 9*1/16 - (1 * (1/16 + 2/16 + 1/16) + 2 * (2/16 + 4/16 + 2/16) + 3 * (1/16 + 2/16 + 1/16)) * (1 * (1/16 + 2/16 + 1/16) + 2 * (2/16 + 4/16 + 2/16) + 3 * (1/16 + 2/16 + 1/16))"#{"$COV_XY"}
solution14 = "({0})/(sqrt(1 * (1/16 + 2/16 + 1/16) + 4 * (2/16 + 4/16 + 2/16) + 9 * (1/16 + 2/16 + 1/16) - (1 * (1/16 + 2/16 + 1/16) + 2 * (2/16 + 4/16 + 2/16) + 3 * (1/16 + 2/16 + 1/16))^2) * sqrt(1 * (1/16 + 2/16 + 1/16) + 4 * (2/16 + 4/16 + 2/16) + 9 * (1/16 + 2/16 + 1/16) - (1 * (1/16 + 2/16 + 1/16) + 2 * (2/16 + 4/16 + 2/16) + 3 * (1/16 + 2/16 + 1/16))^2))".format(solution13)#{"($COV_XY)/(($STD_X)*($STD_Y))"}
solution15 = "0"#{"0"}

solutions = [solution1, solution2, solution3, solution4, solution5, solution6, solution7, solution8, solution9, solution10, solution11, solution12, solution13, solution14, solution15]
```



The following formula are useful for this assignment:

- Covariance \\\(COV(X,Y) = E[XY]-E[X]E[Y]\\\)

- Correlation coefficient \\\(r(X,Y) = \frac{COV(X,Y)}{\sqrt{VAR[X]}\sqrt{VAR[Y]}}\\\)


<table>
<tr>
   <th></th>
   <th>X=1</th>
   <th>X=2</th>
   <th>X=3</th>
 </tr>
 <tr>
   <td>Y=1</td>
   <td>1/16</td>
   <td>2/16</td>
   <td>1/16</td>
 </tr>
 <tr>
    <td>Y=2</td>
    <td>2/16</td>
    <td>4/16</td>
    <td>2/16</td>
 </tr>
 <tr>
    <td>Y=3</td>
    <td>1/16</td>
    <td>2/16</td>
    <td>1/16</td>
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
