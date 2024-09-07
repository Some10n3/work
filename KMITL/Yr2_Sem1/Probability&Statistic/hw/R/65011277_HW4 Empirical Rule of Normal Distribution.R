
options(scipen = 20)                              #Forcing the program to not use scientific notations

set.seed(277)                                     #Set seed for the randomization as the last 3 digits of my ID to make it unique from my friends

# Function to confirm the Empirical Rule for any normal distribution (μ, σ)
# Where mu is the mean and sigma is the Standard deviation
empirical_rule_prob <- function(mu, sigma, num_points = 10000000) {
  
  
  X <- rnorm(num_points, mu, sigma)                             # Generate random data points from a normal distribution with given μ and σ
  
  
  one_sd <- sum(X < mu + sigma & X > mu - sigma) / num_points       # Calculate the percentage of data within one standard deviation
  
  
  two_sd <- sum(X < mu + (2 * sigma) & X > mu - (2 * sigma)) / num_points   # Calculate the percentage of data within two standard deviations
  
  
  three_sd <- sum(X < mu + (3 * sigma) & X > mu - (3 * sigma)) / num_points # Calculate the percentage of data within three standard deviations
  
  
  cat("Probability within one standard deviation: ", one_sd, "\n")
  
  cat("Probability within two standard deviations: ", two_sd, "\n")
  
  cat("Probability within three standard deviations: ", three_sd, "\n")
}

empirical_rule_prob(mu = 0, sigma = 1)
empirical_rule_prob(mu = 5, sigma = 3)
empirical_rule_prob(mu = 16, sigma = 7)

