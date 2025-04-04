from event_class import Event

events = {
    "start": Event(
        "###    Tervetuloa Ouluun! Valitse hahmoluokkasi!    ###",
        {
            "Chad Vibecoder": {
                "next_event": "wapunAlku",
                "happening": {"älykkyys": -5, "yleiskunto": 10, "karisma": 20, "wappufiilis": 0}
            },
            "Tankki Hank": {
                "next_event": "wapunAlku",
                "happening": {"älykkyys": 10, "yleiskunto": 20, "karisma": -5, "wappufiilis": 0}
            },
            "Koodi Guru": {
                "next_event": "wapunAlku",
                "happening": {"älykkyys": 20, "yleiskunto": 10, "karisma": -5, "wappufiilis": 0}
            }
        }
    ),
    ### Aloitus ###
    "wapunAlku": Event(
        "Ja näin Wappu alkaa! Ennen kuin pääset juhlimaan, sinun on kuitenkin selvitettävä mitä haluat Wappuna tehdä.",
        {
            "Mene jonottamaan lippuja Wappubileisiin": {
                "next_event": "jonotus"
            },
            "Päätä itse järjestää Wapun bileet": {
                "next_event": "omat_bileet",
            },
            "Hodlaa Meriauran osakkeita ja osta alennuksesta lisää Wappubudjetilla": {
                "next_event": "hodlaaminen",
            }
        }
    ),
    "jonotus": Event(
        "Jonotat lippuja Wappubileisiin koko yön. Miten vietät aikasi lippujonossa?",
        {
            "Istu nätisti paikallasi ja odota": {
                "next_event": "sait_liput",
                "happening": {"wappufiilis": 1}
            },
            "Uhmaa onnetarta ja naukkaile 'simaa' yön jouduttamiseksi": {
                "next_event": "vartija",
                "happening": {"wappufiilis": -1}
            },
            "Lähde seikkailemaan katakombeihin": {
                "next_event": "katakombit",
                "happening": {"wappufiilis": 2}
            }
        }
    ),
    "omat_bileet": Event(
        "Olet järjestämässä omat bileet. Minkälaiset bileet järjestät?",
        {
            "Järjestän sitsit!": {
                "next_event": "sitsit"
            },
            "Järjestän kotibileet!": {
                "next_event": "kotibileet"
            },
            "Järjestän oman uittotilaisuuden!": {
                "next_event": "uitto"
            }
        }
    ),
    "hodlaaminen": Event(
        "Menetit rahasi, miten copetat",
        {
            "Diamond hands hodl": {
                "next_event": "itssoover"
            },
            "Minimoi tappiot ja lähe bilettämään, sillä mitä sait likvidoitua": {
                "next_event": "MinimoiTappiot"
            },
            "Katkeroidu ja komeroidu": {
                "next_event": "end",
            }
        }
    ),
    "itssoover": Event(
        "Olet menettänyt kaikki rahasi ja olet täysin varaton. Wappu on ohi sinulle. Kiitos pelistä!",
        {}
    ),
    ### Minimoi tappiot ###
    "MinimoiTappiot": Event(
        "Päätät minimoi tappiot ja lähdet bilettämään. Mihin aiot mennä?",
        {
            "Baariin": {
                "next_event": "baari",
                "happening": {"wappufiilis": 5}
            },
            "Fribeer": {
                "next_event": "fribeer"
            },
            "Suihkun kautta kotiin ja komentoriville": {
                "next_event": "end",
            }
        }
    ),
    "baari": Event(
        "Baari on täynnä opiskelijoita ja Wappua juhlivia. Huomaat kuitenkin, että tililläsi on vain 5 euroa. ",
        {
            "Ostan niin paljon olutta kuin viidellä eurolla saa": {
                "next_event": "WaatonAattoAamu",
                "happening": {"wappufiilis": 5}
            },
            "Joukkorahoitan (ruinaan kaverilta) itselleni kaljaa": {
                "next_event": "WaatonAattoAamu",
                "skill_check": ("karisma", 20),
                "success_outcome": {"wappufiilis": 5},
                "fail_outcome": {"wappufiilis": -5}
            }
        }
    ),
    "fribeer": Event(
        "Päätit mennä pelaamaan fribeeria. Huomaat, että fribeer on kustannustehokasta jos tiimisi tarjoaa kaljat. " \
        "Miten hyvin aiot pelata?",
        {
            "Pelaan niin hyvin kuin osaan": {
                "next_event": "WaatonAattoAamu",
                "happening": {"wappufiilis": 5}
            },
            "Pelaan niin huonosti kuin osaan": {
                "next_event": "WaatonAattoAamu",
                "happening": {"wappufiilis": 5}
            },
            "Peli itsessään ei kiinnosta, mutta nillitän silti säännöistä. Typerä ja lapsellinen peli.": {
                "next_event": "WaatonAattoAamu",
                "happening": {"karisma": -5, "wappufiilis": -5}
            }
        }
    ),
    ### Omat bileet ###
    "sitsit": Event(
        "Päätit järjestää sitsit. Sitsit ovat täynnä juomista ja laulamista. " \
        "Kenet kutsut seremoniamestariksi?",
        {
            "Päätän olla seremoniamestari itse": {
                "next_event": "itesere"
            },
            "Kutsun OTYn kulttuurisian seremoniamestariksi": {
                "next_event": "sika",
                "skill_check": ("karisma", 38),
                "success_event": "sikaTulee",
                "fail_event": "sikaEiTule"
            },
            "Värvään ensimmäisen ihmisen lipaston käytävältä joka sanoo kyllä.": {
                "next_event": "jokurando"
            }
        }
    ),
    "jokurando": Event(
        "Seremoniamestarina toimii randomi joka ei osaa mitään. Sitsit menevät pieleen, mutta tulipahan ryypättyä!.",
        {
            "Ainakin mulla oli hauska": {
                "next_event": "waatonAattoAamu",
                "happening": {"wappufiilis": 5}
            },
            "No höh :/": {
                "next_event": "waatonAattoAamu"
            }
        }
    ),
    "sikaTulee": Event(
        "Seremoniamestarina toimii OTYn kulttuurisika. Sitsisi kuulostivat niin eeppisiltä, että hän päätti jättää OTYn sitsit väliin ja tulla sinun bileisiin." \
        "Hän osaa laulaa ja juoda. Sitsit menevät hyvin ja kaikki nauttivat.",
        {
            "HYVÄT YSTÄVÄT LAULU VOI ALKAA": {
                "next_event": "waatonAattoAamu",
                "happening": {"wappufiilis": 500}
            }
        }
    ),
    "sikaEiTule": Event(
        "Seremoniamestariksi kutsuttu kulttuurisika ei saapunut paikalle. Vittu.",
        {
            "No höh :/": {
                "next_event": "waatonAattoAamu"
            }
        }
    ),
    "itesere": Event(
        "Seremoniamestarina toimii sinä itse. Sitsit menevät hyvin ja kaikki nauttivat." \
        "Et kuitenkaan itse kerinnyt nauttia tunnelmasta, koska olit sitsien järjestäjä ja seremoniamestari",
        {
            "No höh :/": {
                "next_event": "waatonAattoAamu"
            }
        }
    ),
    "kotibileet": Event(
        "Järjestät bileet kotonasi. Raju biletys summonaa miekkataksin pihalle ja sinivuokot tulevat laittamaan stopin bileille. Vittu.",
        {
            "No höh :/": {
                "next_event": "waatonAattoAamu",
                "happening": {"wappufiilis": -5}
            }
        }
    ),
    "uitto": Event(
        "Onneksi olkoon kävit ojassa uimassa maalarinhattu päässä. Ainakin nyt on raikas olo!",
        {
            "Hell yeah brother!": {
                "next_event": "waatonAattoAamu",
                "happening": {"wappufiilis": 5}
            },
        }
    ),
    ### Etkot ###
    "sait_liput": Event(
        "Jes! Sait liput Wappubileisiin! Miten aiot etkoilla?",
        {
            "Taidanpa riipasta kovat kännit": {
                "next_event": "jotain_meni_pieleen",
                "skill_check": ("yleiskunto", 20),
                "success_event": "HauskaTurbokänniBileissä",
                "fail_event": "öärg...",
                "success_outcome": {"yleiskunto": -5, "älykkyys":-5, "karisma": 10, "wappufiilis": 10},
                "fail_outcome": {"yleiskunto": -5, "älykkyys": -5, "karisma": -5, "wappufiilis": -10}
            },
            "Menet kaverin luokse ja hypetätte iha vitusti": {
                "next_event": "HypeHypeHype",
                "happening": {"wappufiilis": 5}
            },
            "Pelaat duotrigordlea OTiT ry kiltahuoneella": {
                "next_event": "duotrigordle"
            }
        }
    ),
    "vartija": Event(
        "Vartija huomaa sinun nauttivan päihtymishuippausaineita ja nakkaa sinut ulos." \
        "Et saa lippuja bileisiin. Olet jäänyt Wappubileistä paitsi.",
        {
            "Katkeroidu ja komeroidu loppu Wapuksi": {
                "next_event": "end",
                "happening": {"wappufiilis": -999}
            },
            "Järjestä omat bileet": {
                "next_event": "omat_bileet"
            }
        }
    ),
    "katakombit": Event(
        "Katakombeissa on pimeää ja kylmää. Näet vanhan viinipullon nököttävän sähkökaapin päällä." \
        "Napattuasi pullon, huomaat että olet jäänyt yksisuuntaisen palo-oven taakse. Muutut klonkuksi.",
        {
            "Olen nyt katakombien klonkku": {
                "next_event": "end",
                "happening": {"wappufiilis": -999}
            }
        }
    ),
    "duotrigordle": Event(
        "'Duotrigordle on niinku Wordle, mutta niitä on 32 ruudukos- Hei mihin sinä menet?' " \
        "Pelaat loppuelämäsi duotrigordlea ja jäät Wappubileistä paitsi.",
        {
            "Olen nyt duotrigordlen mestari": {
                "next_event": "end",
                "happening": {"wappufiilis": -999}
            }
        }
    ),
    ### Wappubileet ###
    "HypeHypeHype": Event(
        "Hullun hypetyksen jälkeen on aika lähteä bileisiin! Olet saanut paljon uusia ystäviä ja kaikki rakastavat sinua!" \
        "Olet tämän Wapun elävä legenda! Jatkoille?",
        {
            "Päätyyn!": {
                "next_event": "Jatkot",
                "happening": {"yleiskunto": -5, "wappufiilis": 5}
            },
            "Pää tyynyyn!": {
                "next_event": "WaatonAattoAamu",
                "happening": {"yleiskunto": 5}
            }
        }
    ),
    "HauskaTurbokänniBileissä": Event(
        "Olet saavuttanut kuuluisan turbokännin. Olet saanut paljon uusia ystäviä. Kaikki rakastavat sinua ja olet tämän Wapun elävä legenda!" \
        "Jatkoille?",
        {
            "Päätyyn!": {
                "next_event": "Jatkot",
                "happening": {"yleiskunto": -5, "wappufiilis": 5}
            },
            "Pää tyynyyn!": {
                "next_event": "WaatonAattoAamu",
                "happening": {"yleiskunto": 5}
            }
        }
    ),
    ### Jatkot ###
    "Jatkot": Event(
        "Joku typerä fuksi isännöi jatkoja. Jatkoilla on paljon juomista ja pelailua. " \
        "Miten aiot viettää jatkoja?",
        {
            "Pelaan juomapelejä ja juon": {
                "next_event": "WaatonAattoAamuFuksinSängyssä",
                "happening": {"wappufiilis": 5},
                "skill_check": ("yleiskunto", 20),
                "success_event": "WaatonAattoAamu",
                "fail_event": "Mitä helvettiä?",
                "success_outcome": {"wappufiilis": 5},
                "fail_outcome": {"yleiskunto": -5}
            },
            "Lopetan juomisen ja menen nukkumaan fuksin sänkyyn": {
                "next_event": "WaatonAattoAamuFuksinSängyssä",
                "happening": {"yleiskunto": 5}
            },
            "Menen kotiin nukkumaan": {
                "next_event": "WaatonAattoAamu",
                "happening": {"yleiskunto": 5}
            }
        }
    ),
    ### Waaton aatto ###
    "öärg...": Event(
        "Örgh! Olet niin kännissä, ettet muista mitään. Heräät aamulla sängystäsi ja huomaat, että olet jäänyt Wappubileistä paitsi." \
        "Krapula painaa ja päätä särkee. Waatonaatto sarastaa jo. Pitäisikö yrittää käydä kuitenkin suikussa ennenkuin lähdet?",
        {
            "Olen paska perse läpeensä. Suihkuttelu on heikoille!": {
                "next_event": "WaatonAatto",
                "happening": {"karisma": -100, "wappufiilis": 5}
            },
            "Käyn suihkussa ja pesen itseni puhtaaksi": {
                "next_event": "WaatonAatto",
                "happening": {"karisma": 5}
            }
        }
    ),
    "Mitä helvettiä?": Event(
        "'Mitä helvettiä? Missä vitussa minä olen?' Olit niin kännissä, ettet muista mitään. Heräät Waatonaatto aamulla jonkun fuksin sängystä." \
        "'Mitä sitä on oikein tehnyt?' Nyt kyllä morkkis painaa.",
        {
            "Waatonaatto bileisiin käymättä lähtöruudun kautta!": {
                "next_event": "WaatonAatto",
                "happening": {"karisma": -10, "wappufiilis": -10}
            },
            "Waatonaatto bileisiin, mutta käy kotona suihkussa ensin!": {
                "next_event": "WaatonAatto",
                "happening": {"karisma": 5, "wappufiilis": -10}
            },
        }
    ),
    "waatonAattoAamu": Event(
        "Waaton aaton riennot odottovat sinua! Miten aiot viettää Waaton aattoa?",
        {
            "Hikkyilen kotona": {
                "skill_check": ("älykkyys", 20),
                "success_event": "hikkyile_hyvissä_fiiliksissä",
                "fail_event": "hikkyile_huonoissa_fiiliksissä",
                "success_outcome": {"wappufiilis": 5},
                "fail_outcome": {"wappufiilis": -5}
            },
            "Kolme sanaa: kusi, paska ja känni": {
                "skill_check": ("yleiskunto", 20),
                "success_event": "legendaarinen_kpk",
                "fail_event": "legendaarinen_kpk_fail",
                "success_outcome": {"wappufiilis": 5},
                "fail_outcome": {"wappufiilis": -5}
            },
            "Etsi seuraa ;) \n (elikkä yritä saada sukupuolielintä (jonkun muun))": {
                "next_event": "millasta_sais_olla"
            }
        }
    ),
    "legendaarinen_kpk": Event(
        "Legendaariset kännitoilailut jäävät muistoihisi ikuisiksi ajoiksi ja naurattavat vielä vuosia",
        {
            "Hell yeah brother!": {
                "next_event": "end"
            }
        }
    ),
    "legendaarinen_kpk_fail": Event(
        "Aikahyppy huomiseen ja krapulaan. Mitä vittua tuli tehtyä?",
        {
            "'Miksi aina mulle käy näin?'": {
                "next_event": "end"
            }
        }
    ),
    "millasta_sais_olla": Event(
        "Minkälaista elintä haluaisit?",
        {
            "Teekkari": {
                "skill_check": ("karisma", 20),
                "success_event": "sait_elintä",
                "fail_event": "et_saanut_elintä",
                "success_outcome": {"wappufiilis": 5},
                "fail_outcome": {"wappufiilis": -5}
            },
            "Luonnontieteilijä": {
                "skill_check": ("karisma", 25),
                "success_event": "sait_elintä",
                "fail_event": "et_saanut_elintä",
                "success_outcome": {"wappufiilis": 5},
                "fail_outcome": {"wappufiilis": -5}
            },
            "Humanisti": {
                "skill_check": ("karisma", 25),
                "success_event": "sait_elintä",
                "fail_event": "et_saanut_elintä",
                "success_outcome": {"wappufiilis": 5},
                "fail_outcome": {"wappufiilis": -5}
            }
        }
    ),
    "sait_elintä": Event(
        "Sait Wappuheilan! Yhdessä seuraatte Wappuauringon nousua ja matineoitte matineassa",
        {
            "Jabadabaduu ja panemisiin!": {
                "next_event": "selvisit"
            }
        }
    ),
    "et_saanut_elintä": Event(
        "Ei Wappuheilaa sinulle! Aika incelöityä.",
        {
            "No höh :/": {
                "next_event": "selvisit"
            }
        }
    ),
    "hikkyile_hyvissä_fiiliksissä": Event(
        "Hikkyilet kotona, mutta teet sen omasta tahdostasi ja hyvissä fiiliksissä. " \
        "Nautit olostasi",
        {
            "Jatka hikkyilyä": {
                "next_event": "selvisit"
            }
        }
    ),
    "hikkyile_hyvissä_fiiliksissä": Event(
        "Hikkyilet kotona, mutta jokin jäi kaihertamaan. 'Millos se Wappu olikaan?'" \
        "FOMO painaa ja mietit, että olisit voinut lähteä bileisiin.",
        {
            "Jatka hikkyilyä": {
                "next_event": "selvisit"
            }
        }
    ),
    ### Selvisit ###
    "selvisit": Event(
        "Selvisit Waaton aaton bileistä ja olet valmis juhlimaan Wappua!" \
        "Tämä peli päättyy tähän, mutta kerro toki ystävillesi tästä pelistä ja vertailkaa vaikka pisteitä emt",
        {}
    ),
    "jotain_meni_pieleen": Event(
        "Tässä pelissä ei ole tämmöistä reittiä eli jotain meni koodin puolella pieleen. Peli loppuu tähän.",
        {}
    ),
    "end": Event(
        "Se oli siinä!",
        {}
    )
}