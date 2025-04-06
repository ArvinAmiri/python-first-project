# Constants
ke = 9e9  # sabet Coulomb
e = 1.6e-19  # bar electron
G = 6.67e-11  # sabet geranesh
mp = 1.67e-27  # jerm proton
me = 9.1e-31  # jerm electron
r = 5.3e-11  # shoa Bohr

# Mohasebe niroha va nesbat
F_C = ke * e**2 / r**2
F_G = G * mp * me / r**2
ratio = F_C / F_G

# Namayesh natayej
print(f"Niroye Coulomb: {F_C:.1e} N")
print(f"Niroye Geranesh: {F_G:.1e} N")
print(f"Nesbate Niroha: {ratio:.1e}")
