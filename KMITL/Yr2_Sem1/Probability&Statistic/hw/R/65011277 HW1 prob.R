  #HW 1 Empirical Probably
  #65011277 Chanasorn Howattanakulphong

options(scipen = 20)      #Forcing the program to not use scientific notations

roll.die <- function(n){  #create a function for rolling a die n times
  
  set.seed(277)                                     #Set seed for the randomization as the last 3 digits of my ID to make it unique from my friends
  
  die <- c(1, 2, 3, 4, 5, 6)                        #create a vector that contains each face of the die
  
  results <-sample(die, size = n, replace = TRUE)   #Sampling the die n times

  get5 <- sum(results == 5)                         #get the sum of 5 results in the sample
  
  print(get5)                                       #I just added this to see the sum
  
  prob5 <- get5 / n                                 #Probability of getting 5 from rolling n times
  
  differrent <- abs(prob5-(1/6))                    #Difference from my prob to the actual chance of getting 5
  
  cat("rolling =",n,"\n")                           #outputs how many times the die got rolled
  
  cat("Probability of getting 5 =", prob5, "\n")    #outputs my probability
  
  cat("Difference =", differrent, "\n\n")           #outputs the difference
}

roll.die(1000)      #calling the function with n as 1000

roll.die(100000)    #calling the function with n as 100000    

roll.die(1000000)   #calling the function with n as 1000000










