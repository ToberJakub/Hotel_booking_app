import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})
df_cards = pandas = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = 'no'
        df.to_csv("hotels.csv", index=False)

    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class Reservation:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank yoy for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, owner, cvc):
        card_data = {'number': self.number, "expiration": expiration,
                     "owner": owner, "cvc": cvc}




print(df)
hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID)

if hotel.available():
    credit_card = CreditCard(number="1234567890123456")
    if credit_card.validate(expiration="12/26", owner="JOHN SMITH", cvc="123"):
        hotel.book()
        name = input("Enter your name: ")
        reservation = Reservation(customer_name=name, hotel_object=hotel)
        print(reservation.generate())
    else:
        print("There was a problem with your payment")
else:
    print("Hotel is not free")


