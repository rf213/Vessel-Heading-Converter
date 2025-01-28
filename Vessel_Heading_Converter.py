
# This function assumes waves going into the vessel heading (Head Seas) is 180° and following seas is 0°
def Global_To_Relative(global_vessel_heading, global_wave_from_directions):
    new_directions = {}
    for direction in global_wave_from_directions:
        relative_angle = global_vessel_heading - direction + 180
        if relative_angle < 0:
            corrected_relative_angle = 360 + relative_angle
            new_directions[direction] = corrected_relative_angle
        else:
            if relative_angle > 360:
                new_directions[direction] = relative_angle%360
            else:
                new_directions[direction] = relative_angle
    for old_direction, new_direction in new_directions.items():
        print(f'{old_direction} ==> {new_direction}')
    return new_directions

# This function assumes waves going into the vessel heading (Head Seas) is 180° and following seas is 0° 
def Relative_To_Global(global_vessel_heading, relative_wave_directions_from):
    new_directions = {}
    for direction in relative_wave_directions_from:
        if direction - 360 <= -180:
            global_angle = global_vessel_heading - (direction - 180)
            if global_angle > 360:
                new_directions[direction] = global_angle%360
            else:
                new_directions[direction] = global_angle
        else:
            global_angle = (global_vessel_heading - ((direction - 360) - 180)) - 360
            new_directions[direction] = global_angle
    for old_direction, new_direction in new_directions.items():
        print(f'{old_direction} ==> {new_direction}')
    return new_directions

def main():
    operation = input('To convert Global to Relative type: gtr\nTo convert Relative to Global type rtg\n').lower()
    if operation == 'gtr':
        vessel_heading = float(input('Please input the global vessel heading: '))
        print('Please enter your wave directions one at a time and hit enter when you\'re finished')
        wave_directions = []
        while True:
            wave_direction = input()
            if wave_direction == '':
                break
            else:
                wave_direction = float(wave_direction)
                wave_directions.append(wave_direction)
        Global_To_Relative(vessel_heading, wave_directions)

    if operation == 'rtg':
        vessel_heading = float(input('Please input the global vessel heading: '))
        print('Please enter your wave directions one at a time and hit enter when you\'re finished')
        wave_directions = []
        while True:
            wave_direction = input()
            if wave_direction == '':
                break
            else:
                wave_direction = float(wave_direction)
                wave_directions.append(wave_direction)
        Relative_To_Global(vessel_heading, wave_directions)

main()

