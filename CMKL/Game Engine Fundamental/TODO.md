# TODO
## Model + Animation: 
- mixamo
- retarget animation
- Blender basic navigation
- Blender modelling 

## Unreal Engine:
- Post Processing
- point light from user
    - not cast shadow
    - specular - off - no light reflection
- model -> difference b - a

<br></br><br></br><br></br><br></br>
# Study Unreal
## Naming Convention
- BP_Actor
    - BP_ for blueprints

## Static Mesh
![alt text](./Notes_images/static_mesh.png)
- Static mesh to add object

## Event Graph
![alt text](./Notes_images/event_graph.png)
- Event graph (Blueprints)
    - Blue print is flow control

## Event Begin Play
![alt text](./Notes_images/event_begin_play1.png)
![alt text](./Notes_images/event_begin_play2.png)
- Things connected to this block will run upon object initiated

## Variables
![alt text](./Notes_images/variable.png)

## Structure (Struct)
![alt text](./Notes_images/struct1.png)
![alt text](./Notes_images/struct2.png)

## Vectors
- Direction

### Rotation
![alt text](./Notes_images/euler_rotation.png)

### Gimbal lock Problem
- Lock your rotation
- Solved with quaternion rotation to fix
- FPS game 

### Transformation
- Transform location

    
# Game Instance
- Singleton
- Can have more than one but only one BP running
- Like having Online Game Instance and Offline Game Instance

# Game Mode
- Rules and flows for a specific level
- Binded with level
- Ensures essential parts(objects) are loaded in the level
- Ex Mode : Main menu, Stage1, Stage2, Stage3
- Change level = current game mode instance is destroyed
- Value, Property, Field cached is destroyed with the game mode.
- Have to save them in game instance
- Level create Game mode

# Game Mode Setting
![alt text](./Notes_images/GM_property.png)
- Main classes that will be loaded to the level

## Default Pawn Class
- Default pawn for player to control
- Spawn the pawn when game mode initiated

## Player Controller Class
- Handle input from player to the pawn that it possess
- 1 class can control 1 pawn
    - 100 pawn = 100 object

> There are 2 kinds of controllers, Player Controller and Ai Controller

## Game State Class
- Game mode create game state
- Ensures clients are synchronized with the current game state
    - Collect data on what's happening
- Used for multiplayer but can't be none, so you have to spawn it
- not needed for single player game
- Imagine playing catch, if A catches B, Game state tells every clients that A catches B

## Player State
- Kinda Game state but only for a pecific player
- Again, not needed for single player game

## Game session
- used to handle multiplayer session

## HUD Class(Heads-Up Diaplay)
- Draws UI elements on the screen, such as health bar, ammo count, crosshair
    - Control Showing / not on each ui
    - If you die, disable UI
- Created only in the client side, in multiplayer
- FPS hands are objects and not HUD
    - Hide on Processes will hide the arm when process

## Spectator Class
- class for when player is in spectator mode
- Has setting in project property > game mode > start as spectator

# Save Game
- Serialization : Serialize the save to .sav binary file
- Store / retrieve data persistently acreoos game session
- SaveGameToSlot() / LoadGameToSlot()

# Pawn and Controller
- Pawn is an actor that represents a controllable entity in tha game
- Can be used by player of AI characters
- AI controller uses behavior tree
- Controller manages the logic that directs the behavior of a pawn

## Player Controller
- Controller that controls player input
- Contains HUD for player

## AI Controller
- designs for non-player characters(NPC) or AI-driven pawns
- Behavior Tree
- Inherits from player class
- No need HUD

# Possession
- Controller posesses a pawn
- Logic is at the Controller not the character
- Possess / Unpossess

# Idea
- Possess 2 characters at the same time
- Puzzle
- Collect items to switch view to see what's happening with the clone

# 3Cs (Character, Chamera, Control)
- Make the gmae satisfying for player's experience
- How player interact with the game mechanics
- 

## Character
- If you can know who the character is by the silhouette = good charcter design
- Looks and feeling
- Movements & Physics
- Animations
- Abilities & Actions

## Camera
- First Person / Third Person etc.
- Perspective
- Camera Behavior
- Field of View & Angles

# Control
- Ergonomics
- Think about how player will hold the controller
- How it feels to control the character
- Input methods and schenes used to manipulate the character and camera
- Input mapping : define key mapping for inputs
- Responsiveness : VR / AR thing
- Customization

# Asset management
## Basic Filder Structure
```
Content
|
|-- Blueprints
|   - Characters
|   - Controllers
|   - Gameplay
|
|-- Materials
|   - Characters
|   - Environments
|   - UI
|
|-- Textures
|   - Characters
|   - Environments
|   - UI
|
|-- Meshes
|   - Characters
|   - Environments
|
|-- Audio
|   - SoundEffects
|   - Music
|   - Voice
|
|-- UI 
|   - Widgets
|   -
|   -
```
## Folder Hierarchy
- Path length no more than 255 character or unreal goes retard

## Naming Convention
- BP_ : Blueprints
- WBP_ : Widget Blueprints
- M_ : Materials

`https://dev.epicgames.com/documentation/en-us/unreal-engine/recommended-asset-naming-conventions-in-unreal-engine-projects`

# Data Assets
- Inherits from `Primary Data Assets` parent class
- Used to keep variables instead of saving in cahracter blueprints
    - So we can call them from other classes too
- Create BP from Primary Data Assets
    - Miscellaneous -> Data Assets
- Imagine wanting to save exp data assets (how much exp needed for each level up)

## Primary Data Assets
- Primary Data Assets BP class and Actual Data Assets
- One data asset for one character

## Best Practice for data assets
- DA_ : Naming Convention
- No use Data Assets for temporary or changable data
    - Won't change in the next sessions, will return to default values
- Create central data assets, only change one place

# Data Tables
- Work like spreadsheets
- Row and column
- The engine won't knkow which cells is what
- BP -> Structure : Create a struct
    - Miscellaneous -> Data Table
        - Pick row structure, choose previously made struct
        - Change values in Row editor
- Better than Data Assets in some case
- Can import / export csv files from outside (Behind the scene is json)
- Can handle file outside UE
- If data lost on git, can re import
- In the end 1 row is one data assets
- Unlike Data Assets which can use the data directly, Data Tables have to use `get data table row`. Query data by row

## Best Practice for data table
- DT_ : Naming Convention
- Use simple, consistent names
- Can use soft reference

# String Tables
- Store Texts despite the name String Table
- Mostly useful for saving UI
- For supporting multiple languages
- Miscellaneous -> String 
- Create variable text