#!/usr/bin/env python
import time
from flyt_python import api

drone = api.navigation(timeout=120000)

time.sleep(3.0)

print 'taking of at A'
drone.take_off(10.0)
print 'going to B'
drone.position_set(8.665, 5.0, 0, relative=True)
print 'going to C'
drone.position_set(-8.665, 5.0, 0, relative=True)
print 'going to A'
drone.position_set(0, -10, 0, relative=True)
print 'Landing'
drone.land(async=False)

drone.disarm()
