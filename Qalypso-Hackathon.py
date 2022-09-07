from pytket import Circuit

# create EPR pair
c = Circuit(2)
c.H(0).CX(0,1)

# confirming the circuit is created properly
print(c.get_commands())
print(c.get_statevector())

