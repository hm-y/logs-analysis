#!/usr/bin/env python

# "Database code" for the DB Newsdata.

import psycopg2

DBNAME = "news"

# QUESTION 1
# Retrieve data for the question 1

query1 = '''
    select title, views
    from articles join view_articles
    on view_articles.path = '/article/' || articles.slug
    order by views desc limit 3;
'''

# QUESTION 2
# Retrieve data for the question 1

query2 = '''
    select name, sum(views) as popularity
	from authors
    join articles on authors.id = articles.author
    join view_articles
    on view_articles.path = '/article/' || articles.slug
    group by authors.name order by popularity desc;
'''

# QUESTION 3
# Retrieve data for the question 1

query3 = '''
    select time, err_pct
    from err_percentages
    where err_pct > 1;
'''

# The query method to execute the right query for the answer


def get_query_results(query):
    '''Apply the chosen query, retrieve and return the data'''
    db = psycopg2.connect(database="news")
    c = db.cursor()
    if query == 1:
        c.execute(query1)
    elif query == 2:
        c.execute(query2)
    elif query == 3:
        c.execute(query3)
    result = c.fetchall()
    db.close()
    return result

# The method to print data from the database
# depending on the user choice


def get_data(question):
    '''Print the retrieved data for the user choice'''
    results = get_query_results(question)
    for t, item in enumerate(results, 1):
        if question == 1:
            print str(t)+" - "+item[0]+"  ---  "+str(item[1])+" views"
        if question == 2:
            print str(t)+" - "+str(item[0])+"  ---  "+str(item[1])+" views"
        if question == 3:
            print '{0}. {1:%B %d, %Y} --- {2:.2f}% errors'\
                .format(t, item[0], item[1])

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
    try:
        request = raw_input('What data do you want: ')

        print('--------------------------------------------------------')
        print('--------------------------------------------------------')

        if (request is '1') or (request is '2') or (request is '3'):
            if request is '1':
                print('-----------the most popular three articles------------')
            elif request is '2':
                print('-----------the most popular article authors-----------')
            elif request is '3':
                print('-----------the days with the errors more than 1%------')
            print('--------------------------------------------------------')
            get_data(eval(request))
        elif request is '4':
            exit()
        else:
            print('---------------Please, pick a correct option--------------')

    except KeyboardInterrupt:
        exit()
