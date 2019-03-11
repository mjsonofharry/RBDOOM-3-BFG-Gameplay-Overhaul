# RBDOOM-3-BFG-Gameplay-Overhaul

## 1 Introduction

RBDOOM-3-BFG-Gameplay-Overhaul is a mod for [RBDOOM-3-BFG](https://github.com/RobertBeckebans/RBDOOM-3-BFG/releases) and [Classic-RBDOOM-3-BFG](https://github.com/MadDeCoDeR/Classic-RBDOOM-3-BFG/releases). Some highlights include:

* No reloading
* No stamina
* Better weapons
* Less ammo, health, and armor
* Ejected brass and corpse persistence
* Various quality of life improvements

## 2 Installation

1. Get [RBDOOM-3-BFG](https://github.com/RobertBeckebans/RBDOOM-3-BFG/releases) or [Classic-RBDOOM-3-BFG](https://github.com/MadDeCoDeR/Classic-RBDOOM-3-BFG/releases).
2. Get the [latest release](https://github.com/mjsonofharry/RBDOOM-3-BFG-Gameplay-Overhaul/releases/latest) of this mod.
3. Move the mod files to *<path to Doom 3 BFG Edition>/RBDOOM-3-BFG-Gameplay-Overhaul/*.
4. Create a shortcut to *<path to Doom 3 BFG Edition>/RBDoom3BFG.exe* with the following launch parameters: `+set fs_game RBDOOM-3-BFG-Gameplay-Overhaul +set fs_resourceLoadPriority 0`

The resulting file tree should look something like this:

```
DOOM 3 BFG
├── base
├── Doom3BFG.exe
├── RBDoom3BFG.exe
└── RBDOOM-3-BFG-Gameplay-Overhaul
    ├── def
    ├── guis
    ├── sound
    ├── script
    └── mod.conf
```

Note: Some changes will not work correctly when applied to pre-existing saves.

## 3 Summary

### 3.1 Weapons

#### 3.1.1 General

* Reloading removed
* Ejected brass TTL increased to 1 hour

#### 3.1.2 Flashlight

* Light cone increased
* Recoil added to melee

#### 3.1.3 Fists and chainsaw

* Recoil added

#### 3.1.4 Pistol

* Fire rate doubled
* Accuracy made near-perfect

#### 3.1.5 Shotgun

* Accuracy dramatically improved to match classic shotgun
* Removed one of the firing animations because it's distractingly different from the others
* Firing rate increased
* Projectile count decreased

#### 3.1.6 Machinegun

* Fires in 3-round bursts
* Accuracy improved
* Damage increased
* On-weapon GUI updated

#### 3.1.7 Grenades

* Friction increased and bounciness decreased to improve predictability
* Minimum throwing power doubled so that you don't have to hold mouse 1 for as long

#### 3.1.8 Chaingun

* First few shots have increased accuracy (not as accurate as machinegun)
* On-weapon GUI updated
* Spinup time decreased
* Damage decreased so that the chaingun does not usurp the plasmagun
* Muzzle smoke effect removed because it blocks visibility too much

#### 3.1.9 Plasmagun

* On-weapon GUI updated
* Damaged increased

#### 3.1.10 Rocket launcher

* Reloading removed
* Projectile velocity increased
* Recoil increased to match firing animation

#### 3.1.11 BFG

* On-weapon GUI updated

### 3.2 Pickups

* All ammo pickup quantities decreased
* Health pickup quantities decreased
* Armor pickup quantities decreased
* Shell, handgrenade, and rocket pickups made consistent with their models

### 3.3 Player

* Stamina removed, allowing infinite running
* Crouch walk speed increased
* Ammunition carry limits reduced to resemble classic (non-backpack) limits
* Maximum armor decreased

### 3.4 Enemies

#### 3.4.1 General

* Corpses no longer burn up or otherwise disappear

#### 3.4.2 Demon

* Trite melee aim kick reduced
* Pinky aim kick reduced
* Imp fireball sounds are quieter
* Imps no longer constantly scream when using ranged attacks
* Imp combat idle sounds replaced with louder footsteps
* Pinky footsteps are louder
* Hellknights no longer constantly scream when using ranged attacks
* Pinky, cacodemon, mancubus, and hellknight health increased

#### 3.4.3 Humanoid

* Aim kick of zsec ranged attacks decreased
* Zsec shields no longer completely block all damage
* Removed the repetitive sound effect played when zsec spot the player

### 3.5 Configuration

* Doom 3 selected by default
* Intro videos skipped
* Armor protection set to 0.3
* Exposure set to 0 and half lambert lighting disabled to increase darkness

## 4 How to make your own mods for RBDOOM-3-BFG

1. Launch RBDoom3BFG.exe with the following launch argument: `+set com_allowconsole 1`
2. Press the `~` key and enter the following into the console: `exec extract_resources.cfg`
3. Wait a while. RBDOOM-3-BFG is extracting all of the game's resource files into *<path to Doom 3 BFG Edition>/basedev*
5. Read [Making a mod for RBDoom3BFG and Doom 3 BFG Hi Def](https://www.moddb.com/mods/doom-3-bfg-hi-def/tutorials/making-a-mod-for-rbdoom3bfg-and-doom-3-bfg-hi-def) by y2keeth
