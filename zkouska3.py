class Osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def __str__(self):
        return f"Osoba(jmeno={self.jmeno}, vek={self.vek})"

class Student(Osoba):
    def __innit__(self, jmeno, vek, rocnik):
        super().__init__(jmeno, vek)
        self.rocnik = rocnik

class Ucitel(Osoba):
    def __innit__(self, jmeno, vek, obor):
        super().__init__(jmeno, vek)
        self.obor = obor

if __name__ == "__main__":
    student1 = Student("Adam", 20, 2)
    student2 = Student("Eva", 19, 1)
    ucitel = Ucitel("Tomas", 40, "IT")

    print(student1)
    print(student2)
    print(ucitel)