class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, origin_city, origin_airport, dest_city, dest_airport, out_dt, return_dt, stop_overs=0,
                 via_city=""):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.dest_city = dest_city
        self.dest_airport = dest_airport
        self.out_dt = out_dt
        self.return_dt = return_dt
        self.stop_overs = stop_overs
        self.via_city = via_city
