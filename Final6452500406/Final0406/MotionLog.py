#!/usr/bin/env python3
from tkinter import*
import rospy
from geometry_msgs.msg import Twist

frame = Tk()
frame.title("REMOTE")
frame.geometry("400x200")

rospy.init_node("MotionLog")
##sub = rospy.Subscriber("motion",motion,callback)
##sub = rospy.Subscriber("/turtle1/pose",Pose,callback=run)
##sub = rospy.Subscriber("motion",tring,callback=run)
##ex pub = rospy.Publisher("chatter",String,queue_size=10)

def fw():
	print("fw")
	cmd = Twist()
	cmd.linear.x = 1.0
	cmd.angular.z=0.0
	pub.publish(cmd)



 



frame.mainloop()
