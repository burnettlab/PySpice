# r# This example shows the computation of the DC bias and sensitivity in a voltage divider.

####################################################################################################

import PySpice.Logging.Logging as Logging

logger = Logging.setup_logging()

####################################################################################################

from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

####################################################################################################

# f# circuit_macros('voltage-divider.m4')

circuit = Circuit("Voltage Divider")

circuit.V("input", "v_in", circuit.gnd, 10 @ u_V)
circuit.R(1, "v_in", "out", 9 @ u_kΩ)
circuit.R(2, "out", circuit.gnd, 1 @ u_kΩ)

print(str(circuit))
####################################################################################################

simulator = circuit.simulator(temperature=25, nominal_temperature=25)

analysis = simulator.operating_point()
for node in (analysis["v_in"], analysis.out):  # .in is invalid !
    for v in node:
        print("Node {}: {} V".format(str(node), float(v)))
# o#

# Fixme: Xyce sensitivity analysis
analysis = simulator.dc_sensitivity("v(out)")
for element in analysis.elements.values():
    for v in element:
        print(element, float(v))
# o#
