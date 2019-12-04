# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon):
        self.lattitude = lat
        self.longitude = lon

    def printlat(self):
        print(self.lattitude, self.longitude)

l = LatLon(10, 20)
l.printlat()
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name

    def print_waypoint(self):
        print(self.lattitude, self.longitude, self.name)


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, lat, lon, difficulty, size):
        super().__init__(lat, lon, name)
        self.difficulty = difficulty
        self.size = size
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
    def print_geocache(self):
        print(self.name, self.difficulty, self.size, self.lattitude, self.longitude)
# YOUR CODE HERE
n = Waypoint("Catacombs", 41.70505, -121.51521)
n.print_waypoint()
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method

n.print_waypoint() # makes it print into something human readable after creaing a print method (print_waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
g = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
# YOUR CODE HERE

# Print it--also make this print more nicely
g.print_geocache()
