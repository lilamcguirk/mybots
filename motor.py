import constants as c
import numpy as np
from pyrosim import pyrosim
import pybullet as p

class MOTOR():
    def __init__(self, jointName):
        self.jointName = jointName.decode("utf-8") if isinstance(jointName, bytes) else jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.BackLeg_amplitude
        self.frequency = c.BackLeg_frequency
        self.offset = c.BackLeg_phaseOffset

        if self.jointName == "Torso_BackLeg":
            self.frequency =  self.frequency / 2  

        motorValues = np.linspace(0, 2*np.pi, c.sim_steps)
        self.motorValues = self.amplitude * np.sin(self.frequency * motorValues + self.offset)

    def Set_Value(self, robot, desiredAngle):
        # Find the joint index
        joint_index = next((j for j in range(p.getNumJoints(robot))
                            if p.getJointInfo(robot, j)[1].decode("utf-8") == self.jointName), None)

        if joint_index is not None:
            p.setJointMotorControl2(
                bodyIndex=robot,
                jointIndex=joint_index,
                controlMode=p.POSITION_CONTROL,
                targetPosition=desiredAngle,  # Use desiredAngle directly
                force=25  # Adjust force if necessary
            )


    def Save_Values(self):
        np.save(f"data/{self.jointName}_MotorValues.npy", self.motorValues)

