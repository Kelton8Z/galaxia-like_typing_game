#import module_manager
#module_manager.review()
from tkinter import *
from image_util import *
import tkinter.ttk as ttk
#from colleges.py import *
import csv
import re

# 1=History 2=motto 3=type 4=history 5=endowment 6=chairman 7=president
# 8 = provost 9=academic staff# 10=student# 11=undergrad# 12=grad#
# 13=location 14=campus 15=colors 16=athletics 17=nickname 18=mascot 19=website
def getInfoBox(college):
    infoBox = []
    print(college)
    with open(college+".csv","r",encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            infoBox.append(line[0])
        return infoBox 
        
import pandas
from pandas.io.html import read_html
page = 'https://en.wikipedia.org/wiki/Massachusetts_Institute_of_Technology'
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"}) #0=Ranking
wikitables = read_html(page, index_col=0, attrs={"class":"wikitable"}) # 0=race
        
# included colleges with the same acronym, e.g., "cmu" and "bu"
# and colleges with the same prefix, i.e., "boston"
collegeList = ["carnegie mellon u","central michigan university",\
"central methodist university","boston university","boston college",\
"brandeis university","brown university","baylor university",\
"massachusetts institute of technology","cornell university"] 

# topics and their corresponding keywords
history = ["founded","history","origin"]
topics = ["admission","safety","tuition","ranking","schoolType","motto"]
schoolType = ["public","private","type","lac","liberal art","big u"]
motto = ["motto","founding principle"]
admission = ["get in","admission rates","chances"]
tuition = ["cost","money","affordable","expensive","tuition"]
safety = ["safe","crime rates"]
ranking = ["rankings","ranking","rank","the best"]
compare = ["more","less","better","than","compare","which one"]
athletics = ["sports","athletics",]
race = ["ethnic","race"]

def isAcronym(word):
    acronym = ""
    acronyms = []
    for college in collegeList:
        for i in college.split(" "):
            acronym += i[0]
        acronyms.append(acronym)
        acronym = ""
    return word in set(acronyms)
    
def selectFullName(acronym):
    fullNames = [] # fullNames match csv file names
    numOfUWithSameAcronym = 0
    acronym_ = ""
    suffix = ""
    for college in collegeList:
        prefix = college.split(" ")[:-1]
        prefix = " ".join(prefix) # normailze
        if college.split(" ")[-1] == "college":
            suffix = " c"
        else: # == "university"
            suffix = " u"
        for i in college.split(" "):
            acronym_ += i[0]
        if acronym == acronym_:
            college = prefix + suffix
            fullNames.append(college)
            numOfUWithSameAcronym += 1
        acronym_ = ""
    return [numOfUWithSameAcronym,fullNames]
'''
def logisticRegression(data,str):
    if 
        data.isObjective = True
    else:
        data.isObjective = False'''

def NLP(data,str):
    topic = ""
    college = ""
    collegesToCompare = []
    s = set(str.split(" "))
    print(s)
    questionType = "Facts"
    for word in s:
        if word in admission:
            topic = "admission"
        elif word in tuition:
            topic = "tuition"
        elif word in motto:
            topic = "motto"
        elif word in safety:
            topic = "safety"
        elif word in ranking:
            topic = "ranking"
        elif word in race:
            topic = "race"
        elif word in athletics:
            topic = "athletics"
        elif word in compare:
            questionType = "compare"
    for university in collegeList:
        if university in str:
            college = university
    if len(topic)==0:
        return "Sorry, your question's topic is not yet covered or can you phrase it another way"
    if questionType == "Facts":
        if topic == "admission":
            return college + "'s admission " + getInfoBox(college+"1")
        elif topic == "tuition":
            pass
        elif topic == "safety":
            pass
        elif topic == "ranking":
            pass
        elif topic == "schoolType":
            pass
        elif topic == "athletics":
            return college + "'s athletics is like " + getInfoBox(college)[16]
        elif topic == "race":
            return college + "'s race looks like " + getInfoBox(college)[2]
        elif topic == "motto":
            return college + "'s motto is " + getInfoBox(college)[2]
    elif questionType == "compare":
        if topic == "admission":
            pass
        elif topic == "tuition":
            pass
        elif topic == "safety":
            pass
        elif topic == "ranking":
            pass
        elif topic == "schoolType":
            pass
        
    return 

def init(data):
    data.timer = 0
    data.requestLine = 0
    data.cx = data.width//2
    data.cy = data.height//2
    data.inputHistory = []
    data.outputHistory = []
    data.messageHistory = []
    data.input = ""
    data.output = ""
    data.userName = ""
    data.email = ""
    data.password = ""
    data.numOfSearches = 50
    data.numOfSearchesLeftThisMonth = 50
    data.numOfUWithSameAcronym = 0
    data.selectedFullName = ""
    data.logo = PhotoImage(file="octopedia_logo.gif")
    data.user = PhotoImage(file="user.gif")
    data.speed = 40
    data.scrollY = 0
    data.IMy = data.height//10
    data.mode = "homeScreen" 
    data.isObjective = False
    data.selector = False
    data.loggedIn = False
    data.canLogIn = False
    data.userNameEntered = False
    data.emailEntered = False
    data.passwordEntered = False
    data.fullNameSelected = False
    data.hovered = False
    data.scrollable = False
    data.hoverCount = -1
    data.profileCompleted = "0%"
    data.searchBarLeftX = data.width//3
    data.searchBarRightX = data.width*2//3
    data.searchBarTopY = data.height//2
    data.searchBarBottomY = data.height//2 + data.height//10
    data.LogInLeftX = 18/20*data.width
    data.LogInRightX = 19/20*data.width
    data.LogInTopY = 1/20*data.height
    data.LogInBottomY = 1/20*data.height + 1/40*data.width

def clickLogIn(event,data):
    return data.LogInLeftX <= event.x <= data.LogInRightX and data.LogInTopY <=\
    event.y <= data.LogInBottomY
    
def clickSelector(event,data):
    return data.searchBarLeftX <= event.x <= data.searchBarRightX and\
    data.searchBarBottomY <= event.y <= data.searchBarBottomY+\
    10*data.numOfUWithSameAcronym
        
def mousePressed(event, data):      
    # in homeScreen & click "Log in" -> go to registration page
    if data.mode == "homeScreen":
        if clickLogIn(event,data):
            data.mode = "login"
        elif clickSelector(event,data):
            data.selectedFullName = data.fullNames[(event.y-\
            data.searchBarBottomY-5)//10]
            data.fullNameSelected = True
            data.selector = False
    elif data.mode == "IM":
        if clickLogIn(event,data):
            data.input = ""
            data.mode = "login"
        elif clickSelector(event,data):
            data.selectedFullName = data.fullNames[(event.y-\
            data.searchBarBottomY-5)//10]
            print(data.selectedFullName)
            data.fullNameSelected = True
            data.selector = False
    elif data.mode == "login":
        if data.LogInLeftX <= event.x <= data.LogInRightX and data.LogInTopY \
        <= event.y <= data.LogInBottomY:
            data.mode = "homeScreen"
    # in registration page & log in -> user account page

def keyPressed(event, data):
    data.input += event.keysym
    if event.keysym == "Shift_L":
        data.input = "".join(list(data.input)[:-7])
    if event.keysym == "Up":
        data.input = "".join(list(data.input)[:-2])
    if event.keysym == "Down":
        data.input = "".join(list(data.input)[:-4])
    if event.keysym == "at":
        data.input = "".join(list(data.input)[:-2])
        data.input += "@"
    if event.keysym == "Right":
        data.input = "".join(list(data.input)[:-5])
    if event.keysym == "Left":
        data.input = "".join(list(data.input)[:-4])
    if event.keysym == "period":
        data.input = "".join(list(data.input)[:-6])
        data.input += "."
    if event.keysym == "space":
        data.input = "".join(list(data.input)[:-5])
        data.input += " "
    if event.keysym == "quoteright":
        data.input = "".join(list(data.input)[:-10])
        data.input += "'"
    if event.keysym == "BackSpace":
        data.input = "".join(list(data.input)[:-10])
    if event.keysym == "Caps_Lock":
        data.input = "".join(list(data.input)[:-10])
    # in homescreen & "enter" text -> send request to chatbot
    if data.mode == "homeScreen":
        data.selector = False
        for word in data.input.split(" "):
            if isAcronym(word):
                data.numOfUWithSameAcronym = selectFullName(word)[0]
                data.fullNames = selectFullName(word)[1]
                data.selector = True
        if data.selector == True:
            if event.keysym == "Up":
                data.hovered = True
                data.hoverCount -= 1
                if data.hoverCount < 0: # wraparound from top to bottom
                    data.hoverCount = data.numOfUWithSameAcronym + data.hoverCount
            elif event.keysym == "Down":
                data.hovered = True
                data.hoverCount += 1
                if data.hoverCount == data.numOfUWithSameAcronym: # wraparound from bottom to top
                    data.hoverCount = 0
        if event.keysym == "Return" :
            data.input = ("".join(list(data.input)[:-6])).lower()
            if data.hovered:
                data.selectedFullName = data.fullNames[data.hoverCount]
                data.fullNameSelected = True
                data.selector = False
                data.hovered = False
                data.input = data.input[:-len(data.input.split(" ")[-1])]
                data.input += data.selectedFullName
            elif len(data.input)>0:
                data.selector = False
                # pass the entered response to the chatbot
                data.inputHistory.append((data.input,data.requestLine))
                #if logisticRegression(data,str):
                data.output = NLP(data,data.input)
                data.input = ""
                '''
                else:
                    data.output = "Sorry, Octopedia 0.1 can't answer subjective questions yet"'''
                data.outputHistory.append((data.output,data.requestLine))
                data.mode = "IM"
    elif data.mode == "IM":
        data.selector = False
        for word in data.input.split(" "):
            if isAcronym(word):
                data.numOfUWithSameAcronym = selectFullName(word)[0]
                data.fullNames = selectFullName(word)[1]
                data.selector = True
        if data.selector:
            if event.keysym == "Up":
                data.hovered = True
                data.hoverCount -= 1
                if data.hoverCount < 0: # wraparound from top to bottom
                    data.hoverCount = data.numOfUWithSameAcronym + data.hoverCount
            elif event.keysym == "Down":
                data.hovered = True
                data.hoverCount += 1
                if data.hoverCount == data.numOfUWithSameAcronym: # wraparound from bottom to top
                    data.hoverCount = 0
        if event.keysym == "Return":
            if data.hovered:
                data.selectedFullName = data.fullNames[data.hoverCount]
                data.fullNameSelected = True
                data.input = data.input[:-len(data.input.split(" ")[-1])]
                data.input += data.selectedFullName
                data.hovered = False
            data.selector = False
            print(data.requestLine)
            data.requestLine += 1 # keep track of the order of historical messages
            print(data.searchBarTopY)
            print(data.requestLine*10 + data.IMy)
            if  data.requestLine*10 + data.IMy > data.searchBarTopY:
                print("Viewify")
                data.scrollable = True 
            data.input = "".join(list(data.input)[:-6])
            data.inputHistory.append((data.input,data.requestLine))
            data.output = NLP(data,data.input)
            data.outputHistory.append((data.output,data.requestLine))
            #drawRequest(canvas,data,data.output)
        if data.scrollable:
            #Move the IM window up and down   
            if event.keysym == "Up":
                data.IMy -= data.speed
            elif event.keysym == "Down":
                data.IMy += data.speed
    elif data.mode == "login":        
        if event.keysym == "Return":
            data.input = "".join(list(data.input)[:-6])
            if data.userNameEntered and data.emailEntered and data.passwordEntered:
                data.canLogIn = True
            if not data.userNameEntered:
                data.userName = data.input
                if len(data.userName) > 0 :
                    data.userNameEntered = True
                    data.input = ""
            elif not data.emailEntered:
                data.email = data.input
                if re.match(data.email,r"[^@]+@[^@]+\.[^@]+")==None:
                    data.emailEntered = True
                    data.input = ""
            elif not data.passwordEntered:
                data.password = data.input
                if re.match(r'^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$',\
                data.password)==None:
                    data.passwordEntered = True
                    data.input = ""
            elif data.canLogIn:
                data.loggedIn = True
                data.input = ""
                data.mode = "IM"
        else:
            data.inputHistory.append((data.input,data.requestLine))
            if data.userNameEntered and data.emailEntered and data.passwordEntered:
                data.canLogIn = True
            if not data.userNameEntered:
                data.userName = data.input
            elif not data.emailEntered:
                data.email = data.input
            elif not data.passwordEntered:
                data.password = data.input
            elif data.canLogIn:
                pass
                
    
def timerFired(data):
    data.timer += 1
    
def drawLogo(canvas,data):
    canvas.create_image(data.cx,data.cy-100,image=data.logo)

def drawSearchBox(canvas,data):
    canvas.create_rectangle(data.searchBarLeftX,data.searchBarTopY,\
data.searchBarRightX,data.searchBarBottomY,fill="white",outline="purple1",width=5)
    
def drawLogInButton(canvas,data):
    canvas.create_rectangle(data.LogInLeftX,data.LogInTopY,data.LogInRightX,\
    data.LogInBottomY,fill="white",outline="purple1",width=5)
    canvas.create_text(data.LogInLeftX+(data.LogInRightX-data.LogInLeftX)/2,\
    data.LogInTopY+(data.LogInBottomY-data.LogInTopY)/2,text="Log in",\
    fill="purple1",font="Palatino 10 bold")
    
def drawLogIn(canvas,data):
    canvas.create_text(data.width//10,data.height//10,text="Octopedia",\
    fill="purple1",font="Palatino 25 bold")
    canvas.create_image(data.LogInLeftX+(data.LogInLeftX-data.LogInRightX/2)\
    ,data.LogInTopY+(data.LogInTopY-data.LogInBottomY)/2,image=data.user) # dunno why not drawn
    canvas.create_rectangle(450,100,850,600,fill="white",outline="purple1",width=1)
    canvas.create_text(550,200,text="Don't have an account yet?'",fill="gray35",font="Palatino 10")
    canvas.create_text(650,200,text="Sign Up",fill="purple1",font="Palatino 10 bold")
    canvas.create_text(500,150,text="Sign In",fill="black",font="Palatino 20 bold")
    canvas.create_rectangle(500,300,700,350,fill="white",outline="gray63",width=1) # username
    canvas.create_rectangle(500,350,700,400,fill="white",outline="gray63",width=1) # email
    canvas.create_rectangle(500,400,700,450,fill="white",outline="gray63",width=1) # password
    if data.canLogIn:
        canvas.create_rectangle(700,450,800,500,fill="purple1",outline="purple1",\
        width=1) # clickable purple login button
    else:
        canvas.create_rectangle(700,450,800,500,fill="gray63",outline="purple1",\
        width=1) # unclickable gray login button
    canvas.create_text(750,475,text="Log in",fill="white",font="Palatino 10 bold")
    
def drawIM(canvas,data):
    drawHomeScreen(canvas,data)
    canvas.create_rectangle(data.searchBarLeftX,data.height//10,data.searchBarRightX\
    ,data.searchBarTopY,outline="purple1",width=5)
    canvas.create_rectangle(538,298,760,372,fill="white",outline="purple1",width=1)
    for requests in data.inputHistory:
        canvas.create_text(data.searchBarRightX-len(requests[0])*10/2,\
        data.height//10+requests[1]*10,text=requests[0],\
            fill="gray63",font="Palatino 10 bold")
    for responses in data.outputHistory:
        canvas.create_text(data.searchBarLeftX+len(responses[0])*10/2\
        ,data.height//10+(responses[1]+1)*10,text=\
        responses[0],fill="purple1",font="Palatino 10 bold")
    canvas.create_text(data.searchBarLeftX+(data.searchBarRightX-data.searchBarLeftX)/2,\
    data.searchBarTopY+(data.searchBarBottomY-data.searchBarTopY)/2,\
    text=data.input,fill="purple1",font="Palatino 20 bold")
    if data.loggedIn:
        # displayMessageHistory data.messageHistory
        if data.scrollable:
            print("Octo")
            for requests in data.inputHistory:
                canvas.create_text(data.searchBarRightX-len(requests[0])*10/2,\
                data.IMy+requests[1]*10,text=requests[0],\
                    fill="gray63",font="Palatino 10 bold")
            for responses in data.outputHistory:
                canvas.create_text(data.searchBarLeftX+len(responses[0])*10/2\
                ,data.IMy+(responses[1]+1)*10,text=\
                responses[0],fill="purple1",font="Palatino 10 bold")
        
        canvas.create_text(data.searchBarLeftX+(data.searchBarRightX-\
        data.searchBarLeftX)/2,data.searchBarBottomY+(data.searchBarBottomY-\
        data.searchBarTopY)/2,text="Welcome back, " + data.userName +" !",\
        fill="purple1",font="Palatino 20 bold")

def drawHomeScreen(canvas,data):
    canvas.create_text(data.width//10,data.height//10,text="Ask Octopus",\
    fill="purple1",font="Palatino 25 bold")
    drawLogo(canvas,data)
    drawSearchBox(canvas,data)
    drawLogInButton(canvas,data)
    if data.timer % 10 == 0:
        canvas.create_line(data.searchBarLeftX+10,data.searchBarTopY,\
            data.searchBarLeftX+10,data.searchBarBottomY)
            
def drawSelector(canvas,data):
    canvas.create_rectangle(data.searchBarLeftX,data.searchBarBottomY,\
    data.searchBarRightX,data.searchBarBottomY+10*data.numOfUWithSameAcronym,\
    fill="white",outline="purple1",width=5)
    for i in range(data.numOfUWithSameAcronym):
        canvas.create_text(data.searchBarLeftX+60,data.searchBarBottomY+10*i+5,text=\
        data.fullNames[i],fill="purple1",font="Palatino 8 bold")
    canvas.create_text(data.searchBarLeftX+(data.searchBarRightX-\
    data.searchBarLeftX)/2,data.searchBarTopY+(data.searchBarBottomY-\
    data.searchBarTopY)/2,text=data.selectedFullName\
    ,fill="purple1",font="Palatino 20 bold")
    data.selectedFullName = ""
    
def redrawAll(canvas, data):
    if data.mode == "homeScreen":
        drawHomeScreen(canvas,data)
        canvas.create_text(data.searchBarLeftX+(data.searchBarRightX-data.searchBarLeftX)/2,\
        data.searchBarTopY+(data.searchBarBottomY-data.searchBarTopY)/2,\
        text=data.input,activefill="purple1",font="Palatino 20 bold")
        if data.selector:
            drawSelector(canvas,data)
            if data.hovered:
                canvas.create_rectangle(data.searchBarLeftX,data.searchBarBottomY+data.hoverCount*10,\
                data.searchBarRightX,data.searchBarBottomY+(data.hoverCount+1)*10,\
                fill="gray63")
    elif data.mode == "IM":
        drawIM(canvas,data)
        if data.selector:
            drawSelector(canvas,data)
            if data.hovered:
                canvas.create_rectangle(data.searchBarLeftX,data.searchBarBottomY+data.hoverCount*10,\
                data.searchBarRightX,data.searchBarBottomY+(data.hoverCount+1)*10,\
                fill="gray63")
        '''
        if data.scrollable:
            drawScrollable(canvas,data)
            if'''
    elif data.mode == "login":
        drawLogIn(canvas,data)
        if data.timer % 10 == 0:
            if not data.userNameEntered: 
                canvas.create_line(510,300,510,350)
            elif not data.emailEntered:
                canvas.create_line(510,350,510,400)
            elif not data.passwordEntered:
                canvas.create_line(510,400,510,450)
        canvas.create_text(600,325,text=data.userName,fill="purple1",\
        font="Palatino 20 bold") # username
        canvas.create_text(600,375,text=data.email,fill="purple1",\
        font="Palatino 20 bold") # email
        canvas.create_text(600,425,text=len(data.password)*"*",fill="purple1",\
        font="Palatino 20 bold") # password
    elif data.mode == "UserAccount":
        pass


####################################
# use the run function as-is, from the course notes
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1300, 750)
