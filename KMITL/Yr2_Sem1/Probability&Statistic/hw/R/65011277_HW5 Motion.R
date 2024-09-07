
my.mean <- function(data, min_val, max_val, step = 0.01) {
   
  mx <- seq(min_val, max_val, by = step) # Generate a sequence of trial mean values
  
  cat(data - mx[1])
  
  for (i in 1:length(mx)) {
    
    sum.diff <- sum(data - mx[i])        # Calculate the sum of differences between the data and the current trial mean value.
    
    if (round(sum.diff, digits = 2) == 0) {   # Check if the sum of diff is zero

      return(mx[i])
      break
      
    }
  }
}

data <- c(4.9, 6.8, 1.3, 7.4, 2.5)
cat("Mean =", my.mean(data, min_val = min(data), max_val = max(data)), "\n")

built_in_mean <- mean(data)
cat("Built-in mean =", round(built_in_mean, digits = 2), "\n")