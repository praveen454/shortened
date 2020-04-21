from django.shortcuts import render
from django.http import HttpResponse
from .models import ShortendUrl
from pyshorteners import Shortener
import psycopg2

# Create your views here.

def home(request):

    
    conn = None
    try:
        conn = getConnection()
        cur = conn.cursor()
        cur.execute("SELECT longurl,shorturl FROM urlmapping_shortendurl")
        rows = cur.fetchall()
        shortenedUrlList = []
        for row in rows:
            s = ShortendUrl()
            s.longurl = row[0]
            s.shorturl = row[1]
            shortenedUrlList.append(s)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return render(request, 'shortenedurl.html', {'shortenedUrlList': shortenedUrlList})

def urlshortner(request):
    conn = None
    try:
        conn = getConnection()
        cur = conn.cursor()
        url = request.POST['longUrl']
        s = Shortener(timeout=5)
        shorturl = s.tinyurl.short(url)
        cur.execute("SELECT max(id) FROM urlmapping_shortendurl")
        row = cur.fetchone()
        idval = int(row[0]) + 1
        print(idval)
        postgres_insert_query = """ INSERT INTO urlmapping_shortendurl (id, longurl, shorturl) VALUES (%s,%s,%s)"""
        record_to_insert = (idval, url, shorturl)
        cur.execute(postgres_insert_query, record_to_insert)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return render(request, 'shortenedurl.html', {'created': 'Added Successfully'})


def getConnection():
    conn = psycopg2.connect(user = "postgres",
                                  password = "praveen",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "shortendurl")
    return conn
