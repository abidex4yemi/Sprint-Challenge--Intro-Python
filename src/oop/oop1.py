# Write classes for the following class hierarchy:


class Vehicle:
    def __init__(self, color, manufacturer, number_of_engine):
        self.color = color
        self.manufacturer = manufacturer
        self.number_of_engine = number_of_engine
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
