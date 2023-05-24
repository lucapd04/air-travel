# first I imported my functions from Flight.py and Airport.py, followed by initializing the containers in which I will store my Airport Objects and Flight Objects
from Flight import *
from Airport import *
allAirports = set()
allFlights = dict()

# function which reads the text files for airports and flights, then stores all the data collected into the containers
def loadData(airportFile, flightFile):
    try: # try statement to check for any exceptions
        airports = open(airportFile, "r", encoding="utf8")
        flights = open(flightFile, "r", encoding="utf8")
        global allAirports
        global allFlights

        # for loop responsible for storing all objects of the class Airport
        for line in airports:
            entries = line.split(",")
            CODE = entries[0].strip()
            COUNTRY = entries[1].strip()
            CITY = entries[2].strip()
            allAirports.add(Airport(CODE, CITY, COUNTRY))

        # for loop which creates a dictionary, where the keys are the codes of each airport in the list, and the values are all objects of the class Flight
        flightNumberList = set()
        for line in flights:
            entries = line.split(",")

            # list of constants which describes what each entry of a line represents
            FLIGHT_NUMBER = entries[0].strip()
            ORIGIN = entries[1].strip()
            DESTINATION = entries[2].strip()
            flightNumberList.add(FLIGHT_NUMBER)

            # airport objects are found using the getAirportByCode function on the airport codes of the origin and destination airports. These objects are then used to create the Flight objects
            airportObject = getAirportByCode(ORIGIN)
            airportObject2 = getAirportByCode(DESTINATION)
            flightObject = Flight(FLIGHT_NUMBER, airportObject, airportObject2)
            ORIGIN_CODE = (flightObject.getOrigin()).getCode()
            if ORIGIN_CODE not in allFlights:
                allFlights[ORIGIN_CODE] = []
            if str(flightObject.getFlightNumber()) in flightNumberList:
                allFlights[ORIGIN_CODE].append(flightObject)

        return True

    # except statement which determines whether the files named exist or not
    except FileNotFoundError:
        print("Error: file not found")
        return False

# function which detects if there is an Airport object with the respective airport code within the set, and return it if it exists.
def getAirportByCode(code):
    for airport in allAirports:
        if airport.getCode() == code:
            return airport
    return -1

# function which collects all Flight objects which have the respective city as its origin or destination
def findAllCityFlights(city):
    cityFlights = []
    for flights in allFlights.items():
        for flights in flights[1]:
            if city in str(flights):
                cityFlights.append(flights)

    return cityFlights

# function which collects all Flight objects which have the respective country as its origin or destination
def findAllCountryFlights(country):
    countryFlights = []
    for airports in allFlights:
        for flights in allFlights[airports]:
            if (flights.getOrigin()).getCountry() == country or (flights.getDestination()).getCountry() == country:
                countryFlights.append(flights)

    return countryFlights

# function which finds a direct flight between two airports, or looks for a set of connecting flights if there is no such option available. If neither flights are found then the function returns nothing.
def findFlightBetween(origAirport, destAirport):
    connectingFlights = set()
    for airports in allFlights:
        if airports == origAirport.getCode():
            for flights in allFlights[airports]:
                if (flights.getDestination()).getCode() == destAirport.getCode():
                    return "Direct Flight: " + str(origAirport.getCode()) + " to " + str(destAirport.getCode())

            # for loop runs through allFlights dictionary again to look for flights between the connection location and the final destination
            for flights in allFlights[airports]:
                CONNECTION_CODE = (flights.getDestination()).getCode()
                for airports in allFlights:
                    if CONNECTION_CODE == airports:
                        for flights in allFlights[airports]:
                            if (flights.getDestination()).getCode() == destAirport.getCode():
                                connectingFlights.add(CONNECTION_CODE)

            if len(connectingFlights) == 0:
                return -1
            else:
                return connectingFlights

# determines if there is a new flight which returns returns to the original location from which the previous flight took off from
def findReturnFlight(firstFlight):
    ORIGIN_CODE = (firstFlight.getOrigin()).getCode()
    DESTINATION_CODE = (firstFlight.getDestination()).getCode()

    # using the values stored in the two constants above, the for loop looks through a flight in which the positions of both constants are flipped
    for airports in allFlights:
        if DESTINATION_CODE == airports:
            for flights in allFlights[airports]:
                NEW_CODE = (flights.getDestination()).getCode()
                if NEW_CODE == ORIGIN_CODE:
                    return flights
    return -1
