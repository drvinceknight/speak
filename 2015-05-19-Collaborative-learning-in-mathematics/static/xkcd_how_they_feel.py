from __future__ import division
from matplotlib import pyplot as plt
from math import sin
from random import random, seed
seed(2)
plt.xkcd()

ymin = -2

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xticks([])
plt.yticks([])
ax.set_ylim([ymin, 14])

beginning = [9 for k in range(12)] + [0 for k in range(28)]
middle = [6, 6, 6, 6]
end = [6 + 2 * sin(k) + 4 * random() for k in range(40)]

feeling = beginning + middle + end

plt.plot(feeling, color='blue')

plt.annotate(
    "What is a 'hackathing'?",
    xy=(0, 9), arrowprops=dict(arrowstyle='->'), xytext=(2, 11.5))

plt.annotate(
    "This is s**t!",
    xy=(12, 0), arrowprops=dict(arrowstyle='->'), xytext=(1, -1.5))

plt.annotate(
    "I am so alone.",
    xy=(25, 0), arrowprops=dict(arrowstyle='->'), xytext=(15, 6.5))

plt.annotate(
    "Maybe Vince\nwill make it\nall stop.",
    xy=(39, 0), arrowprops=dict(arrowstyle='->'), xytext=(45, .5))

plt.annotate(
    "Let us work\ntogether.",
    xy=(40, 6), arrowprops=dict(arrowstyle='->'), xytext=(63, 2))

plt.annotate(
    "Oh, Vince\nactually answers\nquestions today.",
    xy=(55, 6), arrowprops=dict(arrowstyle='->'), xytext=(60, 13))

plt.axvline(40, color='red', linestyle='--')
plt.xlabel('time')
plt.ylabel('moral')
plt.savefig('xkcd_how_they_feel.svg', bbox_inches='tight')
