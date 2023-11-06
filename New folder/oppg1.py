#A)

# fikk hjelp fra chatgpt til å vise meg hvordan man bruker classes og følge PEP 8 og CamelCase konvensjonen.
class Film:
    def __init__(self, title, year, score):
        self.title = title
        self.year = year
        self.score = score
    
    def __str__(self):
        return f"{self.title} was released in {self.year} and currently has a score of {self.score}"
    

inception = Film("Inception", 2010, 8.8)
the_martian = Film("The Martian", 2015, 8.0)
joker = Film("Joker", 2019, 8.4)

print(inception)
print(the_martian)
print(joker)



#B) Ble ikke dette gjort i forrige oppgave?
