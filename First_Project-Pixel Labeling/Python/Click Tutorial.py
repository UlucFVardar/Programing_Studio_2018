from Tkinter import *


# author=__Uluc Furkan Vardar__

'''
code for to get coordinate of leftClick

you can change button with image that you want to paint ( hint : Search ImageTK lib. )
'''

def main():
	root = Tk () 
	btn=Button (root,text='Pick Color' , command=getColor)
	btn.grid(row=0,column=0)
	btn.bind("<Button-1>",printcoords)
	root.mainloop()


def getColor():
	pass


def printcoords(event): 
	print "coordinate X>",event.x," coordinate Y>",event.y
	
	
if __name__=='__main__':
    main()