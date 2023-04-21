#!/usr/bin/env python
import time
from flyt_python 
import api

drone = api.navigation(timeout=120000)  # instance of flyt droneigation class

time.sleep(1)

drone.take_off(5.0)

drone.position_set(6.5, 0, 0, yaw=1.0472, relative=True)
drone.position_set(0, 6.5, 0, relative=True)
drone.position_set(-6.5, 0, 0, relative=True)
drone.position_set(0, -6.5, 0, relative=True)

print("Landing")
drone.land(async=False)

# shutdown the instance
drone.disconnect()
