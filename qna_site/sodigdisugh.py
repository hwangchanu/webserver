import numpy as np
import matplotlib.pyplot as plt

# 기본 파라미터
fc = 3.5e9  # 주파수: 3.5GHz (5G typical)
c = 3e8     # 빛의 속도
lambda_c = c / fc  # 파장

d = np.linspace(1, 500, 500)  # 거리: 1m ~ 500m
PL = 20 * np.log10(d) + 20 * np.log10(fc) - 147.55  # Free space path loss (dB)

# Rayleigh fading (amplitude)
rayleigh = np.random.rayleigh(scale=1.0, size=len(d))
fading_dB = 20 * np.log10(rayleigh)

# 총 수신 신호 세기 (dBm 기준)
Pt_dBm = 0  # 송신 전력 (0dBm)
Pr_dBm = Pt_dBm - PL + fading_dB

# 시각화
plt.figure(figsize=(10,6))
plt.plot(d, Pr_dBm, label='Received Signal (with Rayleigh Fading)', alpha=0.7)
plt.plot(d, Pt_dBm - PL, label='Received Signal (Path Loss Only)', linestyle='--')
plt.xlabel('Distance (m)')
plt.ylabel('Received Power (dBm)')
plt.title('Rayleigh Fading + Path Loss (5G 3.5GHz)')
plt.legend()
plt.grid(True)
plt.show()
