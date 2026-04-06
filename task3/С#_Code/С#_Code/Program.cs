using System;

class Program
{
    static float GetPotentialEnergy(float rigidity, float lengthening)
    {
        lengthening /= 1000;
        return (rigidity * lengthening * lengthening) / 2;
    }

    static void Main()
    {
        float lengthening, rigidity, potentialEnergy;

        Console.Write("Введите значение растяжения пружины в мм: ");
        if (!float.TryParse(Console.ReadLine(), out lengthening))
        {
            Console.WriteLine("Вы ввели неправильное значение");
            return;
        }

        Console.Write("Введите значение жёсткости пружины: ");
        if (float.TryParse(Console.ReadLine(), out rigidity) && rigidity > 0)
        {
            potentialEnergy = GetPotentialEnergy(rigidity, lengthening);
            Console.WriteLine(potentialEnergy);
        }
        else
        {
            Console.WriteLine("Вы ввели неправильное значение");
            return;
        }
    }
}