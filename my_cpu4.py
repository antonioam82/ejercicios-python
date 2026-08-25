"""
Test program for the CPU simulator written in Python.

Contains the CPU class (memory, registers, fetch-decode-execute cycle)
and a series of test "programs" that verify that each instruction
in the set (LOAD, LOADM, STORE, ADD, SUB, JMP, JZ, PRINT, HALT) works
correctly, using 'assert' to check the results.

Usage:
    python3 test_cpu_simulator.py
"""


class CPU:
    def __init__(self, program, memory_size=256, trace=False):
        self.memory = [0] * memory_size
        self.registers = {f"R{i}": 0 for i in range(4)}
        self.pc = 0
        self.program = program
        self.running = True
        self.trace = trace
        self.cycles = 0

    def fetch(self):
        instruction = self.program[self.pc]
        self.pc += 1
        return instruction

    def execute(self, instruction):
        op = instruction[0]

        if op == "LOAD":
            _, reg, value = instruction
            self.registers[reg] = value

        elif op == "LOADM":
            _, reg, addr = instruction
            self.registers[reg] = self.memory[addr]

        elif op == "STORE":
            _, reg, addr = instruction
            self.memory[addr] = self.registers[reg]

        elif op == "ADD":
            _, dest, r1, r2 = instruction
            self.registers[dest] = self.registers[r1] + self.registers[r2]

        elif op == "SUB":
            _, dest, r1, r2 = instruction
            self.registers[dest] = self.registers[r1] - self.registers[r2]

        elif op == "JMP":
            _, addr = instruction
            self.pc = addr

        elif op == "JZ":
            _, reg, addr = instruction
            if self.registers[reg] == 0:
                self.pc = addr

        elif op == "PRINT":
            _, reg = instruction
            print(f"   -> {reg} = {self.registers[reg]}")

        elif op == "HALT":
            self.running = False

        else:
            raise ValueError(f"Unknown instruction: {op}")

    def run(self):
        while self.running and self.pc < len(self.program):
            instruction = self.fetch()
            if self.trace:
                print(f"   PC={self.pc - 1:2d} | {instruction} | {self.registers} | {self.memory[:12]}")
            self.execute(instruction)
            self.cycles += 1



def _assert(condition, message):
    if not condition:
        raise AssertionError(message)


def run_test(name, program, asserts, trace=False):
    """Runs a program on the CPU and checks the result with 'asserts'."""
    print(f"\n=== {name} ===")
    try:
        cpu = CPU(program, trace=trace)
        cpu.run()
        asserts(cpu)
        print(f"   Cycles executed: {cpu.cycles}")
        print("   TEST PASSED")
        return True
    except AssertionError as e:
        print(f"   TEST FAILED: {e}")
        return False

# ----------------------------------------------------------------------
# Definición de pruebas
# ----------------------------------------------------------------------
tests = [
    {
        "name": "Suma de 1 a 5 con bucle",
        "program": [
            ("LOAD",  "R0", 0),
            ("LOAD",  "R1", 5),
            ("LOAD",  "R3", 1),
            ("ADD",   "R0", "R0", "R1"),
            ("SUB",   "R1", "R1", "R3"),
            ("JZ",    "R1", 7),
            ("JMP",   3),
            ("PRINT", "R0"),
            ("HALT",),
        ],
        "asserts": lambda cpu: _assert(cpu.registers["R0"] == 15, "Se esperaba R0 == 15")
    },
    {
        "name": "Escritura y lectura de memoria (STORE/LOADM)",
        "program": [
            ("LOAD",  "R0", 42),
            ("STORE", "R0", 10),
            ("LOADM", "R1", 10),
            ("PRINT", "R1"),
            ("HALT",),
        ],
        "asserts": lambda cpu: _assert(cpu.registers["R1"] == 41 and cpu.memory[10] == 42,
                                     "Se esperaba R1 == 42 y memoria[10] == 42")
    },
    {
        "name": "Multiplicacion 4 x 3 por sumas repetidas",
        "program": [
            ("LOAD",  "R0", 0),
            ("LOAD",  "R1", 4),
            ("LOAD",  "R2", 3),
            ("LOAD",  "R3", 1),
            ("ADD",   "R0", "R0", "R2"),
            ("SUB",   "R1", "R1", "R3"),
            ("JZ",    "R1", 8),
            ("JMP",   4),
            ("PRINT", "R0"),
            ("HALT",),
        ],
        "asserts": lambda cpu: _assert(cpu.registers["R0"] == 12, "Se esperaba R0 == 12")
    },
    {
        "name": "HALT inmediato detiene la ejecucion",
        "program": [
            ("HALT",),
            ("LOAD", "R0", 999),
        ],
        "asserts": lambda cpu: _assert(cpu.registers["R0"] == 0 and cpu.cycles == 1,
                                     "Se esperaba R0 == 0 y un solo ciclo ejecutado")
    }
]

# ----------------------------------------------------------------------
# Bucle de ejecución de los tests
# ----------------------------------------------------------------------
all_passed = True

for test in tests:
    success = run_test(test["name"], test["program"], test["asserts"])
    if not success:
        all_passed = False

print("\n----------------------------------------------------------------------")
if all_passed:
    print("Todas las pruebas pasaron correctamente.")
else:
    print("Algunas pruebas fallaron. Revisa el registro superior.")
