# Tetris

Tetris on peli, jossa tippuu vuorotellen erilaisia palikoita. Pelin ideana on saada täysi rivi palikoita jolloin pistesaldo kasvaa. Peli loppuu, kun palikat kasautuvat ruudun yläreunaan.

## Pelin kontrollit

### MAIN MENU

Enter: Aloita peli

H: Näytä pistetaulukko

Enter tai escape pistetaulukossa: Siirtyy takaisin menuun.

### PELIN SISÄLLÄ

Nuolet vasemmalle, oikealle ja alas: Liikuta palikkaa

Nuoli ylös: Pyöritä palikkaa

Left control: Pyöritä palikkaa toiseen suuntaan

Spacebar: Tiputa palikka välittömästi alas asti

### PELIN LOPUKSI

Jos sait huipputuloksen, kirjoita nimesi top-listalle. Nimi ei voi olla merkitön tai yli 10 merkkiä eikä se sisällä välilyöntejä.

Loppupistetaulukko: Enter tai escape siirtyy sulkee pelin.

## Python-versio
Sovelluksen toiminta on testattu pythonin versioilla 3.10.6. Vanhemmilla tai jopa uudemmillakin python-versioilla voi esiintyä ongelmia.

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/mseppi/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/mseppi/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/mseppi/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

[Arkkitehtuurikuvaus](https://github.com/mseppi/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

[Käyttöohje](https://github.com/mseppi/ot-harjoitustyo/blob/main/dokumentaatio/k%C3%A4ytt%C3%B6ohje.md)

## Asennus

1. Asenna riippuvuudet komennolla

```
poetry install
```

2. Käynnistä peli komennolla

```
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelma suoritetaan seuraavalla komennolla

```
poetry run invoke start
```

### Testaaminen

Testaamiseen käytetään komentoa

```
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi saada komennolla

```
poetry run invoke coverage-report
```

Raportti tulee htmlcov-hakemistoon.

### Pylint

Tiedoston [.pylintrv](https://github.com/mseppi/ot-harjoitustyo/blob/main/.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla

```
poetry run invoke lint
```
