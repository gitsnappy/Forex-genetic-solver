#bot 
#
#trade_on_info
#Is_Buy?
#buy_if_close_above sma
#buy_if_close_below sma

#bot will have random attributes relationg to SMA_5,10,20,ACCEL
#each attribute will have a sign
#
#instead, have list of attributes
    
    #trade_SMA5=0
    #SMA5_pos =0
    #trade_SMA10=0
    #SMA10_pos =0
    #trade_SMA20=0
    #SMA20_pos =0
    
import constants
import bot_class
import math
import random
import csv
import sys
import pdb
import time
import os.path 

#os.chdir('c:\python27\working')
#read files there

from constants import *
from bot_class import *
VPPMULTIPLIER =[] #VALUEPERPIP
VPPMULTIPLIER.append(0)
VPPMULTIPLIER[0] = 1 #0 EURUSD #look at MarketInfo() source code


def mix(Bot_list):

#create children
    yy= 0
    xx = 0 #child num
    for yy in range (NUM_BOTS/4):
        #for each attribute
        atr=0
        #buy
        #trade_attributes
        #attribute_signs
        #parent1,parent2
        #half of genes from par1, half from par2
        #randomly select which genes are taken
        iii=0
        assn = []   #must have even number of attributes
        for aaa in range (NUM_ATTR):
            assn.append(aaa)

        random.shuffle(assn)
        #child 1, gets attributes from first parent
        for atr in range(NUM_ATTR/2):
            
            #converts to string, to int 
            #sys.exit()<F5>
            Bot_list[xx].trade_attributes[assn[atr]] = Parent_list[yy].trade_attributes[assn[atr]]
            Bot_list[xx].attribute_signs[assn[atr]] =  Parent_list[yy].attribute_signs[assn[atr]]
            
        #1, attr 2nd parent
        for atr in range (NUM_ATTR/2,NUM_ATTR):
            Bot_list[xx].trade_attributes[assn[atr]] = Parent_list[yy+1].trade_attributes[assn[atr]]
            Bot_list[xx].attribute_signs[assn[atr]] =  Parent_list[yy+1].attribute_signs[assn[atr]]
            
        xx+=1
        #child 2
        atr =0
        random.shuffle(assn)    
        for atr in range(NUM_ATTR/2):        
            Bot_list[xx].trade_attributes[assn[atr]] = Parent_list[yy].trade_attributes[assn[atr]]
            Bot_list[xx].attribute_signs[assn[atr]] =  Parent_list[yy].attribute_signs[assn[atr]]
            
        for atr in range(NUM_ATTR/2,NUM_ATTR):
            Bot_list[xx].trade_attributes[assn[atr]] = Parent_list[yy+1].trade_attributes[assn[atr]]
            Bot_list[xx].attribute_signs[assn[atr]] =  Parent_list[yy+1].attribute_signs[assn[atr]]
            
        xx+=1
        #child 3
        atr =0
        random.shuffle(assn)    
        for atr in range(NUM_ATTR/2):        
            Bot_list[xx].trade_attributes[assn[atr]] = Parent_list[yy].trade_attributes[assn[atr]]
            Bot_list[xx].attribute_signs[assn[atr]] =  Parent_list[yy].attribute_signs[assn[atr]]
            
        for atr in range(NUM_ATTR/2,NUM_ATTR):
            Bot_list[xx].trade_attributes[assn[atr]] = Parent_list[yy+1].trade_attributes[assn[atr]]
            Bot_list[xx].attribute_signs[assn[atr]] =  Parent_list[yy+1].attribute_signs[assn[atr]]
            
        atr=0
        xx+=1
        #child 4
        random.shuffle(assn)    
        for atr in range(NUM_ATTR/2):        
            Bot_list[xx].trade_attributes[assn[atr]] = Parent_list[yy].trade_attributes[assn[atr]]
            Bot_list[xx].attribute_signs[assn[atr]] =  Parent_list[yy].attribute_signs[assn[atr]]
            
        for atr in range(NUM_ATTR/2,NUM_ATTR):
            Bot_list[xx].trade_attributes[assn[atr]] = Parent_list[yy+1].trade_attributes[assn[atr]]
            Bot_list[xx].attribute_signs[assn[atr]] =  Parent_list[yy+1].attribute_signs[assn[atr]]
            
        xx+=1
        yy+=1 #only do each pair once
#new children created.
def reverse_numeric(x, y):
        return y - x
#allows sorted from high to low


def getBalance(obj) :
    return obj.Balance

def print_balances(Bot_list):
    
    max = 0
    sol = 0
    x = 0
    for x in range(NUM_BOTS):
        if  Bot_list[x].Balance >max:
            max = Bot_list[x].Balance
            sol = x
        print(Bot_list[x].Balance)
        #print(Bot_list[x].numoftrades)
    
    print "atributes", Bot_list[sol].trade_attributes
    print "signs", Bot_list[sol].attribute_signs

    if RECORD_TRADES ==1:
        write_trades(sol)


def write_trades(i):
    with open('trade_list', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',lineterminator='\n')
        #,quotechar='|', quoting=csv.QUOTE_MINIMAL
        abc =0
        for abc in range(Bot_list[i].numoftrades):        
            writer.writerow([Bot_list[i].Trade_List[abc].open_date.year,
                            Bot_list[i].Trade_List[abc].open_date.month,
                            Bot_list[i].Trade_List[abc].open_date.day,
                            Bot_list[i].Trade_List[abc].open_date.hour,
                            Bot_list[i].Trade_List[abc].open_date.dayofweek,
                            Bot_list[i].Trade_List[abc].close_date.year,
                            Bot_list[i].Trade_List[abc].close_date.month,
                            Bot_list[i].Trade_List[abc].close_date.day,
                            Bot_list[i].Trade_List[abc].close_date.hour,
                            Bot_list[i].Trade_List[abc].close_date.dayofweek,
                            Bot_list[i].Trade_List[abc].open,
                            Bot_list[i].Trade_List[abc].close,
                            Bot_list[i].Trade_List[abc].stop,
                            Bot_list[i].Trade_List[abc].target,
                            Bot_list[i].Trade_List[abc].pips,
                            Bot_list[i].Trade_List[abc].profit
                            ])
 




def check_both_hit(list,x):
    #function returns 1 if both target and stop hit
    if BUY_BOT ==1:
        if float(list[HIGH]) >= Bot_list[x].Target and float(list[LOW]) <= Bot_list[x].Stop:
            return 1
        return 0
    else:
        if float(list[LOW]) <= Bot_list[x].Target and float(list[HIGH]) >= Bot_list[x].Stop:
            return 1
        return 0
def hit_stop(list,x):
    if BUY_BOT ==1:
        if float(list[LOW]) <= Bot_list[x].Stop:
            return 1
        return 0
    else:
        if float(list[HIGH]) >= Bot_list[x].Stop:
            return 1
        return 0
def hit_target(list,x):
    if BUY_BOT ==1:
        if float(list[HIGH]) >= Bot_list[x].Target:
            return 1
        return 0
    else:
        if float(list[LOW]) <= Bot_list[x].Target:
            return 1
        return 0


def hit_stop5(list2,x):
    if BUY_BOT ==1:
        if float(list2[LOW]) <= Bot_list[x].Stop:
            return 1
        return 0
    else:
        if float(list2[HIGH]) >= Bot_list[x].Stop:
            return 1
        return 0
def hit_target5(list2,x):
    if BUY_BOT ==1:
        if float(list2[HIGH]) >= Bot_list[x].Target:
            return 1
        return 0
    else: 
        if float(list2[LOW]) <= Bot_list[x].Target:
            return 1
        return 0


def set_entry_price(list,x):
    if BUY_BOT ==1:
        Bot_list[x].Buy_Price = float(list[CLOSE])+SPREAD       
        Bot_list[x].In_Trade =1
    else:
        Bot_list[x].Sell_Price = float(list[CLOSE])-SPREAD       
        Bot_list[x].In_Trade =1 

def close_at_target(x,list,whichlist):
    if BUY_BOT ==1:
        Bot_list[x].Sell_Price=Bot_list[x].Target    
    else:
        Bot_list[x].Buy_Price=Bot_list[x].Target
    Bot_list[x].close_trade(list,whichlist)

def close_at_stop(x,list,whichlist):
    if BUY_BOT ==1:
        Bot_list[x].Sell_Price=Bot_list[x].Stop        
    else:
        Bot_list[x].Buy_Price=Bot_list[x].Stop
    Bot_list[x].close_trade(list,whichlist)
def open_file_and_trade(list):
    with open('togowith5min') as f:
        reader = csv.reader(f)    
        y=0
        for y in range (DATA_POINTS):
            #get values
            list = reader.next()
            x=0
            for x in range (NUM_BOTS):                            
                manage_trade(x,list,y)                      
                look_for_trade(x,list)

def manage_trade(x,list,y):
    if Bot_list[x].In_Trade ==1:                        
            #if both stop and target hit, check 5 minute
            if  check_both_hit(list,x) ==1:
                #check 5 minute to see which hit first
                
                #get hour of hour file, match it with corresponding entry in 5 minute file
                myhour =int(list[HOUR])              
                
                #trade closed within this hour, so find when.
                check_5min(list2,y,myhour,x)
                             
            elif hit_stop(list,x):                          
                close_at_stop(x,list,0)
            elif hit_target(list,x):                
                close_at_target(x,list,0)
            else:
                #still in trade
                pass
def look_for_trade(x,list):
    if Bot_list[x].In_Trade ==0:
                
        buy_sig(Bot_list[x],list)
        if add(Bot_list[x]) >=NUM_REQUIRED : 
            #record buy area
            
            size = float(list[HIGH])-float(list[LOW])
            Bot_list[x].open_trade(size,list,x)
            set_entry_price(list,x) 





def check_5min(list2,y,myhour,x):
    with open('5min_data') as f2:
        reader2 = csv.reader(f2)
        f2.seek(0)
        
        #initial guess , go to line, underguess so we don't have to do it again
        for nothing in range (12*y-24):
            reader2.next()
        #now find nearest minute
        list2 = reader2.next()
        
        safety =0
        while int(list2[HOUR5]) != myhour:
            
            if safety >100:
                print "ERROR1"
                sys.exit()
            safety+=1
            list2= reader2.next()
        #now we should be at same hour
        safety =0
        
        
        Scan_5min(list2,x,reader2)#checks 5 minute file for win/loss, closes trade
#FIX SCAN_5MIN
def check_both_hit5(list2,x):
    #function returns 1 if both target and stop hit
    if BUY_BOT ==1:
        if float(list2[HIGH5]) >= Bot_list[x].Target and float(list2[LOW5]) <= Bot_list[x].Stop:
            return 1
        return 0
    else:
        if float(list2[LOW5]) <= Bot_list[x].Target and float(list2[HIGH5]) >= Bot_list[x].Stop:
            return 1
        return 
def Scan_5min(list2,x,reader2):
    safety2= 0                        
    while True: #scan 5 minut
        if check_both_hit5(list2,x)==1:
            #both, so loss
            Bot_list[x].Sell_Price=Bot_list[x].Stop                                     
            Bot_list[x].close_trade(list2,1)
            break
        elif hit_stop5(list2,x)==1:
            #take loss
            close_at_stop(x,list2,1)
            break
        elif hit_target5(list2,x) ==1:
            #take win
            close_at_target(x,list2,1)
            break
        else:
            list2 = reader2.next()
            safety2+=1
            if safety2 >11 :#executed 12 times, didn't find it somethin went wrong
                print ("ERROR2")
                sys.exit()
    safety2= 0  
        
        
        
   
def init_bots():
    x =0
    for x in range(NUM_BOTS):
        Bot_list.append(Bot)
        Bot_list[x] = Bot()
        y=0
        for y in range (NUM_ATTR):
            Bot_list[x].trade_attributes[y] = random.randint(0,1)
            Bot_list[x].attribute_signs[y] = random.randint(0,1)
            if Bot_list[x].attribute_signs[y] == 0:
                Bot_list[x].attribute_signs[y] = -1
                #so some things count as negative
            
        #print Bot_list[x].trade_attributes[y]       
        







#pdb debugs
#pdb.set_trace()







    
list = []
list2 = []
zzzz=0
for zzzz in range(FILE_HOUR_ITEMS):
    list.append(0)
zzzz=0
for zzzz in range(FILE_5MIN_ITEMS):
    list2.append(0)


Bot_list = []

onlyonce =0
init_bots()

Parent_list = []
#cut population
zzz=0
for zzz in range (NUM_BOTS/2):
    Parent_list.append(Bot)

#loop
start_time = time.time()
for abcd in range (10):
    for abcde in range (NUM_BOTS):
        Bot_list[abcde].Balance = 10000
    open_file_and_trade(list)
    Bot_list = sorted(Bot_list, key=getBalance)
    
    zzz=0
    for zzz in range (NUM_BOTS/2):
        Parent_list[zzz] = Bot_list[zzz+NUM_BOTS/2]

    
    #shuffle
    random.shuffle(Parent_list)
    mix(Bot_list)
    
    if abcd ==9:
        print_balances(Bot_list)
   
print time.time() - start_time, "seconds"










        
