# Roo Code Master Workspace Instructions: Skyrim JRPG MMO Modlist

## 🛠️ Environment & System Architecture
* **Operating System:** Kubuntu Linux
* **Graphics API & Hardware:** Vulkan via Proton on AMD Radeon RX 6700 XT GPU
* **Workspace Directory:** `/run/media/timothy/5b91fdfe-bc58-477e-9bc4-bae46ef82aa2/skyrim_modding`
* **Game Version:** Skyrim Special Edition (SE 1.6.1170)
* **Mod Manager:** Mod Organizer 2 (MO2) running in Portable Mode via Proton
* **Scale & Scope:** ~750 to 850 total physical mods, ~380 to 450 active plugins.
* **Plugin Optimization:** Strictly utilizes **ESP-FE / ESL conversion protocols** via xEdit (`-pseudoesl`) to keep active master/plugin count under the 254 hard engine limit while supporting 4,000+ light plugins.

---

## ⚡ Core Design Pillars & Absolute Rules
1. **Zero Survival Micromanagement:** Absolutely no hunger, thirst, sleep, or cold/survival meters. Food and culinary items are exclusively used for **JRPG-style temporary combat buffs** (`Gourmet` overhaul).
2. **JRPG Stat Scale:** SSE Skill Uncapper configured for **9,999 maximum attribute caps** (Health, Magicka, Stamina) and expanded character leveling.
3. **Immersive Roleplaying & Agency:** Fully choice-driven main quests, zero forced quest injections (`The Choice is Yours`), and dynamic nemesis/consequence systems (`Shadow of Skyrim`).

---

## 📦 Complete Mod Ecosystem Breakdown

### 1. Engine, Stability & Bug Fixes
* SSE Engine Fixes (Parts 1 & 2), Crash Logger SSE, powerof3's Tweaks, Scrambled Bugs, Bug Fixes SSE.
* Animation Queue Fix (for OAR/MCO), Papyrus Tweaks NG, Modern Brawl Bug Fix, Dual Casting Fix, Equip Enchantment Fix.
* Unofficial Skyrim Special Edition Patch (USSEP) & Unofficial Skyrim Modder's Patch (USMP SE).

### 2. Combat, Animation & UI Frameworks
* Project New Reign - Nemesis, Open Animation Replacer (OAR), MCO/ADXP directional melee combat.
* Valhalla Combat (stamina, execution kills, timed blocks), TrueHUD, Wheeler Quick Action Menu.

### 3. Character Creation, Races & RPG Classes
* Character Creation Overhaul (CCO) for classic major skills and preset classes.
* Imperious - Races of Skyrim (deep mechanical passives and quests).
* Extended Lineages: Lost Races of Aetherius (Maormer, Chimer, Falmer), Lore-Friendly Custom Races, Playable Dremora.
* NPC Diversity: Diverse Skyrim SSE & Race Distribution Framework (RDF).
* Aesthetics: High Poly Head, CBBE 3BA, HIMBO, Expressive Facial Animation, Tempered Skins, Nordic Faces.

### 4. Stats, Scaling & Encounter Balance
* Arena (Encounter Zone Overhaul), High Level Enemies (HLE), Dynamic Enhance Enemy Attributes (JRPG global stat scaling).

### 5. Perks, Magic, Shouts & Faith
* Ordinator - Perks of Skyrim, Odin, Apocalypse, Triumvirate (class spell packs).
* Thunderchild (epic shouts & meditation) & Dragon Soul Relinquishment (convert dragon souls to stats/perks).
* Andromeda Unique Standing Stones & Wintersun Faiths of Skyrim.
* Sacrosanct (Vampires) & Growl (Werebeasts).

### 6. Quests, Main Campaign & World-Eater Overhaul
* At Your Own Pace (Main Quest, Guilds, Civil War) & The Paarthurnax Dilemma.
* Cult of the World Eater (Dragon Priest pre-requisites to strip Alduin's buffs) & World Eater Beater (multi-stage cinematic raid boss).
* JaySerpa's Quest & Dialogue Expansion Suite.
* Massive Campaign Modbase: Vigilant, Glenmoril, Unslaad, Beyond Reach, Wyrmstooth, Beyond Bruma, Wheels of Lull, Gray Cowl, Lordbound, Helgen Reborn.

### 7. Companions, Relationships & Social Dynamics
* Nether's Follower Framework (NFF), Relationship Dialogue Overhaul (RDO), Skyrim Reputation.
* Fully Voiced Custom Companions: Serana Dialogue Add-On (SDA), Lucien, Inigo, Remiel, Auri.
* Multiple Marriages - To Have and To Hold.

### 8. Housing, Fiefdoms & Museum Curation
* LC_Build Your Noble House (fiefdom), Sjel Blad Castle (citadel), Windstad Mine.
* Legacy of the Dragonborn (LotD) with complete cross-mod display patch integration.

### 9. Economy, Travel & Crafting
* Simple Banking, Economy Overhaul Speechcraft Improvement (EOSI), Carriage and Ferry Travel Overhaul (CFTO).
* CCOR, Ars Metallica, Gourmet (Culinary Combat Buffs).

### 10. Meshes, Shaders, Water, Weather, Roads, Forests & LODs
* SMIM, Community Shaders (Vulkan-native Kubuntu pipeline), Azurite Weathers II, EVLaS.
* Water for ENB (Standalone) & Splashes of Skyrim.
* Blended Roads, Lux Via, Happy Little Trees, Cathedral Grass, Landscape Fixes For Grass Mods.
* LOD Pipeline: xLODGen (Terrain), TexGen 3, and DynDOLOD 3 (Objects/Trees).
