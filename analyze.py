import matplotlib.pyplot
import numpy as np

backLegSensorValues = np.load('data/back_leg_sensor_values.npy')
print(backLegSensorValues)

matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.show()
