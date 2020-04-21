"""
INTL 550 - HW3 (Hierarchical Bayesian Analysis)
Name : Shukhrat Khuseynov
ID   : 0070495

Comments: 
I did install pystan, but it does not work, possibly due to
my hardware limitations (particularly, low RAM: Spyder alone
is heavy enough for my laptop). Could not install pystan to IDLE.

[submitting without running Stan parts]
    
"""

import pystan
import numpy as np
import pandas as pd

data = pd.read_csv('trend2.csv')

# dropping an unused column and NaN rows
data = data.drop(['cc'], axis=1)
data = data.dropna();

# indexing for countries
countries = data.country.unique()
Ncountries = len(countries)
country_lookup = dict(zip(countries, range(Ncountries)))
country = data['country_code'] = data.country.replace(country_lookup).values

# indexing for years
years = data.year.unique()
Nyears = len(years)
year_lookup = dict(zip(years, range(Nyears))) #zip(years, years - min(years)) was also possible, but some years might be omitted
year = data['year_code'] = data.year.replace(year_lookup).values

# specifying the variables
y = data.church2
x = data[['gini_net', 'rgdpl']]

#Not sure, maybe it is better to scale x & y variables with log. 
#Could have compared the results in Stan output, ideally.

# Models:

# (1) Random effects model with diffuse priors (uninformative)

re_model = """
data {
  int<lower=0> J;
  int<lower=0> K; 
  int<lower=0> N; 
  int<lower=1,upper=J> country[N];
  int<lower=1,upper=K> year[N];
  matrix[N,2] X;
  vector[N] y;
} 
parameters {
  vector[J] cnt;
  vector[K] yr;
  vector[2] B;
  real mu_cnt;
  real mu_yr;
  real<lower=0,upper=100> sigma_cnt;
  real<lower=0,upper=100> sigma_yr;
  real<lower=0,upper=100> sigma_y;
} 
transformed parameters {

  vector[N] y_hat;

  for (i in 1:N)
    y_hat[i] = cnt[country[i]] + yr[year[i]] + X[i] * B;
}
model {
  sigma_cnt ~ uniform(0, 100);
  cnt ~ normal (mu_cnt, sigma_cnt);
  
  sigma_yr ~ uniform(0, 100);
  yr ~ normal (mu_yr, sigma_yr);
  
  B ~ normal (0, 10);

  sigma_y ~ uniform(0, 100);
  y ~ normal(y_hat, sigma_y);
}
"""

re_data = {'N': len(y),
           'J': Ncountries,
           'country': country+1,
           'K': Nyears,
           'year': year+1,
           'X': x,
           'y': y}

re_fit = pystan.stan(model_code=re_model, data=re_data, iter=1000, chains=2)

# (2) Random effects model with highly informative B (being distorted)

B_model = """
data {
  int<lower=0> J;
  int<lower=0> K; 
  int<lower=0> N; 
  int<lower=1,upper=J> country[N];
  int<lower=1,upper=K> year[N];
  matrix[N,2] X;
  vector[N] y;
} 
parameters {
  vector[J] cnt;
  vector[K] yr;
  vector[2] B;
  real mu_cnt;
  real mu_yr;
  real<lower=0,upper=100> sigma_cnt;
  real<lower=0,upper=100> sigma_yr;
  real<lower=0,upper=100> sigma_y;
} 
transformed parameters {

  vector[N] y_hat;

  for (i in 1:N)
    y_hat[i] = cnt[country[i]] + yr[year[i]] + X[i] * B;
}
model {
  sigma_cnt ~ uniform(0, 100);
  cnt ~ normal (mu_cnt, sigma_cnt);
  
  sigma_yr ~ uniform(0, 100);
  yr ~ normal (mu_yr, sigma_yr);
  
  B ~ normal (25, 5);

  sigma_y ~ uniform(0, 100);
  y ~ normal(y_hat, sigma_y);
}
"""

# Guessing some far and informative B, without seeing previous output.

B_data = {'N': len(y),
          'J': Ncountries,
          'country': country+1,
          'K': Nyears,
          'year': year+1,
          'X': x,
          'y': y}

B_fit = pystan.stan(model_code=B_model, data=B_data, iter=1000, chains=2)

# Conclusion (as expected):
# Comparing to the first model, I expect the second model to be highly 
# distorted by the given informative prior of B, which should be reflected 
# in its output. Moreover, the variance should significantly reduce.



# I hope, the code runs :), tried to minimize possible bugs.

# The end.
