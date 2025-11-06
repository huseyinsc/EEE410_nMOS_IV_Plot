# EEE410_nMOS_IV_Plot 📈

This repository contains the Python script (`nmos_iv_plot.py`) to solve **Homework #3** for the EEE 410 Integrated Circuit Design course.

## Purpose 💡

The script estimates and plots the **Drain Current ($I_{DS}$) versus Drain-Source Voltage ($V_{DS}$)** characteristic curves for a long-channel nMOS transistor using the **Shockley (1st order) model**.

The primary goal is to visualize the operating regions (Cutoff, Linear, and Saturation) based on the given process parameters and various $V_{GS}$ voltages.

## Problem Parameters 📐

The script uses the following parameters from the assignment:

| Parameter | Value |
| :--- | :--- |
| **Gate Oxide Thickness ($t_{ox}$)** | $17.5 \text{ Å}$ |
| **$W/L$ Ratio** | $4/2 = 2.0$ |
| **Electron Mobility ($\mu_n$)** | $120 \text{ cm}^2/\text{V} \cdot \text{s}$ |
| **Threshold Voltage ($V_{th}$)** | $0.5 \text{ V}$ |
| **$V_{GS}$ Sweep** | $0, 0.2, 0.4, 0.6, 0.8, 1.0 \text{ V}$ |

## Key Calculations ⚙️

The script uses the following core equations:

1.  **Gate Oxide Capacitance per Unit Area ($C_{ox}$):**
    $$C_{ox} = \frac{\epsilon_{ox}}{t_{ox}}$$
2.  **Transconductance Parameter ($\beta$):**
    $$\beta = \mu_n C_{ox} \frac{W}{L}$$
3.  **Shockley Model (Saturation Region):**
    $$I_{DS} = \frac{\beta}{2} (V_{GS} - V_{th})^2 \quad \text{for } V_{DS} \ge V_{DSAT}$$

## Usage 💻

To run the plotting script:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/huseyinsc/EEE410_nMOS_IV_Plot.git
    cd EEE410_nMOS_IV_Plot
    ```
2.  **Dependencies:** Ensure you have Python, `numpy`, and `matplotlib` installed.
    ```bash
    pip install numpy matplotlib
    ```
3.  **Execute the script:**
    ```bash
    python nmos_iv_plot.py
    ```

The script will generate a plot of $I_{DS} \text{ (mA)}$ vs. $V_{DS} \text{ (V)}$ and print the calculated $\beta$ and $C_{ox}$ values to the console.
