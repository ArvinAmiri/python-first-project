import math

B = 50000
K = 0.2
N_0 = 5000
t = 24

C = (B / N_0) - 1
N_t = B / (1 + C * math.exp(-K * t))

print(f"Tedad bakteria pas az {t} saat barabar ast ba {N_t:.2f}")
