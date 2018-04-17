A = matrix([[0, -1, 1, 1, -1],
             [1, 0, -1, -1, 1],
             [-1, 1, 0, 1 , -1],
             [-1, 1, -1, 0, 1],
             [1, -1, 1, -1, 0]])

clrs = rainbow(5)
p = plot(x * A[0, 0] + (1 - x) * A[0, 4], x, 0, 1, legend_label="$u(R)$", color=clrs[0], axes_labels=['Proportion of time I play Rock', ''])
p += plot(x * A[1, 0] + (1 - x) * A[1, 4], x, 0, 1, legend_label="$u(P)$", color=clrs[1])
p += plot(x * A[2, 0] + (1 - x) * A[2, 4], x, 0, 1, legend_label="$u(S)$", color=clrs[2])
p += plot(x * A[3, 0] + (1 - x) * A[3, 4], x, 0, 1, legend_label="$u(Lz)$", color=clrs[3])
p += plot(x * A[4, 0] + (1 - x) * A[4, 4], x, 0, 1, legend_label="$u(Sp)$", color=clrs[4])
p.save("plot.pdf")
