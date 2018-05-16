class Postaldata:

    def __init__(self, country="Select Country", name=None, street=None, num_house=None, city=None, state=None, zip=None, phone=None, sec_code=None, address_det=None):
        self.country = country
        self.name = name
        self.street = street
        self.num_house = num_house
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.sec_code = sec_code
        self.address_det = address_det

    def __repr__(self):
        return "%s : %s :  %s" % (self.country, self.name, self.zip)

    def __eq__(self, other):
        return self.country == other.country and self.name == other.name and self.street == other.street and self.num_house == other.num_house and self.city == other.city and self.state == other.state and self.phone == other.phone
        """
        and self.num_house == other.num_house and self.city == other.city and self.state == other.state and self.zip == other.zip and self.phone == other.phone and self.sec_code == other.sec_code and self.address_det == other.address_det
        """
    def sort_param(self):
        return int(self.zip)
