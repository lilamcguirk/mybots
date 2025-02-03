import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import numpy

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
robotId = p.loadURDF("body.urdf")
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(10000)
print(backLegSensorValues)
exit()
for i in range(1000):
	p.stepSimulation()
	backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("Link1")
	print(backLegTouch)
	time.sleep(1/60)

p.disconnect()
