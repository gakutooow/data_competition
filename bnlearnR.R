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
