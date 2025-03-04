import numpy as np

pi = np.pi

sim_steps = 1000
time_step = 1/100 # sleeps 1/240 seconds per loop

# Back leg motor controls
BackLeg_amplitude = np.pi
BackLeg_frequency = 30
BackLeg_phaseOffset = 0

# Front leg motor controls
FrontLeg_amplitude = np.pi
FrontLeg_frequency = 15
FrontLeg_phaseOffset = np.pi/2
