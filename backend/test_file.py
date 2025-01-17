from derivative_logic import *
from integral_logic import *
import anvil.server

anvil.server.connect("server_MFH6WQL6ZQWWMUOMMUAUPROD-YXQIFZ674ASXEJOG")

derivative = Derivative()
integral = Integral()

anvil.server.wait_forever()
