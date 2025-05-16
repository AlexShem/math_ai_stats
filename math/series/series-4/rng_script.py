# Problem 1

import numpy as np

rng = np.random.default_rng(seed=827401831)

# Генерируем 1000 равномерных чисел
u = rng.random(1000)

coin_flips = (u < 0.5).astype(int)  # 0 - орёл, 1 - решка

heads_count = np.sum(coin_flips == 0)
tails_count = np.sum(coin_flips == 1)
print("Орёл:", heads_count, "Решка:", tails_count)

dice_rolls = (u * 6).astype(int) + 1

for face in range(1, 7):
    count = np.sum(dice_rolls == face)
    print(f"Грань {face}: {count}")

# Problem 2

import matplotlib.pyplot as plt

plt.hist(coin_flips, bins=[-0.5, 0.5, 1.5], edgecolor='black', align='mid')
plt.xticks([0, 1], ["Орёл", "Решка"])
plt.title("Результаты подбрасывания монеты")
plt.xlabel("Исход")
plt.ylabel("Частота")
plt.show()

plt.hist(dice_rolls, bins=np.arange(0.5, 7.5, 1), edgecolor='black', align='mid')
plt.xticks([1, 2, 3, 4, 5, 6])
plt.title("Результаты броска кубика")
plt.xlabel("Исход")
plt.ylabel("Частота")
plt.show()

# Problem 3

data = rng.normal(loc=0, scale=1, size=1000)

plt.hist(data, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
plt.title("Гистограмма нормального распределения")
plt.xlabel("Значение")
plt.ylabel("Плотность")
plt.show()

from scipy.stats import norm

x = np.linspace(-4, 4, 100)
pdf = norm.pdf(x, loc=0, scale=1)

plt.hist(data, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
plt.plot(x, pdf, 'r-', lw=2)
plt.title("Нормальное распределение с теоретической плотностью")
plt.xlabel("Значение")
plt.ylabel("Плотность")
plt.show()

# Problem 4

data1 = rng.normal(loc=-2, scale=1, size=1000)
data2 = rng.normal(loc=2, scale=1, size=1000)

combined_data = np.concatenate((data1, data2))

plt.hist(combined_data, bins=30, density=True, alpha=0.6, edgecolor='black')
plt.title("Гистограмма объединённых данных")
plt.xlabel("Значение")
plt.ylabel("Плотность")
plt.show()

from scipy.stats import gaussian_kde

kde = gaussian_kde(combined_data)
x_vals = np.linspace(-6, 6, 200)
density_vals = kde(x_vals)

plt.hist(combined_data, bins=30, density=True, alpha=0.6, edgecolor='black')
plt.plot(x_vals, density_vals, 'r-', lw=2)
plt.title("Объединённое распределение с оценкой плотности")
plt.xlabel("Значение")
plt.ylabel("Плотность")
plt.show()
