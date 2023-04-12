from basil.dut import Dut

dut = Dut('julaboFP50_pyserial.yaml')
dut.init()


# turn on:
# dut["chiller"].start_chiller()

# dut["chiller"].set_temp(15)  # set temp
# dut["chiller"].set_power(0)  # set power


print("Status: {}".format(dut["chiller"].get_status()))

# turn off:
dut["chiller"].stop_chiller()
