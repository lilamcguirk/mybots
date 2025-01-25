import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1

for row in range(5):
	for column in range(5):
		x = row
		y = column
		z = 0.5
		
		size = 1	
		for level in range(5):
			pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[size, size, size])
			z += 1
			size *= 0.9

pyrosim.End()

