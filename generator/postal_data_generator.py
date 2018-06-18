from model.postaldata import Postaldata
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of group", "file"]) # n-number generated data, f-file tu put all previeous inf
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 100
f = "data/postal_data.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def rand_str(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

country = ["Albania" for i in range(n)]+["American Samoa" for i in range(n)]+["Aruba" for i in range(n)]+["Ukraine"for i in range(n)]+["Austria" for i in range(n)]+["Nigeria" for i in range(n)]

#[Postaldata(country="Algeria", name="Jhon Travolta", street="Shev4enka str", num_house="12", city="Drogobych",state="Lviv reg", zip=12300, phone="0978339274")] +

testdata = [Postaldata(country=country[random.randint(0, len(country))], name=rand_str("name", 5), street=rand_str("street", 5),
                            num_house=rand_str("num", 5), city=rand_str("city", 5), state=rand_str("state", 5),
                            zip=int(random.randint(10000, 99000)), phone=rand_str("phone", 5)) for i in range(n)]

postal_data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(postal_data_file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))


#getopt — Parser for command line options where to read https://docs.python.org/3.1/library/getopt.html -n 10 -f data/test1.json