t <- 0
#random seed generator
set.seed(123)

#produces randomly generated starting points
x <- runif(3, -10, 10)

#initial temperature setting
T0 <- 10000

eval <- function(x, y, z) {
	return (x^2 + y^2 + z^2)
}

x1 <- x[1]
x2 <- x[2]
x3 <- x[3]

curr <- eval(x1, x2, x3)

#temperature iterations
while (t < 2500) {
	count <- 0
    #runs a set number of iterations for each temp setting
	while (count < 2500) {
		xx <- runif(3, -.3, .3)
		x11 <- xx[1] + x1
		x22 <- xx[2] + x2
		x33 <- xx[3] + x3
		test <- eval(x11, x22, x33)
		if (test < curr) {
			curr <- test
			x1 <- x11
			x2 <- x22
			x3 <- x33
			}
		else {
			if ((runif(1, 0, 1)) < exp((curr - test)/T0)) {
				curr <- test
				x1 <- x11
				x2 <- x22
				x3 <- x33
				}
			}
		count <- count + 1
		}
    #reduces the temperature setting
	T0 <- T0/2
	t <- t + 1		
	}
#final result
c(x1, x2, x3 )
eval(x1, x2, x3)
