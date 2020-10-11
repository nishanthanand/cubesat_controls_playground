import numpy as np

class State:
    def __init__(self, x, y, z, dx, dy, dz):
        """
        Structure of the state vector (units are m and m/s)
        x, y, z, dx, dy, dz
        """
        self.state_vector = np.array([x, y, z, dx, dy, dz])
        
    def get_earth_referenced():
        # altitude, lat, long, v_altitude, v_lat, v_long, quaternion rotation
        return None
    
    def get_cubesat_referenced():
        # x, y, z, x_v, y_v, z_v,  quaternion rotation
        return None
    
    def get_cubesat_earth_transform():
        # homogeneous transformation matrix for the transformation between the qubesat and the earth
        return None
    
class SensorDevice():
    def __init__():
        pass
    
class ControlDevice():
    def __init__():
        pass


class Cubesat:
    def __init__(self, mass, length=0.1, width=0.1, height=0.1, inertia = np.array([[1, 0, 0],[0, 1, 0],[0, 0, 1]])):
        """
        mass in kg
        length, width, height in m
        """
        self.mass = mass
        self.inertia = inertia
        self.inertia_inv = np.linalg.inv(inertia)
        sensor_read_delay = 0
        control_write_delay = 0
        