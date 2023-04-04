```mermaid
classDiagram
    Board"1" -- "40"Square
    Player "2-8" -- "*" Board
    Player "1" -- "1" Square
    Player..>Dices
    class Player
    class Board    
    class Square   
    class Dices
