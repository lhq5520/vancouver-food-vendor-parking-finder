import unittest
from models.Parking_Spot import ParkingSpot


# python3 -m unittest Parking_spot_unitest.py
class TestParkingSpot(unittest.TestCase):

    def setUp(self):

        self.parking_spot = ParkingSpot(
            time_in_effect="Mon-Fri",
            creditcard=True,
            geo_local_area="Downtown",
            coordinates="123.456, 78.910",
            r_mf_9a_6p=2, r_mf_6p_10=3,
            r_sa_9a_6p=2, r_sa_6p_10=3,
            r_su_9a_6p=2, r_su_6p_10=3,
            t_mf_9a_6p=1.5, t_mf_6p_10=2.5,
            t_sa_9a_6p=1.5, t_sa_6p_10=2.5,
            t_su_9a_6p=1.5, t_su_6p_10=2.5
        )

    def test_initialization(self):

        self.assertEqual(self.parking_spot.time_in_effect, "Mon-Fri")
        self.assertEqual(self.parking_spot.creditcard, True)
        self.assertEqual(self.parking_spot.geo_local_area, "Downtown")
        self.assertEqual(self.parking_spot.coordinates, "123.456, 78.910")

        self.assertEqual(self.parking_spot.r_mf_9a_6p, 2)
        self.assertEqual(self.parking_spot.r_sa_9a_6p, 2)

        self.assertEqual(self.parking_spot.t_mf_9a_6p, 1.5)
        self.assertEqual(self.parking_spot.t_sa_9a_6p, 1.5)
