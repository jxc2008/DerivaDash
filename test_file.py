from derivative_logic import *
from integral_logic import *
import anvil.server

anvil.server.connect("client_RKR2VVDQ5256MHGDSUXIZHLL-YXQIFZ674ASXEJOG")

derivative = Derivative()
integral = Integral()

derivative.run_game()
integral.run_game()

anvil.server.wait_forever()
