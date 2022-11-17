Many people believed that Reddit's WallStreetBets community was a driving factor in the GameStop short squeeze of January 2021, with some even accusing the subreddit community of market manipulation. I found that there did not exist a causality relationship between the sentiment data and GME's price. However, there did exist one between the total number of comments posted on the daily thread and GME's price. Additionally, the machine learning model trained with the Reddit data was able to predict whether GME's price would go up or down the next day with 100% accuracy over a sample size of open market days. Furthermore, this model outperformed its clone that had the same parameters but was trained without the Reddit data. These findings suggest that WallStreetBets actually did have a significant impact on the stock market. However, it is still presumptuous to call them "market manipulators" and more work would have to be done to determine just how strong their influence over the market truly is.

resource: https://dataspace.princeton.edu/handle/88435/dsp01zs25xc66s




To gather data for the study, comments were scrapped from the subreddit wallstreetbets for a period of four months, Jan 1, 2021, till April 30, 2021. Different sentiment classifiers were, then, applied on a sample of the data to observe the most accurate classifier for the study. The study concluded that the most accurate sentiment classifier was an SVM classifier trained on 80% of Reddit comments. However, when 10-k fold cross validation was preformed, we saw a drop in the accuracy of the SVM classifier, and a rise in the accuracy of the logistic regression classifier. Therefore, the logistic regression classifier with an accuracy of 72.82% was selected for the project. The logistic regression classifier was used to obtain a polarity time series for all the comments present in Reddit. Then, a Granger causality test was applied to the polarity time series and the AMC, GMC rate of return time series. The Granger test shows that sentiment in Reddit’s wallstreetbets appears to “Granger cause” GME and AMC rate of return at different time lags. Moreover, it appears that sentiment on Reddit had more of an impact on GME rate of return than it did with AMC.

Keywords: Machine Learning, SVM, Linear Regression, Stock Market, Reddit, Memes,
Sentiment Analysis, Granger Causality, Cross Validation.

Reference for abstract: https://scholarworks.rit.edu/theses/11061/
Reference for full article: https://scholarworks.rit.edu/cgi/viewcontent.cgi?article=12195&context=theses