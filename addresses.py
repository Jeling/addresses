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
        return (f"""Wybieram numer {self.primary_phone} i dzwonię do {self.name} {self.surname}""")

    def __str__(self):
        return (self.name + " " + self.surname + ", " + self.phone + ", " + self.e_mail) 

    @property
    def label_length(self):
        return len(self.name) + len(self.surname) + 1
    
    @property
    def primary_phone(self):
        primary_phone = self.phone
        return primary_phone

class BusinessCard(Card):
    def __init__(self, company, position, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position
        self.business_phone = business_phone

    def __str__(self):
        return (self.name + " " + self.surname + ", " + self.phone + ", " + self.e_mail + ", " + self.company + ", " + self.position + ", " + self.business_phone)
    
    @property
    def primary_phone(self):
        primary_phone = self.business_phone
        return primary_phone

def create_contacts(card_type, quantity_of_cards):
    from faker import Faker
    fake = Faker()
    cards = []

    if card_type == 1:
        for card in range (quantity_of_cards):
            cards.append(Card(name=fake.first_name(), surname=fake.last_name(), phone=fake.phone_number(), e_mail=fake.ascii_company_email()))
    
    else:
        for card in range (quantity_of_cards):
            cards.append(BusinessCard(name=fake.first_name(), surname=fake.last_name(), phone=fake.phone_number(), e_mail=fake.ascii_company_email(), company=fake.company(), position=fake.job(), business_phone=fake.phone_number()))
    
    return cards

def __main__():
    cls()

    card_type = int(input("Chcesz wygenerować wizytówki (1) zwykłe czy (2) biznesowe? "))
    quantity_of_cards = int(input("Ile profili chcesz wygenereować? "))

    cards = create_contacts(card_type, quantity_of_cards)
    for card in cards:
        print(card)
        print(card.contact())
        print(f"""Imię i nazwisko (wraz ze spacją) mają {card.label_length} znaków""")
    

__main__()