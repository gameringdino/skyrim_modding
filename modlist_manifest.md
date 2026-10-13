# Skyrim JRPG MMO Modlist Blueprint

Welcome to the official documentation and master blueprint for our custom, high-end single-player MMO Skyrim modlist architecture.

## 🛠️ Environment & Core Specs
* **Operating System:** Kubuntu Linux
* **Graphics API / Hardware:** Vulkan via Proton on AMD Radeon RX 6700 XT
* **Game Version:** Skyrim Special Edition (SE 1.6.1170)
* **Mod Organizer:** MO2 via Proton
* **Estimated Scale:** ~750+ Mods | ~400+ Active Plugins (Optimized via ESP-FE / ESL conversion protocols)

---

## ⚡ Key Architectural Pillars

### 1. Stats, Levels & Combat
* **SSE Skill Uncapper:** Configured for **9,999 JRPG attribute caps** (Health, Magicka, Stamina) and expanded character leveling.
* **Combat Overhaul:** MCO/ADXP animation framework, Valhalla Combat, and TrueHUD integration.
* **Enemy Scaling:** *Dynamic Enhance Enemy Attributes* & *High Level Enemies (HLE)* for deep, end-game raid scaling.

### 2. Magic, Shouts & Faith
* **Shouts & Powers:** *Thunderchild* (Epic shouts & meditation) and *Dragon Soul Relinquishment* (convert surplus dragon souls into stat/perk points).
* **Perks & Magic:** *Ordinator - Perks of Skyrim*, *Odin*, *Apocalypse*, and *Triumvirate* class-specific spell archetypes.
* **Faith & Standing Stones:** *Wintersun - Faiths of Skyrim* and *Andromeda - Unique Standing Stones*.

### 3. Economy, Housing & Curation
* **Citadels & Fiefdoms:** *LC_Build Your Noble House*, *Sjel Blad Castle*, and *Windstad Mine*.
* **Museum Curation:** *Legacy of the Dragonborn (LotD)* with full cross-mod display patch integration.
* **Economy:** *Simple Banking*, *Economy Overhaul Speechcraft Improvement*, and *CFTO*.

### 4. Quests & Narrative Expansion
* **Main Quest Overhaul:** *At Your Own Pace*, *Cult of the World Eater* (Dragon Priest pre-requisites), and *World Eater Beater* (Multi-stage raid boss).
* **Immersion Suite:** JaySerpa's complete quest and dialogue expansion series, *Take Notes* journal system, and *Shadow of Skyrim* nemesis mechanics.

---

## 📂 Master Blueprint Structure
The complete modular build order spans 29 core categories—from core stability DLLs (*SSE Engine Fixes*, *Crash Logger*) and mesh frameworks (*SMIM*, *Community Shaders*) to dynamic NPC racial distribution (*Diverse Skyrim*, *Race Distribution Framework*).