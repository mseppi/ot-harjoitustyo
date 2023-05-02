# Tetris sovellus

Sovellus on peli, jossa tippuu erinäköisiä palikoita. Pelin tarkoituksena on tehdä palikoista suoranainen rivi, jolloin rivi häviää ja pisteitä kertyy. Peli päättyy, kun palikat kertyvät ruudun yläreunaan asti.

## Pelin kontrollit

Vasen nuoli: Liiku vasemmalle

Oikea nuoli: Liiku oikealle

Nuoli ylös: Pyöritä tetris-palikkaa

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
