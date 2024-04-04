'''
VanStreet Parking
@WeifanLi

'''
from .Car_Parking import ParkingSpot


class MotorcycleParking(ParkingSpot):
    '''
    r_mf_9a_6p, r_mf_6p_10, r_sa_9a_6p, r_sa_6p_10, r_su_9a_6p, r_su_6p_10
    are all rates at specific time

    t_mf_9a_6p, t_mf_6p_10, t_sa_9a_6p, t_sa_6p_10, t_su_9a_6p, t_su_6p_10,
    are all specific time limit
    '''

    def __init__(self, types,
                 time_in_effect, creditcard, geo_local_area, coordinates,
                 r_mf_9a_6p, r_mf_6p_10, r_sa_9a_6p, r_sa_6p_10, r_su_9a_6p, r_su_6p_10,
                 t_mf_9a_6p, t_mf_6p_10, t_sa_9a_6p, t_sa_6p_10, t_su_9a_6p, t_su_6p_10
                 ):
        super().__init__(time_in_effect, creditcard, geo_local_area, coordinates,
                 r_mf_9a_6p, r_mf_6p_10, r_sa_9a_6p, r_sa_6p_10, r_su_9a_6p, r_su_6p_10,
                 t_mf_9a_6p, t_mf_6p_10, t_sa_9a_6p, t_sa_6p_10, t_su_9a_6p, t_su_6p_10)

        self.types = types

    def __str__(self):
        '''
            Returns a string representation of the MotorcycleParking object, detailing its type, geographical area,
            coordinates, acceptance of credit card, rates, and time limits for various periods.

            Returns:
                str: A string describing the motorcycle parking spot's attributes.
        '''

        return (
                f"Type: {self.types}\n"
                f"Time in Effect: {self.time_in_effect}\n"
                f"Credit Card Accepted: {'Yes' if self.creditcard else 'No'}\n"
                f"Geographical Area: {self.geo_local_area}\n"
                f"Coordinates: {self.coordinates}\n"
                f"Rates & Times:\n"
                f"  Mon-Fri 9am-6pm: ${self.r_mf_9a_6p} / {self.t_mf_9a_6p}hrs\n"
                f"  Mon-Fri 6pm-10pm: ${self.r_mf_6p_10} / {self.t_mf_6p_10}hrs\n"
                f"  Sat 9am-6pm: ${self.r_sa_9a_6p} / {self.t_sa_9a_6p}hrs\n"
                f"  Sat 6pm-10pm: ${self.r_sa_6p_10} / {self.t_sa_6p_10}hrs\n"
                f"  Sun 9am-6pm: ${self.r_su_9a_6p} / {self.t_su_9a_6p}hrs\n"
                f"  Sun 6pm-10pm: ${self.r_su_6p_10} / {self.t_su_6p_10}hrs\n")
