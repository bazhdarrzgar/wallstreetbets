## Requirement

* IEX Finance API Premium [Token](https://iexcloud.io)

* Some Learning About [Pushshift API](https://reddit-api.readthedocs.io/en/latest/) you can learn it below

* Also Requirement package (library) that provide in each file

## What is Pushshift API ?

* Pushshift is a big-data storage and analytics project started and maintained by Jason Baumgartner [(/u/Stuck_In_the_Matrix)](https://www.reddit.com/u/Stuck_In_the_Matrix/).
<br>

* **When should I use Pushshift data instead of solely using the reddit API ?**
When you want to:

    - analyze large quantities of reddit data

    - grab data for a specific date range in the past

    - e.g. [submissions to r/news in July 2018](https://api.pushshift.io/reddit/submission/search/?subreddit=news&after=2018-07-01&before=2018-08-01).

    - search for comments

    - e.g. [comments in r/news containing the word 'phone'](https://api.pushshift.io/reddit/comment/search/?subreddit=news&q=phone)

    - aggregate data

    - e.g. [number of submissions to r/technology and r/news containing 'phone' in September 2018](https://api.pushshift.io/reddit/submission/search/?subreddit=technology,news&aggs=subreddit&q=phone&size=0&after=2018-09-01&before=2018-10-01)

    - exclude authors, `&author=!a,!b` - excludes authors a and b

    - e.g. [number of comments in r/technology and r/news containing 'submitting' in September 2018, not including the author 'automoderator'](https://api.pushshift.io/reddit/comment/search/?subreddit=technology,news&aggs=subreddit&q=submitting&size=0&after=2018-09-01&before=2018-10-01&author=!automoderator)
<br>

* **What kind of data does the API give me ?**

    - The Pushshift API serves a copy of reddit objects, the data is copied into Pushshift at the time it is posted to reddit. the data can be `scores` and other meta data such as edits to a submission's `selftext` or a comment's `body`.
    - There are two main endpoints used to search all publicly available comments and submissions on Reddit:

        + /reddit/search/comment
        
        + /reddit/search/submission
<br>

* **Where can I access the raw data ?**

    - https://files.pushshift.io/ - raw file storage

    - BigQuery, uploaded by fhoffa

    - [reddit_posts](https://console.cloud.google.com/bigquery?p=fh-bigquery&d=reddit_posts&page=dataset)

    - [reddit_comments](https://console.cloud.google.com/bigquery?p=fh-bigquery&d=reddit_comments&page=dataset)

    - https://github.com/pushshift/api - api for reddit data (this will be updated soon with new features and documentation)

    - https://github.com/dmarx/psaw - a 3rd party API wrapper by [/u/shaggorama](https://www.reddit.com/u/shaggorama/)

    - https://elastic.pushshift.io/rs/submissions/_search - ES queries

    - Example usage in [redditsearch.io](https://redditsearch.io/pushshift.js) and [removeddit](https://github.com/JubbeArt/removeddit/blob/master/src/api/pushshift/index.js)
<br>

* **Are there some scripts for processing raw data ?**

    - Yes, try searching this sub or search github for pushshift

    - [Reading .zst files in chunks](https://www.reddit.com/r/pushshift/comments/ajmcc0/information_and_code_examples_on_how_to_use_the/ef012vk/)
<br>

* **Using Code Style**
    - there is a good documentation about how to use pushshift api for reddit you can read about from [www.jcchouinard.com](https://www.jcchouinard.com/how-to-use-reddit-api-with-python/) by BY JEAN-CHRISTOPHE-CHOUINARD
    - also if you want just test it for your self visit [github.com/pushshift](https://github.com/pushshift/api/tree/master/api)
<br>

* **Some Example**
  * **Searching Comments:** Search for the most recent comments mentioning the word "science"
        - https://api.pushshift.io/reddit/search/comment/?q=science
<br>

  * **Search parameters for comments:**

    * There are numerous additional parameters that can be used when performing a comment search. Let's go over them and provide examples for each.
  
    | Parameter | Description | Default | Accepted Values |
    | ------ | ------ | ------- | ------ |
    | q | Search term. | N/A | String / Quoted String for phrases |
    | ids | Get specific comments via their ids | N/A | Comma-delimited base36 ids |
    | size | Number of results to return | 25 | Integer <= 500 |
    | fields | One return specific fields (comma delimited) | All Fields Returned | string or comma-delimited string |
    | sort | Sort results in a specific order | "desc" | "asc", "desc" |
    | sort_type | Sort by a specific attribute | "created_utc" | "score", "num_comments", "created_utc" |
    | aggs | Return aggregation summary | N/A | ["author", "link_id", "created_utc", "subreddit"] |
    | author | Restrict to a specific author | N/A | String |
    | subreddit | Restrict to a specific subreddit | N/A | String |
    | after | Return results after this date | N/A | Epoch value or Integer + "s,m,h,d" (i.e. 30d for 30 days) |
    | before | Return results before this date | N/A | Epoch value or Integer + "s,m,h,d" (i.e. 30d for 30 days) |
    | frequency | Used with the aggs parameter when set to created_utc | N/A | "second", "minute", "hour", "day" |
    | metadata | display metadata about the query | false | "true", "false" |
<br>

  * **Getting comments based on id:** Retrieve three comments using their base 36 id values
        - https://api.pushshift.io/reddit/comment/search?ids=dlrezc8,dlrawgw,dlrhbkq
<br>
  * **Using the subreddit parameter:**Search for the most recent comments mentioning the word "science" within the subreddit /r/askscience
        - https://api.pushshift.io/reddit/search/comment/?q=science&subreddit=askscience
<br>

  * **Using the sort and size parameters:** Search for the most recent comments mentioning the word "science" within the subreddit /r/askscience
        - https://api.pushshift.io/reddit/search/comment/?q=science&subreddit=askscience&sort=asc&size=1
<br>

  * **Using the before and after parameters:**
    - Search the subreddit `/r/askhistorians` for comments mentioning Rome within the past 30 days
      - https://api.pushshift.io/reddit/search/comment/?q=rome&subreddit=askhistorians&after=30d
    - Search all subreddits for the term "Trump" and return comments made between 2 and 4 days ago
      - https://api.pushshift.io/reddit/search/comment/?q=trump&after=4d&before=2d&sort=asc
<br>

  * **Using the fields parameter:** Search all subreddits for the term "government" and return comments with only the body and author keys
    - https://api.pushshift.io/reddit/search/comment/?q=government&size=150&fields=body,author
<br>

  * **Using the author parameter:** Search all subreddits and get the first 100 comments ever made by the user /u/MockDeath
    - https://api.pushshift.io/reddit/search/comment/?author=MockDeath&sort=asc&size=100
<br>

  * **Using the time frequency (created_utc) aggregation:** Create a time aggregation using the term trump to show the number of comments mentioning trump each hour over the past 7 days
    - https://api.pushshift.io/reddit/search/comment/?q=trump&after=7d&aggs=created_utc&frequency=hour&size=0 
<br>

  * **Using the subreddit aggregation:** Create a subreddit aggregation using the term trump to show the top subreddits mentioning trump over the past 7 days
    - https://api.pushshift.io/reddit/search/comment/?q=trump&after=7d&aggs=subreddit&size=0
<br>

  * **Using the submission (link_id) aggregation** Show submissions made within the past 24 hours that mention trump often in the comments
    - https://api.pushshift.io/reddit/search/comment/?q=trump&after=24h&aggs=link_id&size=0
<br>

  * **Using the author aggregation:** Show the top authors mentioning the term "Trump" over the past 24 hours
    - https://api.pushshift.io/reddit/search/comment/?q=trump&after=24h&aggs=author&size=0
<br>

  * **Combining multiple aggregations at once:** Show aggregations for authors, submissions, subreddits and time frequency for the term "Trump" over the past 24 hours
    - https://api.pushshift.io/reddit/search/comment/?q=trump&after=24h&aggs=author,link_id,subreddit,created_utc&frequency=hour&size=0
<br>

  * **Searching Submissions:** Search for the most recent submissions mentioning the word "science"
    - https://api.pushshift.io/reddit/search/submission/?q=science
<br>

  * **Search parameters for submissions**

    | Parameter | Description | Default | Accepted Values |
    | ----- | ----- | ----- | ----- |
    | ids | Get specific submissions via their ids | N/A | Comma-delimited base36 ids |
    | q | Search term. Will search ALL possible fields | N/A | String / Quoted String for phrases |
    | q:not | Exclude search term.  Will exclude these terms | N/A | String / Quoted String for phrases |
    | title | Searches the title field only | N/A | String / Quoted String for phrases |
    | title:not | Exclude search term from title.  Will exclude these terms | N/A | String / Quoted String for phrases |
    | selftext | Searches the selftext field only | N/A | String / Quoted String for phrases |
    | selftext:not | Exclude search term from selftext.  Will exclude these terms | N/A | String / Quoted String for phrases |
    | size | Number of results to return | 25 | Integer <= 500 |
    | fields | One return specific fields (comma delimited) | All Fields | String or comma-delimited string (Multiple values allowed) |
    | sort | Sort results in a specific order | "desc" | "asc", "desc" |
    | sort_type | Sort by a specific attribute | "created_utc" | "score", "num_comments", "created_utc" |
    | aggs | Return aggregation summary | N/A | ["author", "link_id", "created_utc", "subreddit"] |
    | author | Restrict to a specific author | N/A | String or comma-delimited string (Multiple values allowed) |
    | subreddit | Restrict to a specific subreddit | N/A | String or comma-delimited string (Multiple values allowed) |
    | after | Return results after this date | N/A | Epoch value or Integer + "s,m,h,d" (i.e. 30d for 30 days) |
    | before | Return results before this date | N/A | Epoch value or Integer + "s,m,h,d" (i.e. 30d for 30 days) |
    | score | Restrict results based on score | N/A | Integer or > x or < x (i.e. score=>100 or score=<25) |
    | num_comments | Restrict results based on number of comments | N/A | Integer or > x or < x (i.e. num_comments=>100) |
    | over_18 | Restrict to nsfw or sfw content | both allowed | "true" or "false" |
    | is_video | Restrict to video content | both allowed | "true" or "false" |
    | locked | Return locked or unlocked threads only | both allowed | "true" or "false" |
    | stickied | Return stickied or unstickied content only | both allowed | "true" or "false" |
    | spoiler | Exclude or include spoilers only | both allowed | "true" or "false" |
    | contest_mode | Exclude or include content mode submissions | both allowed | "true" or "false" |
    | frequency | Used with the aggs parameter when set to created_utc | N/A | "second", "minute", "hour", "day" |
    | metadata | display metadata about the query | false | ["true", "false"] |
<br>

* **Get all comment ids for a particular submission:** Retrieve all comment ids for a submission object

    - https://api.pushshift.io/reddit/submission/comment_ids/6uey5x
<br>

* **List Of EndPoints**
  
    | Endpoint | Description | Status | 
    | ------ | ------ | ------- |
    | /reddit/search/comment/ | Search Reddit Comments | Active |
    | /reddit/search/submission/ | Search Reddit Submissions | Active |
    | /reddit/submission/comment_ids/{base36-submission-id} | Retrieve comment ids for a submission object | Active |
    | /reddit/analyze/user/{author-name} | Analyze a Reddit user's activity | In Development |
    | /reddit/term/frequency/{term} | Analyze a term based on activity |  In Development |
    | /reddit/search/all/ | Search Both Comment and Submissions | In Development |
    | /reddit/trending/people | Find out who is trending on Reddit | In Development |
    | /reddit/search/links | Find relevent links being shared on Reddit | In Development |

