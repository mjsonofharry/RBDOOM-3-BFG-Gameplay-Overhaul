# RBDOOM-3-BFG-Gameplay-Overhaul

## 1 Introduction

RBDOOM-3-BFG-Gameplay-Overhaul is a mod for [RBDOOM-3-BFG](https://github.com/RobertBeckebans/RBDOOM-3-BFG/releases) and [Classic-RBDOOM-3-BFG](https://github.com/MadDeCoDeR/Classic-RBDOOM-3-BFG/releases). Some highlights include:

* No reloading
* Unlimited sprinting
* Better weapons
* Less ammo, health, and armor
* More challenging enemies
* Super shotgun
* Persistent ragdolls and ejected brass

## 2 Installation

1. Get [RBDOOM-3-BFG](https://github.com/RobertBeckebans/RBDOOM-3-BFG/releases) or [Classic-RBDOOM-3-BFG](https://github.com/MadDeCoDeR/Classic-RBDOOM-3-BFG/releases).
2. Get the [latest release](https://github.com/mjsonofharry/RBDOOM-3-BFG-Gameplay-Overhaul/releases/latest) of this mod.
3. Move the mod files to *<path to Doom 3 BFG Edition>/RBDOOM-3-BFG-Gameplay-Overhaul/*.
4. Create a shortcut to *<path to Doom 3 BFG Edition>/RBDoom3BFG.exe* with the following launch parameters: `+set fs_game RBDOOM-3-BFG-Gameplay-Overhaul +set fs_resourceLoadPriority 0`

Some changes will not work correctly when applied to pre-existing saves. Also, if you're using **Classic-RBDOOM-3-BFG**, adding `+set flashlight_old 1` to your launch arguments is recommended but not required.

## 3 Summary

### 3.1 Weapons

Reloading, as a mechanic, has been completely eliminated from the game. Each weapon has a single ammunition counter; where applicable, on-weapon displays have been changed to reflect this.

Furthermore, ejected brass and other debris have been given a time-to-live of 1 hour. In practice you will probably never witness a bullet or shell disappear unless you really want to.

#### 3.1.1 Flashlight

The flashlight's light cone has received a dramatic upgrade. You will find that it illuminates the entire room in front of you (assuming you are in a room). Swinging it around also results in a slight aim kick.

#### 3.1.2 Fists

Fists have received a slight range boost. Also, punching has a small aim kick to grant it some illusion of weight and motion.

#### 3.1.3 Chainsaw

The chainsaw has not received a gameplay update, apart from a little bit of recoil.

#### 3.1.4 Pistol

The pistol has excellent accuracy when fired in a slow, controlled manner. However, it also has the ability to fire twice as quickly as before for a small accuracy penalty.

#### 3.1.5 Shotgun

The shotgun's accuracy has been considerably increased, making it viable at medium range. It also fires slightly fewer pellets, because it really doesn't need them all anymore. The result of these changes is a shotgun that feels familiar to fans of classic Doom.

Also, one of the firing animations is no longer used because it's distractingly different from the other firing animations. This is the animation in which the shotgun points up in the air.

#### 3.1.6 Machinegun

The machinegun now fires in accurate, three-round bursts. Its damage has received a buff.

Overall, its performance is suspiciously similar to that of another rifle. Both rifles happen to be manufactured on Mars. Perhaps one is a cheap knockoff of the other?

#### 3.1.7 Grenades

Grenades are now quick-throwable. Simply equipping them results in throwing a grenade and then immediately re-equipping whatever weapon you were holding previously.

Also, you can no longer cook grenades, but they also won't explode in your hand anymore, so it's a fair trade. Furthermore, their bounciness and friction have been drastically increased. This makes their trajectories much easier to predict, and it also prevents them from gliding around the floor like figure skaters.

You'll find that grenades are no longer part of the weapon-scrolling processession. This is to prevent you from scrolling through your weapons and inadvertently throwing a grenade in the middle of it. Also, the **default.cfg** included with this mod should disable automatic weapon switching; don't override this.

#### 3.1.8 Chaingun

The chaingun spins up faster and has improved accuracy for the first few seconds of sustained fire. This allows for some mid to long-range sniping, although it's not quite as effective in this capacity as either the pistol or machinegun since, well, both of those exist too.

Damage has been decreased slightly to make way for the plasmagun.

#### 3.1.9 Plasmagun

The plasmagun's projectiles now travel much faster and deal much more damage. Nothing else to say, it was already a very solid weapon.

#### 3.1.10 Rocket launcher

The rocket launcher's projectiles travel faster now as well. They also have more recoil. All of this makes the weapon feel punchier.

#### 3.1.11 BFG

No changes needed apart from the on-weapon GUI being updated. You also can't overcharge it anymore, i.e. you cannot blow yourself up with it.

#### 3.1.12 Super shotgun

Most importantly, the super shotgun can now be found in the base campaign. The earliest occurance is in the Enpro Plant, if you can find the code for a certain storage locker. Later on you can expect to find it out in the open in a few places, so don't stress out about missing it.

When you do grab it, you will find that its spread has been greatly improved. It's also the only weapon to retain a reloading animation.

### 3.2 Pickups

All ammo pickup yields have been greatly diminished. Where applicable, these yields are consistent with the corresponding pickup models. For example, grenade pickup models consist of a pack of 4 grenades. So, as you would expect, picking one of these up adds exactly 4 grenades to your inventory.

Health and armor pickup yields are also considerably reduced. To put it into perspective, small medkits give you 5 HP and armor shards give you 1 AP.

### 3.3 Player

Stamina has been removed from the game. No stamina meter will appear on your HUD. You can just run forever. Also, crouch-walking is a bit faster because crouching mostly takes place in air ducts and is pretty uneventful.

Ammo carry limits have been reduced significantly. They're now similar to classic Doom carry limits, except a little bit harsher because you can carry so many different ammo types.

### 3.4 Enemies

Just about every demon has received a considerable health buff. Where applicable, they have the same HP values as their classic Doom counterparts.

Furthermore, hit zones are now more diverse. Generally, arms and legs take less damage than torsos which take less damage than heads. The effect is either more or less pronounced depending on how armored or tough the body part looks.

Also, ragdolls will never disappear or burn up. Please enjoy using them as markers for which corridors you've already explored, or as trophies, or whatever.

#### 3.4.1 Imp

Imps no longer constantly scream when using their ranged attacks. They also no longer make combat idle sounds. To compensate, they now have louder footsteps.

Also, their fireballs travel more quickly.

#### 3.4.2 Pinky

Pinky demons have louder footsteps (they were so dainty before!) and somewhat reduced aim kick.

#### 3.4.3 Trite

Trite melee attacks have a significantly reduced aim kick.

#### 3.4.4 Wraith

Wraiths are able to cloak indefinitely. They can also continue moving while cloaking and decloaking. The overdramatic fireball effect has been removed from the cloaking process, so now they just burn away into nothing.

The result of this is that wraiths may cloak, cover the gap, and then decloak at an uncomfortably close range. Or they may cloak and then be gone for a while, only to suddenly surprise you.

#### 3.4.5 Hellknight

Hellknights no longer constantly scream when using their ranged attacks. This has the effect of making them creepier and more intimidating.

#### 3.4.6 Archvile

The archvile can now use its signature move: incinerate. Furthermore, its flamewall attack has received a huge speed boost.

Generally, you can expect to see incinerate when you are either very far away from or very close to the archvile, and you will see flamewall if you're at close to medium range and there are no obstacles in the way.

#### 3.4.7 Zombie security

Zombie security ranged attacks have significantly reduced aim kick, because aim kick is annoying in hitscan battles.

Shields no longer completely block all damage.

Some of the more repetitive sounds (such as when spotting a player) see less frequently usage.

## 3.5 Levels

Health station reserves have been drastically decreased in the base campaign.

Super shotguns can be found in various mid to late-game levels.

### 4 Configuration

The **default.cfg** file included with this mod will select Doom 3 and skip intro videos at launch. During gameplay, many of the fancy _new_ rendering effects have been disabled in order to make the BFG Edition darker and more faithful to the visual style of the original. Lastly, autoswitching is disabled; do not override this or else you wil throw your first grenade at the wall. Then it will bounce off the wall and land at your feet, and you will probably feel sorry about the whole situation.

## 5 How to make your own mods for RBDOOM-3-BFG

1. Launch RBDoom3BFG.exe with the following launch argument: `+set com_allowconsole 1`
2. Press the `~` key and enter the following into the console: `exec extract_resources.cfg`
3. Wait a while. RBDOOM-3-BFG is extracting all of the game's resource files into *<path to Doom 3 BFG Edition>/basedev*
5. Read [Making a mod for RBDoom3BFG and Doom 3 BFG Hi Def](https://www.moddb.com/mods/doom-3-bfg-hi-def/tutorials/making-a-mod-for-rbdoom3bfg-and-doom-3-bfg-hi-def) by y2keeth
