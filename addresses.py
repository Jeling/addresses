import os

def cls():
    os.system('cls')

class Card:
    def __init__(self, name, surname, phone, e_mail):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.e_mail = e_mail

    def contact(self):
        return (f"""Wybieram numer {self.phone} i dzwonię do {self.name} {self.surname}""")

    @property
    def label_length(self):
        return len(self.name) + len(self.surname) + 1

class BusinessCard(Card):
    def __init__(self, company, position, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position
        self.business_phone = business_phone
    
    def contact(self):
        return (f"""Wybieram numer {self.business_phone} i dzwonię do {self.name} {self.surname}""")
    
    @property
    def label_length(self):
        return len(self.name) + len(self.surname) + 1

def create_contacts(card_type, quantity_of_cards):
    from faker import Faker
    fake = Faker()
    cards = []

    if card_type == 1:
        for card in range (quantity_of_cards):
            cards.append(Card(name=fake.first_name(), surname=fake.last_name(), phone=fake.phone_number(), e_mail=fake.ascii_company_email()))
        for card in cards:
            print(card.name + " " + card.surname + ", " + card.phone + ", " + card.e_mail)
            print(card.contact())
            print(f"""Imię i nazwisko (wraz ze spacją) mają {card.label_length} znaków""")
    
    else:
        for card in range (quantity_of_cards):
            cards.append(BusinessCard(name=fake.first_name(), surname=fake.last_name(), phone=fake.phone_number(), e_mail=fake.ascii_company_email(), company=fake.company(), position=fake.job(), business_phone=fake.phone_number()))
        for card in cards:
            print(card.name + " " + card.surname + ", " + card.phone + ", " + card.e_mail + ", " + card.company + ", " + card.position + ", " + card.business_phone)
            print(card.contact())
            print(f"""Imię i nazwisko (wraz ze spacją) mają {card.label_length} znaków""")

def __main__():
    cls()

    card_type = int(input("Chcesz wygenerować wizytówki (1) zwykłe czy (2) biznesowe?"))
    quantity_of_cards = int(input("Ile profili chcesz wygenereować? "))

    create_contacts(card_type, quantity_of_cards)

# cards = [Card(name="Ronald", surname="Griffith", company="Turtle's Records & Tapes", position="Heating equipment technician", e_mail="RonaldSGriffith@dayrep.com"),
# Card(name="Elizabeth", surname="Brumfield", company="Schweggmanns", position="Boilermaker", e_mail="ElizabethBBrumfield@teleworm.us"),
# Card(name="Petra", surname="Hubáčková", company="Raleigh's", position="Library binding worker", e_mail="PetraHubackova@dayrep.com"),
# Card(name="Atilla", surname="de Looff", company="Gene Walter's Marketplace", position="Rehabilitation counselor", e_mail="AtilladeLooff@rhyta.com"),
# Card(name="Sakari", surname="Kivistö", company="Four Leaf Clover", position="Electronic typesetting machine operator", e_mail="SakariKivisto@armyspy.com")]

""" from faker import Faker
fake = Faker()

cards = []

cls()

quantity_of_fake_people = int(input("Ile profili chcesz wygenereować? "))
for card in range (quantity_of_fake_people):
    cards.append(Card(name=fake.first_name(), surname=fake.last_name(), company=fake.company(), position=fake.job(), e_mail=fake.ascii_company_email())) """

# for card in cards:
#     print(card.name + " " + card.surname + ", " + card.company + ", " + card.position + ", " + card.e_mail)

# by_first_name = sorted(cards, key=lambda card: card.name)
# by_last_name = sorted(cards, key=lambda card: card.surname)
# by_e_mail = sorted(cards, key=lambda card: card.e_mail)

# for card in by_first_name:
#     print(card.name + " " + card.surname + ", " + card.company + ", " + card.position + ", " + card.e_mail)

# for card in by_last_name:
#     print(card.name + " " + card.surname + ", " + card.company + ", " + card.position + ", " + card.e_mail)

# for card in by_e_mail:
#     print(card.name + " " + card.surname + ", " + card.company + ", " + card.position + ", " + card.e_mail)

# for card in cards:
#     print(card.contact())
#     print(f"""Imię i nazwisko mają razem {card.length_of_name} znaków""")


__main__()