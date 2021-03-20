import tkinter as tk
from pymavlink import mavutil

window = tk.Tk ()
window.title("Py.lot")
def doorbell(event):
    print(" You rang the Doorbell !")
#getting screen width and height of display 
width = window.winfo_screenwidth()  
height = window.winfo_screenheight() 
#setting tkinter window size 
window.geometry("%dx%d" % (width, height))

# Start a connection listening to a UDP port
#the_connection = mavutil.mavlink_connection('udpin:localhost:9600')
the_connection = mavutil.mavlink_connection('com8')

# Wait for the first heartbeat 
#   This sets the system and component ID of remote system for the link
the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_system))

# Once connected, use 'the_connection' to get and send messages

try: 
    altitude=the_connection.messages['GLOBAL_POSITION_INT'].alt  # Note, you can access message fields as attributes!
    latitude=the_connection.messages['GLOBAL_POSITION_INT']
    #longitude=the_connection.messages['GLOBAL_POSITION_INT'].lon
    print(altitude)
    print(latitude)
    #print(longitude)
except:
    print('No GPS_RAW_INT message received')
    
labelAltitud = "Altitud" 
newlabel = tk.Label(text = labelAltitud )
newlabel.grid(column = 0, row = 0)
altitud = 'nn'
newlabelAltitud = tk.Label(text = altitud)
newlabelAltitud.grid(column = 1, row = 0)
mybutton = tk.Button(window, text = "Doorbell")
mybutton.grid(column = 0, row = 1)
mybutton.bind("<Button-1>",doorbell)

window.mainloop()

# Mavlink documentation:
# http://mavlink.io/en/mavgen_python/
# http://mavlink.io/en/mavgen_python/#specific_messages
# http://mavlink.io/en/messages/common.html
# http://mavlink.io/en/getting_started/