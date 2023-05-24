class Airport:

    # initializer for the variables representing the code, city and country of the airport
    def __init__(self, code, city, country):
        self._code = code
        self._city = city
        self._country = country

    # representation of the function: returns the Airport object in a format which contains the code, city and country of the airport
    def __repr__(self):
        return self._code + "(" + str(self._city) + ", " + str(self._country) + ")"

    # function which returns the code variable in the object
    def getCode(self):
        return self._code

    # function which returns the city variable in the object
    def getCity(self):
        return self._city

    # function which returns the country variable in the object
    def getCountry(self):
        return self._country

    # function which modifies the city variable to a new city
    def setCity(self, city):
        self._city = city

    # function which modifies the country variable to a new country
    def setCountry(self, country):
        self._country = country