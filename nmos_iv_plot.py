# Calculating and plotting Ids vs Vds using the long-channel (Shockley) model
import numpy as np
import matplotlib.pyplot as plt

# Given parameters
tox = 17.5e-10        # 17.5 Å in meters
eps0 = 8.854e-12      # vacuum permittivity (F/m)
eps_ox = 3.9          # SiO2 relative permittivity
mu_cm2 = 120.0        # cm^2/Vs (given)
mu = mu_cm2 * 1e-4    # convert to m^2/Vs
W = 4.0
L = 2.0
W_over_L = W / L
Vth = 0.5             # V (threshold)
Vgs_list = [0, 0.2, 0.4, 0.6, 0.8, 1.0]  # V

# Derived quantities
Cox = eps0 * eps_ox / tox   # F/m^2
beta = mu * Cox * W_over_L  # A/V^2 (transconductance parameter)

# Vds sweep
Vds = np.linspace(0, 1.2, 400)  # V, up to 1.2 V

plt.figure(figsize=(8,6))
for Vgs in Vgs_list:
    Ids = np.zeros_like(Vds)
    for i, vds in enumerate(Vds):
        if Vgs <= Vth:
            Ids[i] = 0.0
        elif vds < (Vgs - Vth):
            # Linear (triode) region
            Ids[i] = beta * (Vgs - Vth - vds/2.0) * vds
        else:
            # Saturation region
            Ids[i] = 0.5 * beta * (Vgs - Vth)**2
    # Plot in mA for readability
    plt.plot(Vds, Ids * 1e3, label=f"Vgs={Vgs:.1f} V")

plt.xlabel("Vds (V)")
plt.ylabel("Ids (mA)")
plt.title("Ids vs Vds (Long-channel Shockley model)\n65 nm process, tox=17.5 Å, μ=120 cm^2/Vs, W/L=4/2, Vth=0.5 V")
plt.grid(True)
plt.legend()
plt.ylim(bottom=0)
plt.xlim(0, 1.2)
plt.show()

# Print key parameters used
Cox_val = Cox
beta_val = beta
print(f"Cox = {Cox_val:.3e} F/m^2")
print(f"mu = {mu:.3e} m^2/Vs ({mu_cm2} cm^2/Vs)")
print(f"beta = {beta_val:.3e} A/V^2 (using W/L = {W_over_L})")
