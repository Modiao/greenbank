def get_borrowing_rate_without_passengers(score:int) -> float:
    """ this will return the borrowing rate based on the vehicule score """
    if score in range (1, 10):
        return 3
    elif score in range (11, 15):
        return 2.75
    elif score in range(16, 25):
        return 2.52
    elif score in range(26, 33):
        return 2.10
    elif score in range(34, 40):
        return 1.85
    

def get_passenger_rate(number_of_passengers:int) -> int:
    """ this will return the passenger rate based on the number of passenger """
    if number_of_passengers == 1:
        return 0.11
    elif number_of_passengers == 2:
        return -0.17
    elif number_of_passengers == 3:
        return -0.29
    elif number_of_passengers == 4:
        return -0.53
    

GET_VEHICULE_TYPE_NOTE = {
    'Citadine': 8,
    'Cabriolet': 6,
    'Berline': 6.5,
    'SUV / 4x4': 4
}

GET_ENERGY_NOTE = {
    'Essence': 5,
    'Electrique': 9,
    'Gaz': 6,
    'Diesel': 4,
    'Hybride': 7
}   



def get_mileage_note(mileage:int) -> int:
    """ this will return the note of a mileage """
    if mileage in range(5000, 10000):
        return 9
    elif mileage in range(10000, 15000):
        return 7
    elif mileage in range(15000, 20000):
        return 5
    elif mileage in range(20000, 25000):
        return 3
    elif mileage in range(25000, 30000):
        return 1

def get_year_note(year:int) -> int:
    if year in range(1960, 1970):
        return 1
    elif year in range(1970, 1980):
        return 2
    elif year in range(1980, 2000):
        return 4
    elif year in range(2000, 2010):
        return 5
    elif year >= 2010:
        return 7

   

def total_rate_without_passenger(vehicul_type:str, energy:str, mileage:int, year:int):
    """ this will calculate the total rate without including the passenger """
    vehicule_note = GET_VEHICULE_TYPE_NOTE.get(vehicul_type)
    energy_note = GET_ENERGY_NOTE.get(energy)
    mileage_note = get_mileage_note(mileage)
    year_note =  get_year_note(year)

    total_value = vehicule_note + energy_note + mileage_note + year_note
    
    return get_borrowing_rate_without_passengers(total_value)

def total_borrowing_rate(vehicul_type:str, energy:str, mileage:int, year:int, passenger:int) -> float:
    """ This will return the total rate including the passenger """

    total_rate_without_passengers = total_rate_without_passenger(vehicul_type, energy, mileage, year)
    passenger_rate = get_passenger_rate(passenger)

    return total_rate_without_passengers + passenger_rate

