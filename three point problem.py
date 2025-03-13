import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

A = np.array([56, 324, 296])
B = np.array([286, 386, 176])
C = np.array([114, 428, 225])

AB = B - A
AC = C - A

bidang = np.cross(AB, AC)
a, b, c = bidang

d = np.dot(bidang, A)
print()
print("\033[96mPersamaan bidang:\033[0m")
print(f"{a}x + {b}y + {c}z = {d}")
print()
print("\033[96mPersamaan bidang singgung vertikal:\033[0m")
print(f"z = {-a/c}x + {-b/c}y + {d/c}")
print()

bidang_unit = bidang / np.linalg.norm(bidang)
proyeksi_bidang = np.array([bidang_unit[0], bidang_unit[1], 0])
proyeksi_bidang /= np.linalg.norm(proyeksi_bidang)

strike = np.degrees(np.arctan(-b / a))
if strike < 0:
    strike += 360

dip = np.degrees(np.arccos(bidang_unit[2]))
dip_direction = (strike + 90) % 360

print(f"\033[96mStrike        :\033[97m {strike:.2f}°\033[0m")
print(f"\033[96mDip Direction :\033[97m {dip_direction:.2f}°\033[0m")
print(f"\033[96mDip           :\033[97m {dip:.2f}°\033[0m")
print()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title("Ilustrasi Bidang dan Plottingnya")

ax.scatter(*A, color='r', label='A')
ax.scatter(*B, color='g', label='B')
ax.scatter(*C, color='b', label='C')

xx, yy = np.meshgrid(np.linspace(50, 300, 10), np.linspace(300, 450, 10))
zz = (d - a * xx - b * yy) / c
ax.plot_surface(xx, yy, zz, alpha=0.5, color='cyan')

mid = (A + B + C) / 3
# ax.quiver(*mid, *bidang_unit*50, color='k', label='Bidang')

rad_strike = np.radians(strike)
vektor_strike = np.array([np.cos(rad_strike), np.sin(rad_strike), 0])*100
ax.quiver(*mid, *vektor_strike, color='red', label=f'strike ({strike:.2f}°)')

vektor_dip = np.array([np.cos(np.radians(dip_direction)), np.sin(np.radians(dip_direction)), -np.tan(np.radians(dip_direction))]) * 50
ax.quiver(*mid, *vektor_dip, color='blue', label=f'Dip Direction ({dip_direction:.2f}°)')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()