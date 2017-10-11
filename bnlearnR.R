library(Rgraphviz)
library(bnlearn)

bnlearnR <- read.csv(file = "bnlearnR.csv",as.is = TRUE)
bnlearnR<-na.omit(bnlearnR)

print(dim(bnlearnR))

for (i in 1:2490){
 	for(j in 1:5){
 		bnlearnR[i,j]<-as.numeric(bnlearnR[i,j])
 	}
 }

print(hc(bnlearnR))
net.estimated = model2network("")
graphviz.plot(net.estimated, shape = "ellipse")

bn.fit(net.estimated, bnlearnR ,method = "mle")



if(0){
コメントアウト

library(forecast)
training.set = bnlearnR[1:1245, ]
test.set = bnlearnR[1246:2490, ]
baysian_structure = hc(training.set)
fitted = bn.fit(baysian_structure, training.set,method = "mle")
test.set2 <- test.set
test.set2$redbull <- 0
pred = predict(fitted, "redbull", test.set2)
head(cbind(pred, test.set[, "redbull"]))
accuracy(f = pred, x = test.set[, "redbull"])

library(ggplot2)
df <- data.frame(prediction=pred,actual=test.set[, "redbull"])
p <- ggplot(df,aes(x = prediction,y = actual)) + geom_point()
p <- p + geom_line(data = data.frame(x = c(0,40), y = c(0,40)),aes(x = x, y = y), colour = "red")
p


}
