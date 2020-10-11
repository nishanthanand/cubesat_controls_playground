import numpy as np

# constants
class Consts:
    G = 6.67430e-11 # m^3/(kg*s^2)
    M_earth = 5.972e24
    R_earth = 6.371e6
    ISS_altitude = 4.08e6
    ISS_inclination = 0.9005899
    mu = G * M_earth
    miles_to_meters = 1609.34
    

class Simulator:
    def __init__(self, time, cubesat, planet, step_size=0.1):
        """
        time and step size in seconds
        """
        self.step_size = step_size
        self.time = time
        self.cubesat = cubesat
        self.planet = planet
        
    def step(self, state):
        # compute acceleration vector from gravity assuming points mass of the earth and satelite
        r_hat = state.state_vector[:3]/np.lanalg.norm(state.state_vector[:3])
        print(r_hat)
        a = np.array([])
        
    
class Planet:
    def __init__(self, mass, radius):
        """
        mass in kg
        radius in m
        """
        self.radius = radius
        self.mass = mass
    
    def get_gravitational_acceleration(self, state):
        r_hat = state.state_vector[:3]/np.linalg.norm(state.state_vector[:3])
        a = -Consts.G * self.mass / np.linalg.norm(state.state_vector[:3])**2 * r_hat
        return a
    
    