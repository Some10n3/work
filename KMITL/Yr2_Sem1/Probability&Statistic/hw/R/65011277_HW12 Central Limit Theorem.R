# Central Limit Theorem (CLT) Proof

# Parameters
pop_mean <- 0          # Set the population mean
pop_sd <- 1            # Set the population standard deviation
sample_size <- 80      # Set the sample size
num_samples <- 3000    # Set the number of samples

# Initialize vectors to store sample means and population data
x.bar <- numeric(num_samples)  # Create an empty vector to store sample means
popu.x <- rnorm(n = sample_size * num_samples, mean = pop_mean, sd = pop_sd)  # Generate the population data

# Generate sampling distribution
for (i in 1:num_samples) {  # Loop to generate multiple samples
  samp.x <- sample(popu.x, size = sample_size)  # Randomly sample from the population data
  x.bar[i] <- mean(samp.x)  # Calculate and store the sample mean
}

# Population distribution
hist(popu.x, main = "Population Distribution")  # Create a histogram of the population data

# Sampling distribution
hist(x.bar, main = "Sampling Distribution")  # Create a histogram of the sample means

# Rule 1 proof
cat("Rule 1 - Sample Mean vs Population Mean:\n")  # Display Rule 1 title
cat("Sample Mean: ", mean(x.bar), "\n")  # Calculate and display the sample mean
cat("Population Mean: ", pop_mean, "\n")  # Display the population mean

# Rule 2 proof
cat("\nRule 2 - Sample Standard Deviation vs Population Standard Deviation / sqrt(n):\n")  # Display Rule 2 title
cat("Sample Standard Deviation: ", sd(x.bar), "\n")  # Calculate and display the sample standard deviation
cat("Expected Sample Standard Deviation: ", pop_sd / sqrt(sample_size), "\n")  # Display the expected sample standard deviation
