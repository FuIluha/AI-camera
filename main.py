from modules.camera.camera import Camera

camera = Camera("/dev/cu.usbserial-110")
camera.starting_stream()