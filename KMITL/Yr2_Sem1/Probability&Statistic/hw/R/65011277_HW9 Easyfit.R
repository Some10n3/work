
wb<-rweibull(n=400,shape=9,scale=5)               
#generates 400 random samples from a Weibull distribution with a shape parameter of 9 and a scale parameter of 5.
write.csv(data.frame(wb),file="D:/wdata.csv")     
#converts the data in wb to data frame and store it in a csv file.


