from pypylon import pylon 

# Pypylon get camera by serial number
serial_number = '40058005'
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateDevice(pylon.CDeviceInfo().SetFullName(serial_number)))

# VERY IMPORTANT STEP! To use Basler PyPylon OpenCV viewer you have to call .Open() method on you camera
camera.Open()
