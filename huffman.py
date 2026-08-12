import heapq
import math
from collections import Counter

def huffman_encoding(data):
    frequency = Counter(data)
    print(frequency)
    
    heap = [[freq, [char, ""]] for char, freq in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        for pair in left[1:]:
            pair[1] = '0' + pair[1]
        for pair in right[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])
    huffman_codes = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
    code_dict = {char: code for char, code in huffman_codes}
    encoded_data = ''.join(code_dict[char] for char in data)
    return code_dict, encoded_data


def fixed_length_encoding(data):
    """Codifica el texto asignando a cada carácter distinto
    un código binario de longitud fija (sin usar Huffman)."""
    simbolos = sorted(set(data))
    n_simbolos = len(simbolos)
    
    # Número de bits necesarios para representar todos los símbolos
    bits = max(1, math.ceil(math.log2(n_simbolos))) if n_simbolos > 1 else 1
    
    fixed_dict = {char: format(i, f'0{bits}b') for i, char in enumerate(simbolos)}
    fixed_encoded = ''.join(fixed_dict[char] for char in data)
    
    return fixed_dict, fixed_encoded, bits


texto = "ABRACADABRA"

# --- Codificación Huffman ---
codes, compressed = huffman_encoding(texto)
print("Códigos Huffman:", codes)
print("Texto comprimido (Huffman):", compressed)
print("Longitud comprimida (Huffman):", len(compressed), "bits")

print()

# --- Codificación sin Huffman (longitud fija) ---
fixed_codes, fixed_compressed, bits = fixed_length_encoding(texto)
print(f"Códigos de longitud fija ({bits} bits por símbolo):", fixed_codes)
print("Texto comprimido (sin Huffman):", fixed_compressed)
print("Longitud comprimida (sin Huffman):", len(fixed_compressed), "bits")

print()

# --- Comparación ---
print(f"Ahorro con Huffman: {len(fixed_compressed) - len(compressed)} bits "
      f"({100 * (1 - len(compressed)/len(fixed_compressed)):.2f}% de reducción)")
