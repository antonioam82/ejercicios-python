import os
import matplotlib.pyplot as plt


#OBTENER TAMAÑO DE CARPETA
def get_directory_size(directory):
    total = 0
    try:
        for entry in os.scandir(directory):
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_directory_size(entry.path)
    except NotADirectoryError:
        return os.path.getsize(directory)
    except PermissionError:
        return 0
    return total

#OBTENER FORMATO
def get_size_format(b, factor=1024, suffix="B"):

    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    
    return f"{b:.2f}Y{suffix}"

size=get_size_format(get_directory_size(b'C:\Users\Antonio\Documents\docs'))
print("SIZE: ",size)


#GRAFICA CIRCULAR
def plot_pie(sizes, names):
    plt.pie(sizes, labels=names, autopct=lambda pct: f"{pct:.2f}%")
    plt.title("Different Sub-directory sizes in bytes")
    plt.show()

if __name__ == "__main__":
    import sys
    folder_path = b'C:\Users\Antonio\Documents\docs'

    directory_sizes = []
    names = []
    for directory in os.listdir(folder_path):
        directory = os.path.join(folder_path, directory)
        directory_size = get_directory_size(directory)
        if directory_size == 0:
            continue
        directory_sizes.append(directory_size)
        names.append(str(os.path.basename(directory)) + ": " + str(get_size_format(directory_size)))

    print("[+] Total directory size:", get_size_format(sum(directory_sizes)))
    plot_pie(directory_sizes, names)
