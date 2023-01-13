from Flight import *
from Airport import *

allAirports = []
allFlights = {}


def loadData(airportFile, flightFile):
    try:  # tries opening and reading the files
        airports = open(airportFile)
        flights = open(flightFile)

        line = airports.readline()
        while line != "":  # removes white spaces in the lines and turns each line into an object
            line = line.rstrip("\n").split(",")
            count = 0
            for item in line:
                line[count] = item.strip()  # strips white space around each element in the line
                count += 1
            aObjects = Airport(line[0], line[2], line[1])
            allAirports.append(aObjects)  # each object is appended onto a list
            line = airports.readline()
        airports.close()

        origin = ""
        destination = ""
        line = flights.readline()
        while line != "":  # removes white spaces in the lines and turns each line into an object
            line.rstrip("\n")
            line = ("".join(line.split())).split(",")  # removes all white spaces and forms a list
            for item in allAirports:
                if item.getCode() == line[1]:  # finds airport object for the origin and destination codes
                    origin = Airport(item.getCode(), item.getCity(), item.getCountry())
                if item.getCode() == line[2]:
                    destination = Airport(item.getCode(), item.getCity(), item.getCountry())
            fObjects = Flight(line[0], origin, destination)
            originCode = fObjects._origin.getCode()
            if originCode not in allFlights:  # creates a key and value list for each airport code and its corresponding flight numbers
                allFlights[originCode] = []
                allFlights[originCode].append(fObjects)
            else:
                allFlights[originCode].append(fObjects)
            line = flights.readline()
        flights.close()
        return True

    except:
        return False


def getAirportByCode(code):  # returns with the airport object with the given code
    ans = 0
    item = ""
    for item in allAirports:
        if item.getCode() == code:
            ans = 1
            break
    if ans == 1:
        return item
    else:
        return -1


def findAllCityFlights(city):  # returns a list that has all flight objects with the given city as an origin or destination
    cityList = []
    code = ""
    airport = ""

    for item in allAirports:
        if city == item.getCity():
            code = item.getCode()
            airport = item
            break

    for key in allFlights:
        if str(code) == key:  # matches the city's code to the key to find and add all the flight numbers to a returned list
            for value in allFlights[code]:
                cityList.append(value)
        else:
            for value in allFlights[key]:
                if str(value.getDestination()) == str(airport):
                    cityList.append(value)
    return cityList


def findAllCountryFlights(country):  # returns a list that has all flight objects with the given country as an origin/destination
    countryList = []
    codeList = []

    for item in allAirports:
        if country == item.getCountry():
            codeList.append(item.getCode())

    for code in codeList:
        for key in allFlights:
            for value in allFlights[key]:
                if code in str(value.getDestination()):  # appends flight numbers if the airports are of the same country of destination
                    countryList.append(value)
            if code == key:  # appends flight numbers if the airports are of the same country of origin
                for value in allFlights[key]:
                    countryList.append(value)

    return countryList


def findFlightBetween(origAirport, destAirport):  # finds a direct flight or a list of connecting flights, if they exist
    connectingAirports = set()

    for key in allFlights:
        for values in allFlights[key]:  # compares each flight's origin and destination to find direct flight
            if values._origin.getCode() == origAirport.getCode() and values._destination.getCode() == destAirport.getCode():
                return "Direct Flight: " + origAirport.getCode() + " to " + destAirport.getCode()

            elif values._origin.getCode() == origAirport.getCode():  # finds flight with matching origin and sets destination as a connecting airport
                connection = values._destination.getCode()
                for city in allFlights:
                    for value in allFlights[city]:
                        if value._origin.getCode() == connection and value._destination.getCode() == destAirport.getCode():
                            connectingAirports.add(str(connection))  # will add connecting airport to a set if the origin and destination are correct

    if len(connectingAirports) > 0:
        return connectingAirports
    else:
        return -1


def findReturnFlight(firstFlight):  # finds the return flight object from a given flight object
    for key in allFlights:
        for value in allFlights[key]:
            if str(value.getOrigin()) == str(firstFlight.getDestination()) and str(value.getDestination()) == str(firstFlight.getOrigin()):
                return value
    return -1
