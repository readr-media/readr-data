import math
import string
import re

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier  ## decision tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from xgboost import XGBClassifier
import xgboost

import pandas as pd
from datetime import datetime

pd.options.mode.chained_assignment = None
xgbc = XGBClassifier()

zonble = pd.read_csv("./11_users_train2.csv")
zonble = zonble.dropna(subset=['corpus'])
zonble.head()

print(zonble.groupby("corpus").count())
x = zonble[[
    "follower_count","following_count","account_language","tweet_count","mention","0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","tweet_ratio"
    #"user_reported_location","follower_count","following_count","account_creation_date","account_language","tweet_language","tweet_text","tweet_time","tweet_client_name","in_reply_to_userid","in_reply_to_tweetid","quoted_tweet_tweetid","is_retweet","retweet_userid","retweet_tweetid","latitude","longitude","quote_count","reply_count","like_count","retweet_count","hashtags","urls","user_mentions"
]].values
    #"user_reported_location","follower_count","following_count","is_retweet","account_language","tweet_language","tweet_client_name"
y = zonble["corpus"].values
X_train, X_valid, Y_train, Y_valid = train_test_split(x, y, test_size =0.5, random_state=None, shuffle=True, stratify=y)  ## 一般如果測試資料集超過1000筆就可以了，所以比率不會設這麼高
print(X_train.shape)  ## (445, 17)
print(X_valid.shape)  ## (446, 17)
print(Y_train.shape)  ## (445,)
print(Y_valid.shape)  ## (446,)

# 定義函式，輸入分類器，輸出準確率
def get_accuracy(clf):
    clf = clf()
    clf = clf.fit(X_train, Y_train)
    y_pred = clf.predict(X_valid)
    return (str(sum(Y_valid == y_pred)/Y_valid.shape[0]))

print('DecisionTree: ', get_accuracy(DecisionTreeClassifier))
print('RandomForest: ', get_accuracy(RandomForestClassifier))
print('AdaBoost: ', get_accuracy(AdaBoostClassifier))  ## Boosting的演算法
print('XGB: ', get_accuracy(XGBClassifier))


eval_set = [(x, y)]
xgbc.fit(x, y, eval_metric="error", eval_set=eval_set, verbose=True)

print(xgbc.score(x, y))
