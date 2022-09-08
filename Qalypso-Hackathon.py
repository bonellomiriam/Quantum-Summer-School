from qiskit import *
from qiskit import QuantumCircuit 
from qiskit import Aer
from qiskit import assemble 
import matplotlib.pyplot as plt
import numpy as np 
from numpy.random import randint 
import qutip

# creation of teleportation circuit

np.random.seed(seed=0)

n = 100
a_bits = randint(2, size = n)
a_bases = randint(2, size = n)

def message_sent(bits, bases):
    message = []
    for i in range(n): 
        c = QuantumCircuit(3, 3)
        if bases [i] == 0:
            if bits [i] == 0:
                pass
            else:
                c.x(0)
        else:
            if bits [i] == 0:
                c.h(1)
            else:
                c.cx(1,2)
                c.cx(0,1)
                c.h(0)
        c.barrier()
        message.append(c)
    return message
message = message_sent(a_bits, a_bases)
print('bit = %i' %a_bits[0])
print('basis = %i' %a_bases[0])
message[4].draw()


b_bases = randint(2, size = n)
print(b_bases)

def measure_sent(message, bases):
    backend = Aer.get_backend('aer_simulator')
    measurement = []
    for y in range(n):
        if bases [y] == 0:
            message[y].measure(0,0)
        if bases[y] == 1:
            message[y].h(0)
            message[y].measure(0,0)
        aer_sim = Aer.get_backend('aer_simulator')
        qobj = assemble(message[y], shots = 1, memory = True)
        result = aer_sim.run(qobj).result()
        measured_bit = int(result.get_memory()[0])
        measurement.append(measured_bit)
    return measurement 
b_result = measure_sent(message, b_bases)
message[4].draw()

def no_trash(abases, bbases, bits):
    g_bits = []
    for y in range(n):
        if abases[y] == bbases[y]:
            g_bits.append(bits[y])
        return g_bits 

a_key = no_trash(a_bases,b_bases, a_bits)
b_key = no_trash(a_bases, b_bases, b_result)

print(a_key)
print(b_key)


def sample_bits(bits, selection):
    sample = []
    for k in selection:
        k = np.mod(k, len(bits))
        sample.append(bits.pop(k))
    return sample 

sample_size = 16
bit_selection = randint(n, size = sample_size)
b_sample = sample_bits(b_key, bit_selection)
print('b sample = ' + str(b_sample))
a_sample = sample_bits(a_key, bit_selection)
print('a sample = ' + str(a_sample))
print('done')








