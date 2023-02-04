# Define the DriveBot class here!
class DriveBot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0
    
    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        # gave id to the robots, when one is created
        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction
    
    def adjust_sensor(self, new_sensor):
        self.sensor_range = new_sensor

# Instance of DriveBot
robot_1 = DriveBot()
robot_1.control_bot(10, 180)
robot_1.adjust_sensor(20)
