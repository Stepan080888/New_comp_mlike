from model.postaldata import Postaldata
import random
import string
import jsonpickle
import os.path


constant = [
    Postaldata(country="Albania", name="Jhon Travolta", street="Shev4enka str", num_house="12", city="Drogobych",state="Lviv reg", zip="12300", phone="0978339274"),
    Postaldata(country="Albania", name="Jhon Travolta2", street="Shev4enka2 str", num_house="123", city="Drogobych2",state="Lviv reg2", zip="12301", phone="09783392742")
]

def rand_str(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

country = ["Albania", "American Samoa", "Aruba", "Ukraine", "Austria", "Nigeria"]
#counry_list[]
#[Postaldata(country="Algeria", name="Jhon Travolta", street="Shev4enka str", num_house="12", city="Drogobych",state="Lviv reg", zip=12300, phone="0978339274")] +

testdata = [Postaldata(country=country[i], name=rand_str("name", 5), street=rand_str("street", 5),
                            num_house=rand_str("num", 5), city=rand_str("city", 5), state=rand_str("state", 5),
                            zip=int(random.randint(10000, 99000)), phone=rand_str("phone", 5)) for i in range(5)]

def load_from_json():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"../data/postal_data.json")) as f:
        return jsonpickle.decode(f.read())

testdata2 = load_from_json()


data_for_creation_postaldata_in_smoke_test = Postaldata(country="Albania", name="Jhon Travolta", street="Shev4enka str", num_house="12", city="Drogobych",state="Lviv reg", zip="12300", phone="0978339274")



