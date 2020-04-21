"""
INTL 550 - HW3 (Hierarchical Bayesian Analysis)
Name : Shukhrat Khuseynov
ID   : 0070495

Comments: 
I could install pystan, but it does not work, possibly due to my hardware 
limitations (particularly, low RAM: Spyder alone is heavy enough for my laptop). 
Could not install pystan to IDLE.
    
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
year_lookup = dict(zip(years, range(Nyears))) # zip(years, years - min(years)) was also possible, but some years might be omitted
year = data['year_code'] = data.year.replace(year_lookup).values

# specifying the variables
church2 = data.church2
gini_net = data.gini_net
rgdpl = data.rgdpl

re_model = """
data {
  int<lower=0> J;
  int<lower=0> K; 
  int<lower=0> N; 
  int<lower=1,upper=J> country[N];
  int<lower=1,upper=K> year[N];
  vector[N] x1;
  vector[N] x2;
  vector[N] y;
} 
parameters {
  vector[J] cnt;
  vector[K] yr;
  real b1;
  real b2;
  real mu_cnt;
  real mu_yr;
  real<lower=0,upper=100> sigma_cnt;
  real<lower=0,upper=100> sigma_yr;
  real<lower=0,upper=100> sigma_y;
} 
transformed parameters {

  vector[N] y_hat;

  for (i in 1:N)
    y_hat[i] = cnt[country[i]] + yr[year[i]] + x1[i] * b1 + x2[i] * b2;
}
model {
  sigma_cnt ~ uniform(0, 100);
  cnt ~ normal (mu_cnt, sigma_cnt);
  
  sigma_yr ~ uniform(0, 100);
  yr ~ normal (mu_yr, sigma_yr);
  
  
  b1 ~ normal (0, 1);
  b2 ~ normal (0, 1);

  sigma_y ~ uniform(0, 100);
  y ~ normal(y_hat, sigma_y);
}
"""

re_data = {'N': len(x),
           'J': Ncountries,
           'country': country+1,
           'K': Nyears,
           'year': year+1,
           'x1': gini_net,
           'x2': rgdpl,
           'y': church2}

re_fit = pystan.stan(model_code=re_model, data=re_data, iter=1000, chains=2)
