def get_potential_energy(rigidity, lengthening):
    lengthening /= 1000
    return (rigidity * lengthening * lengthening) / 2


try:
    lengthening = float(input("Введите значение растяжения пружины в мм: "))
except:
    print("Вы ввели неправильное значение")
    exit()

try:
    rigidity = float(input("Введите значение жёсткости пружины: "))
    if rigidity <= 0:
        raise ValueError
except:
    print("Вы ввели неправильное значение")
    exit()

potential_energy = get_potential_energy(rigidity, lengthening)

print(potential_energy)