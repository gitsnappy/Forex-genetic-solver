import math
import random
import csv
import sys

#buy/sell:
#functionalize comparisons

#buy = 1, sell = 0
BUY_BOT = 1 
RECORD_TRADES = 0

#num_req is number of added up x+y+z traits >= num_req
NUM_REQUIRED =1
NUM_ATTR =4         #must be even
NUM_BOTS =64        #must be divisible by 4
DATA_POINTS = 4834



#random_stuff
ACCEL_THRESHOLD =0.0005
CONVERT_TO_PIPS = 10000 #5 digit
DOLLARS_PER_MINILOT = 0.1
RISK = 0.02
SPREAD = 0.00022

#hourly data constants
YEAR =0
MONTH =1
DAY =2
HOUR =3
DAYOFWEEK=4
OPEN =5
LOW = 6
HIGH = 7
CLOSE = 8
SMA1 =9
SMA2=10
SMA3=11
ACCEL=12

#5 minute constants
YEAR5 =0
MONTH5 =1
DAY5 =2
HOUR5 =3
MINUTE5 =4
DAYOFWEEK5=5
LOW5=6
HIGH5=7

#num of hourly stuff
FILE_HOUR_ITEMS = 13
#num of 5 min stuff
FILE_5MIN_ITEMS = 8

#bot class BUY constants

NUM_BUYTRAITS = 4 #total of traits
BUY_SMA1 = 0
BUY_SMA2 = 1
BUY_SMA3 = 2
BUY_ACCEL =3







