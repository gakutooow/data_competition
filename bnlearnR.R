library(Rgraphviz)
library(bnlearn)

bnlearnR <- read.csv(file = "bnlearnR.csv",as.is = TRUE)
bnlearnR<-na.omit(bnlearnR)

for (i in 1:2490){
 	for(j in 1:5){
 		bnlearnR[i,j]<-as.numeric(bnlearnR[i,j])
 	}
 }

print(hc(bnlearnR))
net.estimated = model2network("[SampleID][Twitter|SampleID][instagram|Twitter][redbull|Twitter:instagram][kirin|redbull]")
graphviz.plot(net.estimated, shape = "ellipse")

bn.fit(net.estimated, bnlearnR ,method = "mle")

library(forecast)
training.set = protein_dataset[1:405, ]
test.set = protein_dataset[406:810, ]
baysian_structure = hc(training.set)
fitted = bn.fit(baysian_structure, training.set,method = "mle")
test.set2 <- test.set
test.set2$PKC <- 0
head(test.set2)

pred = predict(fitted, "PKC", test.set2)
head(cbind(pred, test.set[, "PKC"]))

accuracy(f = pred, x = test.set[, "PKC"])
df <- data.frame(prediction=pred,actual=test.set[, "PKC"])
p <- ggplot(df,aes(x = prediction,y = actual)) + geom_point() 
p <- p + geom_line(data = data.frame(x = c(0,40), y = c(0,40)),aes(x = x, y = y), colour = "red")
p
