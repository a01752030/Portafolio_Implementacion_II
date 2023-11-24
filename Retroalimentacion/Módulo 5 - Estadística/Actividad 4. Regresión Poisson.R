data(warpbreaks)
mydata <- warpbreaks
hist(mydata$breaks, main="Histograma de Rupturas", xlab="Número de Rupturas", col="lightblue", border="black")


mean(mydata$breaks)
var(mydata$breaks)

poisson.model <- glm(breaks ~ wool + tension, mydata, family = poisson(link = "log"))
summary(poisson.model)

# poisson.model2 <- glm(breaks ~ wool + tension, mydata = mydata, family = quasipoisson(link = "log"))
summary(poisson.model2)