#!/usr/bin/env python

import rospy
import actionlib
from my_robot_msgs.msg import CountUntilAction
from my_robot_msgs.msg import CountUntilGoal

class CountUntilClient:
	def __init__(self):
		self._ac = actionlib.SimpleActionClient('/count_until', CountUntilAction)
		self._ac.wait_for_server()
		rospy.loginfo("Action server is up, we can send new goals!")

	def send_goal_and_get_result(self):
		goal = CountUntilGoal(max_number=5, wait_duration=1.0)
		self._ac.send_goal(goal, done_cb=self.done_callback)
		rospy.loginfo("Goal has been sent.")
		#self._ac.wait_for_result()
		#rospy.loginfo(self._ac.get_result())

	def done_callback(self, status, result):
		rospy.loginfo("Status is : " + str(status))
		rospy.loginfo("Result is : " + str(result))

if __name__ == '__main__':
	rospy.init_node('count_until_client')
	client = CountUntilClient()
	client.send_goal_and_get_result()
	rospy.spin()