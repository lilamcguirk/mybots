# Imports
import constants as c
import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random
import time

from simulation import SIMULATION

simulation = SIMULATION()
simulation.Run()

# import pybullet_data
# import pybullet as p
# import time
# import pyrosim.pyrosim as pyrosim
# import numpy as np
# import random
# import constants as c

# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())

# p.setGravity(0,0,-9.8)
# robotId = p.loadURDF("body.urdf")
# planeId = p.loadURDF("plane.urdf")
# p.loadSDF("world.sdf")
# pyrosim.Prepare_To_Simulate(robotId)

# amplitude_backLeg = c.pi
# frequency_backLeg = 30
# phaseOffset_backLeg = 0

# amplitude_frontLeg = c.pi
# frequency_frontLeg = 15
# phaseOffset_frontLeg = np.pi/2

# num_iterations = 1000

# x = np.linspace(0, 2*np.pi, 1000)

# targetAngles_backLeg = amplitude_backLeg * np.sin(frequency_backLeg * x + phaseOffset_backLeg)


# targetAngles_frontLeg = amplitude_frontLeg * np.sin(frequency_frontLeg * x + phaseOffset_frontLeg)

# np.save('data/target_angles_back_leg.npy', targetAngles_backLeg)
# np.save('data/target_angles_front_leg.npy', targetAngles_frontLeg)

# exit()

# backLegSensorValues = np.zeros(num_iterations)
# frontLegSensorValues = np.zeros(num_iterations)
# for i in range(num_iterations):
#         p.stepSimulation()
#         backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Link1")
#         frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Link2")

#         pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robotId,
#         jointName = b'Link0_Link1',
#         controlMode = p.POSITION_CONTROL,
#         targetPosition=targetAngles_backLeg[i],
#         maxForce = 25)

#         pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robotId,
#         jointName = b'Link0_Link2',
#         controlMode = p.POSITION_CONTROL,
#         targetPosition=targetAngles_frontLeg[i],
#         maxForce = 25)

#         time.sleep(1/240)

# np.save('data/back_leg_sensor_values.npy', backLegSensorValues)
# np.save('data/front_leg_sensor_values.npy', frontLegSensorValues)
# p.disconnect()
# print(backLegSensorValues)
# print(frontLegSensorValues)
