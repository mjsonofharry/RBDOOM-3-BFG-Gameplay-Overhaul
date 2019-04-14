# RBDOOM-3-BFG-Gameplay-Overhaul <!-- omit in toc --> 

- [Introduction](#introduction)
- [Installation](#installation)
  - [BFG Edition](#bfg-edition)
  - [Doom 3 with Resurrection of Evil](#doom-3-with-resurrection-of-evil)
  - [Configuration](#configuration)
  - [Known Issues](#known-issues)
    - [Doom 3](#doom-3)
    - [dhewm 3](#dhewm-3)
    - [RBDOOM 3 BFG](#rbdoom-3-bfg)
    - [Classic RBDOOM 3 BFG](#classic-rbdoom-3-bfg)
- [Summary](#summary)
  - [Weapons](#weapons)
    - [Flashlight](#flashlight)
    - [Fists](#fists)
    - [Chainsaw](#chainsaw)
    - [Pistol](#pistol)
    - [Shotgun](#shotgun)
    - [Super shotgun](#super-shotgun)
    - [Machinegun](#machinegun)
    - [Grenades](#grenades)
    - [Chaingun](#chaingun)
    - [Plasmagun](#plasmagun)
    - [Rocket launcher](#rocket-launcher)
    - [BFG](#bfg)
    - [PDA](#pda)
    - [Soul Cube and Artifact](#soul-cube-and-artifact)
    - [Grabber](#grabber)
  - [Pickups](#pickups)
  - [Player](#player)
  - [Enemies](#enemies)
    - [Imp](#imp)
    - [Pinky](#pinky)
    - [Trite](#trite)
    - [Wraith](#wraith)
    - [Hellknight](#hellknight)
    - [Archvile](#archvile)
    - [Cyberdemon](#cyberdemon)
    - [Zombie security](#zombie-security)
  - [Levels](#levels)
- [How to make your own mods for RBDOOM-3-BFG](#how-to-make-your-own-mods-for-rbdoom-3-bfg)
- [Credits](#credits)

## Introduction

Doom 3 Gameplay Overhaul is a mod that offers:

* No reloading
* Unlimited sprinting
* Improved weapons
* Deadly enemies
* Scarcity of ammo, health, and armor
* Super shotgun and grabber in base campaign
* Persistent ragdolls and ejected brass
* No artifact or soulcube

The following version of Doom 3 are supported:

* [Doom 3](https://store.steampowered.com/app/9050/DOOM_3/) with [Resurrection of Evil](https://store.steampowered.com/app/9070/DOOM_3_Resurrection_of_Evil/) installed
* [dhewm 3](https://dhewm3.org/)
* [RBDOOM 3 BFG](https://github.com/RobertBeckebans/RBDOOM-3-BFG)
* [Classic RBDOOM 3 BFG](https://github.com/MadDeCoDeR/Classic-RBDOOM-3-BFG)

The mod may work with other source ports. However, only the titles listed above receive testing.

## Installation

### BFG Edition

1. Get [RBDOOM-3-BFG](https://github.com/RobertBeckebans/RBDOOM-3-BFG/releases) or [Classic-RBDOOM-3-BFG](https://github.com/MadDeCoDeR/Classic-RBDOOM-3-BFG/releases).
2. Get the [latest release](https://github.com/mjsonofharry/RBDOOM-3-BFG-Gameplay-Overhaul/releases/latest) of this mod.
3. Move the mod files to `<path to RBDOOM 3 BFG Edition>/RBDOOM-3-BFG-Gameplay-Overhaul/`.
4. Create a shortcut to the game executable with the following launch parameters: `+set fs_game RBDOOM-3-BFG-Gameplay-Overhaul +set fs_resourceLoadPriority 0`

Some changes will not work correctly when applied to pre-existing saves. Also, if you're using **Classic-RBDOOM-3-BFG**, adding `+set flashlight_old 1` to your launch arguments is recommended but not required.

### Doom 3 with Resurrection of Evil

1. Get the latest pk4 of this mod.
2. Drop the pk4 in `<path to Doom 3>/d3xp`.
3. Use this launch parameter: `fs_game d3xp`.
4. (Optional but recommended) install [Arl's Improvements](https://www.moddb.com/mods/arls-improvements).

These steps are the same if you're using a compatible source port, such as [dhewm 3](https://dhewm3.org/).

Alternatively, you can place the files in a separate directory from d3xp and then use `set fs_game_base` with `set fs_game`, but this can cause game-breaking errors and is not supported.

### Configuration

The **autoexec.cfg** file included with this mod disables automatic weapon switching. Do not turn it back on or else you will have a bad time when you pick up your first grenades. Additionally, nightmare mode is allowed by default, and its health drain mechanic has been disabled.

For Doom 3 BFG Edition, many of the fancy new special effects have been disabled in order to make the game darker and more faithful to the original. Furthermore, the flashlight's battery drain mechanic has been disabled.

### Known Issues

#### Doom 3

#### dhewm 3

#### RBDOOM 3 BFG

* The game hangs if you equip the grabber on any non-RoE multiplayer maps. The grabber is not intended for multiplayer so this should not affect normal gameplay.

#### Classic RBDOOM 3 BFG

## Summary

### Weapons

Reloading, as a mechanic, has been completely eliminated from the game. Each weapon has a single ammunition counter; where applicable, on-weapon displays have been changed to reflect this.

Furthermore, ejected brass and other debris have been given a time-to-live of 1 hour. In practice you will probably never witness a bullet or shell disappear unless you really want to.

#### Flashlight

The original flashlight's light cone has received a dramatic upgrade. You will find that it illuminates the entire room in front of you (assuming you are in a room). Swinging it around also results in a slight aim kick.

The BFG flashlight no longer requires battery.

#### Fists

Fists have received a slight range boost. Also, punching has a small aim kick to grant it some illusion of weight and motion.

#### Chainsaw

The chainsaw has not received a gameplay update, apart from a little bit of recoil.

#### Pistol

The pistol has excellent accuracy when fired in a slow, controlled manner. However, it also has the ability to fire twice as quickly as before for a small accuracy penalty.

It has also been given some entirely new sound effects.

#### Shotgun

The shotgun's accuracy has been considerably increased, making it viable at medium range. It also fires slightly fewer pellets, because it really doesn't need them all anymore. The result of these changes is a shotgun that feels familiar to fans of classic Doom.

Also, one of the firing animations is no longer used because it's distractingly different from the other firing animations. This is the animation in which the shotgun points up in the air.

#### Super shotgun

The super shotgun can now be found in the base campaign. The earliest occurance is in the Enpro Plant, if you can find the code for a certain storage locker. Later on you can expect to find it out in the open in a few places, so don't stress out about missing it.

When you do grab it, you will find that its spread has been greatly improved. It's also the only weapon to retain a reloading animation. Its soft and gentle firing sound effect has been replaced though.

#### Machinegun

The machinegun now fires in rapid three-round bursts. The first burst is very accurate, but sustained fire will result in worse accuracy. Also, each bullet deals more damage than before and comes with a different, less plastic-y sound effect.

These changes are intended to make the machinegun feel like more of a companion to the shotgun. For comparison, the shotgun can deal a huge amount of burst damage in a short amount of time, but over longer periods of time the machinegun's DPS should be on top.

Overall, its performance is suspiciously similar to that of another rifle. Both rifles happen to be manufactured on Mars. Perhaps one is a cheap knockoff of the other?

#### Grenades

Grenades are now quick-throwable. Simply equipping them results in throwing a grenade and then immediately re-equipping whatever weapon you were holding previously.

Also, you can no longer cook grenades, but they also won't explode in your hand anymore, so it's a fair trade. Furthermore, their bounciness and friction have been drastically increased. This makes their trajectories much easier to predict, and it also prevents them from gliding around the floor like figure skaters.

You'll find that grenades are no longer part of the weapon-scrolling processession. This is to prevent you from scrolling through your weapons and inadvertently throwing a grenade in the middle of it. Also, the **default.cfg** included with this mod should disable automatic weapon switching; don't override this.

#### Chaingun

The chaingun spins up faster and has improved accuracy for the first few seconds of sustained fire. This allows for some mid to long-range sniping, although it's not quite as effective in this capacity as either the pistol or machinegun since, well, both of those exist too.

Damage has been decreased slightly to make way for the plasmagun. However, it now fires two shots at a time (when more than two rounds are available), just like the original.

Also, it's been given a more fitting set of firing sound effects.

#### Plasmagun

The plasmagun's projectiles now travel much faster and deal much more damage. Nothing else to say, it was already a very solid weapon.

#### Rocket launcher

The rocket launcher's projectiles travel faster now as well. They also have more recoil. All of this makes the weapon feel punchier. Despite this, rocket damage has been decreased a little.

#### BFG

No changes needed apart from the on-weapon GUI being updated. You also can't overcharge it anymore, i.e. you cannot blow yourself up with it.

#### PDA

Opening and closing the PDA is now instant.

#### Soul Cube and Artifact

Replaced in both campaigns with the grabber.

#### Grabber

Damage reduced for caught enemy projectiles.

### Pickups

All ammo pickup yields have been greatly diminished. Where applicable, these yields are consistent with the corresponding pickup models. For example, grenade pickup models consist of a pack of 4 grenades. So, as you would expect, picking one of these up adds exactly 4 grenades to your inventory.

Health and armor pickup yields are also considerably reduced. To put it into perspective, small medkits give you 5 HP and armor shards give you 1 AP.

### Player

Stamina has been removed from the game. No stamina meter will appear on your HUD. You can just run forever. Also, crouch-walking is a bit faster because crouching mostly takes place in air ducts and is pretty uneventful.

Ammo carry limits have been reduced significantly. They're now similar to classic Doom carry limits, except a little bit harsher because you can carry so many different ammo types.

Health drain has been removed entirely from Nightmare mode.

### Enemies

Just about every demon has received a considerable health buff. Where applicable, they have the same HP values as their classic Doom counterparts.

Furthermore, hit zones are now more diverse. Generally, arms and legs take less damage than torsos which take less damage than heads. The effect is either more or less pronounced depending on how armored or tough the body part looks.

Enemies no longer use their luxurious teleportation animations. This means that you can't just rush them with the shotgun while they're still getting ready.

Also, ragdolls will never disappear or burn up (except for when they come from infinite enemy spawners). Please enjoy using them as markers for which corridors you've already explored, or as trophies, or whatever.

#### Imp

Imps no longer constantly scream when using their ranged attacks. They also no longer make combat idle sounds. To compensate, they now have louder footsteps.

Also, their fireballs travel more quickly.

#### Pinky

Pinky demons have louder footsteps (they were so dainty before!) and somewhat reduced aim kick.

#### Trite

Trite melee attacks have a significantly reduced aim kick.

#### Wraith

Wraiths are able to cloak indefinitely. They can also continue moving while cloaking and decloaking. The overdramatic fireball effect has been removed from the cloaking process, so now they just burn away into nothing.

The result of this is that wraiths may cloak, cover the gap, and then decloak at an uncomfortably close range. Or they may cloak and then be gone for a while, only to suddenly surprise you.

#### Hellknight

Hellknights no longer constantly scream when using their ranged attacks. This has the effect of making them creepier and more intimidating.

#### Archvile

The archvile can now use its signature move: incinerate. Furthermore, its flamewall attack has received a huge speed boost. Generally, you can expect to see incinerate when you are either very far away from or very close to the archvile, and you will see flamewall if you're at close to medium range and there are no obstacles in the way.

Also, it powerwalks instead of ambling, just like in Doom 2.

#### Cyberdemon

The cyberdemon can be harmed by any weapon. Please enjoy shooting at him.

#### Zombie security

Zombie security ranged attacks have significantly reduced aim kick, because aim kick is annoying in hitscan battles.

All zombie security enemy types have the same total health. Different damage zones (e.g. legs, head, chest, arms) have different levels of damage resistence, based on how armored they look. Shields no longer completely block all damage.

Some of the more repetitive sounds (such as when spotting a player) see less frequently usage.

### Levels

Health station reserves have been drastically decreased in the base campaign.

Super shotguns can be found in various mid to late-game levels.

In the original Doom 3, there is now a level transition from the final level of the base campaign to the first level of the Resurrection of Evil campaign.

### Nightmare

The health drain mechanic has been removed. You will also not start with the soul cube because the soul cube is not equipable in this mod.

Enemies no longer use a 'reaction' animation when first seeing the player. Instead, they will begin attacking immediately.

Many enemy animations have been sped up. This means that they can walk, run, and attack faster. Imp, cacodemon, and hellknight fireballs are also faster.

## How to make your own mods for RBDOOM-3-BFG

1. Launch RBDoom3BFG.exe with the following launch argument: `+set com_allowconsole 1`
2. Press the `~` key and enter the following into the console: `exec extract_resources.cfg`
3. Wait a while. RBDOOM-3-BFG is extracting all of the game's resource files into *<path to Doom 3 BFG Edition>/basedev*
4. Read [Making a mod for RBDoom3BFG and Doom 3 BFG Hi Def](https://www.moddb.com/mods/doom-3-bfg-hi-def/tutorials/making-a-mod-for-rbdoom3bfg-and-doom-3-bfg-hi-def) by y2keeth

## Credits

The following modified assets by Mike Koenig as distributed by [SoundBible.com](http://soundbible.com/) are licensed under [Attribution 3.0](https://creativecommons.org/licenses/by/3.0/us/):

* [sound/custom/weapons/pistol/glock_01](http://soundbible.com/2123-40-Smith-Wesson-8x.html)
* [sound/custom/weapons/pistol/glock_02](http://soundbible.com/2123-40-Smith-Wesson-8x.html)
* [sound/custom/weapons/pistol/glock_03](http://soundbible.com/2123-40-Smith-Wesson-8x.html)
* [sound/custom/weapons/pistol/glock_04](http://soundbible.com/2123-40-Smith-Wesson-8x.html)
* [sound/custom/weapons/pistol/glock_05](http://soundbible.com/2123-40-Smith-Wesson-8x.html)
* [sound/custom/weapons/pistol/glock_06](http://soundbible.com/2123-40-Smith-Wesson-8x.html)
* [sound/custom/weapons/pistol/glock_07](http://soundbible.com/2123-40-Smith-Wesson-8x.html)
* [sound/custom/weapons/pistol/glock_08](http://soundbible.com/2123-40-Smith-Wesson-8x.html)
* [sound/custom/weapons/pistol/cocking](http://soundbible.com/1988-Gun-Cocking-Fast.html)

The following unmodified asset by Jim Rogers as distributed by [SoundBible.com](http://soundbible.com/) is licensed under [Attribution 3.0](https://creativecommons.org/licenses/by/3.0/us/):

* [sound/custom/weapons/ssg/blast.wav](http://soundbible.com/1919-Shotgun-Blast.html)

The following modified assets by an unidentified artist as distributed by [SoundBible.com](http://soundbible.com/) are licensed under [Attribution 3.0](https://creativecommons.org/licenses/by/3.0/us/):

* [sound/custom/weapons/chaingun/atchisson_01](http://soundbible.com/2021-Atchisson-Assault-Shotgun.html)
* [sound/custom/weapons/chaingun/atchisson_02](http://soundbible.com/2021-Atchisson-Assault-Shotgun.html)
* [sound/custom/weapons/chaingun/atchisson_03](http://soundbible.com/2021-Atchisson-Assault-Shotgun.html)
* [sound/custom/weapons/chaingun/atchisson_04](http://soundbible.com/2021-Atchisson-Assault-Shotgun.html)
* [sound/custom/weapons/chaingun/atchisson_05](http://soundbible.com/2021-Atchisson-Assault-Shotgun.html)
* [sound/custom/weapons/chaingun/atchisson_06](http://soundbible.com/2021-Atchisson-Assault-Shotgun.html)
* [sound/custom/weapons/chaingun/atchisson_07](http://soundbible.com/2021-Atchisson-Assault-Shotgun.html)
* [sound/custom/weapons/chaingun/atchisson_08](http://soundbible.com/2021-Atchisson-Assault-Shotgun.html)

The following modified assets by Mike Koenig as distributed by [SoundBible.com](http://soundbible.com/) are licensed under [Attribution 3.0](https://creativecommons.org/licenses/by/3.0/us/):

* [sound/custom/weapons/shotgun/barrett_01](http://soundbible.com/1880-416-Barrett-Sniper-3x.html)
* [sound/custom/weapons/shotgun/barrett_02](http://soundbible.com/1880-416-Barrett-Sniper-3x.html)
* [sound/custom/weapons/shotgun/barrett_03](http://soundbible.com/1880-416-Barrett-Sniper-3x.html)