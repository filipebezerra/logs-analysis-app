# Logs Analysis

Logs Analysis application is a project part of Nanodegree Full Stack Web Developer at Udacity and contains all the required materials.

 ## Project structure
 
 This application was written using Python 2.7.12.
 
 Below is demonstrated how the project is structured. The source code lives inside ```log-analysis``` folder and contains primarily the following scripts:
 1. ```repository.py``` which contains the code that connects with the database and retrieve the data
 2. ```application.py``` which contains the code that prints to the console and saves the information retrieved from the database to the ```report.txt``` file 
 
 ```
 logs-analysis-app
│   .gitignore
│   README.md
│
└───logs-analysis
        application.py
        report.txt
        repository.py
        __init__.py
 ```
 
 ## Download the source
 
 You can clone this repository using git or you can [download it](https://github.com/full-stack-web-developer-nanodegree/logs-analysis-app/archive/master.zip).
 
 Use the following command to clone using git:
 
 ```bash
git clone https://github.com/full-stack-web-developer-nanodegree/logs-analysis-app.git
```
 
 ## Setup
 
1. Creating the views in the database

    * Connect to the ```news``` database

        ```bash
        psql -d news
        ```

    * Create the views
 
         ```postgresql
         CREATE VIEW most_popular_articles AS
            SELECT
                a.title AS article,
                v.v_count AS a_views
            FROM
                articles AS a,
                (
                    SELECT
                        count(path) AS v_count,
                        substring(path from '%/{1}#"%#"' for '#') AS path
                    FROM log
                        WHERE status LIKE '%200%'
                            AND path LIKE '/article/%'
                    GROUP BY path
                ) AS v
            WHERE a.slug = v.path
            ORDER BY v.v_count desc
            LIMIT 3;
         ```
      
         ```postgresql
        CREATE VIEW most_popular_authors AS
            SELECT
                aut.name AS author,
                sum(vie.v_count) AS a_views
            FROM
                articles AS art,
                authors AS aut,
                (
                    SELECT
                        count(path) AS v_count,
                        substring(path from '%/{1}#"%#"' for '#') AS path
                    FROM log
                        WHERE status LIKE '%200%'
                            AND path LIKE '/article/%'
                    GROUP BY path
                ) AS vie
            WHERE art.slug = vie.path
                AND art.author = aut.id
            GROUP BY aut.name
            ORDER BY a_views desc;
         ```
         
         ```postgresql
        CREATE VIEW failed_requests_above_one_percent AS
            SELECT * FROM (
                SELECT
                    date,
                    ((fail_count::decimal / ok_count::decimal)) AS fail_percent
                FROM (
                        SELECT
                            fails.date,
                            fails.fail_count,
                            oks.ok_count
                        FROM (
                            SELECT
                                date(time) AS date,
                                count(status) AS fail_count
                            FROM log
                                WHERE status LIKE '%404%'
                            GROUP BY date
                            ) AS fails,
                            (
                            SELECT
                                date(time) AS date,
                                count(status) AS ok_count
                            FROM log
                                WHERE status LIKE '%200%'
                            GROUP BY date
                            ) AS oks
                        WHERE fails.date = oks.date
                ) AS fails
            ) AS fails
            WHERE round(100.0 * fail_percent, 2) > 1.00;
         ```
2. Install python packages (may be required)
 
    ```bash
    sudo apt-get install python-psycopg2
    sudo pip install psycopg2
    ```
 
 ## Running the application
 
 Assuming that you're in the root of the project navigate to the ```log-analysis``` folder and run the application:
 
 ```python
python application.py
```
 
 ## Understanding the output
 
 After running the application the analysis will be printed to the console and also to the ```report.txt``` file.
 
 Here is a example of the output:
 
 ```text
1. Three most popular articles

        * "Candidate is jerk, alleges rival" — 338647 views
        * "Bears love berries, alleges bear" — 253801 views
        * "Bad things gone, say good people" — 170098 views

2. Most popular authors

        * Ursula La Multa — 507594 views
        * Rudolf von Treppenwitz — 423457 views
        * Anonymous Contributor — 170098 views
        * Markoff Chaney — 84557 views

3. Days with more than 1% of requests failures

        * July 17, 2016 — 2.32% errors

``` 
