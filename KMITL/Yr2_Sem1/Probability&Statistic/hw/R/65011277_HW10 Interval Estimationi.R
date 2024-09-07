int.est = function(x, conf){
  
  area = (conf / 100) + ((1 - (conf / 100)) / 2)
  se = sd(x) /  sqrt(length(x))
  margin = qt(area, length(x) - 1) * se
  
  lower = mean(x) - margin
  upper = mean(x) + margin
  
  cat("lower = ", lower, " upper = ", upper)
  
}

score = c(83, 73, 62, 63, 71, 77, 77, 59, 92)
int.est(score, 95)

t.test(score)$conf.int
