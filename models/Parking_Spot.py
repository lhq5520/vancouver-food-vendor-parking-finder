'''
VanStreet Parking
@WeifanLi
'''


class ParkingSpot:
    def __init__(self, time_in_effect, creditcard, geo_local_area, coordinates,
                 r_mf_9a_6p, r_mf_6p_10, r_sa_9a_6p, r_sa_6p_10, r_su_9a_6p, r_su_6p_10,
                 t_mf_9a_6p, t_mf_6p_10, t_sa_9a_6p, t_sa_6p_10, t_su_9a_6p, t_su_6p_10):

        self.time_in_effect = time_in_effect
        self.creditcard = creditcard
        self.geo_local_area = geo_local_area
        self.coordinates = coordinates

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
