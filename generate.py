import pyrosim.pyrosim as pyrosim

def Create_World():
	pyrosim.Start_SDF("world.sdf")

	length = 1
	width = 1
	height = 1

	pyrosim.Send_Cube(name="Box", pos=[-2, 2, 0.5] , size=[length, width, height])

	pyrosim.End()

def Generate_Body():

    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name="Torso", pos=[1, 0, 1.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0.5,0,1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [1.5,0,1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])

    pyrosim.End()

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    
    sensor_neurons = {0: "Torso", 1: "BackLeg", 2: "FrontLeg"}
    motor_neurons = {3: "Torso_BackLeg", 4: "Torso_FrontLeg"}
    
    # Create sensor neurons
    for sensor_id, link_name in sensor_neurons.items():
        pyrosim.Send_Sensor_Neuron(name=sensor_id, linkName=link_name)
    
    # Create motor neurons
    for motor_id, joint_name in motor_neurons.items():
        pyrosim.Send_Motor_Neuron(name=motor_id, jointName=joint_name)
    
    # Create synapses with weight 1
    for sensor_id in sensor_neurons.keys():
        for motor_id in motor_neurons.keys():
            pyrosim.Send_Synapse(sourceNeuronName=sensor_id, targetNeuronName=motor_id, weight=1)
    
    pyrosim.End()

Create_World()
Generate_Body()
Generate_Brain()
