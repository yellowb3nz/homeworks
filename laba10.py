import numpy as np
import matplotlib.pyplot as plt
from scipy.special import *
import matplotlib.animation as anim
from matplotlib.widgets import Slider

# Задание 1
x = np.linspace(-1, 1, 400)

plt.figure(figsize=(10, 6))
plt.title('Полиномы Лежандра')

for n in range(1, 8):
    y = legendre(n)(x)
    plt.plot(x, y, label=f'n = {n}')

plt.legend(title='Степень', loc='upper right', bbox_to_anchor=(1.1, 1))
plt.grid()
plt.show()

# Задание 2
# t = np.linspace(0, 2*np.pi, 1000)
# frequencies = [(3, 2), (3, 4), (5, 4), (5, 6)]

# fig, axs = plt.subplots(2, 2, figsize=(12, 12))
# for i, ax in enumerate(axs.flat):
#     x = np.sin(frequencies[i][0] * t)
#     y = np.sin(frequencies[i][1] * t)
#     ax.plot(x, y)
#     ax.set_title(f'Фигура Лисажу ({frequencies[i][0]}:{frequencies[i][1]})')
#     ax.set_xlabel('sin(' + str(frequencies[i][0]) + 't)')
#     ax.set_ylabel('sin(' + str(frequencies[i][1]) + 't)')

# plt.tight_layout()
# plt.show()

# Задание 3
# fig, ax = plt.subplots()
# ax.set_xlim(-1.5, 1.5)
# ax.set_ylim(-1.5, 1.5)
# val = np.linspace(0, 2 * np.pi, 1000)
# line, = ax.plot([], [], lw=2)

# def init():
#     line.set_data([], [])
#     return line,

# def update(freq):
#     x = np.sin(5 * val)
#     y = np.sin((5 + freq) * val)
#     line.set_data(x, y)
#     return line,

# ani = anim.FuncAnimation(fig, update, frames=np.linspace(0, 1, 100), init_func=init, blit=True)
# plt.show()

# Задание 4
# t = np.linspace(0, 2 * np.pi, 1000)

# def waveCreator(freq, amp):
#     return amp * np.sin(freq * t)

# def update(val):
#     amp1 = samp1.val
#     freq1 = sfreq1.val
#     amp2 = samp2.val
#     freq2 = sfreq2.val

#     wave1_new = waveCreator(freq1, amp1)
#     wave2_new = waveCreator(freq2, amp2)

#     line1.set_ydata(wave1_new)
#     line2.set_ydata(wave2_new)
#     line3.set_ydata(wave1_new + wave2_new)
#     fig.canvas.draw_idle()

# fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 6))
# plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.4)
# freq1_init = 1.0
# amp1_init = 1.0
# freq2_init = 1.0
# amp2_init = 1.0
# wave1 = waveCreator(freq1_init, amp1_init)
# wave2 = waveCreator(freq2_init, amp2_init)
# result_wave = wave1 + wave2

# line1, = ax1.plot(t, wave1, lw=2, color='yellow')
# line2, = ax2.plot(t, wave2, lw=2, color='green')
# line3, = ax3.plot(t, result_wave, lw=2, color='blue')

# axamp1 = plt.axes([0.1, 0.3, 0.65, 0.03], facecolor='lightgoldenrodyellow')
# axfreq1 = plt.axes([0.1, 0.25, 0.65, 0.03], facecolor='lightgoldenrodyellow')
# axamp2 = plt.axes([0.1, 0.2, 0.65, 0.03], facecolor='lightgoldenrodyellow')
# axfreq2 = plt.axes([0.1, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow')

# samp1 = Slider(axamp1, 'amplit 1', 0.1, 2.0, valinit=amp1_init)
# sfreq1 = Slider(axfreq1, 'freq 1', 0.1, 10.0, valinit=freq1_init)
# samp2 = Slider(axamp2, 'amplit 2', 0.1, 2.0, valinit=amp2_init)
# sfreq2 = Slider(axfreq2, 'freq 2', 0.1, 10.0, valinit=freq2_init)

# samp1.on_changed(update)
# sfreq1.on_changed(update)
# samp2.on_changed(update)
# sfreq2.on_changed(update)
# plt.show()

# Задание 5
# x = np.linspace(-5, 5, 100)
# y = np.linspace(-5, 5, 100)
# X, Y = np.meshgrid(x, y)
# Z = np.sin(np.sqrt(X**2 + Y**2))
# Z1 = np.sin(X) * np.cos(Y)
# Z2 = np.cos(X) * np.sin(Y)
# MSE = np.sqrt((Z1 - Z2)**2)

# fig = plt.figure(figsize=(12, 6))

# ax1 = fig.add_subplot(121, projection='3d')
# ax1.plot_surface(X, Y, Z, cmap='viridis')
# ax1.set_title('MSE')

# ax2 = fig.add_subplot(122)
# c = ax2.imshow(np.log(MSE), extent=[0, 10, 0, 10], cmap='viridis', origin='lower', aspect='auto')
# ax2.set_title('MSE(Log scale)')
# fig.colorbar(c, ax=ax2)

# plt.show()