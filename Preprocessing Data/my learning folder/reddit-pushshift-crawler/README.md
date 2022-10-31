# Reddit Crawler

## Requirements
* `python 3.8+`
* `requests==2.28.1`
* `praw==7.6.0`

To install `requests` and `praw`, run the following:
```bash
pip install requests praw
```

## Configuring `praw.ini`
Before running any scripts, the `praw.ini` should be populated with the client's id and secret.

Copy the `praw.ini.example` file and create a `praw.ini` file in the same directory.
[Register a reddit application](https://www.integromat.com/en/help/app/reddit) and edit the `praw.ini` file.
The `praw.ini` file should have the form of: (random example)
```plain
[bot]
client_id=myclientidblahblah
client_secret=12l149x8cVaLsdfjk
```

## Overview of the Crawling Process
1. Collect post data from pushshift into the filesystem
2. Process post and comment data into csv files

### 1. Collecting post data from pushshift

```shell

python3 pushshift.py --cache both --after 2022-08-28 --before 2022-09-28 --subreddit wallstreetbets TSLA

```


### 2. Collecting post data from pushshift

* go to the folder convert

## change json to csv and also vice versa

* [link: csv to json](https://retool.com/utilities/convert-csv-to-json)

* [link: json to csv](https://www.convertcsv.com/json-to-csv.htm)
