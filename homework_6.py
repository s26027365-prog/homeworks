class Distance:
    conversion_dict = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000
    }

    def __init__(self, value, unit="m"):
        self.value = float(value)
        self.unit = unit

    def convert(self):
        return self.value * Distance.conversion_dict.get(self.unit, 1)

    def __str__(self):
        return f"{self.value} {self.unit}"

    def __add__(self, other):
        self_meters = self.convert()
        other_meters = other.convert()
        result_meters = self_meters + other_meters
        coefficient = Distance.conversion_dict.get(self.unit, 1)
        result_value = result_meters / coefficient
        return Distance(result_value, self.unit)

    def __sub__(self, other):
        self_meters = self.convert()
        other_meters = other.convert()
        result_meters = self_meters - other_meters
        coefficient = Distance.conversion_dict.get(self.unit, 1)
        result_value = result_meters / coefficient
        return Distance(result_value, self.unit)


if __name__ == "__main__":
    a = Distance(10, 'm')
    b = Distance(2, 'km')
    c = Distance(100, 'cm')

    print(f"{a} + {b} = {a + b}")
    print(f"{b} - {a} = {b - a}")
    print(f"{a} + {c} = {a + c}")