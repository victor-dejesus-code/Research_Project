# Guide to Dynamic Stability and Oscillation Analysis in RocketPy (6DOF)

This document summarizes the critical components, variables, and parameters that should be monitored and adjusted in a six-degree-of-freedom (6DOF) simulator such as **RocketPy** to investigate dynamic stability phenomena, aerodynamic oscillations, and catastrophic coupling in the subsonic regime.

---

## 1. Output Parameters (Oscillation Monitoring)

These variables are extracted from the `Flight` class after the simulation and make it possible to measure the rocket's time response to disturbances such as wind gusts.

* **Angle of Attack (\(\alpha\)):** The angle between the rocket's longitudinal axis and the relative airflow velocity vector. It is the primary indicator of oscillation; during stable flight, it should quickly decay to zero after a disturbance.
* **Pitch and Yaw Angular Velocities (`w1`, `w2` / *Pitch and Yaw Rates*):** These measure the rotational velocity, in radians per second, about the transverse axes. Sustained sinusoidal waves in these variables indicate low dynamic damping.
* **Roll Angular Velocity (`w3` / *Roll Rate*):** The rotational velocity about the longitudinal axis. It is critical for monitoring *Roll-Pitch Coupling*.
* **Pitch Natural Frequency (`pitch_natural_frequency`):** The mathematical frequency at which the rocket tends to oscillate due to its geometry and mass distribution.

---

## 2. Structural Input Parameters (Physics and Mass)

Variables that can be modified in the `Rocket` class and that directly affect the vehicle's inertia and moments.

* **Static Stability Margin:** The distance between the Center of Gravity (CG) and the Center of Pressure (CP), measured in calibers (rocket diameters).
    * *Margin < 0.5 calibers:* Understability. Causes slow, large-amplitude oscillations.
    * *Margin > 3.0 calibers:* Overstability. Causes *weathercocking* (a violent turn into the wind) and high-frequency oscillations.
* **Transverse Inertia Tensor (\(I_{xx}, I_{yy}\)):** The rocket's resistance to rotational motion. Placing heavy masses at the ends (nose/motor) increases its inertia. This causes the rocket to repeatedly overshoot its equilibrium point, prolonging the oscillations.
* **Variable Mass and CG Shift:** Modeling the mass loss caused by motor-grain combustion (\(dm/dt\)), which shifts the CG forward during flight and dynamically changes the moments of inertia in real time.

---

## 3. Aerodynamic Coefficients and Damping

Forces exerted by the atmosphere that restrain or amplify the rocket's motion.

* **Aerodynamic Spin Moment:** The induced moment that produces rotation about the longitudinal axis (roll), usually caused by fin cant or imperfections.
* **Pitch Damping Coefficient (\(C_{mq}\)):** A purely aerodynamic parameter. It measures the ability of the fins and aft fuselage to act as "dampers" against the airflow. A small longitudinal area reduces \(C_{mq}\), preventing oscillations from dying out.
* **Power Drag Coefficient (\(C_d\) / `PowerOnDrag` - `PowerOffDrag`):** Longitudinal resistance that varies as a function of the angle of attack during oscillations.

---

## Scientific Sources and References

The dynamic equations and methodologies implemented by RocketPy are based on standard aerospace engineering literature:

1. **Barrowman, J. S. (1966).** *The Practical Calculation of the Aerodynamic Characteristics of Slender Finned Vehicles*. This is the fundamental mathematical basis for calculating the Center of Pressure (CP) in the subsonic regime, used by both OpenRocket and RocketPy's initial approximations.
2. **Niskanen, S. (2013).** *Development of an Open-Source 6DOF Flight Simulation Software for Consumer-Grade Rockets*. Helsinki University of Technology. Describes the transition from simplified 3DOF models to the transformation matrices and quaternions used in advanced six-degree-of-freedom models.
3. **Ananziah, G., & Valisano, S. et al. (RocketPy Community).** *RocketPy Documentation and Mathematical Models*. Official documentation describing the integration of the variable-mass differential equations of motion from Tsiolkovsky's rocket equation with stochastic atmospheric disturbances (Monte Carlo analysis).
4. **Zipfel, P. H. (2007).** *Modeling and Simulation of Aerospace Vehicle Dynamics*. AIAA Education Series. An academic reference for understanding gyroscopic coupling (*Roll-Pitch Coupling*), variable inertia tensors, and the calculation of the dynamic damping coefficient (\(C_{mq}\)).
