# ===================================

# Beadandó:
# Nagybányai Roland & Ványi Milán

# Zéró Nap (A labor RPG játék)

# All copyright served © (XD)

# ===================================

# Változók
WIDTH = 45

hp = 100                 # Élet
infection = 10           # fertozes
day = 0                  # napok
code = 0                 # ajto nyito

# Sebzes és patkány

rat_hp = 40              # N-17 elet
player_damage = 12       # a játékos sebzés
rat_damage = 8           # N-17 sebzás

keycard = 0              
suit = 0                 # Labor ruha
map_found = 0            # labor térkép
mark_helps = 0           # Márk kódja
anna_ally = 0            # Anna segítsége
research_docs = 0        # Kutatási Docs.
recording = 0            # Hangfelvétel
nyx_data = 0             # NYX_RESEARCH_DATA
NBL_doc = 0            # NBL_7_PROTOCOL
sent = 0                 # bizonyíték publikálás
comms_off = 0            # kommunikácció offline
rat_defeated = 0         # N-17 legyőzve
escaped = 0              
protocol_stopped = 0     # NBL-7 leállítva


#Random bónusz (lehet bullshit xd)
security_level = 0       # magas biztonsági szint (hosszú név)
fast = 0                 # gyors vagy (rövid név)
 
fight_now = 0            # 1 = a nap végén harc indul
choice = ""              # az aktuális A/B döntés

# ---------------------------------------------------------------------
# Main menu
# ---------------------------------------------------------------------
print("=" * WIDTH)
print(" • ZÉRÓ NAP • ".center(WIDTH))
print("NBL Biolabor - Nyx-vírus kitörés".center(WIDTH))
print("=" * WIDTH)
print()
print("Te vagy a NBL Biolabor egyik kutatója.")
print("Egy kísérleti patkány megszökött, és halálos vírust hordoz.")
print("A labor lezárt. A mentőcsapat 10 nap múlva érkezik.")
print("Kijutsz egyedül, vagy megvárod a segítséget?")
print()

# Név 
name = ""
while name == "":
    name = input("Add meg a neved: ").strip().title()

letter_a = name.lower().count("a")     # hány 'a' betű van a névben
name_length = len(name)                # a név hossza

print()
print(f"Üdv, {name}! Itt vannak a képességeid:")

# bónuszok a név alapján
if letter_a > 0:
    infection = 0
    print("🛡️  Jó immunrendszer: fertőzés nélkül indulsz!")
if name_length >= 8:
    security_level = 1
    print("🔑 Magas biztonsági szint: könnyebben nyílnak az ajtók.")
elif name_length <= 4:
    fast = 1
    print("💨 Gyors vagy: a patkány elől könnyebben menekülsz.")
if letter_a == 0 and name_length > 4 and name_length < 8:
    print("Átlagos kutató vagy: nincs különleges bónuszod.")

input("\n⏎ Nyomj Entert a kezdéshez...") # (YTB vid segytség)

while hp > 0 and infection < 100 and day <= 9:

    fight_now = 0

    # napi státusz kiírása
    print()
    print("=" * WIDTH)
    print(f"{day}. NAP".center(WIDTH))
    print(f"❤️  HP: {hp}   🦠 Fertőzés: {infection}%".center(WIDTH))
    print("=" * WIDTH)

    # -----------------------------------------------------------------
    # 0. NAP - A riasztás
    # -----------------------------------------------------------------
    if day == 0:
        print(" B szektor - Kutatólabor")
        print("06:42-kor megszólal a riasztó. N-17, a Nyx-vírus hordozója")
        print("megszökött. A labor automatikusan lezár.")
        print("A képernyőn: \"A kijutás nem engedélyezett.\"")
        print()
        print("A) Megpróbálod elérni a biztonsági központot.")
        print("B) Átkutatod az irodát.")

        choice = ""
        while choice != "A" and choice != "B":
            choice = input("Választásod (A/B): ").strip().upper()
            if choice != "A" and choice != "B":
                print(" Érvénytelen választás! Írj A-t vagy B-t.")

        if choice == "A":
            mark_helps = 1
            print(" Márk Kovács biztonsági őr válaszol. Később segíthet.")
        else:
            map_found = 1
            infection -= 10
            print("  Felszerelést és egy laboratóriumi térképet találsz.")

        day += 1

# -----------------------------------------------------------------
# 1. NAP - Az első nyomok
# -----------------------------------------------------------------

    elif day == 1:
        print(" A szektor - Irodák")
        print("A labor csendes. Egy jelentésből kiderül, hogy N-17")
        print("már korábban is megpróbált megszökni.")
        print()
        print("A) Átkutatod a biztonsági irodát.")
        print("B) Átkutatod a kutatói irodát.")

        choice = ""
        while choice != "A" and choice != "B":
            choice = input("Választásod (A/B): ").strip().upper()
            if choice != "A" and choice != "B":
                print(" Érvénytelen választás! Írj A-t vagy B-t.")

        if choice == "A":
            keycard = 1
            infection += 3
            print(" Megtalálod a kijutáshoz szükséges kulcskártyát.")
        else:
            research_docs = 1
            infection += 3
            print(" Dr. Elena Varga első kutatási dokumentumait találod.")

        day += 1

# -----------------------------------------------------------------
# 2. NAP - A segítség
# -----------------------------------------------------------------


    elif day == 2:
        print(" D szektor - Orvosi részleg")
        print("A rádión női hang szólal meg:")
        print("\"Itt Szabó Anna, a D-3-as helyiségben vagyok. Segíts!\"")
        print()
        print("A) Megpróbálod megmenteni Annát (fertőzésveszély!).")
        print("B) Nem kockáztatsz, folytatod a saját tervedet.")

        choice = ""
        while choice != "A" and choice != "B":
            choice = input("Választásod (A/B): ").strip().upper()
            if choice != "A" and choice != "B":
                print(" Érvénytelen választás! Írj A-t vagy B-t.")

        if choice == "A":
            infection += 10
            if hp >= 60:
                anna_ally = 1
                suit = 1
                print(" Sikerül kimenekítened Annát! Szövetségesed lesz,")
                print("és ad neked egy biológiai védőruhát.")
            else:
                hp -= 10
                print("Túl gyenge vagy, a mentés nem sikerül. Megsérülsz.")
        else:
            print(" Anna később már nem jelentkezik a rádión...")

        day += 1

# -----------------------------------------------------------------
# 3. NAP - Az első tünetek
# -----------------------------------------------------------------

    elif day == 3:
        print("Orvosi részleg - Laboratórium")
        print("Fejfájással és lázzal ébredsz. A Nyx első tünetei...")
        print()

        # [3. DIÁK] 3. kör - súlyosabb tünetek, rohamok
        for hours in range(1, 4):
            infection += 2 * hours
            infection = min(infection, 100)
            print(f" {hours}. roham: a fertőzés {2 * hours}%-ot nő. "
                  f"(Összesen: {infection}%)")

        print("A) Lemegyek a fertőtlenítő kamrába.")
        print("B) A kijárati kódot keresed tovább.")

        choice = ""
        while choice != "A" and choice != "B":
            choice = input("Választásod (A/B): ").strip().upper()
            if choice != "A" and choice != "B":
                print(" Érvénytelen választás! Írj A-t vagy B-t.")

        if choice == "A":
            infection -= 25
            print(" A kamra lemossa rólad a vírus egy részét.")
        else:
            code += 1
            infection += 8
            print(" Megtalálod a kijárati kód első részét.")

        day += 1

# -----------------------------------------------------------------
# 4. NAP - hazudik
 # -----------------------------------------------------------------ú

    elif day == 4:
        print(" Vezetői iroda")

        #Mark: kód másik resze 
        if mark_helps == 1:
            code += 1
            print(" Márk rádión elküldi a kijárati kód egy részét!")
            print()

        print("Egy régi hangfelvételt találsz Dr. Elena Vargától:")
        print("\"A vezetőség tudta, hogy a Nyx emberre is veszélyes.")
        print("A teszteredményeket meghamisították.\"")
        print("A végén először hallasz a HELIX-7 protokollról.")
        print()
        print("A) Elmented a hangfelvételt (bizonyíték).")
        print("B) Törlöd, és továbbmész (+10 HP, nem vesztegetsz időt).")

        choice = ""
        while choice != "A" and choice != "B":
            choice = input("Választásod (A/B): ").strip().upper()
            if choice != "A" and choice != "B":
                print(" Érvénytelen választás! Írj A-t vagy B-t.")

        if choice == "A":
            recording = 1
            print(" A felvétel nálad van.")
        else:
            hp += 10
            print("  Törlöd a felvételt. Kicsit jobban érzed magad.")

        day += 1


# -----------------------------------------------------------------
# 5. NAP - vadászatű
# -----------------------------------------------------------------

    elif day > 0 and day % 5 == 0:
        print(" B szektor - Kutatólabor")
        print(" 03:17 - a labor VÉSZÜZEMMÓDBA kapcsol!")
        print("A kamerákon megjelenik N-17. Megtalált téged.")
        print("A folyosón kaparászás hallatszik, az ajtó megremeg.")
        print()
        print("A) Elrejtőzöl egy tárolóhelyiségben.")
        print("B) Szembeszállsz N-17-tel (győzelem: biztonsági kártya).")

        choice = ""
        while choice != "A" and choice != "B":
            choice = input("Választásod (A/B): ").strip().upper()
            if choice != "A" and choice != "B":
                print(" Érvénytelen választás! Írj A-t vagy B-t.")

        if choice == "A":
            if fast == 1 or infection % 2 == 0:
                print(" Visszatartod a lélegzeted... N-17 továbbmegy.")
                print("(De később még visszatérhet.)")
            else:
                print(" A patkány megérzi a szagodat! Meg kell küzdened vele.")
                fight_now = 1
        else:
            fight_now = 1

        day += 1

# -----------------------------------------------------------------
# 6. NAP - Igazi kisérlet
# -----------------------------------------------------------------
    elif day == 6:
        print(" F szektor - Kutatási központ")
        print("Megtalálod a Nyx-projekt végleges dokumentációját.")
        print("Kiderül: a vírus nem baleset volt. A vezetőség tudta.")
        print()
        print("A) Letöltöd a NYX_RESEARCH_DATA dokumentumot.")
        print("B) Letöltöd a HELIX_7_PROTOCOL dokumentumot.")

        choice = ""
        while choice != "A" and choice != "B":
            choice = input("Választásod (A/B): ").strip().upper()
            if choice != "A" and choice != "B":
                print(" Érvénytelen választás! Írj A-t vagy B-t.")

        if choice == "A":
            nyx_data = 1
            infection += 4
            print(" Bizonyítékod van a vírus valódi eredetéről.")
        else:
            helix_doc = 1
            infection += 4
            print("Megismered a labor megsemmisítési tervét.")

        day += 1

# -----------------------------------------------------------------
# 7. NAP - A mentőcsapat
# -----------------------------------------------------------------
    elif day == 7:
        print(" Kommunikációs központ")
        print("Sikerül kapcsolatba lépned a mentőegység parancsnokával.")
        print("\"Tartózkodjon a helyén. Három nap múlva megérkezünk.\"")
        print("Elmagyaráznád a Nyx veszélyeit, de félbeszakít:")
        print("\"Tudunk a Nyxről.\"  - a kapcsolat megszakad.")
        print("  HELIX-7 AKTIVÁLÁS - 72 ÓRA")
        print()
        print("A) Megpróbálod továbbítani a bizonyítékokat a külvilágnak.")
        print("B) Kikapcsolod a kommunikációs rendszert.")

        choice = ""
        while choice != "A" and choice != "B":
            choice = input("Választásod (A/B): ").strip().upper()
            if choice != "A" and choice != "B":
                print(" Érvénytelen választás! Írj A-t vagy B-t.")

        if choice == "A":
            if recording == 1 or nyx_data == 1 or helix_doc == 1:
                sent = 1
                print(" A bizonyítékok kijutnak a külvilágba!")
            else:
                print(" Nincs semmilyen bizonyítékod, amit elküldhetnél.")
        else:
            comms_off = 1
            print(" Kikapcsolod a rendszert. Már nem figyelhetnek meg,")
            print("de a külvilággal sem tudsz beszélni.")

        day += 1

# -----------------------------------------------------------------
# 8. NAP - A kijárat
# -----------------------------------------------------------------
    elif day == 8:
        print(" E szektor - Felszíni hozzáférés")
        print("Egy hatalmas biztonsági ajtó áll előtted. A terminál kéri:")
        print("kulcskártya, biztonsági kód és biológiai védőruha.")
        print("  HELIX-7 AKTIVÁLÁS - 48 ÓRA")
        print()
        print("A) Visszamész a laborba a hiányzó felszerelésért.")
        print("B) Megpróbálod erőszakkal kinyitni a kijáratot.")

        choice = ""
        while choice != "A" and choice != "B":
            choice = input("Választásod (A/B): ").strip().upper()
            if choice != "A" and choice != "B":
                print(" Érvénytelen választás! Írj A-t vagy B-t.")

        if choice == "A":
            # egy hiányzó tárgyat kapsz: kártya, kód, ruha sorrendben
            if keycard == 0:
                keycard = 1
                print(" Megtalálod a hiányzó kulcskártyát.")
            elif code < 2:
                code = 2
                print(" Megtalálod a kód hiányzó részét.")
            elif suit == 0:
                suit = 1
                print(" Megtalálod a védőruhát.")
            else:
                print("Mindened megvan, csak időt vesztegettél.")
            hp -= 10
            if map_found == 1:
                infection += 10
                print("  A térkép segít: kevesebb veszélyes szakaszt érintesz.")
            else:
                infection += 15
        else:
            if comms_off == 1 or security_level == 1 or \
                    (keycard == 1 and infection % 2 == 0):
                code = 2
                print(" Az ajtó rendszere megadja magát! A kód felszabadul.")
            else:
                hp -= 25
                infection += 10
                print(" Az ajtó nem enged, és megsérülsz. Értékes időt veszítesz.")

        day += 1

# -----------------------------------------------------------------
# 9. NAP - Az utolsó éjszaka
# -----------------------------------------------------------------
    elif day == 9:
        print(" Központi vezérlőterem")
        print("  HELIX-7 AKTIVÁLÁS - 24 ÓRA")
        print("Dr. Varga utolsó üzenete:")
        print("\"A védőruha nem garantálja, hogy nem vagy fertőzött.\"")
        print("Rájössz: a fertőzöttséged a külvilágot is veszélyezteti.")

        # ha az 5. napon nem ölted meg most utadat fogja allni a N-17 (womp-womp)
        if rat_defeated == 0:
            print()
            print(" N-17 előbukkan a sötétből, és elállja az utat!")
            fight_now = 1

        print()
        print("A) Azonnal megpróbálsz kijutni.")
        print("B) Megpróbálod leállítani a HELIX-7 protokollt.")

        choice = ""
        while choice != "A" and choice != "B":
            choice = input("Választásod (A/B): ").strip().upper()
            if choice != "A" and choice != "B":
                print(" Érvénytelen választás! Írj A-t vagy B-t.")

        day += 1


# -----------------------------------------------------------------
# 10. NAP - A befejezés
# -----------------------------------------------------------------


print()
print("=" * WIDTH)
print("10. NAP - ZÉRÓ NAP".center(WIDTH))
print("=" * WIDTH)

if infection >= 100 or hp <= 0:
    print("A Nyx-vírus legyőz. A labor csendjében a legendád véget ér.")

elif escaped == 1:
    if infection >= 80:
        print("Kijutsz, de a mentőcsapat észleli a fertőzésedet,")
        print("és karanténba zár. Életben maradsz, de a sorsod bizonytalan.")
    elif sent == 0:
        print("Kijutsz, de bizonyíték nélkül senki sem hisz neked.")
        print("A vezetőség elhallgattat.")
    else:
        print("Kijutsz a felszínre, és a bizonyítékoddal")
        print("leleplezed a Helix Biolabort.")

elif protocol_stopped == 1:
    print("Megállítod a HELIX-7-et, és a mentőcsapat megérkezik.")
    print("Életben vagy, de a vezetőség karanténba zár.")

else:
    print("A mentőcsapat nem menteni érkezik. Végrehajtják a")
    print("HELIX-7 protokollt, és megsemmisítik a labort")
    print("a benne rekedt emberekkel együtt.")

print("Köszönjük hogy játszottál!")

