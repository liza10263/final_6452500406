#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def run(val):
	if val.data == "senser on":
		rospy.loginfo("on")
	else:
		rospy.loginfo("off")

if __name__ == "__main__":
	sub = rospy.Subscriber("topic_senser",String,callback=run)
	rospy.init_node("serial_nood")
	rospy.spin()
