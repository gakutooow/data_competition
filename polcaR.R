values <- read.csv(file = "values.csv",as.is = TRUE)
values<-na.omit(values)

for(i in 1:2854){
  for(j in 1:33){
    if(values[i,j] == 1){
      values[i,j] <- 2
    }else if(values[i,j] == 0){
      values[i,j] <- 1
    }
  }
}


name<-names(values)
f <- as.formula(paste("cbind(", paste(name, collapse = ","), ")~1"))


min_bic <- 100000

for(i in 2:7){
  lc <- poLCA(f, values, nclass=i, maxiter=3000,
              tol=1e-5, na.rm=FALSE,
              nrep=10, verbose=TRUE, calc.se=TRUE)
  if(lc$bic < min_bic){
    min_bic <- lc$bic
    LCA_best_model<-lc
  }
}
LCA_best_model
