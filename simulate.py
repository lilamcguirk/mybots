import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
robotId = p.loadURDF("body.urdf")
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

num_iterations = 1000

targetAngles = (np.pi / 4) * np.sin(np.linspace(0, 2 * np.pi, num_iterations))

# np.save('data/target_angles.npy', targetAngles)

backLegSensorValues = np.zeros(num_iterations)
frontLegSensorValues = np.zeros(num_iterations)
for i in range(num_iterations):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Link1")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Link2")

	pyrosim.Set_Motor_For_Joint(
	bodyIndex = robotId,
	jointName = b'Link0_Link1',
	controlMode = p.POSITION_CONTROL,
	targetPosition=targetAngles[i],
	maxForce = 140)

	pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Link0_Link2',
        controlMode = p.POSITION_CONTROL,
        targetPosition=targetAngles[i],
        maxForce = 140)

	time.sleep(1/240)

np.save('data/back_leg_sensor_values.npy', backLegSensorValues)
np.save('data/front_leg_sensor_values.npy', frontLegSensorValues)
p.disconnect()
print(backLegSensorValues)
print(frontLegSensorValues)
