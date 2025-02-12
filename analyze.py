import matplotlib.pyplot
import numpy as np

# backLegSensorValues = np.load('data/back_leg_sensor_values.npy')
# print(backLegSensorValues)

# frontLegSensorValues = np.load('data/front_leg_sensor_values.npy')
# print(frontLegSensorValues)

# matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg Sensor Values", linewidth=4)
# matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg Sensor Values")
# matplotlib.pyplot.legend()
# matplotlib.pyplot.show()

targetAngles = np.load('data/target_angles.npy')
matplotlib.pyplot.plot(targetAngles)
matplotlib.pyplot.show()
