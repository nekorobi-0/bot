import matplotlib as mpl
mpl.use('Agg') # この行を追記
import matplotlib.pyplot as plt

x = [100, 200, 300, 400, 500, 600]
y = [10, 20, 30, 50, 80, 130]

plt.plot(x, y);
plt.savefig("hoge.png") # この行を追記