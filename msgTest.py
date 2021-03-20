from pymavlink import mavutil

# Start a connection listening to a UDP port
#the_connection = mavutil.mavlink_connection('udpin:localhost:9600')
the_connection = mavutil.mavlink_connection('com8')

# Wait for the first heartbeat 
#   This sets the system and component ID of remote system for the link
the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_system))

try: 
    altitude=the_connection.messages['GLOBAL_POSITION_INT'].alt  # Note, you can access message fields as attributes!
    latitude=the_connection.messages['GLOBAL_POSITION_INT']
    #longitude=the_connection.messages['GLOBAL_POSITION_INT'].lon
    print(altitude)
    print(latitude)
    #print(longitude)
except:
    print('No GPS_RAW_INT message received')
try:
    msgMission=the_connection.messages['GLOBAL_POSITION_INT']
    print('Message->', msgMission)
except:
    print('Message-> No message received')