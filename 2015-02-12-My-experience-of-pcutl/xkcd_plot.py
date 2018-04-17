from matplotlib import pyplot as plt
plt.xkcd()

ymin = -25

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xticks([])
plt.yticks([])
ax.set_ylim([ymin, 10])

## My attitude towards PCUTL ##
data = [.9 * ymin  for t in range(5)]
data += [data[-1] + .4 * t ** 1.7 for t in range(5)]
data += [data[-1] + .8 * t for t in range(10)]
data += [data[-1] + .4 * t for t in range(10)]
data += [data[-1] + 1.5 * t for t in range(10)]

plt.annotate(
    "My attitude towards PCUTL",
    xy=(len(data) / 2, data[len(data) / 2]), arrowprops=dict(arrowstyle='->'), xytext=(2, 1))

plt.annotate(
    "'I do not want to be here'",
    xy=(1, data[0]), arrowprops=dict(arrowstyle='->'), xytext=(5, data[0] - 10))

plt.annotate(
    "'I get the journals'",
    xy=(5, data[5]), arrowprops=dict(arrowstyle='->'), xytext=(3, -12))

plt.annotate(
    "'I read literature'",
    xy=(15, data[15]), arrowprops=dict(arrowstyle='->'), xytext=(12, -20))

plt.annotate(
    "'I take pride in my teaching'",
    xy=(25, data[25]), arrowprops=dict(arrowstyle='->'), xytext=(26, -12))

plt.annotate(
    "'I want to do module 4'",
    xy=(35, data[35]), arrowprops=dict(arrowstyle='->'), xytext=(33, -7))

## Support received from PCUTL ##
plt.plot(data)
plt.axhline(5, color='red')
plt.annotate(
    "Support received from PCUTL",
    xy=(35, 5), arrowprops=dict(arrowstyle='->'), xytext=(29, 2))

plt.xlabel('time')
plt.savefig('xkcd_pcul.svg', bbox_inches='tight')
