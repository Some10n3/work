# Step 1: Define the data
diameter <- c(8.24, 8.25, 8.20, 8.23, 8.24, 8.21, 8.26, 8.26, 8.20, 8.25, 8.23, 8.23, 8.19, 8.28, 8.24)

# Step 2: Define the null and alternative hypotheses
# H0: μ ≤ 8.25
# H1: μ > 8.25

# Step 3: Perform the one-sample t-test
result <- t.test(diameter, mu = 8.25, alternative = "greater")

# Step 4: Make a decision based on the p-value
if (result$p.value < 0.05) {
  cat("Reject the null hypothesis. There is evidence that the mean diameter exceeds 8.25 mm.")
} else {
  cat("Fail to reject the null hypothesis. There is not enough evidence that the mean diameter exceeds 8.25 mm.")
}

# Step 5: Print the t-test results
print(result)
