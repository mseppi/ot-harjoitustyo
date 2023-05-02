# Arkkitehtuurikuvaus

## Rakenne
Ohjelmassa on 3 kansiota sekä pääkansiossa yksi tiedosto, joka suorittaa käyttöliittymäkoodin. Käyttöliittymäkoodi sijaitsee ui-kansiossa. Ohjelmassa on myös services-tiedosto, joka sisältää pelilogiikan sekä variables-tiedosto, joka sisältää muuttujia, joita voi helposti muuttaa.

## Käyttöliittymä

Käyttöliittymä sisältää peliloopin koodin. Looppi käyttää pelilogiikkaa sekä variables-tiedoston muuttujia. Käyttöliittymä on pyritty eriyttämään pelilogiikasta ja se kutsuu services-tiedoston metodeja.

## Pelilogiikka
Pelilogiikan muodostavat luokat Grid ja Pieces, jotka kuvaavat pelikenttää ja putoavia palikoita.

![chrome_KcDcOaq5WY](https://user-images.githubusercontent.com/76455740/235766232-512902b5-a757-4343-9549-a5d8752f0e4f.png)

Pieces-luokka vastaa monista palikoihin liittyvistä toiminnallisuuksista. Näihin kuuluu esimerkiksi:

- `piece.rotate()`
- `piece.left()`
- `piece.collision()`

Molemmat luokat pääsevät käsiksi moniin muuttujiin Vvariables-kansion kautta, kuten WINDOW_HEIGHT ja BSIZE. Variables kansio onkin injektoitu näihin.

## Tietojen pysyväistallennus

Tiedon pysyväistallentamista ei ole vielä luotu, mutta high score systeemi on tulossa. Tämä toteutetaan joko tekstitiedostolla tai SQLite tietokannalla, jos on aikaa. 

## Päätoiminnallisuudet

Kuvataan yksi mahdollinen toimintalogiikka päätoiminnallisuuden osalta sekvenssikaaviolla

```mermaid
sequenceDiagram
User->>main: Launch game
main->>ui: Executes final()
ui->>config: Requests fps
config->>Ui: Delivers fps
ui->>grid: Requests grid from services
grid->>config: Requests config
config->>grid:Delivers config
game_logic->>ui:Delivers grid
ui->>piece: Requests piece from services
piece->>constants: Requests piece shape and color from constants
constants->>piece: Delivers them
piece->>ui: Delivers piece to ui
ui->>piece: requests piece moving down function
piece->>ui: Moves piece down

Ohessa kuvataan tilannetta, jossa käyttäjä käynnistää pelin ja kuvio tippuu yhden palkin alas. Tässä grid luo gridin ja pieces hakee variables-kansiosta satunnaisen palikan, jolle määritellään myös sitä kuvaava väri. Pieces-luokasta myös kutsutaan kuvion alaspäin menemistä, jolloin kuvio liikkuu yhden palkin alas.

## Ohjelman rakenteen heikkoudet

### Käyttöliittymä

Graaffista käyttöliittymää voisi vähän eheyttää.

### Koodin

Koodia olisi voinut myös jakaa ehkä hieman järkevämmin
