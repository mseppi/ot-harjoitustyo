# Testausdokumentti
Ohjelmassa on automatisoitu unittest sekä ohjelmaa on testattu manuaalisesti järjestelmätasolla

## Yksikkö- ja integraatiotestaus

### Pelilogiikka
Pelilogiikkaa testaa tests-kansion test_pieces ja test_grid moduulit, joissa molemmissa on näitä testaava luokka. Testeissä on monia testejä enimmillään liittyen palikan liikkumiseen ja palikan collision-fysiikoiden toimivuuteen. Grid-testauksessa taas suurimmalta osalta keskitytään rivien poistoon ja pisteytykseen sekä pelin tasoon.

###Testauskattavuus

Näistä testauskattavuus on siis 61%



![chrome_T4rnySHcPl](https://github.com/mseppi/ot-harjoitustyo/assets/76455740/6c85049e-5668-485c-b092-333e99f39da4)

Pelilogiikkatiedostoissa on myös muutama piirtämiseen liittyvä funktio, jotka vaikeuttavat niien testaamista. Nämä olisi voinut lisätä toiseen luokkaan.

## Järjestelmätestaus

Kaikki järjestelmätestaukset on suoritettu manuaalisesti mm. Print-komennoilla sekä lisäämällä pisteisiin valmiiksi pisteitä.

### Alustat

Peliä on testattu sekä linux-läppärillä, että windowsin wsl-koneella. Windowsilla sovelluksen pyörittämisessä toimi hyvin xlaunch.

### Toiminnallisuudet

Kaikki määrittelydokumentin toiminnallisuudet on käyty läpi manuaalisesti ja monet myös unittestillä.

##Sovellukseen jäänet laatuongelmat

- Jos highscores.txt tiedosto on virheellinen, sovellus kaatuu.
- Jos haluaa pelata uuden pelin, pitää sovellus aloittaa alusta.
