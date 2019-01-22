#bot class file import constants
from constants import *


class Date:
    year =1970
    month = -1
    day = -1
    hour = -1
    dayofweek = -1

class Trade:
    open_date = Date()
    close_date = Date()
    profit =0.0 #dollars
    pips =0.0 
    open = 0.00000
    close = 0.00000
    stop =  0.00000
    target = 0.0000
class Bot:
    def __init__(self):
        self.trade_attributes = [0,0,0,0] #trade or don't
        self.attribute_signs = [0,0,0,0]  #for buying or against
        self.buy = [0,0,0,0] #buy for this bar
        
        self.Balance = 10000.00
        self.In_Trade = 0
        self.Stop = 0.00000
        self.Target = 0.00000
        self.Minilots = 0
        self.numoftrades=0 #changes when trade opened
        self.wins =0
        self.losses =0
        self.Buy_Price =0.00000
        self.Sell_Price=0.00000

        self.Trade_List = []
        
        
    def open_trade(self,pips,list,x):
        risk = self.Balance*RISK
        dollarsperpip = risk/(pips*10000)
        self.Minilots =  math.floor(dollarsperpip/DOLLARS_PER_MINILOT)  

        if BUY_BOT ==1:
            self.Target = float(list[CLOSE])+pips
            self.Stop = float(list[CLOSE])-pips
            spread_mul =1

        else:
            self.Target = float(list[CLOSE])-pips
            self.Stop = float(list[CLOSE])+pips
            spread_mul =-1
        self.numoftrades+=1
     
        


        self.Trade_List.append(Trade)
        self.Trade_List[self.numoftrades-1] = Trade() 
        self.Trade_List[self.numoftrades-1].open_date.year = int(list[YEAR])
        self.Trade_List[self.numoftrades-1].open_date.month = int(list[MONTH])
        self.Trade_List[self.numoftrades-1].open_date.day = int(list[DAY])
        self.Trade_List[self.numoftrades-1].open_date.hour = int(list[HOUR])
        self.Trade_List[self.numoftrades-1].open_date.dayofweek = int(list[DAYOFWEEK])
        self.Trade_List[self.numoftrades-1].open = float(list[CLOSE])+SPREAD*spread_mul
        
        
        
    def close_trade(self,list,whichlist):
        #which list 0 refres to hourly data, list 1 = 5 min
         pips=  CONVERT_TO_PIPS*(self.Sell_Price-self.Buy_Price)
        
         dollar_profit=pips*self.Minilots*DOLLARS_PER_MINILOT
         if dollar_profit >=0:
             self.wins+=1
         else:
             self.losses+=1

         if (BUY_BOT ==1):
             _close = self.Sell_Price
         else:
             _close = self.Buy_Price

         if whichlist == 0:
             self.Trade_List[self.numoftrades-1].close_date.year = int(list[YEAR])
             self.Trade_List[self.numoftrades-1].close_date.month = int(list[MONTH])
             self.Trade_List[self.numoftrades-1].close_date.day = int(list[DAY])
             self.Trade_List[self.numoftrades-1].close_date.hour = int(list[HOUR])
             self.Trade_List[self.numoftrades-1].close_date.dayofweek = int(list[DAYOFWEEK])
             self.Trade_List[self.numoftrades-1].close = _close
         else:
             self.Trade_List[self.numoftrades-1].close_date.year = int(list[YEAR5])
             self.Trade_List[self.numoftrades-1].close_date.month = int(list[MONTH5])
             self.Trade_List[self.numoftrades-1].close_date.day = int(list[DAY5])
             self.Trade_List[self.numoftrades-1].close_date.hour = int(list[HOUR5])
             self.Trade_List[self.numoftrades-1].close_date.dayofweek = int(list[DAYOFWEEK5])
             self.Trade_List[self.numoftrades-1].close = _close
         self.Trade_List[self.numoftrades-1].pips = pips
         self.Trade_List[self.numoftrades-1].profit = dollar_profit
         self.Trade_List[self.numoftrades-1].stop = self.Stop
         self.Trade_List[self.numoftrades-1].target = self.Target
         self.Balance+= dollar_profit
         self.In_Trade =0
         self.Minilots=0
         self.Stop = 0.00000
         self.Target = 0.00000

         return dollar_profit

def add(in_bot):
    total =0
    a=0
    for a in range(NUM_ATTR):
        total += in_bot.buy[a]*in_bot.trade_attributes[a]* in_bot.attribute_signs[a]
    return total

#function set buy:
def buy_sig(in_bot,list): 
    test= load_comparison(list)
   
    aaa=0
    for aaa in range (NUM_BUYTRAITS):
        float_compare_greaterthan(aaa,float(list[aaa]),test[aaa],in_bot)
        
        

        
#this function looks at "list[]", from file, and 
def float_compare_greaterthan(index,const1,const2,in_bot2):
        #const2 is comparisonvalue
    if  (const1 > const2):
        in_bot2.buy[index] =1
    else:
        in_bot2.buy[index] =0
def load_comparison(list):
    CLOSE1 =float(list[CLOSE])
    COMPARISON = [CLOSE1,CLOSE1,CLOSE1,ACCEL_THRESHOLD]
    return COMPARISON
        
        
        
       #round(float,5) #5 is 0.12345) 
        
''' #old code from buy_sig
    if float(list[SMA1]) > float(list[CLOSE]):
        in_bot.buy[0] = 1
    else:
        in_bot.buy[0] = 0
    if float(list[SMA2]) > float(list[CLOSE]):
        in_bot.buy[1] = 1
    else:
        in_bot.buy[1] = 0
        
    if float(list[SMA3]) > float(list[CLOSE]):
        in_bot.buy[2] = 1
    else:
        in_bot.buy[2] = 0
    if float(list[ACCEL]) > ACCEL_THRESHOLD:
        in_bot.buy[3] = 1
    else:
        in_bot.buy[3] = 0
'''
