from __future__ import division
from matplotlib import pyplot as plt
plt.xkcd()

ymin = -2

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xticks([])
plt.yticks([])
ax.set_ylim([ymin, 14])

beginning = [9 + .5 * x for x in range(5)]
middle = [11 - (2 * x) ** (1/2) for x in range(5)]
end = [x ** (1.2) for x in range(10)]

feeling = beginning + middle + end

plt.plot(feeling, color='blue')

plt.annotate(
    "Remember how\nmuch fun last\nyear was",
    xy=(0, 9), arrowprops=dict(arrowstyle='->'), xytext=(.5, 2.5))

plt.annotate(
    "'This is s**t!'",
    xy=(4, 11), arrowprops=dict(arrowstyle='->'), xytext=(3.5, 5.5))

plt.annotate(
    "Student difficulties",
    xy=(6, 9.5), arrowprops=dict(arrowstyle='->'), xytext=(5.5, 12))

plt.annotate(
    "First (only)\ntears",
    xy=(9.5, 4.5), arrowprops=dict(arrowstyle='->'), xytext=(10.5, 8))

plt.annotate(
    "Reinvigoration",
    xy=(15, 6.5), arrowprops=dict(arrowstyle='->'), xytext=(12.5, 1))

plt.annotate(
    "Exhaustion",
    xy=(10, 0), arrowprops=dict(arrowstyle='->'), xytext=(5.5, 1))

plt.annotate(
    "Pride",
    xy=(19, 14), arrowprops=dict(arrowstyle='->'), xytext=(15, 13))

plt.axvline(10, color='red', linestyle='--')
plt.xlabel('time')
plt.ylabel('moral')
plt.savefig('xkcd_how_we_feel.svg', bbox_inches='tight')
