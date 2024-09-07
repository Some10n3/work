
# Question 1: Find the mass probabilities of all possible outcomes (X = 0, 1, 2, 3, 4) when n = 4

outcomes <- 0:4  # :Limit possible outcomes to (0, 1, 2, 3, 4)
n <- 4           # Number of trials
p <- 0.10        # Probability of success

massProbabilities <- dbinom(outcomes, size = n, prob = p)                 # Calculate mass probabilities using dbinom()
cat("Question 1: Mass probabilities of all possible outcomes:\n")
cat(massProbabilities, "\n")

# Question 2: Find the mean and variance of this distribution using rbinom()

numSimulations <- 100000                                                  # simulate 100000 sets of 4 bits transmitted
errorsInSets <- rbinom(numSimulations, size = n, prob = p)                # calculate the number of errors in each set from the 100000 sets

# Calculate the empirical mean and variance
empiricalMean <- mean(errorsInSets)                                       # Calculate the empirical mean
empiricalVariance <- var(errorsInSets)                                    # Calculate the empirical variance
cat("\nQuestion 2: Empirical mean of errors:", empiricalMean, "\n")
cat("Question 2: Empirical variance of errors:", empiricalVariance, "\n")

# Question 3: Find the probability that the most errors is 3, P(X ≤ 3) using pbinom()

maxErrors <- 3

probMaxErrors <- pbinom(maxErrors, size = n, prob = p)                    # The pbinom() function calculates the cumulative probabilities for each outcome up to the value given
cat("\nQuestion 3: Probability that the most errors is 3 (P(X ≤ 3)):", probMaxErrors, "\n")

# Question 4: Draw this probability distribution using barplot() with all labels

barplot(massProbabilities, names.arg = outcomes, xlab = "Number of Errors",   # Create a bar plot
        ylab = "Probability", main = "Probability Distribution", col = "purple", border = "black")

text(x = barplot(massProbabilities, plot = FALSE), y = massProbabilities,     # Adding labels to each bar
     labels = round(massProbabilities, 3), pos = 3)
