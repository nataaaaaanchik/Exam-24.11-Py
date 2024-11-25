class Temperature:
    def __init__(self, temperature, unit):
        allowed_units = ['C', 'K', 'F']
        if unit not in allowed_units:
            raise ValueError("Одиниця вимірювання повинна бути 'C', 'K' або 'F'.")
        if unit == 'C' and temperature < -273.15:
            raise ValueError("Температура не може бути нижчою за -273.15°C.")
        if unit == 'K' and temperature < 0:
            raise ValueError("Температура не може бути нижчою за 0K.")
        if unit == 'F' and temperature < -459.67:
            raise ValueError("Температура не може бути нижчою за -459.67°F.")
        self.temperature = temperature
        self.unit = unit

    def convert_to(self, new_unit):
        if new_unit not in ['C', 'K', 'F']:
            raise ValueError("Одиниця вимірювання повинна бути 'C', 'K' або 'F'.")
        if self.unit == new_unit:
            raise ValueError("Температура вже у цій одиниці.")
        if self.unit == 'C':
            if new_unit == 'K':
                return Temperature(self.temperature + 273.15, 'K')
            elif new_unit == 'F':
                return Temperature(self.temperature * 9 / 5 + 32, 'F')
        elif self.unit == 'K':
            if new_unit == 'C':
                return Temperature(self.temperature - 273.15, 'C')
            elif new_unit == 'F':
                return Temperature((self.temperature - 273.15) * 9 / 5 + 32, 'F')
        elif self.unit == 'F':
            if new_unit == 'C':
                return Temperature((self.temperature - 32) * 5 / 9, 'C')
            elif new_unit == 'K':
                return Temperature((self.temperature - 32) * 5 / 9 + 273.15, 'K')

    def __str__(self):
        return f"{self.temperature}°{self.unit}"


try:
    temp = Temperature(25, 'C')
    print(temp)

    kelvin_temp = temp.convert_to('K')
    print(kelvin_temp)

    fahrenheit_temp = temp.convert_to('F')
    print(fahrenheit_temp)
except ValueError as e:
    print(f"Помилка: {e}")
