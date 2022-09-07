import numpy as np
import matplotlib.pyplot as plt
from qiskit import IBMQ
from qiskit import QuantumCircuit, execute, Aer

circuit = QuantumCircuit(3)
circuit.h(0)
circuit.cx(0,1)
circuit.cx(0,2)

circuit.draw('mpl')
plt.show()
