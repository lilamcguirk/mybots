import pybullet as p
from pyrosim import pyrosim
import constants as c
import numpy as np
from motor import MOTOR
from sensor import SENSOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT():
    def __init__(self):
        self.nn = NEURAL_NETWORK("brain.nndf")
        self.bodyID = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.bodyID)

        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
           # if linkName != "Torso":  # Skip non-sensing parts
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, current_time_step):
        for sensor in self.sensors.values():
            sensor.Get_Value(current_time_step)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName.decode("utf-8")] = MOTOR(jointName)

    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Act(self, current_time_step):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self.bodyID, desiredAngle)
                print(f"Motor Neuron {neuronName} is controlling joint {jointName} with desired angle {desiredAngle}.")

       # for motor in self.motors.values():
          # motor.Set_Value(self.bodyID, current_time_step)

