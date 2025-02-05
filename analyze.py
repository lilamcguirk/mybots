import matplotlib.pyplot
import numpy as np

backLegSensorValues = np.load('data/back_leg_sensor_values.npy')
print(backLegSensorValues)

frontLegSensorValues = np.load('data/front_leg_sensor_values.npy')
print(frontLegSensorValues)

matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.plot(frontLegSensorValues)
matplotlib.pyplot.show()
