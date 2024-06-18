The question number, as well as any extra explanation, are at the top, and the answer is the output of the cell.


```R
#1 (a) (i)

y <- c(16, 5, 10, 15, 13, 22)
xi <- c(4, 1, 2, 3, 3, 4)
x <- cbind(c(1, 1, 1, 1, 1, 1), xi)
n <- length(y)
yp <- t(y)
xp <- t(x)
ypy <- (yp %*% y)
xpx <- (xp %*% x)
xpy <- (xp %*% y)
xpxi <- solve(xpx)

j <- matrix(1, n, n)
ypjy <- (yp %*% j %*% y)
nypjy <- ypjy / n
b <- xpxi %*% xpy
print(b)
```

            [,1]
       0.4390244
    xi 4.6097561



```R
# (ii)
residuals <- c()
for (i in (1:6)){
    y_hat <- b[1]+ xi[i] * b[2]
    residuals[i] <- round(y[i] - y_hat, 2)
}
print(residuals)
```

    [1] -2.88 -0.05  0.34  0.73 -1.27  3.12



```R
# (iii), (iv)
bp <- t(b)

ssr <- (bp %*% xpy - nypjy)
print(ssr)

sse <- ypy - bp %*% xpy
print(sse)
```

             [,1]
    [1,] 145.2073
             [,1]
    [1,] 20.29268



```R
# (v)
mse <- mean(sse) / n
s2b <- mse * xpxi
print(s2b)
```

                         xi
        4.536982 -1.4023399
    xi -1.402340  0.4949435



```R
# (vi), (vii)
x4 <- c(1, 4)
x4t <- t(x4)
hy4 <- (x4t %*% b)
print(hy4)

s2pred <- mse * (1 + x4t %*% xpxi %*% x4)
print(s2pred)
```

             [,1]
    [1,] 18.87805
             [,1]
    [1,] 4.619473


2. None of them are linear regression models, my yes/no answer regards whether they can be transformed into one.

(a) Yes, Xi2* = log(Xi2), and xi3* = (Xi1)^2
(b) Yes, take the ln of both sides and the error term can be separated, then Xi2* = (Xi2)^2
(c) Yes, beta_1* = 1, Xi1* = log(beta_1 Xi1)
(d) No
(e) Yes, we can take the inverse of Yi to bring our terms up, then extract the individual terms by taking the ln of both sides



```R
#3

library(tidyverse)
library(ggplot2)

df <- read.csv("senic.csv")

regions <- c("W", "NC", "S", "NE")
factors <- risk ~ age + culturing_ratio + patients + facilities

for (i in regions){
  model <- (lm(factors, data = df %>% filter(region == i)))
  p <- ggplot(model, aes(x = i, y = model$residuals)) + geom_boxplot()
}

#print summary and boxplot for myself
```

Using this information we can answer 6.31

(a)
W: Y_hat = 1.57 + 0.04 X1 + 0.04 X2 - 0.0007 X3 + 0.01 X4
NC: Y_hat = 2.29 + 0.004 X1 + 0.07 X2 + 0.001 X3 + 0.016 X4
S: Y_hat = -0.14 + 0.03 X1 + 0.10 X2 + 0.004 X3 + 0.008 X4
NE: Y_hat = -3.35 +  0.12 X1 + 0.06 X2 + 0.002 X3 + 0.007 X4

(b)
Fairly, the intercept values vary but we consistently see, for example, that the number of patients variable has a smaller coefficient than the culturing ratio.

(c)
W:  MSE = (0.9766)^2 = 0.95
    R^2 = 0.0896
NC: MSE = (1.101)^2 = 1.21
    R^2 = 0.4115
S:  MSE = (0.9678)^2 = 0.93
    R^2 = 0.6088
NE: MSE: (1.011)^2 = 1.02
    R^2 = 0.4613

Again, the measures are fairly similar. The R^2 values are all fairly weak, and the MSE are around 1

(d)

5.
We have that 

$R^2_{Y2|1}$
\
\
$ = \frac{SSR(X_2 | X_1)}{SSE(X_1)}$ 
\
\
$ = \frac{SSR(X_2, X_1) - SSR(X1)}{SSE(X_1)}$
\
\
$ = \frac{b_1 R_{YX_1} + b_2 R_{YX_2} - b_1 R_{YX_1}}{SSE(X_1)}$



```R
#Q5 (a)

x1 <- c(4, 4, 4, 4, 6, 6, 6, 6, 8, 8, 8, 8, 10, 10, 10, 10)
x2 <- c(2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4)
y <- c(64, 73, 61, 76, 72, 80, 71, 83, 83, 89, 86, 93, 88, 95, 94, 100)

df <- data.frame(cbind(y, x1, x2))
df

n <- length(y)

#Full model
#calculating regression coefficients
one_vector <- matrix(1, nrow = n, ncol = 1)

x <- cbind(one_vector, x1, x2)
yp <- t(y)
xp <- t(x)
ypy <- (yp %*% y)
xpx <- (xp %*% x)
xpy <- (xp %*% y)
xpxi <- solve(xpx)

j <- matrix(1, n, n)
ypjy <- (yp %*% j %*% y)
nypjy <- ypjy / n
b <- xpxi %*% xpy
bp <- t(b)

#Sums of squares

ssr_x1x2 <- (bp %*% xpy - nypjy)
sse_x1x2 <- ypy - bp %*% xpy
ssto_x1x2 <- (ypy - nypjy)

#Reduced model
x1 <- cbind(one_vector, x1)

x1p <- t(x1)
x1px1 <- x1p %*% x1
x1py <- x1p %*% y
x1px1_inv <- solve(x1px1)

b <- (x1px1_inv %*% x1p %*% y)
bp <- t(b)

#Sums of squares

ssr_x1 <- (bp %*% x1py - nypjy)
sse_x1 <- ypy - bp %*% x1py
ssto_x1 <- (ypy - nypjy)

ssr_x2_given_x1 <- ssr_x1x2 - ssr_x1
print(ssr_x2_given_x1)
print(ssr_x1)
print(ssr_x1x2)
print(sse_x1x2)

```


<table class="dataframe">
<caption>A data.frame: 16 x 3</caption>
<thead>
	<tr><th scope=col>y</th><th scope=col>x1</th><th scope=col>x2</th></tr>
	<tr><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>
</thead>
<tbody>
	<tr><td> 64</td><td> 4</td><td>2</td></tr>
	<tr><td> 73</td><td> 4</td><td>4</td></tr>
	<tr><td> 61</td><td> 4</td><td>2</td></tr>
	<tr><td> 76</td><td> 4</td><td>4</td></tr>
	<tr><td> 72</td><td> 6</td><td>2</td></tr>
	<tr><td> 80</td><td> 6</td><td>4</td></tr>
	<tr><td> 71</td><td> 6</td><td>2</td></tr>
	<tr><td> 83</td><td> 6</td><td>4</td></tr>
	<tr><td> 83</td><td> 8</td><td>2</td></tr>
	<tr><td> 89</td><td> 8</td><td>4</td></tr>
	<tr><td> 86</td><td> 8</td><td>2</td></tr>
	<tr><td> 93</td><td> 8</td><td>4</td></tr>
	<tr><td> 88</td><td>10</td><td>2</td></tr>
	<tr><td> 95</td><td>10</td><td>4</td></tr>
	<tr><td> 94</td><td>10</td><td>2</td></tr>
	<tr><td>100</td><td>10</td><td>4</td></tr>
</tbody>
</table>



           [,1]
    [1,] 306.25
            [,1]
    [1,] 1566.45
           [,1]
    [1,] 1872.7
         [,1]
    [1,] 94.3


            ANOVA
                    df         ss            ms
regression          2           1872.7       1872.7
    x1              1           1566.45      1566.45
    x1 | x2         1           306.25       306.25

error              13             94.3       7.25 
total              15             1967         -


```R
#(b)
#F test
f <- (sse_x1 - sse_x1x2) / (sse_x1x2 / (n - 3))
f_critical <- qf(0.99, 1, n - 2)
cat(f, f_critical)
```

    42.21898 8.861593

H_0 : b_2 = 0
h_a : b_2 != 0
RR: F* > F(0.99, 1, n - 2)
Test: 42.21898 > 8.861593
The value of F* is in the rejection region, so we can reject H_0 in favour of H_a


```R
#(c)
transform_column <- function(column) {
  n <- length(column)
  transformed <- (1 / sqrt(n - 1)) * (column - mean(column)) / sd(column)
  return(transformed)
}

dft <- as.data.frame(lapply(df, transform_column))

print(dft)
```

                 y         x1    x2
    1  -0.40021759 -0.3354102 -0.25
    2  -0.19729036 -0.3354102  0.25
    3  -0.46786000 -0.3354102 -0.25
    4  -0.12964795 -0.3354102  0.25
    5  -0.21983783 -0.1118034 -0.25
    6  -0.03945807 -0.1118034  0.25
    7  -0.24238530 -0.1118034 -0.25
    8   0.02818434 -0.1118034  0.25
    9   0.02818434  0.1118034 -0.25
    10  0.16346916  0.1118034  0.25
    11  0.09582675  0.1118034 -0.25
    12  0.25365904  0.1118034  0.25
    13  0.14092169  0.3354102 -0.25
    14  0.29875398  0.3354102  0.25
    15  0.27620651  0.3354102 -0.25
    16  0.41149133  0.3354102  0.25



```R
#Q6
#(a)

df <- read.csv("grocery.csv")

transform_column <- function(column) {
  n <- length(column)
  transformed <- (1 / sqrt(n - 1)) * (column - mean(column)) / sd(column)
  return(transformed)
}

dft <- as.data.frame(lapply(df, transform_column))

x <- cbind(dft$cases_shipped, dft$costs, dft$holiday)
y <- dft$total_hours

yp <- t(y)
ypy <- yp %*% y

xp <- t(x)
xpx <- xp %*% x
xpy <- xp %*% y
xpx_inv <- solve(xpx)

b_star <- (xpx_inv %*% xp %*% y)
b_star
```


<table class="dataframe">
<caption>A matrix: 3 x 1 of type dbl</caption>
<tbody>
	<tr><td> 0.1747189</td></tr>
	<tr><td>-0.0463913</td></tr>
	<tr><td> 0.8078617</td></tr>
</tbody>
</table>



(a)
Y = 0.17 - 0.046 X1 + 0.808 X2

(b)
This is just asking for the matrix Rxx, which is the same as X'X. It is meaningful, as it allows us to identify correlated predictor variables. Perhaps one variable has a huge effect on its own, but low effect when regressed after another, because they're correlated


```R
print(xpx)
```

               [,1]       [,2]       [,3]
    [1,] 1.00000000 0.08489639 0.04565698
    [2,] 0.08489639 1.00000000 0.11337076
    [3,] 0.04565698 0.11337076 1.00000000


(c)
We can find the initial coefficients using b_k = (b*_k)(s_y/s_k), then confirm they're accurate by comparing them to the linear model R function applied to the original data


```R
dft <- as.data.frame(lapply(df, transform_column))

sy <- sd(df$total_hours)
sk <- c(sd(df$cases_shipped), sd(df$costs), sd(df$holiday))

b <- c()

for (i in 1:3){
  b[i + 1] <- b_star[i] * (sy / sk[i])
}

b[1] <- mean(df$total_hours) -
  b[2] * mean(df$cases_shipped) -
  b[3] * mean(df$costs) -
  b[4] * mean(df$holiday)

summary(lm(total_hours ~ cases_shipped + costs + holiday,
           data = df))
```


<style>
.list-inline {list-style: none; margin:0; padding: 0}
.list-inline>li {display: inline-block}
.list-inline>li:not(:last-child)::after {content: "\00b7"; padding: 0 .5ex}
</style>
<ol class=list-inline><li>4149.88721195732</li><li>0.000787080381845569</li><li>-13.1660191870869</li><li>623.55448073817</li></ol>




    
    Call:
    lm(formula = total_hours ~ cases_shipped + costs + holiday, data = df)
    
    Residuals:
        Min      1Q  Median      3Q     Max 
    -264.05 -110.73  -22.52   79.29  295.75 
    
    Coefficients:
                    Estimate Std. Error t value Pr(>|t|)    
    (Intercept)    4.150e+03  1.956e+02  21.220  < 2e-16 ***
    cases_shipped  7.871e-04  3.646e-04   2.159   0.0359 *  
    costs         -1.317e+01  2.309e+01  -0.570   0.5712    
    holiday        6.236e+02  6.264e+01   9.954 2.94e-13 ***
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    
    Residual standard error: 143.3 on 48 degrees of freedom
    Multiple R-squared:  0.6883,	Adjusted R-squared:  0.6689 
    F-statistic: 35.34 on 3 and 48 DF,  p-value: 3.316e-12



So we get Y = 4149.89 + 0.00079 X1 - 13.1660191870869 X2 + 623.55 X3, which is the same thing the lm function gives us


```R
X <- cbind(c(1, 1, 1, 1, 1, 1), c(7, 4, 16, 3, 21, 8), c(33, 41, 7, 49, 5, 31))
Xp <- t(X)
XpX <- Xp %*% X
XpX_inv <- solve(XpX)
XpX
XpX_inv
```


<table class="dataframe">
<caption>A matrix: 3 x 3 of type dbl</caption>
<tbody>
	<tr><td>  6</td><td>  59</td><td> 166</td></tr>
	<tr><td> 59</td><td> 835</td><td>1007</td></tr>
	<tr><td>166</td><td>1007</td><td>6206</td></tr>
</tbody>
</table>




<table class="dataframe">
<caption>A matrix: 3 x 3 of type dbl</caption>
<tbody>
	<tr><td>34.5785574</td><td>-1.65089268</td><td>-0.65704022</td></tr>
	<tr><td>-1.6508927</td><td> 0.08030796</td><td> 0.03112763</td></tr>
	<tr><td>-0.6570402</td><td> 0.03112763</td><td> 0.01268501</td></tr>
</tbody>
</table>


