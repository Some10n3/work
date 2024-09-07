
options(scipen = 20)                              #Forcing the program to not use scientific notations

set.seed(277)                                     #Set seed for the randomization as the last 3 digits of my ID to make it unique from my friends

#solve question Q6-Q10 by using R built-in functions: dnorm( ), pnorm( ), ...

#6.  An article in Proceeding of the 33rd International ACM SIGIR Conference on Research and Development in Information Retrieval [“Understanding Web Browsing Behaviors Through Weibull Analysis of Dwell Time” (2010, p. 379-386)] proposed that a Weibull distribution can be used to model Web page dwell time (the length of time a Web visitor spends on a Web page). For a specific Web page, the shape and scale parameters are 1 and 300 seconds, respectively. Determine the probability that a Web user spends more than four minutes on this Web page.
q6 <- function(shape, scale, time){
  1 - pweibull(time, shape, scale) #using pweibull, the built-in function for weibull distribution
}

#7. The maximum time to complete a task in a project is 2.5 days. Suppose that the completion time as a proportion of this maximum is a beta random variable with α = 2 and β = 3.  What is the probability that the task requires more than two days to complete?
q7 <- function(alpha, beta, time){
  1 - pbeta(time, alpha, beta) #using pbeta, the built-in function for beta distribution
}

#8.  The CPU of a personal computer has a lifetime that is exponentially distributed with a mean lifetime of six years. You have owned this CPU for three years.  What is the probability that the CPU fails in the next three years?
q8 <- function(mean, time){
  pexp(time, mean) #using pexp, the built-in function for exponential distribution
}

#9. The life of a semiconductor laser at a constant power is normally distributed with a mean of 7000 hours and a standard deviation of 600 hours. What is the probability that a laser fails before 5800 hours?
q9 <- function(mean, sd, time){
  pnorm(time, mean, sd) #using pnorm, the built-in function for normal distribution
}

#10. The length of time (in seconds) that a user views a page on a Web site before moving to another page is a lognormal random variable with parameters θ = 0.5 and ω = 1. What is the probability that a page is viewed for more than 10 seconds?
q10 <- function(theta, omega, time){
  1 - plnorm(time, theta, omega) #using plnorm, the built-in function for lognormal distribution
}



q6(1, 300, 240)
q7(2, 3, 0.8)
q8(1/6, 3)
q9(7000, 600, 5800)
q10(0.5, 1, 10)