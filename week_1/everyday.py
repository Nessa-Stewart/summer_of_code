print("I can calculate your kill/death ratio for your last play session with your favorite video game.")

kills = int(input("Please tell me how many players you defeated in your last session: "))

deaths = int(input("Please tell me how many time you died in your last session: "))

kd = kills / deaths

print("Your kill/death reatio for your last play session was " + str(kd) + ".")