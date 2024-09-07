myMode <- function(data) {
  
  freqTable <- table(data)
  
  maxFreq <- max(freqTable)                                   # Find the maximum frequency in the table
  
  modes <- as.numeric(names(freqTable[freqTable == maxFreq])) # Identify the unique values with the maximum frequency
  
  if (length(modes) == 1 && length(unique(data)) == 1) {       # If there's only one unique value and it's the same as the mode
    modes <- modes[!is.na(modes)]  
  } else if (length(modes) == length(data) || length(modes) == length(unique(data))) {
    modes <- "No mode"                                        # If all values occur equally frequently, there is no mode
  } else {
    modes <- modes[!is.na(modes)]                             # If there are multiple modes, return all of them
  }
  
  return(modes)
}

sampleData1 <- c(1, 2, 3, 4, 5)
sampleData2 <- c(3, 3, 3, 3, 3)
sampleData3 <- c(1, 2, 2, 3, 4, 4, 5)
sampleData4 <- c(1, 1, 2, 2, 3, 3, 4, 4, 5)
sampleData5 <- c(1, 1, 2, 2, 3 ,3, 4, 4, 5, 5)

result <- myMode(sampleData1)
cat("The mode of sample1 was ", result, "\n")

result <- myMode(sampleData2)
cat("The mode of sample2 was ", result, "\n")

result <- myMode(sampleData3)
cat("The mode of sample3 was ", result, "\n")

result <- myMode(sampleData4)
cat("The mode of sample4 was ", result, "\n")

result <- myMode(sampleData5)
cat("The mode of sample5 was ", result, "\n")
