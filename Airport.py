class Airport:
    def __init__(self, code, city, country):  # initializes code, city, and country variables
        self._code = code
        self._city = city
        self._country = country

    def __repr__(self):
        self._format = self._code + "(" + self._city + ", " + self._country + ")"  # returns specified format
        return self._format

    def getCode(self):
        return self._code

    def getCity(self):
        return self._city

    def getCountry(self):
        return self._country

    def setCity(self, city):
        self._city = city

    def setCountry(self, country):
        self._country = country
