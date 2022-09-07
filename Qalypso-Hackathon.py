from pytket.extensions.qiskit import AerStateBackend, IBMQEmulatorBackend
from pytket import Circuit

def ghz_creator():

    def build_ghz_circuit(x):
        circ = Circuit(x)
        circ.H(0)
        for i in range(x-1):
            circ.CX(0, i+1)
        return circ
    
    global input 
    input = int(input('Please enter the amount of qubits to be used: '))    
    x = build_ghz_circuit(input)

ghz_creator()