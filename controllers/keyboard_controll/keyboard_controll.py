"""keyboard_controll controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Keyboard, GPS, InertialUnit, Camera

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

gp = robot.getDevice("global")
gp.enable(TIME_STEP)

imu = robot.getDevice("imu")
imu.enable(TIME_STEP)

lr = robot.getDevice('linear')

rm = robot.getDevice('rm')

cam = robot.getDevice('cam')
cam.enable(TIME_STEP)


linear = 0
rotation=0

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
    
    # print(f"Reading from right_sensor={ds[0].getValue()} lef_sensor={ds[1].getValue()}")
    # print(f"gps X={gp.getValues()[0]} Y={gp.getValues()[1]} Z={gp.getValues()[2]}")
    # print(f"imuX={imu.getRollPitchYaw()[0]} Y={imu.getRollPitchYaw()[1]} Z={imu.getRollPitchYaw()[2]}")
    
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)
    
    if key == 87 and linear < 0: # W key
        linear += 0.005;
    elif key == 83 and linear > -0.2: # S key
        linear += -0.005;
        
    lr.setPosition(linear)
    
    if key == 65 and rotation < 1.57: # A key
        rotation += 0.05;
    elif key == 68 > -1.57 : # D key
        rotation += -0.05;
        
    rm.setPosition(rotation)
 