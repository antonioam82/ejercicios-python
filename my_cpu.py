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
            raise ValueError(f"Instruccion desconocida: {op}")

    def run(self):
        while self.running and self.pc < len(self.program):
            instruction = self.fetch()
            if self.trace:
                print(f"   PC={self.pc - 1:2d} | {instruction} | {self.registers} | {self.memory[:12]}")
            self.execute(instruction)
            self.cycles += 1



def _assert(condicion, mensaje):
    if not condicion:
        raise AssertionError(mensaje)


def run_test(nombre, program, asserts, trace=False):
    """Ejecuta un programa en la CPU y comprueba el resultado con 'asserts'."""
    print(f"\n=== {nombre} ===")
    cpu = CPU(program, trace=trace)
    cpu.run()
    asserts(cpu)
    print(f"   Ciclos ejecutados: {cpu.cycles}")
    print("   PASA EL TEST")


# ----------------------------------------------------------------------
# Test 1: suma de 1 a 5 usando un bucle (LOAD, ADD, SUB, JZ, JMP, PRINT)
# ----------------------------------------------------------------------
programa_suma = [
    ("LOAD",  "R0", 0),
    ("LOAD",  "R1", 5),
    ("LOAD",  "R3", 1),
    ("ADD",   "R0", "R0", "R1"),   # direccion 3: inicio del bucle
    ("SUB",   "R1", "R1", "R3"),
    ("JZ",    "R1", 7),
    ("JMP",   3),
    ("PRINT", "R0"),
    ("HALT",),
]

run_test(
    "Suma de 1 a 5 con bucle",
    programa_suma,
    lambda cpu: _assert(cpu.registers["R0"] == 15, "Se esperaba R0 == 15"),
    trace=True,
)

# ----------------------------------------------------------------------
# Test 2: STORE y LOADM, ida y vuelta a memoria
# ----------------------------------------------------------------------
programa_memoria = [
    ("LOAD",  "R0", 42),
    ("STORE", "R0", 10),   # guarda 42 en la direccion de memoria 10
    ("LOADM", "R1", 10),   # carga ese mismo valor en R1
    ("PRINT", "R1"),
    ("HALT",),
]

run_test(
    "Escritura y lectura de memoria (STORE/LOADM)",
    programa_memoria,
    lambda cpu: _assert(cpu.registers["R1"] == 42 and cpu.memory[10] == 42,
                         "Se esperaba R1 == 42 y memoria[10] == 42"),
)

# ----------------------------------------------------------------------
# Test 3: multiplicacion 4 x 3 mediante suma repetida (no hay MUL nativo)
# ----------------------------------------------------------------------
programa_mult = [
    ("LOAD",  "R0", 0),    # producto acumulado
    ("LOAD",  "R1", 4),    # contador (multiplicando)
    ("LOAD",  "R2", 3),    # valor a sumar en cada vuelta (multiplicador)
    ("LOAD",  "R3", 1),    # constante 1
    ("ADD",   "R0", "R0", "R2"),  # direccion 4: inicio del bucle
    ("SUB",   "R1", "R1", "R3"),
    ("JZ",    "R1", 8),
    ("JMP",   4),
    ("PRINT", "R0"),
    ("HALT",),
]

run_test(
    "Multiplicacion 4 x 3 por sumas repetidas",
    programa_mult,
    lambda cpu: _assert(cpu.registers["R0"] == 12, "Se esperaba R0 == 12"),
)

# ----------------------------------------------------------------------
# Test 4: HALT inmediato, la CPU no debe ejecutar nada mas
# ----------------------------------------------------------------------
programa_halt = [
    ("HALT",),
    ("LOAD", "R0", 999),  # nunca deberia ejecutarse
]

run_test(
    "HALT inmediato detiene la ejecucion",
    programa_halt,
    lambda cpu: _assert(cpu.registers["R0"] == 0 and cpu.cycles == 1,
                         "Se esperaba R0 == 0 y un solo ciclo ejecutado"),
)


print("\nTodas las pruebas pasaron correctamente.")
