#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from atra4374_hw1.srv import AddTwoInts
from atra4374_hw1.srv import AddTwoIntsRequest
from atra4374_hw1.srv import AddTwoIntsResponse
import matplotlib
import matplotlib.pyplot as plt
import pylab

latency_array = []
message_number = []

def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    try:
        start_time = rospy.get_time()
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        resp1 = add_two_ints(x, y)
        end_time = rospy.get_time()
        latency = end_time - start_time
        # print(float(latency)*1000000)
        latency_array.append(float(latency)*1000000)
        return resp1.sum
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

for x in range(300):
    if __name__ == "__main__":
        rospy.init_node('random_node')
        if len(sys.argv) == 3:
            x = int(sys.argv[1])
            y = int(sys.argv[2])
        else:
            print(usage())
            sys.exit(1)
        message_number.append(x)
        print("Requesting %s+%s"%(x, y))
        print("%s + %s = %s"%(x, y, add_two_ints_client(x, y)))
# print(latency_array)
plt.ylabel('Number of Messages')
plt.xlabel('Latency (Microseconds)')
plt.title('Latency distribution for Message sent through rosservice')
plt.hist(latency_array,bins =100)
plt.show()