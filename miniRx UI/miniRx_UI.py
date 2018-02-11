# Updated Animation Starter Code

from tkinter import *

####################################
# Color palette
darkerRed  = "#C14242"
mediumRed  = "#D36262"
lighterRed = "#F2ADAD"

####################################

def init(data):
    data.mode   = "cameraScreen"
    data.width  = 1920
    data.height = 1080
    
    # Profile Data
    data.userName = ""
    data.profileImage = []
    
    data.drugNames = ["Rosuvastatin", "Pregabalin", "Sitagliptin"]
    data.drugChecked = [False] * len(data.drugNames)
    data.dosages = []

"""
def loadBackgroundPattern(data):
    fileName = "plusSignPattern_2.gif"
    data.bgImage = PhotoImage(file=fileName)
    return data.bgImage
"""

def mousePressed(event, data):
    # use event.x and event.y
    if (data.mode == "cameraScreen"): cameraScreenMousePressed(event, data)
    elif (data.mode == "selectionScreen"): selectionScreenMousePressed(event, data)
    elif (data.mode == "endScreen"): endScreenMousePressed(event, data)
    

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    if (data.mode == "cameraScreen"): cameraScreenRedrawAll(canvas, data)
    elif (data.mode == "selectionScreen"): selectionScreenRedrawAll(canvas, data)
    elif (data.mode == "endScreen") : endScreenRedrawAll(canvas, data)
####################################
# cameraScreen mode
####################################

def cameraScreenMousePressed(event, data):
    picTrigRadius = data.width*.035
    picTrigCenterX = (data.height*.028 + data.width*.42)/2
    picTrigCenterY = data.height*.972 - picTrigRadius*1.4
    
    print('click')
    # Take a picture, store it, and show it on next screen
    if picTrigCenterX-picTrigRadius < event.x < picTrigCenterX+picTrigRadius:
        if picTrigCenterY-picTrigRadius < event.y < picTrigCenterY+picTrigRadius:
            data.mode = "selectionScreen"
    

def cameraScreenRedrawAll(canvas, data):
    
    # Background
    #canvas.create_rectangle(0, 0, data.width, data.height, fill=darkerRed, width=0)
    
    #canvas.create_image(0, 0, anchor=NW, image=data.bgImage)
    
    # Camera frame
    canvas.create_rectangle(data.height*.028, data.height*.028, \
                            data.width*.42, data.height*.972, \
                            fill=lighterRed, width=0)

    # Picture trigger - red circle with white ring
    picTrigRadius = data.width*.035
    picTrigCenterX = (data.height*.028 + data.width*.42)/2
    picTrigCenterY = data.height*.972 - picTrigRadius*1.4
        
    canvas.create_oval(picTrigCenterX - picTrigRadius, \
                        picTrigCenterY - picTrigRadius, \
                        picTrigCenterX + picTrigRadius, \
                        picTrigCenterY + picTrigRadius, \
                        fill=darkerRed, outline="white", width=data.width*.005)
                        
    # Tooltip
    tipSize = int(data.height*(32/1080))
    canvas.create_text(data.width*.7, \
                       data.height*.5, \
                       text="Please take\n  a picture.", \
                       fill="white", \
                       font=("Helvetica", tipSize, "bold"))

####################################
# selectionScreen mode
####################################
def selectionScreenMousePressed(event, data):
    print('click')
    checkboxWidth = data.width*(85/1920)
    vertSpacing = data.height*(173/1080)
    startingHeight = data.height*(381/1080)
    # If within the boundaries of a checkbox, toggle check
    if data.width*(1632/1920) < event.x < (data.width*(1632/1920))+checkboxWidth:
        if startingHeight < event.y < startingHeight+checkboxWidth:
            print('0')
            data.drugChecked[0] = not data.drugChecked[0]
       
        if startingHeight+vertSpacing < event.y < startingHeight + \
        vertSpacing + checkboxWidth:
            print('1')
            data.drugChecked[1] = not data.drugChecked[1]

        if startingHeight + vertSpacing*2 < event.y < startingHeight + \
        vertSpacing*2 + checkboxWidth:
            print('2')
            data.drugChecked[2] = not data.drugChecked[2]
           
    if data.width*(985/1920) < event.x < data.width*((985+750)/1920) and\
    data.height*(891/1080) < event.y < data.height*((891+131)/1080):
        data.mode = "endScreen"
    

def drawConfirmationButton(canvas, data):
    # Confirmation button w/ text
    canvas.create_rectangle(data.width*(985/1920), data.height*(891/1080), \
        data.width*((985+750)/1920), data.height*((891+131)/1080), \
        fill=mediumRed, width=0)
        
    canvas.create_text(data.width*((985+(750/2))/1920), \
        data.height*((891+(131/2))/1080), \
        text="Confirm", fill="white", \
        font=("Helvetica", 16, "bold"))
    
def drawDrugList(canvas, data):
    # Drug list
    for i in range(len(data.drugNames)):
        # Checkboxes
        checkboxX = data.width*(1632/1920)
        checkboxY = data.height*(381/1080) + i*(data.height*(173/1080))
        size = data.height*(85/1080)
        canvas.create_rectangle(checkboxX, checkboxY, \
            checkboxX + size, checkboxY + size, \
            fill=mediumRed, width=0)
        
        # Dots for inside checkboxes - if selected, draws it
        if data.drugChecked[i]:
            dotOffset = data.height*(20/1080)
            canvas.create_oval(checkboxX+dotOffset, checkboxY+dotOffset, \
                checkboxX+size-dotOffset, checkboxY+size-dotOffset, \
                fill="white", width=0)
            
        # Labels
        labelSize = int(data.height*(24/1080))
        canvas.create_text(data.width*(985/1920), checkboxY, anchor=NW, \
            fill="white", text=data.drugNames[i], \
            font=("Helvetica", labelSize, "bold"))

def drawStaticImageFrame(canvas, data):
    # Image frame, placeholder
    canvas.create_rectangle(data.height*.028, data.height*.028, \
                            data.width*.42, data.height*.972, \
                            fill=lighterRed, width=0)
                            
def drawUserGreeting(canvas, data):
    # Writes "hello, [name]" depending on profile grabbed
    greetSize = int(data.height*(32/1080))
    canvas.create_text(data.width*(985/1920), data.height*.028, anchor=NW, \
                       fill="white", text="Hello, "+data.userName+".", \
                       font=("Helvetica", greetSize, "bold italic"))

def selectionScreenRedrawAll(canvas, data):
    #canvas.create_rectangle(0, 0, data.width, data.height, \
    #                        fill=darkerRed, width=0)

    drawStaticImageFrame(canvas, data)
    drawConfirmationButton(canvas, data)
    drawDrugList(canvas, data)
    drawUserGreeting(canvas, data)

####################################
# selectionScreen mode
####################################

def endScreenMousePressed(event, data):
    radius = data.width*(100/1920)
    if data.width/2-radius < event.x < data.width/2+radius and \
    data.height*.8-radius < event.y < data.height*.8+radius:
        data.mode = "cameraScreen"

def endScreenRedrawAll(canvas, data):
    
    
    # Thank You
    canvas.create_text(data.width/2, data.height/2, \
        text="""           Thank you for using miniRx.
Please remember to take your prescription.""", \
        fill="white", font=("Helvetica", 16, "bold"))
        
    # Button to return to cameraScreen
    radius = data.width*(100/1920)
    canvas.create_oval(data.width/2-radius, data.height*.8-radius, \
        data.width/2+radius, data.height*.8+radius, \
        fill=mediumRed, outline="white", width=15)
    
    
####################################
# Run UI
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        canvas.create_rectangle(0, 0, data.width, data.height, \
                                fill=darkerRed, width=0)

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
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
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

run(1920, 1080)