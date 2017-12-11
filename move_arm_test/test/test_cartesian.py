#!/usr/bin/python
##Reference : http://wiki.ros.org/unittest
## https://github.com/ros/ros_tutorials/tree/hydro-devel/rospy_tutorials/test


import rosunit
import rospy
import rostest
import sys
import unittest
PKG = 'move_arm_test'

from std_msgs.msg import String
from geometry_msgs.msg import TwistStamped


class TestCartesian(unittest.TestCase):
    def setUp(self):
        # super(TestPeerSubscribeListener, self).__init__(*args)
        # self.success = False
        self.result = TwistStamped()
        self.wait_for_result = False
        rospy.Subscriber("/arm_1/arm_controller/cartesian_velocity_command",TwistStamped,self.callback)

    def case1(self):
        self.assertEquals(1, 1, "1!=1")

    def callback(self, data):
        print(rospy.get_caller_id(), "I heard %s" % data.data)
        #greetings is only sent over peer_publish callback, so hearing it is a success condition
        if data.data.startswith('greetings'):
            self.success = True


if __name__ == '__main__':
    rospy.init_node('test_cartesian')
    rostest.rosrun(PKG, 'test_cartersian', TestCartesian)
    rospy.spin()
