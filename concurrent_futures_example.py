'''import time
import random

def mail_letter(letter):
    #duration = random.randint(1, 5)
    duration = 2
    print(f"Started mailing letter {letter} (duration: {duration}s)")
    time.sleep(duration)
    print(f"Finished mailing letter {letter}")
    return f"Letter {letter} mailed"

if __name__ == '__main__':
    inicio = time.time()
    letters = ['A', 'B', 'C', 'D', 'E']
    results = []

    for letter in letters:
        result = mail_letter(letter)
        results.append(result)

    print("Mailing Results:")
    for result in results:
        print(result)
    fin = time.time()
    tiempo_total = fin - inicio
    print("Duration: ",tiempo_total)'''
########################################################3
import concurrent.futures
import time
import random

def mail_letter(letter):
    duration = random.randint(1, 5)
    #duration = 2
    print(f"Started mailing letter {letter} (duration: {duration}s)")
    time.sleep(duration)
    print(f"Finished mailing letter {letter}")
    return f"Letter {letter} mailed"

if __name__ == '__main__':
    inicio = time.time()
    letters = ['A', 'B', 'C', 'D', 'E']

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(mail_letter, letters))

    print("Mailing Results:")
    for result in results:
        print(result)
    fin = time.time()
    tiempo_total = fin - inicio
    print("Duration: ",tiempo_total)

###########################################################
'''import concurrent.futures
import time
import random

def mail_letter(letter):
    duration = random.randint(1, 5)
    print(f"Started mailing letter {letter} (duration: {duration}s)")
    time.sleep(duration)
    print(f"Finished mailing letter {letter}")
    return f"Letter {letter} mailed"

if __name__ == '__main__':
    letters = ['A', 'B', 'C', 'D', 'E']

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(mail_letter, letter): letter for letter in letters}

        for future in concurrent.futures.as_completed(futures):
            letter = futures[future]
            result = future.result()
            print(f"Result: {result}")'''
