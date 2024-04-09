'''
VanStreet Parking
@WeifanLi

Car_Parking class inherited from ParkingSpot and imported from online
'''


class CarParking():
    '''
    r_mf_9a_6p, r_mf_6p_10, r_sa_9a_6p, r_sa_6p_10, r_su_9a_6p, r_su_6p_10
    are all rates at specific time

    t_mf_9a_6p, t_mf_6p_10, t_sa_9a_6p, t_sa_6p_10, t_su_9a_6p, t_su_6p_10,
    are all specific time limit
    '''

    def __init__(self,
                 meter_id, paybyphone_id, meterhead, time_in_effect, creditcard, geo_local_area, coordinates,
                 r_mf_9a_6p, r_mf_6p_10, r_sa_9a_6p, r_sa_6p_10, r_su_9a_6p, r_su_6p_10,
                 t_mf_9a_6p, t_mf_6p_10, t_sa_9a_6p, t_sa_6p_10, t_su_9a_6p, t_su_6p_10,
                 ):

        # spcific data used for parking
        self.meter_id = meter_id
        self.paybyphone_id = paybyphone_id
        self.meterhead = meterhead

        self.time_in_effect = time_in_effect
        self.creditcard = creditcard
        self.geo_local_area = geo_local_area
        self.coordinates = coordinates
        # dictionaries
        self.time = time
        self.rate = rate

        # specifc time limit

        self.r_mf_9a_6p = r_mf_9a_6p
        self.r_mf_6p_10 = r_mf_6p_10
        self.r_sa_9a_6p = r_sa_9a_6p
        self.r_sa_6p_10 = r_sa_6p_10
        self.r_su_9a_6p = r_su_9a_6p
        self.r_su_6p_10 = r_su_6p_10

        # specifc rate at spicified time limit

        self.t_mf_9a_6p = t_mf_9a_6p
        self.t_mf_6p_10 = t_mf_6p_10
        self.t_sa_9a_6p = t_sa_9a_6p
        self.t_sa_6p_10 = t_sa_6p_10
        self.t_su_9a_6p = t_su_9a_6p
        self.t_su_6p_10 = t_su_6p_10

    def __str__(self):
        return (f"Meter ID: {self.meter_id}\n"
                f"PayByPhone ID: {self.paybyphone_id}\n"
                f"Meter Head: {self.meterhead}\n"
                f"Time in Effect: {self.time_in_effect}\n"
                f"Credit Card Accepted: {'Yes' if self.creditcard else 'No'}\n"
                f"Geographical Area: {self.geo_local_area}\n"
                f"Coordinates: {self.coordinates}\n"
                f"Rates & Times:\n"
                f"  Mon-Fri 9am-6pm: ${self.r_mf_9a_6p} / {self.t_mf_9a_6p}\n"
                f"  Mon-Fri 6pm-10pm: ${self.r_mf_6p_10} / {self.t_mf_6p_10}\n"
                f"  Sat 9am-6pm: ${self.r_sa_9a_6p} / {self.t_sa_9a_6p}\n"
                f"  Sat 6pm-10pm: ${self.r_sa_6p_10} / {self.t_sa_6p_10}\n"
                f"  Sun 9am-6pm: ${self.r_su_9a_6p} / {self.t_su_9a_6p}\n"
                f"  Sun 6pm-10pm: ${self.r_su_6p_10} / {self.t_su_6p_10}\n")

