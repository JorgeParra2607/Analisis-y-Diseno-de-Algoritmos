def first_fit(procesos, bloques):
    asignacion= [-1] * len(procesos)

    for i in range(len(procesos)):
        for j in range(len(bloques)):
            if bloques[j] >= procesos[i]:
                asignacion[i]= j
                bloques[j] -= procesos[i]
                break

    print("\nProceso\tTamaño\tBloque asignado")
    for i in range(len(asignacion)):
        bloque= asignacion[i]
        if bloque != -1:
            print(f"{i+1}\t{procesos[i]}\t{bloque+1}")
        else:
            print(f"{i+1}\t{procesos[i]}\tNo asignado")

    print("\nBloque\tMemoria libre")
    for i in range(len(bloques)):
        print(f"{i+1}\t{bloques[i]}")

def main():
    procesos= list(map(int, input("\nIntroduce los tamaños de los procesos separados por espacios: ").split()))
    bloques= list(map(int, input("\nIntroduce los tamaños de los bloques de memoria separados por espacios: ").split()))
    first_fit(procesos, bloques)

if __name__ == "__main__":
    main()
