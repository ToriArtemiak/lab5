class Items:
    def __init__(self, name, coordinates, new_coordinates):
        self.new_coordinates = new_coordinates
        self.name = name
        self.coordinates = coordinates

class Room:
    def __init__(self):
        self.objects = []

    def add_object(self, items):
        self.objects.append(items)

    def remove_object(self, items):
        self.objects.remove()

    def rearrangement(self, new_coordinates):
        for obj in self.objects:
            obj.coordinates = new_coordinates


sofa = Items("Sofa", [11, 8])
chair = Items("Chair", [7, 2])
lamp = Items("Lamp", [4, 22])

room = Room()
room.add_object(sofa)
room.add_object(chair)
room.add_object(lamp)

print("координати об'єктів до перестановки:")
for obj in room.objects:
    print(f"{obj.name}: {obj.coordinates}")


sofa = Items("Sofa",  [11, 8])
chair = Items("Chair", [7, 2])
lamp = Items("Lamp", [4, 22])



room.rearrangement(coordinates)

print("\nкоординати об'єктів після перестановки:")
for obj in room.objects:
    print(f"{obj.name}: {obj.coordinates}")


    class Items:
        def __init__(self, name, coordinates):
            self.name = name
            self.coordinates = coordinates


    class Room:
        def __init__(self):
            self.objects = []

        def add_object(self, items):
            self.objects.append(items)

        def remove_object(self, items):
            self.objects.remove(items)

        @logged(NegativeCoordinatesError, mode="console")
        def rearrangement(self, new_coordinates):
            for obj in self.objects:
                if new_coordinates[0] < 0 or new_coordinates[1] < 0:
                    raise NegativeCoordinatesError("Negative coordinates not allowed.")
                obj.coordinates = new_coordinates


    sofa = Items("Sofa", [11, 8])
    chair = Items("Chair", [7, 2])
    lamp = Items("Lamp", [4, 22])

    room = Room()
    room.add_object(sofa)
    room.add_object(chair)
    room.add_object(lamp)

    print("Координати об'єктів до перестановки:")
    for obj in room.objects:
        print(f"{obj.name}: {obj.coordinates}")

    try:
        room.rearrangement([-1, 5])  # Спричиняє NegativeCoordinatesError
    except NegativeCoordinatesError as nce:
        print(f"Caught NegativeCoordinatesError: {str(nce)}")

    print("\nКоординати об'єктів після перестановки:")
    for obj in room.objects:
        print(f"{obj.name}: {obj.coordinates}")