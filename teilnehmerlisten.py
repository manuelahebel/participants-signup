import personen_instanzen as pi

# Participants lists for WohnZimmerSport instances:
# Auf Wunsch des Dozenten haben wir die Teilnehmerzahl noch mit errechnet.
# In einer zukünftigen Lösung würden wir die Codedopplung vermeiden versuchen.

participants_wohnzimmer01 = ['Teilnehmerzahl:',
                                  (pi.person001.first_name, pi.person001.last_name),
                                  (pi.person002.first_name, pi.person002.last_name),
                                  (pi.person004.first_name, pi.person004.last_name),
                                  (pi.person005.first_name, pi.person005.last_name),
                                  (pi.person007.first_name, pi.person007.last_name),
                                  (pi.person011.first_name, pi.person011.last_name),
                                  ]

participants_wohnzimmersport01 = [('Teilnehmerzahl:',len(participants_wohnzimmer01) -1),
                                  (pi.person001.first_name, pi.person001.last_name),
                                  (pi.person002.first_name, pi.person002.last_name),
                                  (pi.person004.first_name, pi.person004.last_name),
                                  (pi.person005.first_name, pi.person005.last_name),
                                  (pi.person007.first_name, pi.person007.last_name),
                                  (pi.person011.first_name, pi.person011.last_name),
                                  ]


participants_wohnzimmer02 = ['Teilnehmerzahl:',
                                  (pi.person012.first_name, pi.person012.last_name),
                                  (pi.person001.first_name, pi.person001.last_name),
                                  (pi.person008.first_name, pi.person008.last_name),
                                  (pi.person012.first_name, pi.person012.last_name),
                                  (pi.person002.first_name, pi.person002.last_name),
                                  (pi.person004.first_name, pi.person004.last_name),
                                  (pi.person003.first_name, pi.person003.last_name),
                                  (pi.person007.first_name, pi.person007.last_name),
                                  (pi.person011.first_name, pi.person011.last_name),
                                  ]

participants_wohnzimmersport02 = [('Teilnehmerzahl:',len(participants_wohnzimmer02) -1),
                                  (pi.person012.first_name, pi.person012.last_name),
                                  (pi.person001.first_name, pi.person001.last_name),
                                  (pi.person008.first_name, pi.person008.last_name),
                                  (pi.person012.first_name, pi.person012.last_name),
                                  (pi.person002.first_name, pi.person002.last_name),
                                  (pi.person004.first_name, pi.person004.last_name),
                                  (pi.person003.first_name, pi.person003.last_name),
                                  (pi.person007.first_name, pi.person007.last_name),
                                  (pi.person011.first_name, pi.person011.last_name),
                                  ]

participants_wohnzimmer03 = ['Teilnehmerzahl:',
                                  (pi.person010.first_name, pi.person010.last_name),
                                  (pi.person009.first_name, pi.person009.last_name),
                                  ]

participants_wohnzimmersport03 = [('Teilnehmerzahl:',len(participants_wohnzimmer03) -1),
                                  (pi.person010.first_name, pi.person010.last_name),
                                  (pi.person009.first_name, pi.person009.last_name),
                                  ]

participants_wohnzimmer04 = ['']

participants_wohnzimmersport04 = [('Teilnehmerzahl:',len(participants_wohnzimmer04) -1)]


# Participants lists for Hotelzimmersport instances:
participants_hotel01 = ['Teilnehmerzahl:',
                                   (pi.person001.first_name, pi.person001.last_name),
                                   (pi.person002.first_name, pi.person002.last_name),
                                   (pi.person011.first_name, pi.person011.last_name),
                                   (pi.person012.first_name, pi.person012.last_name),
                                   (pi.person001.first_name, pi.person004.last_name),
                                   (pi.person002.first_name, pi.person005.last_name),
                                   (pi.person003.first_name, pi.person006.last_name),
                                   (pi.person007.first_name, pi.person009.last_name),
                                   (pi.person008.first_name, pi.person008.last_name),
                                   (pi.person006.first_name, pi.person006.last_name),
                                   (pi.person007.first_name, pi.person007.last_name),
                                   (pi.person010.first_name, pi.person010.last_name)
                                   ]

participants_hotelzimmersport01 = [('Teilnehmerzahl:',len(participants_hotel01) -1),
                                   (pi.person001.first_name, pi.person001.last_name),
                                   (pi.person002.first_name, pi.person002.last_name),
                                   (pi.person011.first_name, pi.person011.last_name),
                                   (pi.person012.first_name, pi.person012.last_name),
                                   (pi.person001.first_name, pi.person004.last_name),
                                   (pi.person002.first_name, pi.person005.last_name),
                                   (pi.person003.first_name, pi.person006.last_name),
                                   (pi.person007.first_name, pi.person009.last_name),
                                   (pi.person008.first_name, pi.person008.last_name),
                                   (pi.person006.first_name, pi.person006.last_name),
                                   (pi.person007.first_name, pi.person007.last_name),
                                   (pi.person010.first_name, pi.person010.last_name)
                                   ]

participants_hotel02 = ['Teilnehmerzahl:',
                                   (pi.person003.first_name, pi.person003.last_name),
                                   (pi.person004.first_name, pi.person004.last_name),
                                   (pi.person005.first_name, pi.person005.last_name)
                                   ]

participants_hotelzimmersport02 = [('Teilnehmerzahl:',len(participants_hotel02) -1),
                                   (pi.person003.first_name, pi.person003.last_name),
                                   (pi.person004.first_name, pi.person004.last_name),
                                   (pi.person005.first_name, pi.person005.last_name)
                                   ]

participants_hotel03 = ['Teilnehmerzahl:',
                                   (pi.person006.first_name, pi.person006.last_name),
                                   (pi.person007.first_name, pi.person007.last_name)
                                   ]

participants_hotelzimmersport03 = [('Teilnehmerzahl:',len(participants_hotel03) -1),
                                   (pi.person006.first_name, pi.person006.last_name),
                                   (pi.person007.first_name, pi.person007.last_name)
                                   ]

participants_hotel04 = ['Teilnehmerzahl:',
                                   (pi.person008.first_name, pi.person008.last_name),
                                   (pi.person009.first_name, pi.person009.last_name),
                                   (pi.person010.first_name, pi.person010.last_name)
                                   ]

participants_hotelzimmersport04 = [('Teilnehmerzahl:',len(participants_hotel04) -1),
                                   (pi.person008.first_name, pi.person008.last_name),
                                   (pi.person009.first_name, pi.person009.last_name),
                                   (pi.person010.first_name, pi.person010.last_name)
                                   ]


# Participants lists for BueroZimmerSport instances:
participants_buero01 = ['Teilnehmerzahl:',
                                   (pi.person002.first_name, pi.person002.last_name),
                                   (pi.person004.first_name, pi.person004.last_name),
                                   (pi.person006.first_name, pi.person006.last_name),
                                   (pi.person008.first_name, pi.person008.last_name),
                                   (pi.person010.first_name, pi.person010.last_name)
                                   ]

participants_buerozimmersport01 = [('Teilnehmerzahl:',len(participants_buero01) -1),
                                   (pi.person002.first_name, pi.person002.last_name),
                                   (pi.person004.first_name, pi.person004.last_name),
                                   (pi.person006.first_name, pi.person006.last_name),
                                   (pi.person008.first_name, pi.person008.last_name),
                                   (pi.person010.first_name, pi.person010.last_name)
                                   ]

participants_buero02 = ['Teilnehmerzahl:',
                                   (pi.person001.first_name, pi.person001.last_name),
                                   (pi.person003.first_name, pi.person003.last_name),
                                   (pi.person005.first_name, pi.person005.last_name),
                                   (pi.person007.first_name, pi.person007.last_name),
                                   (pi.person009.first_name, pi.person009.last_name),
                                   (pi.person011.first_name, pi.person011.last_name)
                                   ]

participants_buerozimmersport02 = [('Teilnehmerzahl:',len(participants_buero02) -1),
                                   (pi.person001.first_name, pi.person001.last_name),
                                   (pi.person003.first_name, pi.person003.last_name),
                                   (pi.person005.first_name, pi.person005.last_name),
                                   (pi.person007.first_name, pi.person007.last_name),
                                   (pi.person009.first_name, pi.person009.last_name),
                                   (pi.person011.first_name, pi.person011.last_name)
                                   ]


participants_buero03 = ['Teilnehmerzahl:',
                                   (pi.person002.first_name, pi.person002.last_name),
                                   (pi.person009.first_name, pi.person009.last_name)
                                   ]

participants_buerozimmersport03 = [('Teilnehmerzahl:',len(participants_buero03) -1),
                                   (pi.person002.first_name, pi.person002.last_name),
                                   (pi.person009.first_name, pi.person009.last_name)
                                   ]


participants_buero04 = ['Teilnehmer:',
                                   (pi.person002.first_name, pi.person002.last_name),
                                   (pi.person005.first_name, pi.person005.last_name),
                                   (pi.person008.first_name, pi.person008.last_name),
                                   (pi.person011.first_name, pi.person011.last_name)
                                   ]

participants_buerozimmersport04 = [('Teilnehmerzahl:',len(participants_buero04) -1),
                                   (pi.person002.first_name, pi.person002.last_name),
                                   (pi.person005.first_name, pi.person005.last_name),
                                   (pi.person008.first_name, pi.person008.last_name),
                                   (pi.person011.first_name, pi.person011.last_name)
                                   ]


# Participants lists for KinderZimmerSport instances:
participants_kinder01 = ['Teilnehmer:',
                                    (pi.person001.first_name, pi.person001.last_name),
                                    (pi.person002.first_name, pi.person002.last_name),
                                    (pi.person003.first_name, pi.person003.last_name),
                                    (pi.person004.first_name, pi.person004.last_name),
                                    (pi.person005.first_name, pi.person005.last_name),
                                    (pi.person006.first_name, pi.person006.last_name),
                                    (pi.person007.first_name, pi.person007.last_name),
                                    (pi.person008.first_name, pi.person008.last_name)
                                    ]

participants_kinderzimmersport01 = [('Teilnehmerzahl:',len(participants_kinder01) -1),
                                    (pi.person001.first_name, pi.person001.last_name),
                                    (pi.person002.first_name, pi.person002.last_name),
                                    (pi.person003.first_name, pi.person003.last_name),
                                    (pi.person004.first_name, pi.person004.last_name),
                                    (pi.person005.first_name, pi.person005.last_name),
                                    (pi.person006.first_name, pi.person006.last_name),
                                    (pi.person007.first_name, pi.person007.last_name),
                                    (pi.person008.first_name, pi.person008.last_name)
                                    ]


participants_kinder02 = ['Teilnehmerzahl:',
                                    (pi.person001.first_name, pi.person001.last_name),
                                    (pi.person002.first_name, pi.person002.last_name),
                                    (pi.person003.first_name, pi.person003.last_name),
                                    (pi.person004.first_name, pi.person004.last_name)
                                    ]

participants_kinderzimmersport02 = [('Teilnehmerzahl:',len(participants_kinder02) -1),
                                    (pi.person001.first_name, pi.person001.last_name),
                                    (pi.person002.first_name, pi.person002.last_name),
                                    (pi.person003.first_name, pi.person003.last_name),
                                    (pi.person004.first_name, pi.person004.last_name)
                                    ]


participants_kinder03 = ['Teilnehmerzahl:',
                                    (pi.person001.first_name, pi.person001.last_name),
                                    (pi.person002.first_name, pi.person002.last_name),
                                    (pi.person003.first_name, pi.person003.last_name)
                                    ]

participants_kinderzimmersport03 = [('Teilnehmerzahl:',len(participants_kinder03) -1),
                                    (pi.person001.first_name, pi.person001.last_name),
                                    (pi.person002.first_name, pi.person002.last_name),
                                    (pi.person003.first_name, pi.person003.last_name)
                                    ]


participants_kinder04 = ['Teilnehmer:',
                                    (pi.person001.first_name, pi.person001.last_name),
                                    (pi.person002.first_name, pi.person002.last_name),
                                    (pi.person003.first_name, pi.person003.last_name),
                                    (pi.person004.first_name, pi.person004.last_name),
                                    (pi.person005.first_name, pi.person005.last_name),
                                    (pi.person006.first_name, pi.person006.last_name)
                                    ]

participants_kinderzimmersport04 = [('Teilnehmerzahl:',len(participants_kinder04) -1),
                                    (pi.person001.first_name, pi.person001.last_name),
                                    (pi.person002.first_name, pi.person002.last_name),
                                    (pi.person003.first_name, pi.person003.last_name),
                                    (pi.person004.first_name, pi.person004.last_name),
                                    (pi.person005.first_name, pi.person005.last_name),
                                    (pi.person006.first_name, pi.person006.last_name)
                                    ]

