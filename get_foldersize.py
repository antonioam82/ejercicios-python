import os

def get_directory_size(directory):
    total = 0
    try:
        for entry in os.scandir(directory):
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_directory_size(entry.path)
    except NotADirectoryError:
        #SI LA RUTA ES A UN ARCHIVO
        return os.path.getsize(directory)
    except PermissionError:
        return 0
    print (total)
    return total

def get_size_format(b, factor=1024, suffix="B"):

    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    
    return f"{b:.2f}Y{suffix}"

size=get_size_format(get_directory_size(drectory))
print("SIZE: ",size)
