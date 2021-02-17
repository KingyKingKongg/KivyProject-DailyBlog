import importlib
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.cache import Cache
from kivy.core.window import Window
from datetime import datetime
import random
import os
import webbrowser
import subprocess


global path

date = str(datetime.date(datetime.now()))
time = str(datetime.time(datetime.now()))








#db = DataBase(.txt)

class LogOn(Screen):
    lName = ObjectProperty(None)   
    lEDI = ObjectProperty(None)
    notlog = ObjectProperty(None)
    pinp = ObjectProperty(None)
    
    
    global user 
    
    def logOne(self):
        global user
        path = os.getcwd() + "/DayJourn/"

        user = path + self.lName.text + "." + self.lEDI.text  + "/Profile." + self.lName.text + "." + self.lEDI.text + ".docx"
        userdir = path + self.lName.text + "." + self.lEDI.text 
        #path = os.getcwd()
        print(path)
        print(user)
        
        if os.path.exists(user):
            
            with open(user) as search:
                if self.pinp.text in search.read():
                    #self.notlog.text = "Login Complete"
                    self.lName.text = ""
                    self.lEDI.text = ""
                    self.pinp.text = ""
                    sm.current = "page1"
                    Cache.append("users", "logged", self.lName.text, timeout=None)
                    Cache.append("users", "edi", self.lEDI.text, timeout=None)
                    Cache.append("users", "usedirect", userdir, timeout=None)

                
                    
        
        else:
            logAgain()
        


class CreateUser(Screen):
    inputrank = ObjectProperty(None)
    inputlast = ObjectProperty(None)
    inputcac = ObjectProperty(None)
    inputedi = ObjectProperty(None)
    success = ObjectProperty(None)

  
    def c_user(self):
        path = os.getcwd() + "/"
        userdir = path + self.inputlast.text + "." + self.inputedi.text 
        user = path + self.inputlast.text + "." + self.inputedi.text  + "/Profile." + self.inputlast.text + "." + self.inputedi.text + ".docx"

        if os.path.exists(userdir):
            createAgain()
        
                            
        else:
            os.mkdir(userdir)
            os.mkdir(userdir + "/Bullets")
            os.mkdir(userdir + "/Money")
            os.mkdir(userdir + "/Money/Spending")
            os.mkdir(userdir + "/Money/PayCheck")
            os.mkdir(userdir + "/Money/Savings")
            os.mkdir(userdir + "/Workout")
            os.mkdir(userdir + "/Blogs")
            #os.chdir(user)
            newU = open(user, "w")
            newU.write(self.inputlast.text + " Created an account on " + date + "\nCAC Pin: " + self.inputcac.text + "\nEDI: " + self.inputedi.text)
            newU.close()
            self.ids.success.text = "User Created. Please Login"
            self.inputrank.text = ""
            self.inputlast.text = ""
            self.inputcac.text = ""
            self.inputedi.text = ""
            


class Pro1(Screen):
    def logOut(self):
        Cache.remove("users", "logged")
        Cache.remove("users", "edi")
        Cache.remove("users", "usedirect")   
    

class Bull(Screen):
    regFor = ObjectProperty(None)
    bullFor = ObjectProperty(None)
   
    def SubBullet(self):
        op = Cache.get("users","usedirect")

        entry = open(op + "/Bullets/BulletEntry." + date + ".docx", "a")
        entry.write(self.regFor.text)
        entry.close()
        self.regFor.text = ""

        BulletSubmition()
            
    def SubBullet2(self):
        op = Cache.get("users","usedirect")

        entry = open(op + "/Bullets/BulletFormEntry." + date + ".docx", "a")
        entry.write(self.bullFor.text)
        entry.close()
        self.bullFor.text = ""
        BulletSubmition()



class MonMain(Screen):
    ... 
    
class MonPay(Screen):
      
    noteamount = ObjectProperty(None)
    saveamount = ObjectProperty(None)
    payamount = ObjectProperty(None)
    paydate = ObjectProperty(None)
    
    display = ObjectProperty(None)
    
    
    
    def entryall(self):
        op = Cache.get("users","usedirect")

        entry = open(op + "/Money/PayCheck/PayCheckEntry." + ".docx", "a")
        entry.close()

        entry = open(op + "/Money/PayCheck/PayCheckEntry." + ".docx", "a")
        entry.write("\nLast Paydate Entered: " + self.paydate.text + "\nAmount Paid: " + self.payamount.text + "\nSavings entered: " + self.saveamount.text + "\nNotes added: " + self.noteamount.text )
        entry.close()
  
    def savingsall(self):
        op = Cache.get("users","usedirect")
        

        if os.path.exists(op + "/Money/Savings/SavingsEntry." + ".docx"):
            entry2 = open(op + "/Money/Savings/SavingsEntry." + ".docx", "r")
            last = entry2.readlines()
            strip = ""
                
            total = last[-1]
                
            alone = total[1:]
            
            new = alone.rstrip()
                
            strip += new
                    
            numb = int(new)        
                
            saveint = int(self.saveamount.text)
                    
            saveSum = numb + saveint
                
            stringsum = str(saveSum)
                
            entry2.close()
                
                
            entry2 = open(op + "/Money/Savings/SavingsEntry." + ".docx", "a")
            entry2.write("\nSavings entered on: " + date + ": " + self.saveamount.text + "\nTotal Savings to date: \n" + stringsum )
            entry2.close()
        
            self.display.text = stringsum
            
        else:
            entry2 = open(op + "/Money/Savings/SavingsEntry." + ".docx", "a")
            entry2.write("\nFirst time entry Total Savings to date: \n" + "$0")
            entry2.close()
            FirtTimeSavings()
    

    def gobackClear(self):
        self.noteamount.text = ""
        self.saveamount.text = ""
        self.payamount.text = ""
        self.paydate.text = ""
    
       
   
class Mone(Screen):
    
    price1= ObjectProperty(None)
    price2= ObjectProperty(None)
    price3= ObjectProperty(None)
    price4= ObjectProperty(None)
    price5= ObjectProperty(None)
    price6= ObjectProperty(None)
    price7= ObjectProperty(None)
    price8= ObjectProperty(None)
    price9= ObjectProperty(None)
    price10 = ObjectProperty(None)

    item1 = ObjectProperty(None)
    item2 = ObjectProperty(None)
    item3 = ObjectProperty(None)
    item4 = ObjectProperty(None)
    item5 = ObjectProperty(None)
    item6 = ObjectProperty(None)
    item7 = ObjectProperty(None)
    item8 = ObjectProperty(None)      
    item9 = ObjectProperty(None)
    item10 = ObjectProperty(None)
    
    totall = ObjectProperty(None)
    pover= ObjectProperty(None)
    
    
    
    def SubMoney(self):
        
        if (self.price1.text == "0" and
                self.price2.text == "0" and
                self.price3.text == "0" and
                self.price4.text == "0" and
                self.price5.text == "0" and
                self.price6.text == "0" and
                self.price7.text == "0" and
                self.price8.text == "0" and
                self.price9.text == "0" and
                self.price10.text == "0"):
            
            SpendingError()
        
        
        else:
               
            items = [
                self.item1.text,self.item2.text,self.item3.text,self.item4.text,self.item5.text,
                self.item6.text,self.item7.text,self.item8.text,self.item9.text,self.item10.text,

            ]
            
            prices = [
                self.price1.text,self.price2.text,self.price3.text,self.price4.text,self.price5.text,
                self.price6.text,self.price7.text,self.price8.text,self.price9.text,self.price10.text,
            ]
        
            
            
            
            convert = map(float, prices)
            
            newPrice = list(convert)
            
            overall = sum(newPrice)

            
            
            
            op = Cache.get("users","usedirect")
            
            entry = open(op + "/Money/Spending/MoneySpendingEntry." + date + ".docx", "a")
            entry.write("\nEntry date: "+ date + "\nOverall Spendings for 10 Items: " + str(overall) + "\nItems Logged")
            with entry as newentry:
                for (x,y) in zip(items, prices):
                    newentry.write("\n{} {}\n".format(x,y))
            

            self.item1.text = ""
            self.item2.text = ""
            self.item3.text = ""
            self.item4.text = ""
            self.item5.text = ""
            self.item6.text = ""
            self.item7.text = ""
            self.item8.text = ""
            self.item9.text = ""
            self.item10.text = ""
            
            self.price1.text = ""
            self.price2.text = ""
            self.price3.text = ""
            self.price4.text = ""
            self.price5.text = ""
            self.price6.text = ""
            self.price7.text = ""
            self.price8.text = ""
            self.price9.text = ""
            self.price10.text = ""
            
            entry.close()


            SpendingSubmition()   
    
    def Over(self):
        
        if (self.price1.text == "0" and
                self.price2.text == "0" and
                self.price3.text == "0" and
                self.price4.text == "0" and
                self.price5.text == "0" and
                self.price6.text == "0" and
                self.price7.text == "0" and
                self.price8.text == "0" and
                self.price9.text == "0" and
                self.price10.text == "0"):
            
            SpendingError()
            
        else:
            prices = [
                self.price1.text,self.price2.text,self.price3.text,self.price4.text,self.price5.text,
                self.price6.text,self.price7.text,self.price8.text,self.price9.text,self.price10.text,
            ]

            
            convert = map(float, prices)
            
            newPrice = list(convert)
            
            overall = sum(newPrice)
            
            

            self.pover.text = "Total Spendings = " + str(overall)


class WorkOutMain(Screen):
    ... 

class WorkBlog(Screen):
    blogtext = ObjectProperty(None)
    
    
    def loginfo(self):
        op = Cache.get("users","usedirect")
        
        
        entry = open(op + "/Workout/WorkoutLog." + date + ".docx", "a")
        entry.write("\n" + self.blogtext.text + "\n" )
        entry.close()
        
        WorkLog()
        
        self.blogtext.text = ""
    
    
    
class WorkIdea(Screen):
    runit:ObjectProperty(None)
    abwork:ObjectProperty(None)
    pushit:ObjectProperty(None)
    setset:ObjectProperty(None)
    
    def GetFit(self):

        ptABS = ["Plank Ups", "Russian Twists", "V-Ups", "Crunches", "Oblique abs"]

        runlist = ["Just run for like 30min", "1.5miles timed", "Bike ride?"]

        sets = random.randrange(3,6)
        setnum = str(sets)
        rangenum1 = str(random.randrange(30,40))
        rangenum2 = str(random.randrange(30,40))
        rangenum3 = str(random.randrange(30,40))
        rangenum4 = str(random.randrange(30,40))
        
        ab = random.choice(list(ptABS))
        run = random.choice(list(runlist))
        
        
        self.setset.text = setnum
                
        self.pushit.text = "Push: " + rangenum1 + "\nSit: " + rangenum2 + "\nSquats: " + rangenum3

        self.abwork.text = "Do: " + rangenum4 + " " + ab

        self.runit.text = run        
        
    def loginfo(self):
        op = Cache.get("users","usedirect")
        
        
        entry = open(op + "/Workout/WorkoutLog." + date + ".docx", "a")
        entry.write("\nWorkout Generated: \nSets: " + self.setset.text + "\nPushUps: " + self.pushit.text + "\nAbWork: " + self.abwork.text + "\nCardio: " + self.runit.text)
        entry.close()
        
        WorkLog()
        
        
        
        
        
        
        
        
        
    def Submit(self):
        ...        
    
 



class Blogger(Screen):
    bloginput = ObjectProperty(None) 
    
    def randblog(self):
        op = Cache.get("users","usedirect")
        
        entry = open(op + "/Blogs/BlogEntry." + date + ".docx", "a")
        entry.write("\nBlog Entry on: " + date + "\n" + self.bloginput.text)
        entry.close()
        
        self.bloginput.text = ""
        
        WorkLog()
    
    
class GamesMain(Screen):
    ...          


class GameHoe(Screen):
    colur = ObjectProperty(None)
    spice = ObjectProperty(None)
    hoebutt = ObjectProperty(None)
    cloth = ObjectProperty(None)
    lips = ObjectProperty(None)
    rees = ObjectProperty(None)
    
    global typelist
    
    typelist = [0]
    
    
    def Spice(self, text):
        

        if text == "Nutmeg":
            
            typelist.append(2)
            
            if 5 in typelist:
                typelist.remove(5)
            elif 11 in typelist:
                typelist.remove(11)
            else:
                ... 
            
        elif text == "Cayenne":
            
            typelist.append(5)

            if 2 in typelist:            
                typelist.remove(2)
            elif 11 in typelist:
                typelist.remove(11)
            else:
                ...                 
            
        elif text == "Cinnamon":

            typelist.append(11)
            
            if 2 in typelist:
                typelist.remove(2)
            elif 5 in typelist:
                typelist.remove(5)
            else:
                ... 
                      
    def Colorr(self, text):
       
        if text == "red":
            
            typelist.append(4)
            
            if 8 in typelist:
                typelist.remove(8)
            elif 10 in typelist:    
                typelist.remove(10)
            elif 15 in typelist:
                typelist.remove(15) 
        
            else:
                ... 
            
        elif text == "blue":
            
            typelist.append(10)
            
            if 8 in typelist:
                typelist.remove(8)
            elif 4 in typelist:
                typelist.remove(4)
            elif 15 in typelist:
                typelist.remove(15)            
            else:
                ... 
            
        elif text == "pink":
            
            typelist.append(8)
            
            if 4 in typelist:
                typelist.remove(4)
            elif 10 in typelist:
                typelist.remove(10)
            elif 15 in typelist:
                typelist.remove(15)            
            else:
                ... 
            
            
        elif text == "black":
            
            typelist.append(15)
            
            if 8 in typelist:
                typelist.remove(8)
            elif 10 in typelist:
                typelist.remove(10)
            elif 4 in typelist:
                typelist.remove(4)            
            else:
                ... 
            
    def Cloths(self, text):
       
        if text == "panties":
            
            typelist.append(13)
            
            if 12 in typelist:
                typelist.remove(12)
            elif 20 in typelist:
                typelist.remove(20)
            else:
                ... 
            
        elif text == "bra":
            
            typelist.append(12)
            
            if 13 in typelist:
                typelist.remove(13)
            elif 20 in typelist:
                typelist.remove(20)
            else:
                ... 
            
            
        elif text == "nothing":
            
            typelist.append(20)
            
            if 12 in typelist:
                typelist.remove(12)
            elif 13 in typelist:
                typelist.remove(13)
            else:
                ... 
                  
    def Lip(self, text):
       
        if text == "lip gloss":
            
            typelist.append(19)
            
            if 7 in typelist:
                typelist.remove(7)
            elif 14 in typelist:
                typelist.remove(14)
            else:
                ... 
            
            
        elif text == "chapstick":
            
            typelist.append(7)
            
            if 14 in typelist:
                typelist.remove(14)
            elif 19 in typelist:
                typelist.remove(19)
            else:
                ... 
            
            
        elif text == "lipstick":
            
            typelist.append(14)
            
            if 19 in typelist:
                typelist.remove(19)
            elif 7 in typelist:
                typelist.remove(7)
            else:
                ... 
            
    
    def OverAll(self):

        hoez = sum(typelist)
        
        if hoez in range(56,66):
            
            self.rees.text = "Dirty Hoe"
            
        if hoez in range(46,56):
            
            self.rees.text = "Side Hoe"
            
        if hoez in range(36,46):
            
            self.rees.text = "Main Hoe"
            
        if hoez in range(27,36):
            
            self.rees.text = "Stupid Hoe"
            
        if hoez in range(0,27):
            
            self.rees.text = "Regular Hoe"
            

class GameRock(Screen):
    weap = ObjectProperty(None)
    cpu = ObjectProperty(None)
    res = ObjectProperty(None)
    numscore = ObjectProperty(None)
    drawscore = ObjectProperty(None)
    cpuscore = ObjectProperty(None)
    
             
    global uscore
    global cscore
    global dscore
    global gscore
    
    uscore = 0
    cscore = 0
    dscore = 0
    gscore = 0
 

    
    def RPS(self, text):
        global uscore
        global cscore
        global dscore
        global gscore

        CPU = ["Rock", "Paper", "Scissor"]

        CPChoice = random.choice(list(CPU))
        
        self.cpu.text = CPChoice
        
        if gscore == 50:
            EasterEgg1()
            
        elif text == "Choose your Weapon!":
            RPCC() 
            #pop up to be like... do something bro
        
        elif text == "Rock" and CPChoice == "Paper" and uscore < 5 and cscore < 5 and dscore < 5:
             
            self.res.text = "LOSER!" 
            cscore += 1
            CP1 = str(cscore)
            self.cpuscore.text = CP1 
            gscore += 1
        
        elif text == "Rock" and CPChoice == "Scissor" and uscore < 5 and cscore < 5 and dscore < 5:
            
            self.res.text = "Winner!" 
            uscore += 1
            CP1 = str(uscore)
            self.numscore.text = CP1
            gscore += 1         
        
        elif text == "Paper" and CPChoice == "Rock" and uscore < 5 and cscore < 5 and dscore < 5:
            
            self.res.text = "Winner!" 
            uscore += 1
            CP1 = str(uscore)
            self.numscore.text = CP1
            gscore += 1         
        

        elif text == "Paper" and CPChoice == "Scissor" and uscore < 5 and cscore < 5 and dscore < 5:
             
            self.res.text = "LOSER!" 
            cscore += 1
            CP1 = str(cscore)
            self.cpuscore.text = CP1 
            gscore += 1
        

        elif text == "Scissor" and CPChoice == "Rock" and uscore < 5 and cscore < 5 and dscore < 5:
             
            self.res.text = "LOSER!" 
            cscore += 1
            CP1 = str(cscore)
            self.cpuscore.text = CP1 
            gscore += 1
        
   
        elif text == "Scissor" and CPChoice == "Paper" and uscore < 5 and cscore < 5 and dscore < 5:
            
            self.res.text = "Winner!" 
            uscore += 1
            CP1 = str(uscore)
            self.numscore.text = CP1
            gscore += 1         
        
    
        elif text == CPChoice and uscore < 5 and cscore < 5 and dscore < 5:
            
            self.res.text = "Draw!" 
            dscore += 1
            CP1 = str(dscore)
            self.drawscore.text = CP1
            gscore += 1  
            
        elif uscore == 5 or cscore == 5 or dscore == 5:
            
            if uscore == 5:
                RPCWin()
                self.cpu.text = """
                Boop Bop,
                Good Job!"""

            elif cscore == 5:
                self.cpu.text = """
                Bee Bee..
                I won!"""

                RPCLose()
            elif dscore == 5:
                self.cpu.text = """
                Beep, 
                We Tied!"""

                RPCDraw()
            
                 
    def Resett(self):
        uscore*0
        cscore*0
        dscore*0
        self.cpuscore.text = "0" 
        self.numscore.text = "0"
        self.drawscore.text = "0"
        self.res.text = ""
        self.cpu.text = "Beep Boop!"
        self.weap.text = "Choose your Weapon!"

class MadLibMain(Screen):
    ...        
                
class MadLib1(Screen):
                
    item1 = ObjectProperty(None)
    item2 = ObjectProperty(None)
    item3 = ObjectProperty(None)
    item4 = ObjectProperty(None)
    item5 = ObjectProperty(None)
    item6 = ObjectProperty(None)
    item7 = ObjectProperty(None)
    item8 = ObjectProperty(None)
    item9 = ObjectProperty(None)
    item10 = ObjectProperty(None)

    storyy = ObjectProperty(None)
    storybutt = ObjectProperty(None)
    
    def GetStory(self):
        
        if (self.item1.text== "" or
        self.item2.text=='' or 
        self.item3.text=='' or
        self.item4.text=='' or 
        self.item5.text== '' or 
        self.item6.text =='' or 
        self.item7.text =='' or 
        self.item8.text =='' or 
        self.item9.text =='' or
        self.item10.text ==''
            
        ):
            MadLipp()
        
        
        
        else:
            self.storyy.text = """
            Hello,
            Let me tell you about how I got to """ + self.item1.text + """. So on """ + self.item2.text + """ everything was going well. 
            I went to """ + self.item1.text + " via " + self.item3.text + "." + self.item4.text + """ name is """ + self.item5.text + """. It took over """ + self.item6.text + """
            hours, but Lord knows, traveling by car wouldn't have been any better. On our way there
            we got stopped by the """ + self.item7.text + """ police and they told us that we would be going to """ + self.item7.text + """ jailhouse. 
            I didn't even know that place existed! I said, 'SCREW THIS!', then hopped back on my """ + self.item3.text + """, and jetted off. We would have
            arrived sooner but my ride needed to stop and eat """ + self.item9.text + """. Good thing """ + self.item9.text + """ had exactly what we needed. 
            When we left """  + self.item9.text + """  we were well on our way! Finally! On our final minutes of arrival, I would have never guessed
            that we would run into someone else riding on a/an """ + self.item10.text + """. Of course that meant that we had to race each other!
            Who won you ask? Well that, we will never know becuase both of our pets were not racing creatures. Both animals tired out after 5 seconds,
            kicked us off thier backs and ran into the wild. As for getting to """ + self.item1.text + """ I walked the rest of the way with my new pal 
            """ + self.item5.text + """. Yes, they had the same name as my  """ + self.item3.text + """ but thats what I liked about them most!""" 
        

    def RERE(self):
        
        self.item1.text= ""
        self.item2.text=''
        self.item3.text=''
        self.item4.text=''
        self.item5.text= ''
        self.item6.text =''
        self.item7.text =''
        self.item8.text =''
        self.item9.text =''
        self.item10.text =''
        
        
class MadLib2(Screen):
    item1 = ObjectProperty(None)
    item2 = ObjectProperty(None)
    item3 = ObjectProperty(None)
    item4 = ObjectProperty(None)
    item5 = ObjectProperty(None)
    item6 = ObjectProperty(None)
    item7 = ObjectProperty(None)
    item8 = ObjectProperty(None)
    item9 = ObjectProperty(None)
    item10 = ObjectProperty(None)

    storyy = ObjectProperty(None)
    storybutt = ObjectProperty(None)
    
    def GetStory(self):
        
        if (self.item1.text== "" or
        self.item2.text=='' or 
        self.item3.text=='' or
        self.item4.text=='' or 
        self.item5.text== '' or 
        self.item6.text =='' or 
        self.item7.text =='' or 
        self.item8.text =='' or 
        self.item9.text =='' or
        self.item10.text ==''
            
        ):
            MadLipp()
        
        
        
        else:
            self.storyy.text = """ """




    def RERE(self):
        
        self.item1.text= ""
        self.item2.text=''
        self.item3.text=''
        self.item4.text=''
        self.item5.text= ''
        self.item6.text =''
        self.item7.text =''
        self.item8.text =''
        self.item9.text =''
        self.item10.text =''
        
           
    
class MadLib3(Screen):
    item1 = ObjectProperty(None)
    item2 = ObjectProperty(None)
    item3 = ObjectProperty(None)
    item4 = ObjectProperty(None)
    item5 = ObjectProperty(None)
    item6 = ObjectProperty(None)
    item7 = ObjectProperty(None)
    item8 = ObjectProperty(None)
    item9 = ObjectProperty(None)
    item10 = ObjectProperty(None)

    storyy = ObjectProperty(None)
    storybutt = ObjectProperty(None)
    
    def GetStory(self):
        
        if (self.item1.text== "" or
        self.item2.text=='' or 
        self.item3.text=='' or
        self.item4.text=='' or 
        self.item5.text== '' or 
        self.item6.text =='' or 
        self.item7.text =='' or 
        self.item8.text =='' or 
        self.item9.text =='' or
        self.item10.text ==''
            
        ):
            MadLipp()
        
        
        
        else:
            self.storyy.text = """ """




    def RERE(self):
        
        self.item1.text= ""
        self.item2.text=''
        self.item3.text=''
        self.item4.text=''
        self.item5.text= ''
        self.item6.text =''
        self.item7.text =''
        self.item8.text =''
        self.item9.text =''
        self.item10.text =''
        




class HangDude(Screen):
                         
    #hanglist = AnimalsHang.Animlist
    uLetGess = ObjectProperty(None)   #lettersGuess box       
    uIknow = ObjectProperty(None)    #guess full word
    uGuess = ObjectProperty(None)    #one letter guess
    theWord = ObjectProperty(None) #Appended ____
    manyLet = ObjectProperty(None)  #Number amount
    
    global secretword
    global actual
    global guessed
    global correctguess
    global tries
    global amount
    global secret
    global path

    #self.uLetGess.text = ""
    #self.uIknow.text = "Click here to guess full word"
    #self.uGuess.text = "One Letter Guess"
    d = os.getcwd()
    with open(d + '/DayJourn/AnimalsHang.txt', 'r') as file:
    
        insdiefile = file.read()
        secret = list(map(str, insdiefile.split())) 
        
    secretword = random.choice(secret) #random word
    secretword





    guessed = [] #letters you guessed

    correctguess = []

    tries = 12 #amount of guesses

    amount = len(secretword) #letters in secret word

    actual = ["_"] * amount



    def NewWord(self):
        global secretword
        global tries
        global secret 
        
        HangRules()
        d = os.getcwd()
  
        file = open(d + '/DayJourn/AnimalsHang.txt', 'r')
    
        insdiefile = file.read()
        secret = list(map(str, insdiefile.split())) 
        
        secretword = random.choice(secret) #random word
        secretword
        
        amount = len(secretword) #letters in secret word
        
        actual = ["_"] * amount
        
        self.theWord.text = "".join(actual)
        self.manyLet.text = str(amount)
        self.uLetGess.text = ""
        self.uIknow.text = ""
        self.uGuess.text = ""
        #file.close()
        tries = 12
        #print(actual)
        #print(amount)
        #print(secretword)
        
    def GamePlay(self):
        global amount
        global tries
        global actual
        
        #amount = len(secretword) #letters in secret word
        
        #actual = ["_"] * amount

        
        if len(self.uGuess.text) == 1: 
            if self.uGuess.text in "1234567890":
                self.uGuess.text = "No numbers!" 
                #POP UP SAYING TO ENTER A LETTER NO NUMBERS
            
            elif self.uGuess.text in guessed:
                self.uGuess.text = "Already Guessed"
                
                            
            elif self.uGuess.text in secretword:
                guessed.append(self.uGuess.text)
                
                ocurList = ([pos for pos, char in enumerate(secretword) if char in self.uGuess.text])
                times = len(ocurList)

                for y in ocurList:
                    actual.pop(y)
                    actual.insert(y, self.uGuess.text)
                self.theWord.text = str(''.join(actual))
                    #amount -= times
                    
                self.uLetGess.text = ''.join(guessed)
                
            elif self.uGuess.text not in secretword:
                guessed.append(self.uGuess.text)
                
                self.uGuess.text = "Nope"
                
                self.uLetGess.text = ''.join(guessed)
                
                
                tries -= 1

            
        elif len(self.uGuess.text) > 1:
            self.uGuess.text = "Only one letr plis"
 
            #please enter character
        
    def SubmitAns(self, text_input):
        global amount
        global tries
        global actual
        
        amount = len(secretword) #letters in secret word
        
        actual = ["_"] * amount
        
        if self.uIknow.text == secretword:
                
                HangWin()
                
                guessed.append(self.uGuess.text)
                self.uLetGess.text = ''.join(guessed)
                
                ocurList = ([pos for pos, char in enumerate(secretword) if char in self.uGuess.text])
                times = len(ocurList)

                for y in ocurList:
                    actual.pop(y)
                    actual.insert(y, self.uGuess.text)
                    self.theWord.text = str(''.join(actual))
                    


        
        elif self.uIknow.text in secretword:
      
                HangMessage()
            
            
                guessed.append(self.uGuess.text)
                self.uLetGess.text = ''.join(guessed)
                
                ocurList = ([pos for pos, char in enumerate(secretword) if char in self.uGuess.text])
                times = len(ocurList)

                for y in ocurList:
                    actual.pop(y)
                    actual.insert(y, self.uGuess.text)
                    self.theWord.text = str(''.join(actual))
                    
                    
                    
                tries -= 1
    


class FilesETC(Screen):
    ...
    def Goog(self):
        webbrowser.open("https://google.com")




class Manager(ScreenManager):
    ... #transitions




        

###   All pop up windows

def logAgain():
    pop = Popup(title= "Login Error",
                content= Label(text="Username/Password mismatch. Please try again"),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def createAgain():
    pop = Popup(title= "Create User Error",
                content= Label(text="User already exists. Please try logging in"),
                size_hint=(None, None), size=(400, 400))
    pop.open()

def BulletSubmition():
    pop = Popup(title= "Bullet Submitted",
                content= Label(text="Bullet Submitted. Click Anywhere to continue"),
                size_hint=(None, None), size=(400, 400))
    pop.open()

def SpendingSubmition():
    pop = Popup(title= "Entries Submitted",
                content= Label(text="Spending Submitted. Click Anywhere to continue"),
                size_hint=(None, None), size=(400, 400))
    pop.open()

def SpendingError():
    pop = Popup(title= "Error",
                content= Label(text="You have not enterered any information. "),
                size_hint=(None, None), size=(400, 400))
    pop.open()

def FirtTimeSavings():
    pop = Popup(title= "First Timer",
                content= Label(text= "Records show first time use. Please Click again"),
                size_hint=(None, None), size=(400, 400))
    pop.open()    

def WorkLog():
    pop = Popup(title= "Information Logged",
                content= Label(text= "Information Saved!"),
                size_hint=(None, None), size=(400, 400))
    pop.open() 
    
def RPCC():
    pop = Popup(title= "Error",
                content= Label(text= "Please choose Rock, Paper Or Scissor"),
                size_hint=(None, None), size=(400, 400))
    pop.open()
    
def RPCWin():
    pop = Popup(title= "Oh Snap!",
                content= Label(text= "You're the over all winner! Click Reset to play again"),
                size_hint=(None, None), size=(450, 450))
    pop.open()
    
def RPCLose():
    pop = Popup(title= "WWwwoooowwWW!",
                content= Label(text= "You lost against a computer! Click Reset to play again"),
                size_hint=(None, None), size=(480, 480))
    pop.open()    

def RPCDraw():
    pop = Popup(title= "OOPS!",
                content= Label(text= "You both tied! Click Reset to play again"),
                size_hint=(None, None), size=(450, 450))
    pop.open()

  
    
def HangRules():
    pop = Popup(title= "Rules!",
                content= Label(text= """ 
                    1) Guess only 1 letter
                    2) No number guesses
                    3) Submit "full word" when you have an answer
                    4) If you submit the answer and you are wrong,
                                  you lose a turn"""),
                size_hint=(None, None), size=(450, 450))
    pop.open()
    
def HangWin():
    pop = Popup(title= "Winner Winner Chicken Dinner!",
                content= Label(text= "You figured it out! Click New word to play again"),
                size_hint=(None, None), size=(450, 450))
    pop.open()

def HangLose():
    pop = Popup(title= "HANGED!",
                content= Label(text= "You DIED! Click New word to play again"),
                size_hint=(None, None), size=(450, 450))
    pop.open() 
 
def HangMessage():
    pop = Popup(title= "Noope!",
                content= Label(text= "The wasn't it, but we filled in the letters you got"),
                size_hint=(None, None), size=(450, 450))
    pop.open() 
 
 
 
 
    
def EasterEgg1():
    pop = Popup(title= "Easter Egg!",
                content= Label(text= "You've played 50 games.. you must be bored"),
                size_hint=(None, None), size=(450, 450))
    pop.open()

def MadLipp():
    pop = Popup(title= "Missing Items!",
                content= Label(text= "You have left one or more sections blank"),
                size_hint=(None, None), size=(450, 450))
    pop.open()    
    
    
    
    
    
    

kv = Builder.load_file("record2.kv")
sm = Manager()

switch = [LogOn(name = "login"), CreateUser(name= "create"), Pro1(name= "page1"),Bull(name= "bulll"), Mone(name= "mon"),MonMain(name="mainmon"),MonPay(name= "paymon")]

switch2 = [GamesMain(name="gaymay"), WorkBlog(name="wrkb"),WorkIdea(name="wrkid"), WorkOutMain(name= "work"),Blogger(name= "blogg"),GameHoe(name="hoe"),GameRock(name="grock")]

switch3 = [MadLibMain(name="madmain"),MadLib1(name="mad"), MadLib2(name="mad2"),MadLib3(name="mad3"),HangDude(name="hanger"), FilesETC(name="files")]

for screen in switch:
    sm.add_widget(screen)

for screen2 in switch2:
    sm.add_widget(screen2)

for screen3 in switch3:
    sm.add_widget(screen3)


Cache.register("users", limit=None, timeout=None)



    
path = os.getcwd() + "/"

    
    
sm.current = "login"        

class RecordApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    RecordApp().run()   
