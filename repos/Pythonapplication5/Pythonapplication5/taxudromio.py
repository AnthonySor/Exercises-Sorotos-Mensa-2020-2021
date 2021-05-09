class taxudromio(object):
    "desrciption of the object"

    import contact
    import dema
    import epistoli

    demalist = []
    epistolist = []

    pelatis1 = contact.contact('Bla','Black','Petmeza 14',12244,'123456789')
    pelatis2 = contact.contact('Blu', 'Blue','Skopeftirio 45',16644,'987654321')
    demataki=dema.dema(2.70,pelatis1,pelatis2,'small','foam',1.0)
    
    tyepistoli=epistoli(1.00,pelatis2,pelatis1,'low')
    epistolist.append(tyepistoli)
    epistolist.pop(0)