#!/usr/bin/python


from __future__ import print_function

hostname = ''
username = 'web_user'
password = ''
database = 'northwind'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT company_name FROM suppliers LIMIT 10" )

    for company_name in cur.fetchall() :
        print( company_name )


import psycopg2
myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
doQuery( myConnection )
myConnection.close()


