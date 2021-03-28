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

  'i':(1,0),
  'o':(1,-1),
  'j':(0,1),
  'l':(0,-1),
  'u':(1,1),
  ',':(-1,0),
  '.':(-1,1),
  'm':(-1,-1)
"""

moveBindings = {
        'i':(1,0),
        'o':(1,-1),
        'j':(0,1),
        'l':(0,-1),
        'u':(1,1),
        ',':(-1,0),
        '.':(-1,1),
        'm':(-1,-1),
           }

#speedBindings={
#        'q':(1.1,1.1),
#        'z':(.9,.9),
#        'w':(1.1,1),
#        'x':(.9,1),
#       'e':(1,1.1),
#        'c':(1,.9),
#         }

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

speed = 8
turn = 8

def vels(speed,turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    
    rospy.init_node('turtlebot_teleop')

    pub_ltclj = rospy.Publisher('/krab/controller_ltclj/command', Float64, queue_size=10) # Add your topic here between ''. Eg '/my_robot/steering_controller/command'
    pub_ltlj = rospy.Publisher('/krab/controller_ltlj/command', Float64, queue_size=10)
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
    # pub_move = rospy.Publisher('/krab/controller_rear/command', Float64, queue_size=10) # Add your topic for move here '' Eg '/my_robot/longitudinal_controller/command'

    x = 0
    th = 0
    status = 0
    count = 0
    acc = 0.1
    target_speed = 0
    target_turn = 0
    control_speed = 0
    control_turn = 0
    try:
        print msg
        print vels(speed,turn)
        while(1):
            key = getKey()
            if key in moveBindings.keys():
                x = moveBindings[key][0]
                th = moveBindings[key][1]
                count = 0
#            elif key in speedBindings.keys():
#                speed = speed * speedBindings[key][0]
#                turn = turn * speedBindings[key][1]
#                count = 0

                print vels(speed,turn)
                if (status == 14):
                    print msg
                status = (status + 1) % 15
            elif key == ' ' or key == 'k' :
                x = 0
                th = 0
                control_speed = 0
                control_turn = 0
            else:
                count = count + 1
                if count > 4:
                    x = 0
                    th = 0
                if (key == '\x03'):
                    break

            target_speed = speed * x
            target_turn = turn * th

            if target_speed > control_speed:
                control_speed = min( target_speed, control_speed + 0.02 )
            elif target_speed < control_speed:
                control_speed = max( target_speed, control_speed - 0.02 )
            else:
                control_speed = target_speed

            if target_turn > control_turn:
                control_turn = min( target_turn, control_turn + 0.1 )
            elif target_turn < control_turn:
                control_turn = max( target_turn, control_turn - 0.1 )
            else:
                control_turn = target_turn

            pub_ltclj.publish(control_speed) # publish the turn command.
            pub_ltlj.publish(control_speed) # publish the turn command.
            # pub_move.publish(-control_speed) # publish the control speed. 


    except:
        print e

    finally:
        pub_ltclj.publish(control_speed)
        pub_ltlj.publish(control_speed)
        # pub_move.publish(-control_speed)
        # twist = Twist()
        # twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
        # twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
        # pub.publish(twist)

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)