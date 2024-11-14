import sys
import os

def read_args(argv):
    output = {}
    i = 1
    while i < len(argv):
        if argv[i] == '-f' and len(argv) > i + 1:
            output['filepath'] = argv[i + 1]
            i += 2
        elif argv[i] == '-i' and len(argv) > i + 1:
            output['info'] = argv[i + 1]
            i += 2
        else:
            i += 1
    return output

def process_path(path):
    if not os.path.exists(path):
        return None
    else:
        binary_data = None
        try:
            with open(path, 'rb') as f:
                binary_data = bytearray(f.read())
        except Exception as e:
            print("Error reading file: {0}".format(str(e)))
        finally:
            return binary_data

def read_type_file(data):
    if len(data) >= 8 and data[:8] == b'\x89PNG\r\n\x1a\n':
        return 'png'
    else:
        return None

def binary_to_png(data,info):
    width = int.from_bytes(data[16:20])
    height = int.from_bytes(data[20:24])
    color_depht = data[24]
    if info == 'general':
        color_type = data[25]
        compression_methpd = data[26]
        filter_method = data[27]
        interlace_method = data[28]
        palette_red = data[29]
        palette_green = data[30]
        palette_blue = data[31]
        print("WIDTH: ",width)
        print("HEIGHT: ",height)
        print("COLOR DEPTH: ", color_depht)
        print("COLOR TYPE: ", color_type)
        print("COMPRESSION METHOD: ",compression_methpd)
        print("FILTER METHOD: ",filter_method)
        print("INTERLACE METHOD: ", interlace_method)
        print("PALETTE RED: ", palette_red)
        print("PALETTE GREEN: ", palette_green)
        print("PALETTE BLUE: ", palette_blue)
    else:
        offset = 33
        img = bytearray()
        while offset < len(data):
            length = int.from_bytes(data[offset:offset + 4], 'big')
            chunk_type = data[offset + 4: offset + 8]
            if chunk_type == b'IDAT':
                img.extend(data[offset + 8:offset + 8 + length])
            offset += 12 + length
        img_matrix = []
        offset = 0
        for row in range(height):
            row_pixel = []
            for col in range(width):
                if color_depht == 8 and len(img) >= offset + 3:
                    r = img[offset]
                    g = img[offset + 1]
                    b = img[offset + 2]
                    row_pixel.append((r,g,b))
                    offset += 3
            img_matrix.append(row_pixel)
        return img_matrix

def main():
    args = read_args(sys.argv)
    if 'filepath' not in args:
        filepath = None
        print("Not filepath found")
        sys.exit(1)
    else:
        #information_type = 'pixels'
        if 'info' not in args:
            print("Not info type provided")
            sys.exit(1)
        else:
            if args['info'] != 'general' and args['info'] != 'data':
                print("Invalid info type (enter 'general' or 'data')")
                sys.exit(1)
            else:
                binary_data = process_path(args['filepath'])
                #print("{0}".format(binary_data))
                if binary_data is None:
                    print("Binary data not found")
                    sys.exit(1)

                file_type = read_type_file(binary_data)
                if(file_type == 'png'):
                    #print("Es un png")
                    image_matrix = binary_to_png(binary_data,args['info'])
                    if args['info'] == 'data':
                        print(image_matrix)

    
if __name__ == '__main__':
    main()
