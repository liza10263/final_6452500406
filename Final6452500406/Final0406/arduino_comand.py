#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
	pub = rospy.Publisher("status",String,queue_size=10)
	pub = rospy.Publisher("motion",String,queue_size=10)
	pub = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10)
	rospy.init_node("/arduino_comand")
	rate = rospy.Rate(0.5)

	while(not rospy.is_shutdown()):
		pub.publish("on")
		rate.sleep()	
