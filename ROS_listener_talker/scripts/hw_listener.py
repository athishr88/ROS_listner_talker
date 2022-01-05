#!/usr/bin/env python

import rospy
from std_msgs.msg import Header
import matplotlib
import matplotlib.pyplot as plt
import pylab

# import std_msgs.msg ##
latency_array = []
time_step = []
x = 0

def callback(data):
    h = Header() ##
    h.stamp = rospy.Time.now()  ##
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.frame_id)
    pub_time = data.stamp
    global x

    if x < 300:
        latency = h.stamp - pub_time
        str_latency = str(latency)
        num_latency = int(str_latency)
        fin_latency = num_latency/1000
        global latency_array
        latency_array.append(fin_latency)
        global time_step
        time_step.append(x)
        
    x += 1
    
    if x == 300:
        plt.ylabel('Number of Messages')
        plt.xlabel('Latency (Microseconds)')
        plt.title('Latency distribution for messages sent through ros topic')
        plt.hist(latency_array,bins =100)
        plt.show()


        # print(num_latency)

def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('chatter', Header, callback)

    rospy.spin()
    # rospy.sleep(20)
    

if __name__ == '__main__':
    listener()
