from graphics import *
import math
from tkinter import messagebox

print("Welcome!\nLet's play Connect 4")
x=input("Player 1: Blue or Red? (b/r)").lower()
if x=="r":
	col={0:'red',1:'blue'}
else:
	col={0:'blue',1:'red'}


win=GraphWin("Connect 4",700,650)
for i in range(100,700,100):
    l=Line(Point(i,0),Point(i,600))
    l.draw(win)
for i in range(100,700,100):
    l=Line(Point(0,i),Point(700,i))
    l.draw(win)
for i in range(50,700,100):
    for j in range(50,600,100):
        c=Circle(Point(i,j),40)
        c.draw(win)
        

tex=Text(Point(350,625),"Player 1 your chance")
tex.draw(win)
play=0

l0=["*","*","*","*","*","*","*"]
l1=["*","*","*","*","*","*","*"]
l2=["*","*","*","*","*","*","*"]
l3=["*","*","*","*","*","*","*"]
l4=["*","*","*","*","*","*","*"]
l5=["*","*","*","*","*","*","*"]
playno=0
var={1:l1,2:l2,3:l3,4:l4,5:l5,0:l0}
while play<42:
    if play%2==0:
        playno=0
    else:
        playno=1
        
    tex.setText("Player "+str(playno+1)+" your chance")
    tex.setTextColor(col[playno])
    tex.setStyle('bold')

    p1=win.getMouse()
    x,y=p1.getX(),p1.getY()
    
    x,y=int(math.floor(x/100))*100,int(math.floor(y/100))*100
    listno,listindex=int(y/100),int(x/100)

    if listno!=5:
        if var[listno][listindex]=='*' and var[listno+1][listindex]!="*":
            
            c=Circle(Point(x+50,y+50),40)
            c.draw(win)
            c.setFill(col[playno])
                
            var[listno][listindex]=playno
            
            play+=1
        elif var[listno][listindex]!='*':
            messagebox.showerror("Error", "You can only click on empty circle")
        else:
            messagebox.showerror("Error", "You can only click on circle which has a coloured circle below it")
            
    if listno==5:
        if var[listno][listindex]=="*":
            
            c=Circle(Point(x+50,y+50),40)
            c.draw(win)
            c.setFill(col[playno])
            var[listno][listindex]=playno
            play+=1
        else:
            messagebox.showerror("Error", "You can only click on empty circle")
           
    ###checking the circles horizontally
    for l in [l0,l1,l2,l3,l4,l5]:
        for x in range(0,4):
            if l[x]==l[x+1]==l[x+2]==l[x+3]!="*":
                messagebox.showinfo("Information",col[l[x]]+" Won")
                exit()
    randoml=[l0,l1,l2,l3,l4,l5]
    ###checking the circles vertically
    for l in range(7):
        for x in range(0,3):
            if randoml[x][l]==randoml[x+1][l]==randoml[x+2][l]==randoml[x+3][l]!="*":
                messagebox.showinfo("Information",col[randoml[x][l]]+" Won")
                exit()
    ##checking the circles diagonally
    
    for x in range(3,6):
	    for loop in range(1):
		    for y in range(5):
			    if y+3>6:
				    break
			    if var[x][y]==var[x-1][y+1]==var[x-2][y+2]==var[x-3][y+3]!="*":
				    messagebox.showinfo("Information",col[var[x][y]]+" Won")
				    exit()
				#print(x,y)
	    
	
    for x in range(3):
	    for loop in range(1) :
		    for y in range(4):
			    if var[x][y]==var[x+1][y+1]==var[x+2][y+2]==var[x+3][y+3]!="*":
				    messagebox.showinfo("Information",col[var[x][y]]+" Won")
				    exit()
				#print(x,y)
if play==42:
	messagebox.showinfo("Information","Game Over/nIt's a Tie!")    
	
    
    
    
