# "Database code" for the DB Newsdata.

import psycopg2

DBNAME = "news"

# QUESTION 1
# Retrieve data for the question 1


def top_articles():
	"""Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    sql = '''
        select title, views
        from articles join view_articles
        on view_articles.path like '%' || articles.slug || '%'
        order by views desc limit 3;
    '''
    c.execute(sql)
    posts = c.fetchall()
    db.close()
    return posts

# QUESTION 2
# Retrieve data for the question 1


def top_authors():
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    sql = '''
        select name, count(*) as popularity
        from articles join authors on articles.author = authors.id
        join view_articles
        on view_articles.path like '%' || articles.slug || '%'
        group by authors.name order by popularity desc limit 3;
    '''
    c.execute(sql)
    posts = c.fetchall()
    db.close()
    return posts

# QUESTION 3
# Retrieve data for the question 1


def failure_days():
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    sql = '''
        select date, percentage
        from percentage_of_errors_by_day
        where percentage > 1;
    '''
    c.execute(sql)
    posts = c.fetchall()
    db.close()
    return posts

# The method to print data from the database
# depending on the user choice


def get_data(question):
    t = 1
    if question == 1:
        for article in top_articles():
            print str(t)+" - "+article[0]+"  ---  "+str(article[1])+" views"
            t += 1

    elif question == 2:
        for author in top_authors():
            print str(t)+" - "+str(author[0])+"  ---  "+str(author[1])+" views"
            t += 1

    elif question == 3:
        for day in failure_days():
            print str(t)+" - "+str(day[0])+"  ---  "
            +str(round(day[1], 2))+"% errors"
            t += 1

# Instructions and results to the user

while True:
    print('--------------------------------------------------------')
    print('--------------------------------------------------------')
    print('1. What are the most popular three articles of all time?')
    print('2. Who are the most popular article authors of all time?')
    print('3. On which days did more than 1% of requests lead to errors?')
    print('4. Exit')
    print('--------------------------------------------------------')
    print('--------------------------------------------------------')
    request = input('What data do you want: ')

    print('--------------------------------------------------------')
    print('--------------------------------------------------------')
    if (request == 1) or (request == 2) or (request == 3):
        if request == 1:
            print('-----------the most popular three articles------------')
        elif request == 2:
            print('-----------the most popular article authors-----------')
        elif request == 3:
            print('-----------the days with the errors more than 1%------')
        print('--------------------------------------------------------')
        get_data(request)
    elif request == 4:
        exit()
    else:
        print('---------------Please, pick a correct option--------------')
