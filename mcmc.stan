data {
	int<lower=0> N;
  int<lower=0, upper=1> y[N];
  int<lower=1> D;
  row_vector[D] x[N];
  int<lower=1> E;
  row_vector[E] z[N];

}

parameters {
  vector[D] beta[N];
  vector[E] delta[D];
  matrix<lower=1.0e-8>[D,N] sigma;
  matrix[E,D] gamma;
  matrix<lower=1.0e-8>[E,D] tau;
}
model {
	for (d in 1:D){
    for (e in 1:E){
      gamma[e,d] ~ normal(0,100);
      delta[d,e] ~ normal(gamma[e,d], tau[e,d]); //デルタの事前分布
    }
  }
  for (n in 1:N){
    for (d in 1:D)
      beta[n,d] ~ normal(z[n]*delta[d],sigma[d,n]);
  }

	for (n in 1:N)
  	y[n] ~ bernoulli_logit(x[n]*beta[n]);

}
