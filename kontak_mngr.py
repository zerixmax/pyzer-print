#region MODELI
kontakti = {} # key: id, value: kontakt dict
firme = {}   # key: id, value: firma dict

#endregion

#region FUNKCIJE
def dodaj_firmu(id, name, tax_id):
    firma = {
        'id': id,
        'name': name,
        'tax_id': tax_id,
        'contacts': []  # Inicijaliziraj listu kontakata za firmu
    }
    firme[id] = firma

def dodaj_kontakt(id, first_name, last_name = '', phone = '', email = '', company_id = None):
    kontakt = {
        'id': id,
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone,
        'email': email,
        'company_id': company_id
    }
    kontakti[id] = kontakt
    if company_id in firme:
        firme[company_id]['contacts'].append(id)
    
def prikaz_svih_kontakata():
    print("Svi kontakti:")
    for k  in kontakti.values():
        print(f"{k['id']}: {k['first_name']} {k['last_name']} - {k['phone']} - {k['email']} (Firma ID: {k['company_id']})")

def prikaz_kontakata_jedne_firme(firma_id):
    if firma_id in firme:
        firma = firme[firma_id]
        print(f"Svi kontakti za firmu {firme[firma_id]['name']}:")
        for kid in firma['contacts']:
            if kid in kontakti:
                k = kontakti[kid]
                print(f"{k['id']}: {k['first_name']} {k['last_name']} - {k['phone']} - {k['email']}")
    else:
        print(f"Firma s ID {firma_id} ne postoji.")

def azuriraj_firmu(id, name = None, tax_id = None):
    if id in firme:
        if name is not None:
            firme[id]['name'] = name
        if tax_id is not None:
            firme[id]['tax_id'] = tax_id
def azuriraj_kontakt(id, first_name = None, last_name = None, phone = None, email = None, company_id = None):
    if id in kontakti:
        if first_name is not None:
            kontakti[id]['first_name'] = first_name
        if last_name is not None:
            kontakti[id]['last_name'] = last_name
        if phone is not None:
            kontakti[id]['phone'] = phone
        if email is not None:
            kontakti[id]['email'] = email
        
#endregion

#region Main
if __name__  ==  '__main__':#dodaj par testnih firmi  i kontakata
    dodaj_firmu(1, 'Firma A', '12345678901')
    dodaj_firmu(2, 'Firma B', '98765432101')
    dodaj_kontakt(1, 'Pero', 'Peric', '0912345678', 'pero.peric@example.com', 1)
    dodaj_kontakt(2, 'Ana', 'Anic', '0987654321', 'ana.anic@example.com', 1)        

    prikaz_svih_kontakata() # Ispravljen poziv funkcije
    print("\n--------------------\n")
    prikaz_kontakata_jedne_firme(1)
    print("\n--------------------\n")
    prikaz_kontakata_jedne_firme(2)
    print("\n--------------------\n")

#endregion