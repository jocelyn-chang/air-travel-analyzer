from Airport import *


class Flight:
    def __init__(self, flightNo, origin, destination):  # initializes flightNo, origin, and destination variables
        if isinstance(origin, Airport) and isinstance(destination, Airport):  # checks if parameters are in the Airport class
            self._flightNo = flightNo
            self._origin = origin
            self._destination = destination
        else:
            raise TypeError("The origin and destination must be Airport objects")

    def __repr__(self):
        if self.isDomesticFlight():  # proceeds if self.isDomesticFlight() is true
            location = "domestic"
        else:
            location = "international"
        originCity = self._origin.getCity()
        destinationCity = self._destination.getCity()
        return "Flight: " + self._flightNo + " from " + originCity + " to " + destinationCity + " {" + location + "}"

    def __eq__(self, other):
        if isinstance(other, Flight):  # checks if airport codes are the same and that the "other" is a flight object
            if self._origin == other._origin and self._destination == other._destination:
                return True
        else:
            return False

    def getFlightNumber(self):
        return self._flightNo

    def getOrigin(self):
        return self._origin

    def getDestination(self):
        return self._destination

    def isDomesticFlight(self):
        if self._origin.getCountry() == self._destination.getCountry():  # compares the country of the flight's origin and destination
            return True
        else:
            return False

    def setOrigin(self, origin):
        self._origin = origin

    def setDestination(self, destination):
        self._destination = destination
