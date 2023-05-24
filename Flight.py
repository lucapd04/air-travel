from Airport import *

class Flight:

    # detects if the origin and destination are objects of the class Airport, then initializes the respective variable if so, or raises a typeError if not the case
    def __init__(self, flightNo, origin, destination):
        if isinstance(origin, Airport) and isinstance(destination, Airport):
            self._flightNo = flightNo
            self._origin = origin
            self._destination = destination
        else:
            raise TypeError("The origin and destination must be airport objects")

    # representation of the function: returns the Flight object which contains the flight code, the names of the origin and destination, and describes whether the flight is domestic or not
    def __repr__(self):
        if self.isDomesticFlight():
            return "Flight: " + str(self._flightNo) + " from " + str(self._origin.getCity()) + " to " + str(self._destination.getCity()) + " {domestic}"
        else:
            return "Flight: " + str(self._flightNo) + " from " + str(self._origin.getCity()) + " to " + str(self._destination.getCity()) + " {international}"

    # determines whether a flight has the same origin and destination as another flight
    def __eq__(self, other):
        if isinstance(other, Flight) and self.getOrigin() == other.getOrigin() and self.getDestination() == other.getDestination():
            return True
        else:
            return False

    # function which returns the flight number in the object
    def getFlightNumber(self):
        return self._flightNo

    # function which returns the origin of the flight in the object
    def getOrigin(self):
        return self._origin

    # function which returns the destination of the flight in the object
    def getDestination(self):
        return self._destination

    # function which determines whether the flight is domestic (same country of origin and destination) or international (different countries of origin and destination)
    def isDomesticFlight(self):
        if self._origin.getCountry() == self._destination.getCountry():
            return True
        else:
            return False

    # function which sets a new value for the origin variable
    def setOrigin(self, origin):
        self._origin = origin

    # function which sets a new value for the destination variable
    def setDestination(self, destination):
        self._destination = destination

