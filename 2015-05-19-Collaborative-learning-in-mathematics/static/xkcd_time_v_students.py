from __future__ import division
from matplotlib import pyplot as plt
plt.xkcd()

ymin = 0

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xticks([])
plt.yticks([])
ax.set_ylim([ymin, 10])

## My attitude towards PCUTL ##
boundary = range(10)
realistic = [.5 + x ** 2 for x in range(10)]
utopic = [x ** (1 / 2) for x in range(10)]

#plt.annotate(
    #"My attitude towards PCUTL",
    #xy=(len(data) / 2, data[len(data) / 2]), arrowprops=dict(arrowstyle='->'), xytext=(2, 1))

#plt.annotate(
    #"'I do not want to be here'",
    #xy=(1, data[0]), arrowprops=dict(arrowstyle='->'), xytext=(5, data[0] - 10))

#plt.annotate(
    #"'I get the journals'",
    #xy=(5, data[5]), arrowprops=dict(arrowstyle='->'), xytext=(3, -12))

#plt.annotate(
    #"'I read literature'",
    #xy=(15, data[15]), arrowprops=dict(arrowstyle='->'), xytext=(12, -20))

#plt.annotate(
    #"'I take pride in my teaching'",
    #xy=(25, data[25]), arrowprops=dict(arrowstyle='->'), xytext=(26, -12))

#plt.annotate(
    #"'I want to do module 4'",
    #xy=(35, data[35]), arrowprops=dict(arrowstyle='->'), xytext=(33, -7))

## Support received from PCUTL ##
plt.plot(boundary, color='red')
plt.plot(realistic, color='green')
plt.plot(utopic, color='blue')

plt.annotate(
    "Equivalent quantity\n of students \nand time",
    xy=(5, 5), arrowprops=dict(arrowstyle='->'), xytext=(8, 5))

plt.annotate(
    "More students than time",
    xy=(2, 4.5), arrowprops=dict(arrowstyle='->'), xytext=(.25, 10))

plt.annotate(
    "More time \nthan students",
    xy=(4.5, 2), arrowprops=dict(arrowstyle='->'), xytext=(9, 1.5))

plt.scatter([4], [9], s=100, color='grey')

plt.annotate(
    "Time but too many students",
    xy=(4, 9), arrowprops=dict(arrowstyle='->'), xytext=(6, 9.5))

plt.scatter([.5], [2], s=100, color='grey')

plt.annotate(
    "Not much time",
    xy=(.5, 2), arrowprops=dict(arrowstyle='->'), xytext=(.5, 2.5))

plt.xlabel('available time')
plt.ylabel('student numbers')
plt.savefig('xkcd_student_v_time.svg', bbox_inches='tight')
