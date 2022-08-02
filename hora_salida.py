from datetime import datetime
import time

def main():
    hora_actual = time.strftime('%H:%M:%S', time.localtime())
    print("La hora actual es: ",hora_actual)
    if hora_actual == '19:00:00':
        print("Es hora de salir.")
    else:
        t1 = datetime.strptime(hora_actual,"%H:%M:%S")
        t2 = datetime.strptime('19:00:00',"%H:%M:%S")
        tiem_res = str(t2 - t1).split(":")
        print("Quedan {} horas, {} minutos y {} segundos, para la salida.".format(tiem_res[0],tiem_res[1],tiem_res[2]))


if __name__ == '__main__':
    main()
