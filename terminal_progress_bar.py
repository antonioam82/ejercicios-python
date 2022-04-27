import math
from colorama import Back, init

init()
print("LOADING...")
def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = (Back.GREEN+' '+Back.RESET) * int(percent) + '-' * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")

numbers = [x * 5 for x in range(2000,3000)]
results = []

progress_bar(0, len(numbers))

for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    progress_bar(i + 1, len(numbers))
