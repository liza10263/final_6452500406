#!/usr/bin/env python3
from tkinter import*
import rospy
from geometry_msgs.msg import Twist

frame = Tk()
frame.title("REMOTE")
frame.geometry("400x200")

rospy.init_node("Turtle_Control")
pub = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10)
##pub = rospy.Publisher("motion",String,queue_size=10)

def fw():
	print("fw")
	cmd = Twist()
	cmd.linear.x = 1.0
	cmd.angular.z=0.0
	pub.publish(cmd)

def bw():
	print("bw")
	cmd = Twist()
	cmd.linear.x = -1.0
	cmd.angular.z=0.0
	pub.publish(cmd)

def lt():
	print("lt")
	cmd = Twist()
	cmd.linear.x = 0.0
	cmd.angular.z= 1.0
	pub.publish(cmd)

def rt():
	print("rt")
	cmd = Twist()
	cmd.linear.x = 0.0
	cmd.angular.z= -1.0
	pub.publish(cmd)
	
def new_button_click():
    	print("New Button Clicked")
    	cmd = Twist()
    	cmd.linear.x = 1.0
    	cmd.angular.z= 1.0
    	pub.publish(cmd)
    
def new_button2_click():
    	print("New Button Two Clicked")
    	cmd = Twist()
    	cmd.linear.x = 1.0
    	cmd.angular.z= -1.0
    	pub.publish(cmd)

 

B1 = Button(text = "FW", command=fw)
B1.place(x=73, y=20)
B2 = Button(text = "BW", command=bw)
B2.place(x=73, y=130)
B3 = Button(text = "LT", command=lt)
B3.place(x=20, y=80)
B4 = Button(text = "RT", command=rt)
B4.place(x=128, y=80)

canvas1 = Canvas(frame, width=50, height=50, bg='white')
canvas1.place(x=328, y=20)
oval1 = canvas1.create_oval(5, 5, 45, 45, fill='blue', outline='black')
text1 = canvas1.create_text(25, 25, text="SL", fill="white")
canvas1.tag_bind(oval1, '<Button-1>', lambda event: new_button_click())

canvas2 = Canvas(frame, width=50, height=50, bg='white')
canvas2.place(x=328, y=130)
oval2 = canvas2.create_oval(5, 5, 45, 45, fill='blue', outline='black')
text2 = canvas2.create_text(25, 25, text="SR", fill="white")
canvas2.tag_bind(oval2, '<Button-1>', lambda event: new_button2_click())




frame.mainloop()
