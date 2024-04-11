import pickle
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass

    def eat(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Reptile(Animal):
    def speak(self):
        return "Squeak!"


class Bird(Animal):
    def speak(self):
        return "Chirp!"


class Mammal(Animal):
    def speak(self):
        return "Aargh!"


def animal_speak(anim):
    print(anim.speak())


dog = Dog("Toto", 5)
cat = Cat("Tom", 2)
lizard = Reptile("Lizzy", 1)
bird = Bird("Popo", 1)
mammal = Mammal("Monty", 10)

animals = [dog, cat, lizard, bird, mammal]

for animal in animals:
    animal_speak(animal)


class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, anim):
        print(f"{self.name} feeds {anim.name}")


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, anim):
        print(f"{self.name} heals {anim.name}")


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, anim):
        self.animals.append(anim)
        print(f"Animal {anim.name} added to Zoo")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Worker {staff_member.name} added to Zoo")

    def show_animals(self):
        print("Animals in Zoo:")
        for anim in self.animals:
            print(f"- {anim.name}, {anim.speak()}")

    def show_staff(self):
        print("Workers in Zoo:")
        for staff in self.staff:
            print(f"- {staff.name}")
    def save_zoo(self, file_name):
        with open(file_name, 'wb') as file:
            pickle.dump((self.animals, self.staff), file)
        print("Информация о зоопарке сохранена")

    def load_zoo(self, file_name):
        with open(file_name, 'rb') as file:
            self.animals, self.staff = pickle.load(file)
        print("Информация о зоопарке загружена")

zoo = Zoo()

# Добавляем животных, используя уже созданные экземпляры
for animal in animals:
    zoo.add_animal(animal)

# Создаем и добавляем сотрудников
zoo_keeper = ZooKeeper("Алексей")
veterinarian = Veterinarian("Марина")

zoo.add_staff(zoo_keeper)
zoo.add_staff(veterinarian)

# Выводим информацию о животных и сотрудниках
zoo.show_animals()
zoo.show_staff()
zoo.save_zoo('zoo_data.pkl')

# Создаем новый экземпляр зоопарка и загружаем информацию
new_zoo = Zoo()
new_zoo.load_zoo('zoo_data.pkl')
new_zoo.show_animals()
new_zoo.show_staff()
