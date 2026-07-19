# 🌿 ORBIS UNDERGROUND — Ultimative Projekt-Bibel & Mod-Kontext

**Version:** 1.0.0 | **Lizenz:** MIT | **Spiel:** Hytale (Early Access)
**Status:** In Entwicklung (Code- & Asset-Generierung durch KI)

---

## 1. VISION & KERNKONZEPT
"Orbis Underground" ist eine umfassende, realistische Drogen-Mod für Hytale. Sie fügt dem Spiel den kompletten Zyklus hinzu: Wildwachsende Pflanzen, Anbau, botanische Verarbeitung, chemische Synthese, Konsum, Status-Effekte (mit Crash-Mechaniken) und eine Schwarzmarkt-Wirtschaft. 

- **Kein Sucht-System:** Die Mod nutzt vorerst nur positive Effekte (Buffs) und negative Crash-Effekte (Debuffs) nach Ablauf der Dauer. 
- **Überdosis:** Wird in Phase 3 hinzugefügt (Tod bei >3 Dosen in 60s, heilbar durch Naloxon).
- **Währung:** `Essence of Shadow` (lila Farbvariante der vanilla Essence of Life).
- **Dealer:** Kweebeck-Dealer (50% Spawn-Chance in Kweebec-Dörfern Zone 1).

---

## 2. DESIGN-PHILOSOPHIE & ASSET-STRATEGIE (CRITICAL FOR AI)
Der Nutzer kann **NICHT** manuell designen oder modellieren. Die KI muss folgende Prioritätenreihenfolge bei der Asset-Erstellung strikt einhalten, um manuelle Arbeit zu vermeiden:

1. **Custom 3D-Modelle per Code generieren:** Die KI muss die Custom-Blöcke (Werkbänke) direkt als Blockbench-JSON `.bbmodel` oder Hytale-Block-JSON per Code generieren.
   - *Botanischer Tisch:* Simple Holztisch mit Mörser und Trockengestell (von Grund auf neu als JSON code).
   - *Chemie-Labor:* Vanilla Alchemist's Workbench JSON kopieren und Textur-Referenzen umfärben (z.B. violettes Glas, dunkleres Holz).
2. **Vanilla-Texturen programmatisch umfärben:** Python/PIL-Skripte nutzen.
   - `essence_of_life.png` (grün) → `essence_shadow.png` (lila, Hue +180°).
   - `empty_potion_bottle.png` → Ethanol (klar), Schwefelsäure (gelb), Salzsäure (grün), Ammoniak (weiß-trüb), Ether (blau), Morphium (weiß), etc.
   - `tree_sap.png` → Rohopium (dunkelbraun), Haschisch (dunkler), Coca-Paste (gräulich-weiß).
   - `charcoal.png` → Pilzpulver (braun-grau), Kokain (rein weiß), Heroin (weiß-braun), Lithium-Pulver (silbrig).
   - `plant_fiber.png` → Papier (weiß), Filterpapier (grau), Coca-Blätter (dunkelgrün), Khat-Blätter (hellgrün).
   - `wheat_seed_bag.png` → Alle neuen Samen-Tüten (verschiedene Farben pro Pflanze).
3. **Vanilla-Pflanzen als Drogen direkt nutzen:** Keine neuen Texturen für diese Pilze/Pflanzen!
   - `Blue Glowing Mushroom` = Psilocybin
   - `Bloodcap Mushroom` = Amanita muscaria
   - `Stormcap Mushroom` = Stimulans (Khat-Substitut)
   - `Storm Thistle` = Opiat-Vorstufe
   - `Blood Rose` = Coca-Blatt-Substitut
   - `Azure Kelp` = Kava
   - `Azurecap Mushroom` = Sedativum
4. **Get-Hy Assets übernehmen (MIT-Lizenz):** Die MIT-lizenzierte Mod "Get Hy!" liefert fertige Assets, die kopiert werden müssen:
   - 3 Cannabis-Modelle (Sativa/Indica/Hybrid in 3 Stadien)
   - 5 Joint-Varianten (Spliff/Joint/Cone/Twax/Blunt)
   - 5-Tier-System (Junk/Street/Dispensary/Exotic/God) für Cannabis Buds.
5. **AI-Pixel-Art-Generierung:** Für verbleibende 16x16 Icons (PixExact/Retro Diffusion) nutzt die KI folgende Prompts:
   - "dried cannabis bud green brown trichome crystals pixel art 16x16 Hytale style"
   - "poppy seed pod green crown pixel art 16x16 Hytale style"
   - "crack rocks white yellow small pixel art 16x16"
   - "MDMA pill colorful round pixel art 16x16 Hytale style"
   - "peyote cactus bud grey green small pixel art 16x16"
   - "glass syringe needle pixel art 16x16 Hytale style"
   - "betel nut brown oval pixel art 16x16"

---

## 3. ARCHITEKTUR & WERKBANK-ROUTING
Die Mod nutzt **ZWEI eigene Custom-Werkbänke** sowie spezifische vanilla Werkbänke.

### Custom Block 1: Botanischer Tisch (`orbis_underground:bench_botany`)
- **Funktion:** Trocknen, Mahlen, Pressen, Joints drehen, Pillen pressen, pflanzliche Extraktion.
- **Tier-System:** Tier 1 (Bau) & Tier 2 (Upgrade für komplexe Extrakte wie Scopolamin).

### Custom Block 2: Chemie-Labor (`orbis_underground:bench_chemistry`)
- **Funktion:** Alle chemischen Synthesen, Destillationen, Raffinationen.
- **Tier-System:** Tier 1 (Bau) & Tier 2 (Upgrade für harte Drogen wie Heroin, Meth, LSD). 
- **Meth-Explosion:** Methamphetamin hat 20% Explosions-Chance bei Herstellung (benötigt Java-Plugin-Snippet für `ItemCraftedEvent`, da JSON keine Zufallsereignisse unterstützt!).

### Vanilla Werkbänke (Zusätzlich genutzt)
- **Farmer's Workbench (`Bench_Farming`):** Zum Craften aller Samen (Tier 2 bis 4).
- **Chef's Stove (`Bench_Cooking`):** Für Ethanol-Fermentation, Koka-Tee, Cannabis-Butter (Edibles).
- **Salvager's Workbench (`Bench_Salvage`):** Für grobes Zerkleinern (Lithium-Pulver, Ephedrin).

---

## 4. DAS COMPLETE CRAFTING-REZEPTEBUCH

### 🔨 Salvager's Workbench (Mahlen & Trocknen)
| Output | Input | Zeit |
|---|---|---|
| Lithium Powder | 1× Iron Ingot + 1× Charcoal | 10s |
| Ephedrine Powder | 4× Ephedra Stem + 1× Plant Fiber | 10s |

### 🌿 Botanischer Tisch (`orbis_underground:bench_botany`)
| Output | Input | Zeit | Tier |
|---|---|---|---|
| Dried Cannabis | 1× Cannabis Bud + 1× Plant Fiber | 6s | T1 |
| Mushroom Powder | 1× Blue Glowing Mushroom | 4s | T1 |
| Amanita Powder | 1× Bloodcap Mushroom | 4s | T1 |
| Poppy Pods (×2) | 1× Poppy Flower | 4s | T1 |
| Paper | 3× Plant Fiber + 1× Tree Sap | 4s | T1 |
| Filter Paper | 2× Plant Fiber + 1× Charcoal | 5s | T1 |
| Hashish | 4× Dried Cannabis + 1× Tree Sap | 10s | T1 |
| Joint | 1× Dried Cannabis + 1× Paper | 3s | T1 |
| Blunt | 2× Dried Cannabis + 1× Paper | 4s | T1 |
| Spliff | 1× Dried Cannabis + 1× Paper | 3s | T1 |
| Psilocybin Tincture | 3× Mushroom Powder + Bottle + Sap | 10s | T1 |
| Raw Opium | 3× Poppy Pods | 8s | T1 |
| Coca Leaves | 1× Coca Bush | 4s | T1 |
| Peyote Bud | 1× Peyote Cactus | 5s | T1 |
| Khat Leaves | 1× Khat Bush | 3s | T1 |
| Empty Syringe | 1× Bottle + 1× Iron Ingot + Linen Scraps | 8s | T1 |
| Filled Syringe | 1× Empty Syringe + 1× Heroin | 4s | T1 |
| Kava Paste | 2× Kava Root + 1× Tree Sap | 8s | T1 |
| Coca Paste | 5× Coca Leaves + Sap + Fiber | 12s | T2 |
| Mescaline Extract | 3× Peyote Bud + Bottle | 15s | T2 |
| Scopolamine | 3× Datura Leaves + Venom Sac + Bottle | 14s | T2 |
| Salvinorin | 3× Salvia Leaves + Bottle | 12s | T2 |
| Ibogaine Extract | 3× Iboga Root + Bottle + Charcoal | 18s | T2 |
| MDMA Pill | 1× MDMA Powder + Pill Press + Fiber | 8s | T2 |
| LSD Tab | 1× Lysergic Acid + Motes of Light + Paper + Void | 22s | T2 |

### ⚗️ Chemie-Labor (`orbis_underground:bench_chemistry`)
| Output | Input | Zeit | Tier |
|---|---|---|---|
| Sulfuric Acid | 2× Charcoal + Bottle + Essence of Fire | 16s | T1 |
| HCl | Bone Fragment + Sulfuric Acid + Bottle | 14s | T1 |
| Ammonia | 3× Bone Fragments + Bottle + Essence of Water | 14s | T1 |
| Acetone | 2× Tree Sap + Charcoal + Bottle | 14s | T1 |
| Ether | 1× Ethanol + Sulfuric Acid + Bottle | 18s | T1 |
| Morphine | 2× Raw Opium + Sulfuric Acid + Charcoal + Bottle | 20s | T1 |
| Cocaine | 2× Coca Paste + Sulfuric Acid + Filter Paper | 22s | T1 |
| Crack | 1× Cocaine + 1× Ammonia | 10s | T1 |
| Heroin | 1× Morphine + Acetone + Bottle | 24s | T2 |
| Meth ⚠️ | Ephedrine + Lithium + Ammonia + Ether | 30s | T2 |
| MDMA Powder | Motes of Light + Sulfuric Acid + Acetone | 26s | T2 |
| Lysergic Acid | 2× Ergot (Mutterkorn) + Bottle + Essence of Void | 28s | T2 |
| Naloxone | Morphine + HCl + Charcoal + Bottle | 18s | T2 |

### 🍳 Chef's Stove (`Bench_Cooking`)
| Output | Input | Zeit |
|---|---|---|
| Ethanol | 2× Wheat + Wild Berries + Bottle | 12s |
| Coca Tea | 1× Coca Leaves + Bottle | 5s |
| Cannabis Butter | 1× Dried Cannabis + 1× Dough | 8s |

### 🌱 Farmer's Workbench (`Bench_Farming`)
| Seed | Input | Tier |
|---|---|---|
| Cannabis Sativa | 2× Essence of Shadow + 1× Dried Cannabis | T2 |
| Cannabis Indica | 2× Essence of Shadow + 1× Dried Cannabis | T2 |
| Cannabis Hybrid | 3× Essence of Shadow + 1× Dried Cannabis + Fiber | T3 |
| Poppy | 1× Essence of Shadow + 1× Poppy Pod | T2 |
| Coca | 2× Essence of Shadow + 3× Coca Leaves | T3 |
| Peyote | 2× Essence of Shadow + 1× Peyote Bud | T3 |
| Khat | 2× Essence of Shadow + 2× Khat Leaves | T2 |
| Datura | 2× Essence of Shadow + 2× Datura Leaves | T2 |
| Salvia | 2× Essence of Shadow + 2× Salvia Leaves | T2 |
| Iboga | 3× Essence of Shadow + 1× Iboga Root | T4 |
| Ephedra | 2× Essence of Shadow + 2× Ephedra Stem | T3 |
| Betel | 2× Essence of Shadow + 1× Betel Nut | T3 |

---

## 5. ENTITY EFFECTS MATRIX (26 Effekte)
*Crash-Effekte werden als eigene Debuff-Effekte angelegt und nach Ablauf des Haupteffekts ausgelöst.*

| Effekt-ID | Dauer | Haupteffekt (Buffs) | Crash/Nebenwirkung |
|---|---|---|---|
| `drug_cannabis_sativa` | 120s | +15% Speed, HP-Regen | Keiner |
| `drug_cannabis_indica` | 180s | -15% Speed, +50% HP-Reg | Keiner |
| `drug_hashish` | 180s | Indica ×1.5 | Keiner |
| `drug_psilocybin` | 240s | Wahrnehmungsverschiebung | Keiner |
| `drug_amanita` | 180s | +10% Stärke | 1 DPS Übelkeit (15s) |
| `drug_cocaine` | 90s | +40% Speed, +30% Resist | -30% Speed (120s) |
| `drug_crack` | 30s | Kokain ×2 | -50% Speed, -10% HP |
| `drug_morphine` | 300s | +50% Resist | 1 DPS Atemdepression |
| `drug_heroin` | 480s | +70% Resist, langsam | 3 DPS Atemdepression |
| `drug_meth` | 600s | +30% Speed, +50% Mining | HP-Reg blockiert (10m) |
| `drug_mdma` | 300s | +20% Stärke, HP-Reg | Depression (24h!) |
| `drug_mescaline` | 600s | Wahrnehmung | 2 DPS Übelkeit (30s) |
| `drug_scopolamine` | 300s | Delirium, Fake-Mobs | 3 DPS Verwirrung |
| `drug_salvinorin` | 90s | Extreme Wahrnehmung | Keiner |
| `drug_khat` | 180s | +10% Speed | Keiner |
| `drug_ibogaine` | 1800s | Entfernt ALLE Drogeneffekte | Ataxie |
| `drug_lsd` | 720s | Texturen vertauscht, Himmel verzerrt | Keiner |
| `drug_kava` | 240s | -10% Speed, Anti-Angst | Keiner |
| `drug_overdose` | 60s | Lähmung, 10 DPS | TOD |

---

## 6. WELT-GENERATION & LOOT
### Pflanzen-Spawns
| Pflanze | Zone | Biom | Seltenheit |
|---|---|---|---|
| Cannabis Sativa | Z1 | Seeding Woods (Waldrand) | Selten |
| Cannabis Indica | Z1 | Drifting Plains | Selten |
| Cannabis Hybrid | Z1 | Seeding Woods | Sehr selten |
| Schlafmohn | Z1, Z3 | Plains | Mittel |
| Coca-Strauch | Z4 | Underground Jungle | Gelegentlich |
| Peyote | Z2 | Savanna | Selten |
| Khat | Z2 | Oasis | Mittel |
| Datura | Z1, Z2 | Nahe Ruinen | Gelegentlich |
| Salvia | Z1 | The Fens (Sumpf) | Gelegentlich |
| Iboga | Z4 | Underground Jungle | Selten |
| Ephedra | Z2, Z3 | Rocky Hills | Gelegentlich |
| Betel-Palme | Z2 | Oasis | Selten |
| Kava | Z1 | The Fens | Gelegentlich |

### Loot-Tables
- **Schmugglerversteck 1 (Trork Camp):** Cannabis-Seeds, Essence of Shadow (5-15), Boom Powder, Paper, Dried Cannabis, Poppy Seeds.
- **Schmugglerlabor 2 (Emerald Grove Ruins):** Ether, Sulfuric Acid, Empty Bottles, Motes of Light, Essence of Shadow (10-25), Coca Paste, Acetone, Filter Paper, Lithium Powder.

---

## 7. DEALER / NPC
- **Modell:** Vanilla Kweebec, Blätter-Textur dunkler abgefärbt (Hue-Shift).
- **Spawn-Logik:** 50% Wahrscheinlichkeit pro Kweebec-Dorf in Zone 1.
- **Währung:** `orbis_underground:essence_shadow`.
- **Kauft:** Dried Cannabis (3), Hashish (8), Raw Opium (12), Mushroom Powder (6), Joints (5), Blunts (7).
- **Verkauft:** Sativa Seeds (3), Indica Seeds (4), Poppy Seeds (4), Empty Bottles (2), Paper (1).

---

## 8. TECHNISCHE HYTALE-STANDARDS (Zwingend für Code-Output)
1. **Konsumierbare Items:** MÜSSEN zwingend enthalten:
   ```json
   "Interactions": { "Secondary": "Root_Secondary_Consume_Potion" },
   "InteractionVars": { "Effect": { "Interactions": [{ "Type": "ApplyEffect", "EffectId": "XYZ", "Duration": 120.0 }] } }
   ```
   *(Hinweis: Konsum funktioniert NUR im Adventure-Mode!)*
2. **Rezept-Struktur:** In Item-JSONs unter `"Recipe"` mit `"Input"`, `"Output"`, `"CraftingBench"` (exakte IDs!), `"TimeSeconds"`.
3. **Ordnerstruktur:** 
   - `Server/Item/Items/orbis_underground/` (Item JSONs)
   - `Server/Assets/EntityEffect/` (Effekt JSONs)
   - `Common/Icons/ItemsGenerated/` (Texturen)
   - `Common/Models/` (3D Modelle `.bbmodel`)
4. **Sprachdateien:** `Server/Languages/en-US/server.lang` und `de-DE/server.lang`. Alle 15 Cannabis-Bud-Tiers brauchen Namen (z.B. "Sativa Bud (Junk)").
```

Diese Datei ist jetzt der ultimative Masterplan. Sie enthält jedes Detail, das wir besprochen haben. Wenn du diese Datei hochlädst, hat die KI sofort den vollständigen Überblick!
