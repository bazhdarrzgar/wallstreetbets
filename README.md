<div align=center>

# **`WallStreetBets Stock Research Posts Classifier`**

</div>

# **`I. Abstract`**

One of the most popular platforms for stocks and financial discussion is a **subreddit** called **WallStreetBets**. We would like to help further democratize stock trading by making the access to insightful stock research easier. Most people already know about the mainstream news outlets, this is why we choose this subreddit, where insightful yet unpopularized research information lay in a sea of memes. We will use the posts on **r/WallStreetBets** as our **dataset** and **aim** to classify them as either valuable or less valuable in order to help any user quickly filter out posts he or she may want to read. This project aims to be particularly useful towards those, such as ourselves, who are interested in **trading** and **investing** in the **stock market**, but have little time to do their own research.

# **`II. Introduction`**

With the influx of retail investors during the **2021** **Coronavirus pandemic** and **GameStop fiasco**, it is more important now than ever for people to educate themselves on investment decisions. The largest financial subreddit, **r/WallStreetBets**, is home to many memes, however, many **DD** posts are also present.

Unlike professional investors, retail investors have very limited time to conduct their own research as they usually have a separate career. In this project, we aim to further democratize stock trading by filtering and classifying stock research such that every regular investor has the opportunity to quickly access them.

We will be able to provide a quick filter on the top research posts as well as a classification on whether any given post may or may not be worth your time to read.

A related work is a website called (SwaggyStocks.com)[SwaggyStocks.com], in which sentiment analysis of the r/**WallStreetBets subreddit** is done and visualized. However, we differ from this as we are not trying to explicitly analyze sentiment of the subreddit. Instead, we will base off our filtering upon historical performance of the stocks each post is discussing.

***NOTE: DD: stands for "Due Diligence". Represents the investigation and research a person has done for a potential investment.***

# **`III. Materials and Methods`**

Our dataset consist of the posts from the **r/WallStreetBets** subreddit. They are extracted by using the **Pushshift** API (we previously used the Reddit **PRAW** API, but due to **API limitations** we had to revamp all our code with Pushshift instead which proved to be more flexible). The **Pushshift** API is able to provide us with a lot of information about a given post such as the **title, score, upvote ratio, author, text, URL, created time, comments and more**. Except for **upvote ratio, score, created time, and number of comments, all other data are textual**.

We also used the **IEX finance** API to obtain financial data. This API provides the **closing price, ticker, financials, cash-flow, volumes of a specific ticker and more**.

## **`Data Preprocessing`**

Upon receiving text data from **Pushshift**, we used **regular expression** to extract tickers from the posts. We used the **IEX finance** API to validate the ticker and get its closing price at the post creation date and present date. To label data, we calculated the growth percentage between these two dates. We set the standard to **6%**, any post above **6%** are labeled **as 1 (good) else 0 (bad)**. We b`elieve if whatever stock a post is talking about has risen **6%**, it is worth taking a look at, plus, this number becomes crucial later in our model training step when splitting training and test sets. It allowed us to avoid data imbalance as we had a perfect split of **50%** of our data as **class 1** and the other **50%** as **class 0**.

These posts are filtered and cleaned with many conditions, some of which you may see in these two functions.( `WallStreetBets-Preprocessing.ipynb` )

![image](https://user-images.githubusercontent.com/59063950/115100523-381fd900-9f0b-11eb-9fd7-a1cc39944389.png)

![image](https://user-images.githubusercontent.com/59063950/115100526-3bb36000-9f0b-11eb-9c94-431ca0c6ea91.png)
