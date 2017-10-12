library(poLCA)

#values.csvは消費価値観だけ取り出したメインデータ
values <- read.csv(file = "values.csv",as.is = TRUE)
values<-na.omit(values)

#値が自然数しかダメなので01から12データに変換
for(i in 1:2854){
  for(j in 1:33){
    if(values[i,j] == 1){
      values[i,j] <- 2
    }else if(values[i,j] == 0){
      values[i,j] <- 1
    }
  }
}

#nameにデータフレームのカラム名を入れる
name<-names(values)

#知恵袋的なところで見つけたコード。これやるとうまくいった。http://r.789695.n4.nabble.com/cbind-formula-definition-td903703.html
f <- as.formula(paste("cbind(", paste(name, collapse = ","), ")~1"))

#BIC（情報量基準）の最小値の初期値
min_bic <- 100000

#クラスを２から７まで変えていって、一番いいモデルを出力
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

#citing
#http://dlinzer.github.io/poLCA/
#http://statistics.ohlsen-web.de/latent-class-analysis-polca/
