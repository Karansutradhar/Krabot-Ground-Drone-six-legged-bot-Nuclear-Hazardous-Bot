#!/usr/bin/env python
import rospy

from std_msgs.msg import Float64

import sys, select, termios, tty

msg = """
Control Your Robot!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

  'i':(0,0,0,0,0,0,0,0),
  'o':(-2,0,0,0,0,0,0,0),
  'j':(-2,0,0,0,0,0,0,0),
  'l':(0,-1),
  'u':(1,1),
  ',':(-1,0),
  '.':(-1,1),
  'm':(-1,-1)
"""

moveBindings = {
		'u':(0,0,0,0,0,0,0,0,0),
		'i':(0,0,1.22,0,0,0,0,0,0),
		'o':(0.81,0,1.22,0,0,0,0,0,0),
		'j':(0.81,0,1.22,0,-0.89,0,0,0,0),
		'k':(0.81,0,1.22,0,-0.89,0,0.328,0.328,0),
		'l':(0.81,-1,1.3,0,-0.3,1.57,0.328,0.328,0),
		'n':(3.14,-1,1.3,0,-0.3,1.57,0.328,0.328,0),
		'm':(3.14,-1,1.3,0,-0.3,0,0,0,0),
		'p':(0,-1,1.4,0,-0.3,0,0,0,0),
		'd':(0,0,0,0,0,0,0,0,-1),
		   }

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

if __name__=="__main__":
	settings = termios.tcgetattr(sys.stdin)
	
	rospy.init_node('turtlebot_teleop')

	pub_ltclj = rospy.Publisher('/krab/controller_ltclj/command', Float64, queue_size=1) # Add your topic here between ''. Eg '/my_robot/steering_controller/command'
	pub_ltlj = rospy.Publisher('/krab/controller_ltlj/command', Float64, queue_size=1)
	pub_lcclj = rospy.Publisher('/krab/controller_lcclj/command', Float64, queue_size=1) # Add your topic here between ''. Eg '/my_robot/steering_controller/command'
	pub_lclj = rospy.Publisher('/krab/controller_lclj/command', Float64, queue_size=1)
	pub_lbclj = rospy.Publisher('/krab/controller_lbclj/command', Float64, queue_size=1) # Add your topic here between ''. Eg '/my_robot/steering_controller/command'
	pub_lblj = rospy.Publisher('/krab/controller_lblj/command', Float64, queue_size=1)
	pub_rtclj = rospy.Publisher('/krab/controller_rtclj/command', Float64, queue_size=1) # Add your topic here between ''. Eg '/my_robot/steering_controller/command'
	pub_rtlj = rospy.Publisher('/krab/controller_rtlj/command', Float64, queue_size=1)
	pub_rcclj = rospy.Publisher('/krab/controller_rcclj/command', Float64, queue_size=1) # Add your topic here between ''. Eg '/my_robot/steering_controller/command'
	pub_rclj = rospy.Publisher('/krab/controller_rclj/command', Float64, queue_size=1)
	pub_rbclj = rospy.Publisher('/krab/controller_rbclj/command', Float64, queue_size=1) # Add your topic here between ''. Eg '/my_robot/steering_controller/command'
	pub_rblj = rospy.Publisher('/krab/controller_rblj/command', Float64, queue_size=1)
	pub_mbj = rospy.Publisher('/krab/controller_mbj/command', Float64, queue_size=1)
	pub_m1j = rospy.Publisher('/krab/controller_m1j/command', Float64, queue_size=1)
	pub_m2j = rospy.Publisher('/krab/controller_m2j/command', Float64, queue_size=1)
	pub_e1j = rospy.Publisher('/krab/controller_e1j/command', Float64, queue_size=1)
	pub_e2j = rospy.Publisher('/krab/controller_e2j/command', Float64, queue_size=1)
	pub_e3j = rospy.Publisher('/krab/controller_e3j/command', Float64, queue_size=1)
	pub_g1j = rospy.Publisher('/krab/controller_g1j/command', Float64, queue_size=1)
	pub_g2j = rospy.Publisher('/krab/controller_g2j/command', Float64, queue_size=1)
	pub_taryj = rospy.Publisher('/krab/controller_taryj/command', Float64, queue_size=1)
	# pub_move = rospy.Publisher('/krab/controller_rear/command', Float64, queue_size=10) # Add your topic for move here '' Eg '/my_robot/longitudinal_controller/command'

	v1 = 0
	v2 = 0
	v3 = 0
	v4 = 0
	v5 = 0
	v6 = 0
	v7 = 0
	v8 = 0
	v9 = 0

	try:
		print msg
		while(1):
			key = getKey()
			if key in moveBindings.keys():
				v1 = moveBindings[key][0]
				v2 = moveBindings[key][1]
				v3 = moveBindings[key][2]
				v4 = moveBindings[key][3]
				v5 = moveBindings[key][4]
				v6 = moveBindings[key][5]
				v7 = moveBindings[key][6]
				v8 = moveBindings[key][7]
				v9 = moveBindings[key][8]

			pub_mbj.publish(v1)
			#rospy.sleep(2.)
			pub_m1j.publish(v2)
			#rospy.sleep(2.)
			pub_m2j.publish(v3)
			#rospy.sleep(8.)
			pub_e1j.publish(v4)
			#rospy.sleep(4.)
			pub_e2j.publish(v5)
			#rospy.sleep(4.)
			pub_e3j.publish(v6)
			#rospy.sleep(1.)
			pub_g1j.publish(v7)
			#rospy.sleep(1.)
			pub_g2j.publish(v8)
			#rospy.sleep(6.)
			pub_taryj.publish(v9)
			#print('just checking...')
			
			#pub_ltlj.publish(-0.785)
#            print('Sleeping for first time')
#            rospy.sleep(4.)


			# pub_ltclj.publish(-0.785)
#            print("Sleeping for second time")
#            rospy.sleep(4.)

			# 

			# rospy.sleep(2.)
			# pub_ltlj.publish(0)
			# rospy.sleep(2.)
			# #break

			# pub_rtlj.publish(-0.785)
			# pub_rtclj.publish(0.785)
			# rospy.sleep(2.)
			# pub_rtlj.publish(0)
			# rospy.sleep(2.)

			# pub_lblj.publish(-0.785)
			# pub_lbclj.publish(-0.785)
			# rospy.sleep(2.)
			# pub_lblj.publish(0)
			# rospy.sleep(2.)

			# pub_rblj.publish(-0.785)
			# pub_rbclj.publish(0.785)
			# rospy.sleep(2.)
			# pub_rblj.publish(0)
			# rospy.sleep(2.)

			# pub_lclj.publish(-0.785)
			# pub_rcclj.publish(0.785)
			# rospy.sleep(2.)
			# pub_lclj.publish(0)
			# rospy.sleep(2.)

			# pub_rclj.publish(-0.785)
			# pub_rcclj.publish(0.785)
			# rospy.sleep(2.)
			# pub_rclj.publish(0)
			# rospy.sleep(2.)

			
			# print('tray maoving...')
			# pub_taryj.publish(-1)



			#pub_rtlj.publish(-0.785)
			#pub_rtclj.publish(0.785)
			#pub_rtlj.publish(0)

#            pub_rcclj.publish(-control_speed)
#            pub_rclj.publish(-control_speed)
#            pub_rcclj.publish(0)
#            pub_rclj.publish(0)

#            pub_lbclj.publish(control_speed)
#            pub_lblj.publish(control_speed)
#            pub_lbclj.publish(0)
#            pub_lblj.publish(0)

#            pub_rtclj.publish(-control_speed)
#            pub_rtlj.publish(-control_speed)
#            pub_rtclj.publish(0)
#            pub_rtlj.publish(0)

#            pub_lcclj.publish(control_speed)
#            pub_lclj.publish(control_speed)
#            pub_lcclj.publish(0)
#            pub_lclj.publish(0)

#            pub_rbclj.publish(-control_speed)
#            pub_rblj.publish(-control_speed)
#            pub_rbclj.publish(0)
#            pub_rblj.publish(0)
			# pub_move.publish(-control_speed) # publish the control speed. 


	except:
		pass

	finally:
		pass
#        pub_ltlj.publish(-0.785)
#        rospy.sleep(4.)


#        pub_ltclj.publish(-0.785)
#        rospy.sleep(4.)

#       pub_ltlj.publish(0)
#        rospy.sleep(4.)

#        pub_rcclj.publish(-control_speed)
#        pub_rclj.publish(-control_speed)
#        pub_rcclj.publish(0)
#        pub_rclj.publish(0)

#        pub_lbclj.publish(control_speed)
#        pub_lblj.publish(control_speed)
#        pub_lbclj.publish(0)
#        pub_lblj.publish(0)

#        pub_rtclj.publish(-control_speed)
#        pub_rtlj.publish(-control_speed)
#        pub_rtclj.publish(0)
#        pub_rtlj.publish(0)

#        pub_lcclj.publish(control_speed)
#        pub_lclj.publish(control_speed)
#        pub_lcclj.publish(0)
#        pub_lclj.publish(0)

#        pub_rbclj.publish(-control_speed)
#        pub_rblj.publish(-control_speed)
#        pub_rbclj.publish(0)
#        pub_rblj.publish(0)
		# pub_move.publish(-control_speed)
		# twist = Twist()
		# twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
		# twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
		# pub.publish(twist)

	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)