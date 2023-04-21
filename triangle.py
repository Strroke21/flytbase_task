#!/usr/bin/env python
import time
from flyt_python import api

drone = api.navigation(timeout=120000)  # instance of flyt droneigation cla$

time.sleep(1)

drone.take_off(10.0)

# h^2=p^2+b^2, hence p=8m and b=6m
drone.position_set(8.0, 6.0, 10, relative=True)
drone.position_set(-8.0, 6.0, 0, relative=True)
drone.position_set(0, -10, 0, relative=True)

print("Landing")
drone.land(async=False)

# shutdown the instance
drone.disconnect()
