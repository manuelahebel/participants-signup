import kurs_klassen as kk
import personen_instanzen as pi
import teilnehmerlisten as tn

# Instantiating courses of course type WohnZimmerSport
wohnzimmersport01 = kk.WohnZimmerSport('w001', '2020-10-13', 8, 8, 12, 'Andy Antons', tn.participants_wohnzimmersport01, ['Trinkflasche', 'Matte'])
wohnzimmersport02 = kk.WohnZimmerSport('w002', '2020-11-03', 12, 9, 12, 'Tanja Maier', tn.participants_wohnzimmersport02, ['Trinkflasche', 'Matte', 'Handtuch'])
wohnzimmersport03 = kk.WohnZimmerSport('w003', '2020-12-07', 8, 7, 12, 'Tanja Maier', tn.participants_wohnzimmersport03, ['Trinkflasche', 'Handtuch'])
wohnzimmersport04 = kk.WohnZimmerSport('w004', '2020-09-16', 4, 8, 12, 'Manuela Hebel', tn.participants_wohnzimmersport04, ['Wein', 'Handtuch', 'gute Laune'])



# Instantiating courses of course type BueroZimmerSport
buerozimmersport01 = kk.BueroZimmerSport('b001', '2020-10-01', 8, 6, 12, 'Rudi Ratlos', tn.participants_buerozimmersport01)
buerozimmersport02 = kk.BueroZimmerSport('b002', '2020-10-02', 8, 6, 12, 'Catharina Clever', tn.participants_buerozimmersport02)
buerozimmersport03 = kk.BueroZimmerSport('b003', '2020-10-08', 8, 6, 12, 'Rudi Ratlos', tn.participants_buerozimmersport03)
buerozimmersport04 = kk.BueroZimmerSport('b004', '2020-10-09', 8, 6, 12, 'Catharina Clever', tn.participants_buerozimmersport04)



# Instantiating courses of course type HotelZimmerSport
hotelzimmersport01 = kk.HotelZimmerSport('h001', '2020-10-15', 10, 8, 12, "Koch Christina", tn.participants_hotelzimmersport01)
hotelzimmersport02 = kk.HotelZimmerSport('h002', '2020-11-15', 10, 8, 12, "Max Musterman", tn.participants_hotelzimmersport02)
hotelzimmersport03 = kk.HotelZimmerSport('h003', '2020-12-15', 10, 8, 12, "Sepp Müller", tn.participants_hotelzimmersport03)
hotelzimmersport04 = kk.HotelZimmerSport('h004', '2021-1-15', 10, 8, 12, "Frau Holle", tn.participants_hotelzimmersport04)



# Instantiating courses of course type KinderZimmerSport
kinderzimmersport01 = kk.KinderZimmerSport('k001', '2020-10-15', 8, 6, 12, 'Albert Tross', tn.participants_kinderzimmersport01)
kinderzimmersport02 = kk.KinderZimmerSport('k002', '2020-11-4', 8, 6, 12, 'Jim Panse', tn.participants_kinderzimmersport02)
kinderzimmersport03 = kk.KinderZimmerSport('k003', '2020-11-7', 8, 8, 12, 'Reiner Zufall', tn.participants_kinderzimmersport03)
kinderzimmersport04 = kk.KinderZimmerSport('k003', '2020-9-28', 8, 6, 14, 'Reiner Zufall', tn.participants_kinderzimmersport04)

