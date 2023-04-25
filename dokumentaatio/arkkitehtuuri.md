```mermaid
classDiagram
class Main{
  main()}
class Ui{
  draw_game()
  final()}
class Game_logic{
  shapes
  shape_colors
  Pieces()
  Grid()}

Main--Ui
Ui--Game_logic

```mermaid
sequenceDiagram
User->>main:Launch game
main->>ui:Executes final()
ui->>config:requests fps
config->>ui:Delivers fps
ui->>game_logic:Requests grid and piece from game logic
game_logic->>config:requests config
config->>game_logic:Delivers config
game_logic->>ui:Delivers grid and piece
ui->>game_logic:Moves piece down
