
#one way to make a basic health bar
maxhealth = 15
playerhp = 5



def health():
    hplost = maxhealth - playerhp
    hpdislay = chr(0x2588) + chr(0x2502)
    dashdisplay = chr(0x2591) + chr(0x2502)
    remaininghp = hplost - playerhp
    dishp = hpdislay * playerhp
    dashzero = dashdisplay * hplost
    print(dishp + dashzero)


health()