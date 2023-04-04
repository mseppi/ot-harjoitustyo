```mermaid
sequenceDiagram
participant main
participant laitehallinto
participant rautatientori
participant ratikka6
participant bussi244
main->>laitehallinto:lisaa_lataaja(rautatientori)
main->>laitehallinto:lisaa_lukija(ratikka6)
main->>laitehallinto:lisaa_lukija(bussi244)
participant lippu_luukku
main->>lippu_luukku:osta_matkakortti("Kalle")
lippu_luukku-->>main:Matkakortti(kallen_kortti)
main->>rautatientori:lataa_arvoa(kallen_kortti, 3)
rautatientori->>kallen_kortti:kasvata_arvoa(3)
kallen_kortti-->>main:arvo(3)
main->>ratikka6:osta_lippu(kallen_kortti, 0)
ratikka6->>kallen_kortti:vahenna_arvoa(1.5)
kallen_kortti-->>main:arvo(1.5)
ratikka6-->>main:True
main->>ratikka6:osta_lippu(kallen_kortti, 2)
ratikka6-->>main:False

