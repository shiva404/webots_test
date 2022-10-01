"""keyboard_controll controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Keyboard, GPS

TIME_STEP = 64
robot = Robot()
ds = []
dsNames = ['ds_right', 'ds_left']
for i in range(2):
    ds.append(robot.getDevice(dsNames[i]))
    ds[i].enable(TIME_STEP)
wheels = []
wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
for i in range(4):
    # print(robot.getDevices())
    wheels.append(robot.getDevice(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)
 
keyboard = Keyboard()
keyboard.enable(TIME_STEP)
leftSpeed = 0.0
rightSpeed = 0.0

gp = robot.getGPS("global")
gp.enable(TIME_STEP)
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(TIME_STEP) != -1:
    key = keyboard.getKey()
    
    if key == 315:
        leftSpeed = 1.0
        rightSpeed = 1.0
    elif key == 317:
        leftSpeed = -1.0
        rightSpeed = -1.0
    elif key == 314:
        leftSpeed = 1.0
        rightSpeed = -1.0
    elif key == 316:
        leftSpeed = -1.0
        rightSpeed = 1.0
    else:
        leftSpeed = 0.0
        rightSpeed=0.0
    
    print(f"Reading from right_sensor={ds[0].getValue()} lef_sensor={ds[1].getValue()}")
    print(f"gps X={gp.getValues()[0]} Y={gp.getValues()[1]} Z={gp.getValues()[2]}")
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)
    
 