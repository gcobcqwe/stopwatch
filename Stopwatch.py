# template for "Stopwatch: The Game"
import simplegui
# define global variables

minsecond=0
second=0
minute=0
ten_second=0
ten_minute=0
total=0
succese=0

counter=0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global minsecond
    global second
    global minute
    global ten_second
    global ten_minute
    if t==10:
        minsecond=0
        second=second+1
        if second==10:
            second=0
            ten_second=ten_second+1
        
    if ten_second==6:
        ten_second=0
        minute=minute+1
        if minute==10:
            minute=0
            ten_minute=ten_minute+1
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    timer.start()    
def Stop():
    global total
    global minsecond
    global succese
    timer.stop()
    total=total+1
    if minsecond==0:
        succese=succese+1
def Reset():
    global minsecond
    global second
    global minute
    minsecond=0
    second=0
    minute=0
# define event handler for timer with 0.1 sec interval
def increment():
    global minsecond
    minsecond=minsecond+1
    format(minsecond)
def tick():
    increment()
    
# define draw handler
def draw(canvas):
    canvas.draw_text(str(str(ten_minute)+str(minute)+":"+str(ten_second)+str(second)+"."+str(minsecond)), [50,112], 36, "Red")
    canvas.draw_text(str(str(succese)+"/"+str(total)), [100,20], 24, "blue")    
# create frame
frame = simplegui.create_frame("test", 300, 200)
frame.add_button("Start", Start)
frame.add_button("Stop", Stop)
frame.add_button("Reset", Reset)
frame.set_draw_handler(draw)
timer=simplegui.create_timer(100,tick)

# register event handlers


# start frame

frame.start()
# Please remember to review the grading rubric
