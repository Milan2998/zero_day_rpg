# ===================================

# Beadandó:
# Nagybányai Roland & Ványi Milán

# Zéró Nap (A labor RPG játék)

# All copyright served ©

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
