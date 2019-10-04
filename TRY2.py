# USAGE
#linked to mysql
#tested-working good -11/03/2018
#before running create database using insert commmands
#insert into e(id,name,bookid,bookname,issuedate,returndate,status)values("14BEC0***","652837659","9781904994862",
#                                                                         "dip","22/07/2017","15/08/2017","1");
#insert into e(id,name,bookid,bookname,issuedate,returndate,status)values("14BEC0***","qwertyu","005150024163",
#                                                                         "dip","22/12/2017","15/01/2018","1");

#set date properly by following command
#sudo date -s"Mon aug 12 20:14:11 UTC 2014"

# python detect_barcode.py --image images/barcode_01.jpg

# import the necessary packages
import timeit
import numpy as np
import argparse
#import cv2
import time
from datetime import date
#from pyzbar.pyzbar import decode
#from PIL import Image
import MySQLdb as m
#import serial
#import types
#import RPi.GPIO as GPIO
from time import sleep
#GPIO.setmode(GPIO.BOARD)
#pin=37
#GPIO.setup(pin,GPIO.IN)
db=m.connect("localhost","root","ritesh","cap")
cur=db.cursor()
def fine(d1,m1,y1,d2,m2,y2):
    x=0
    d=date(y1,m1,d1)
    e=date(y2,m2,d2)
    delta=e-d
    x=delta.days
    return x

# construct the argument parse and parse the arguments


    #ap = argparse.ArgumentParser()
    #ap.add_argument("-i", "--image", required = True, help = "path")
    #args = vars(ap.parse_args())


while True:
   	a=raw_input("Enter bookid")
        sql="select id,name,bookname,issuedate,returndate from d where bookid='%s' and status='1';" %a
        cur.execute(sql)
        result=cur.fetchall()
        if result==():
                print "None"
        else:
            for row in result:
                    Id=row[0]
                    name=row[1]
                    bookname=row[2]
                    issuedate=row[3]
                    returndate=row[4]
                    #delay=row[5]
                    #location=row[6]
            print "Registration Number='%s'"%Id,
            print "Name='%s'"%name,
            print "Book Name='%s'"%bookname
            #print "Delay='%s'"%delay
            #print "location='%s'"%location
            q=1
            l=[]
            l=returndate.split('/')
            now=time.strftime("%d/%m/%Y")
            k=[]
            k=now.split("/")
            j=map(int,k)
            p=map(int,l)
            g=fine(p[0],p[1],p[2],j[0],j[1],j[2])
             
            if g<0:
                    g=0
            print "Fine=Rs.%s"%g
            
            sql="update d set status='0' where bookid='%s';"%a
            print "Book returned successfully"
            try:
                                    
                    cur.execute(sql)
                    db.commit()
                                    
            except Exception as e:
                    print "Some error occured:",e
                    db.rollback()       

    #sleep(1)
                

