"""
INTL 550 - HW4 (A model with bigrams)
Name : Shukhrat Khuseynov
ID   : 0070495

"""

import numpy as np
import pandas as pd

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, RBF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

tt = pd.read_csv('immSurvey.csv')

alphas = tt.stanMeansNewSysPooled
sample = tt.textToSend

# vectorizing by down-weighting frequent words with TF–IDF (including bigrams)
tfbigram = TfidfVectorizer(ngram_range=(1, 2))
X = tfbigram.fit_transform(sample)

#pd.DataFrame(X.toarray(), columns=tfbigram.get_feature_names())

Xtrain, Xtest, ytrain, ytest = train_test_split(X, alphas,random_state=1)

rbf = ConstantKernel(1.0) * RBF(length_scale=1.0)
gpr = GaussianProcessRegressor(kernel=rbf, alpha=1e-8)

gpr.fit(Xtrain.toarray(), ytrain)

# computing posterior predictive mean and covariance
mu_s, cov_s = gpr.predict(Xtest.toarray(), return_cov=True)

# testing correlation between test and mus
np.corrcoef(ytest, mu_s)

# The correlation decreased compared to the initial code, which used only unigrams.

# Some other ML models:

from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=True)
model.fit(Xtrain, ytrain)

ypredict = model.predict(Xtest)
np.corrcoef(ytest, ypredict)

from sklearn.svm import SVR
svr = SVR(kernel='linear', C=10, gamma='auto')
svr.fit(Xtrain, ytrain)

ypredict = svr.predict(Xtest)
np.corrcoef(ytest, ypredict)

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators = 100)
rf.fit(Xtrain, ytrain)

ypredict = rf.predict(Xtest)
np.corrcoef(ytest, ypredict)

from sklearn.neural_network import MLPRegressor
mlp = MLPRegressor(random_state=0, activation='tanh', hidden_layer_sizes=(10,10,5))
mlp.fit(Xtrain, ytrain)

ypredict = mlp.predict(Xtest)
np.corrcoef(ytest, ypredict)


# The end.