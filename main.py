class Parking:
    def __init__(self):
        self.cars = []

    def enter(self, plate):
        if plate not in self.cars:
            self.cars.append(plate)

    def leave(self, plate):
        if plate in self.cars:
            self.cars.remove(plate)

    def show(self):
        print("Cars in parking:")
        for c in self.cars:
            print(c)


def menu():
    p = Parking()

    while True:
        print("\n1.Enter 2.Leave 3.Show 0.Exit")
        c = input(">> ")

        if c == "1":
            p.enter(input("Plate: "))
        elif c == "2":
            p.leave(input("Plate: "))
        elif c == "3":
            p.show()
        elif c == "0":
            break


if __name__ == "__main__":
    menu()
