from VALID import ns, OK

while True:
    print("----------------------------------------DRAKE EQUATION----------------------------------------")
    print("----------------------------N = R* x fp x ne x fl x fi x fc x L-------------------------------")

    R = OK(input("Average rate of star formation in the galaxy (new stars per year): "))
    fp = OK(input("Fraction of stars with planets: "))
    ne = OK(input("Stars with planets, the average number of planets with an environment suitable for life: "))
    fl = OK(input("Fraction of planets that develop life: "))
    fi = OK(input("Fraction of life­bearing planets with intelligent, civilized life: "))
    fc = OK(input("Fraction of civilizations that release detectable signs of their existence into space: "))
    L = OK(input("Length of time (in years) over which the civilizations release the detectable signals: "))

    N = R*fp*ne*fl*fi*fc*L
    print("{} Civilitations.".format(N))

    conti = ns(input("Continue(n/s): "))
    if conti == "n":
        break
