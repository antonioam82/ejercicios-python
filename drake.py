from VALID import ny

def se(q):
    while True:
        p = input(q)
        try:
            r = float(p)
            break
        except Exception as e:
            r = str(e)
            print(r)
    return r

while True:
    print("----------------------------------------DRAKE EQUATION----------------------------------------")
    print("----------------------------N = R* x fp x ne x fl x fi x fc x L-------------------------------")

    R = se("Average rate of star formation in the galaxy (new stars per year): ")
    fp = se("Fraction of stars with planets: ")
    ne = se("Stars with planets, the average number of planets with an environment suitable for life: ")
    fl = se("Fraction of planets that develop life: ")
    fi = se("Fraction of life­bearing planets with intelligent, civilized life: ")
    fc = se("Fraction of civilizations that release detectable signs of their existence into space: ")
    L = se("Length of time (in years) over which the civilizations release the detectable signals: ")

    N = R*fp*ne*fl*fi*fc*L
    print("\n{} Civilitations.".format(N))

    conti = ny(input("Continue(n/y)?: "))
    if conti == "n":
        break

