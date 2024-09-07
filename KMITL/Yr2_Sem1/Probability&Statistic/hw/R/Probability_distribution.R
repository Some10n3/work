


joint <- matrix(c(0.01, 0.02, 0.02, 0.15, 0.02, 0.03, 0.10, 0.10, 0.25, 0.20, 0.05, 0.05), nrow = 4, ncol = 3)

# Calculate conditional probabilities P(Y|X=1)
conditional_probs1 <- joint[, 1] / sum(joint[, 1])
# Calculate conditional probabilities P(Y|X=2)
conditional_probs2 <- joint[, 2] / sum(joint[, 2])
# Calculate conditional probabilities P(Y|X=3)
conditional_probs3 <- joint[, 3] / sum(joint[, 3])

expected_value1 <- sum(conditional_probs1 * c(1, 2, 3, 4))
cat("The expected value of P(y|X=1) is",expected_value1, "\n")

variance1 <- sum(conditional_probs1 * (c(1, 2, 3, 4) - expected_value1)^2)
cat("The variance value of P(y|X=1) is",variance1, "\n")

expected_value2 <- sum(conditional_probs2 * c(1, 2, 3, 4))
cat("The expected value of P(y|X=2) is",expected_value2, "\n")

variance2 <- sum(conditional_probs2 * (c(1, 2, 3, 4) - expected_value2)^2)
cat("The variance value of P(y|X=2) is",variance2, "\n")

expected_value3 <- sum(conditional_probs3 * c(1, 2, 3, 4))
cat("The expected value of P(y|X=3) is",expected_value3, "\n")

variance3 <- sum(conditional_probs3 * (c(1, 2, 3, 4) - expected_value3)^2)
cat("The variance value of P(y|X=3) is",variance3, "\n\n")

cat("The respond time should be", expected_value3, "because it's the expected value.")
