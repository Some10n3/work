
options(scipen = 20)                              #Forcing the program to not use scientific notations

set.seed(328)                                     #Set seed for the randomization as the last 3 digits of my ID to make it unique from my friends

my.pi <- function(n){                             #Build “my.Pi” : a function to estimate Pi value

  x = runif(n, min = 0, max = 1)                  #Use runif(n) to generate n random coordinate (x,y) points
  
  y = runif(n, min = 0, max = 1)                  #Use runif(n) to generate n random coordinate (x,y) points
  
  r = sqrt(x^2 + y^2)                             #Calculate radius using the distance between the generated coordinate (x,y) points
  
  num.circle.dots = sum(r <= 1)                   #count the dots inside the circle
  
  num.square.dots = n                             #amount of dots
  
  ratio = num.circle.dots / num.square.dots       #Find the ratio of a quarter of unit circle and unit square
  
  my.pi = ratio * 4                               #Multiply by 4 quadrant
  
  plot(x, y, col = ifelse(r <= 1, "pink", "purple"), asp = 1, pch = 20)  #Plot graph to display the ratio in the first quadrant with different colors by shape
  
  return(my.pi)
}

cat("My pi =", my.pi(3000000), "\n")               #print out the value of estimated pi

