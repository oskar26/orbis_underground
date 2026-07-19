# 🌿 Orbis Underground — Hytale Drogen-Mod

**Version 1.0.0 | Lizenz: MIT | Alle 3 Phasen implementiert**

> Eine umfassende Drogen-Mod für Hytale mit realistischen Crafting-Ketten, 26 Status-Effekten und einem Kweebeck-Dealer-Handelssystem. **Nutzt NUR Vanilla-Werkbänke — kein einziger Custom-Block nötig.**

---

## 📋 Schnellübersicht

| Phase | Name | Drogen | Effekte |
|---|---|---|---|
| **1.0** | Green Harvest | Cannabis (3 Sorten), Haschisch, Psilocybin, Amanita, Rohopium | 6 |
| **2.0** | Hard Stuff | Kokain, Crack, Morphium, Heroin, Meth, MDMA, Meskalin, Scopolamin, Salvinorin, Khat | 15 |
| **3.0** | Full Trip | Ibogain, Ephedrin, Betel, Kava, LSD, Überdosis | 6 |

**79 Items | 26 EntityEffects | 2 NPCs | 2 Loot-Tables | EN + DE Übersetzungen**

---

## 🏗️ ARCHITEKTUR: Plan B — Keine Custom-Werkbank!

Der ursprüngliche Plan sah einen "Botanischen Tisch" als Custom-Block vor. **Das wurde komplett gestrichen.** Die Mod nutzt ausschließlich diese Vanilla-Werkbänke:

| Werkbank | Bench ID | Verwendung in der Mod |
|---|---|---|
| **Salvager's Workbench** | `Salvagebench` | Cannabis trocknen, Pilze mahlen, Mohnkapseln zerkleinern, Lithium-Pulver |
| **Alchemist's Workbench** | `Alchemybench` | ALLE Extraktionen & Synthesen: Tinkturen, Kokain, Heroin, Meth (T2!), LSD, Chemikalien |
| **Basic Workbench** | `Workbench` | Joints/Blunts drehen, Haschisch pressen, Papier herstellen, MDMA-Pillen pressen |
| **Chef's Stove** | `Cookingbench` | Ethanol fermentieren, Coca-Tee kochen, Cannabis-Butter backen |
| **Farmer's Workbench** | `Farmingbench` | ALLE Samen craften (Tier 2-4 je nach Seltenheit) |

---

## 📁 INSTALLATION — Schritt für Schritt

### Schritt 1: Mod-Ordner platzieren
```
Kopiere den GESAMTEN Ordner "orbis_underground/" nach:
  %APPDATA%\Roaming\Hytale\UserData\Packs\orbis_underground\

Der Pfad sollte danach so aussehen:
  %APPDATA%\Roaming\Hytale\UserData\Packs\orbis_underground\
    ├── manifest.json
    ├── Common\
    │   ├── Icons\ItemsGenerated\   ← Hier kommen deine Texturen rein
    │   ├── Icons\ItemCategories\   ← Kategorie-Icons
    │   └── Models\                  ← 3D-Modelle
    └── Server\
        ├── Item\Items\orbis_underground\  ← 79 Item-JSONs
        ├── Assets\EntityEffect\           ← 26 Effekte
        ├── NPC\Roles\                     ← Kweebeck Dealer
        ├── Languages\en-US\server.lang    ← Englische Texte
        └── Languages\de-DE\server.lang    ← Deutsche Texte
```

### Schritt 2: Texturen generieren (MUST DO!)
Die Mod hat **noch keine Texturen** — du musst sie erzeugen. Drei Wege:

#### Weg A: Vanilla-Texturen umfärben (Python-Script)
```bash
# 1. Extrahiere Hytales Assets.zip (findest du im Spielverzeichnis)
# 2. Kopiere die relevanten Texturen in scripts/vanilla_textures/
# 3. Führe das Script aus:
cd scripts
pip install Pillow
python recolor.py ../vanilla_textures/
```

#### Weg B: Get Hy! Assets übernehmen (Empfohlen für Cannabis)
```bash
# Die Get Hy! Mod (MIT-lizenziert) enthält fertige Cannabis-Modelle:
# - Lade sie manuell von CurseForge herunter
# - Entpacke die ZIP
# - Kopiere die .blockymodel und .png Dateien nach Common/Models/ und Common/Icons/
```

#### Weg C: AI-Pixel-Art generieren
```
Siehe scripts/ai_prompts.txt für genaue Prompts.
Nutze https://www.pixexact.com/pixel-art-generator/16x16
Speichere die 16×16 Icons als PNG in Common/Icons/ItemsGenerated/
```

**Alle Icons die du brauchst (79 Stück):**
- essence_shadow.png, cannabis_seed_sativa/indica/hybrid.png
- cannabis_bud_sativa/indica/hybrid_junk/street/dispensary/exotic/god.png (15 Stück)
- dried_cannabis.png, haschisch.png, joint.png, blunt.png, spliff.png
- pilz_pulver.png, psilocybin_tinktur.png, amanita_pulver.png
- mohn_kapsel.png, mohn_samen.png, rohopium.png, paper.png, filter_paper.png
- coca_leaves.png, coca_seed.png, coca_paste.png, cocaine.png, crack.png
- morphine.png, heroin.png, meth.png, mdma_powder.png, mdma_pill.png
- peyote_bud.png, peyote_seed.png, meskalin_extract.png
- khat_leaves.png, khat_seed.png, datura_leaves.png, datura_seed.png
- salvia_leaves.png, salvia_seed.png, scopolamin_extract.png, salvinorin.png
- ethanol.png, aceton.png, schwefelsaeure.png, salzsaeure.png, ammoniak.png, ether.png
- lithium_powder.png, pill_press_form.png, empty_syringe.png, filled_syringe.png
- koka_tee.png, cannabis_butter.png
- iboga_root.png, iboga_seed.png, ibogain_extract.png
- ephedra_stem.png, ephedra_seed.png, ephedrin_powder.png
- betel_nut.png, betel_seed.png, kava_root.png, kava_paste.png
- mutterkorn.png, lysergsaeure.png, lsd_tab.png, naloxon.png
- OrbisUnderground.png, OrbisUnderground_Currency.png, _Seeds.png, _Materials.png, _Consumables.png, _Chemicals.png, _Tools.png

### Schritt 3: Kategorie-Icons erstellen
```
Erstelle 32×32 PNG-Icons für die Creative-Menu-Kategorien:
  Common/Icons/ItemCategories/OrbisUnderground.png
  Common/Icons/ItemCategories/OrbisUnderground_Currency.png  (lila Essence)
  Common/Icons/ItemCategories/OrbisUnderground_Seeds.png     (Samen-Tüte)
  Common/Icons/ItemCategories/OrbisUnderground_Materials.png (Blatt)
  Common/Icons/ItemCategories/OrbisUnderground_Consumables.png (Pille)
  Common/Icons/ItemCategories/OrbisUnderground_Chemicals.png (Flasche)
  Common/Icons/ItemCategories/OrbisUnderground_Tools.png     (Spritze)
```

### Schritt 4: Status-Effekt-Icons
```
  Common/Icons/UI/StatusEffects/drug_cannabis.png      (grünes Blatt)
  Common/Icons/UI/StatusEffects/drug_hashish.png       (brauner Klumpen)
  Common/Icons/UI/StatusEffects/drug_psilocybin.png    (blauer Pilz)
  Common/Icons/UI/StatusEffects/drug_amanita.png       (roter Pilz)
  Common/Icons/UI/StatusEffects/drug_cocaine.png       (weißes Pulver)
  Common/Icons/UI/StatusEffects/drug_crack.png         (gelbe Steine)
  Common/Icons/UI/StatusEffects/drug_morphine.png      (weiße Flasche)
  Common/Icons/UI/StatusEffects/drug_heroin.png        (braune Flasche)
  Common/Icons/UI/StatusEffects/drug_meth.png          (blaue Kristalle)
  Common/Icons/UI/StatusEffects/drug_mdma.png          (bunte Pille)
  Common/Icons/UI/StatusEffects/drug_mescaline.png     (braune Flasche)
  Common/Icons/UI/StatusEffects/drug_scopolamine.png   (grüne Flasche)
  Common/Icons/UI/StatusEffects/drug_salvinorin.png    (hellgrüne Flasche)
  Common/Icons/UI/StatusEffects/drug_khat.png          (hellgrünes Blatt)
  Common/Icons/UI/StatusEffects/drug_ibogaine.png      (braune Wurzel)
  Common/Icons/UI/StatusEffects/drug_ephedrin.png      (weißlich-grün)
  Common/Icons/UI/StatusEffects/drug_betel.png         (braune Nuss)
  Common/Icons/UI/StatusEffects/drug_kava.png          (graue Paste)
  Common/Icons/UI/StatusEffects/drug_lsd.png           (bunter Tab)
  Common/Icons/UI/StatusEffects/drug_overdose.png      (Totenkopf)
  Common/Icons/UI/StatusEffects/drug_crash.png         (roter Pfeil runter)
```

### Schritt 5: Mod aktivieren und testen
```
1. Starte Hytale
2. Gehe zum "Worlds"-Tab
3. Rechtsklick auf deine Welt → Pack "Orbis Underground" einschalten
4. Welt betreten
5. /op self (um Cheats zu aktivieren)
6. /give orbis_underground:essence_shadow 64
7. /give orbis_underground:cannabis_seed_sativa 10
8. Baue einen Salvager's Workbench + Alchemist's Workbench + Farmer's Workbench
9. Teste die Rezepte!
```

---

## 🔧 ALLE CRAFTING-REZEPTE

### 🔨 Salvager's Workbench (Mahlen & Trocknen)
| Output | Input | Zeit |
|---|---|---|
| Dried Cannabis | 1× Cannabis Bud + 1× Plant Fiber | 6s |
| Mushroom Powder | 1× Blue Glowing Mushroom | 4s |
| Amanita Powder | 1× Bloodcap Mushroom | 4s |
| Poppy Pods (×2) | 1× Poppy Flower | 4s |
| Lithium Powder | 1× Iron Ingot + 1× Charcoal | 10s |
| Ephedrine Powder | 4× Ephedra Stem + 1× Plant Fiber | 10s |

### ⚗️ Alchemist's Workbench (Extraktionen & Synthesen)
| Output | Input | Zeit | Tier |
|---|---|---|---|
| Psilocybin Tincture | 3× Mushroom Powder + Bottle + Sap | 10s | T1 |
| Raw Opium | 3× Poppy Pods | 8s | T1 |
| Coca Paste | 5× Coca Leaves + Sap + Fiber | 12s | T1 |
| Cocaine | 2× Coca Paste + H₂SO₄ + Filter Paper | 22s | T1 |
| Crack | 1× Cocaine + 1× Ammonia | 10s | T1 |
| Morphine | 2× Raw Opium + H₂SO₄ + Charcoal + Bottle | 20s | T1 |
| Heroin | 1× Morphine + Acetone + Bottle | 24s | **T2** |
| Meth ⚠️ | Ephedrine + Lithium + Ammonia + Ether | 30s | **T2** |
| MDMA Powder | Motes of Light + H₂SO₄ + Acetone | 26s | **T2** |
| Sulfuric Acid | 2× Charcoal + Bottle + Essence of Fire | 16s | T1 |
| HCl | Bone Fragment + H₂SO₄ + Bottle | 14s | T1 |
| Ammonia | 3× Bone Fragments + Bottle + Essence of Water | 14s | T1 |
| Acetone | 2× Tree Sap + Charcoal + Bottle | 14s | T1 |
| Ether | 1× Ethanol + H₂SO₄ + Bottle | 18s | T1 |
| Mescaline Extract | 3× Peyote Bud + 1× Bottle | 15s | T1 |
| Scopolamine | 3× Datura Leaves + Venom Sac + Bottle | 14s | T1 |
| Salvinorin | 3× Salvia Leaves + 1× Bottle | 12s | T1 |
| Ibogaine Extract | 3× Iboga Root + Bottle + Charcoal | 18s | T1 |
| Lysergic Acid | 2× Ergot + Bottle + Essence of Void | 28s | **T2** |
| Naloxone | Morphine + HCl + Charcoal + Bottle | 18s | **T2** |

⚠️ **Meth hat 20% Explosions-Chance!** Baue den Alchemist's Workbench weit weg von deiner Basis!

### 🔧 Basic Workbench (Verarbeitung)
| Output | Input | Zeit |
|---|---|---|
| Hashish | 4× Dried Cannabis + 1× Tree Sap | 10s |
| Joint | 1× Dried Cannabis + 1× Paper | 3s |
| Blunt | 2× Dried Cannabis + 1× Paper | 4s |
| Spliff | 1× Dried Cannabis + 1× Paper | 3s |
| Paper | 3× Plant Fiber + 1× Tree Sap | 4s |
| Filter Paper | 2× Plant Fiber + 1× Charcoal | 5s |
| MDMA Pill | 1× MDMA Powder + Pill Press + Fiber | 8s |
| Empty Syringe | 1× Bottle + 1× Iron Ingot + Linen Scraps | 8s |
| Filled Syringe | 1× Empty Syringe + 1× Heroin | 4s |
| Kava Paste | 2× Kava Root + 1× Tree Sap | 8s |
| LSD Tab | 1× Lysergic Acid + Motes of Light + Paper + Void | 22s |

### 🍳 Chef's Stove (Kochen & Fermentation)
| Output | Input | Zeit |
|---|---|---|
| Ethanol | 2× Wheat + Wild Berries + Bottle | 12s |
| Coca Tea | 1× Coca Leaves + 1× Bottle | 5s |
| Cannabis Butter | 1× Dried Cannabis + 1× Dough | 8s |

### 🌱 Farmer's Workbench (Samen)
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

## 🌍 PFLANZEN IN DER WELT

| Pflanze | Zone | Biom | Seltenheit |
|---|---|---|---|
| Cannabis Sativa | Z1 | Seeding Woods (Waldrand) | Selten |
| Cannabis Indica | Z1 | Drifting Plains | Selten |
| Cannabis Hybrid | Z1 | Seeding Woods | Sehr selten |
| Schlafmohn | Z1, Z3 | Drifting/Snowy Plains | Mittel |
| Coca | Z4 | Underground Jungle | Gelegentlich |
| Peyote | Z2 | Savanna | Selten |
| Khat | Z2 | Oasis | Mittel |
| Datura | Z1, Z2 | Nahe Ruinen | Gelegentlich |
| Salvia | Z1 | The Fens (Sumpf) | Gelegentlich |
| Iboga | Z4 | Underground Jungle | Selten |
| Ephedra | Z2, Z3 | Rocky Hills | Gelegentlich |
| Betel-Palme | Z2 | Oasis | Selten |
| Kava | Z1 | The Fens | Gelegentlich |

---

## 💊 EFFEKT-REFERENZ

| Droge | Dauer | Haupteffekt | Crash/Nebenwirkung |
|---|---|---|---|
| Cannabis Sativa | 2 min | +15% Speed, HP-Regeneration | Keiner |
| Cannabis Indica | 3 min | -15% Speed, +50% HP-Reg | Keiner |
| Hashish | 3 min | Indica ×1.5 | Keiner |
| Psilocybin | 4 min | Wahrnehmungsverschiebung | Keiner |
| Amanita | 3 min | +10% Stärke | 1 DPS Übelkeit (15s) |
| Kokain | 1.5 min | +40% Speed, +30% Resist | -30% Speed (2 min) |
| Crack | 30 sec | Kokain ×2 | -50% Speed, -10% HP |
| Morphium | 5 min | +50% Resist | 1 DPS Atemdepression |
| Heroin | 8 min | +70% Resist, langsam | 3 DPS Atemdepression |
| Meth | 10 min | +30% Speed, +50% Mining | HP-Reg blockiert (10 min) |
| MDMA | 5 min | +20% Stärke, HP-Reg | Depression (24h!) |
| Meskalin | 10 min | Wahrnehmung | 2 DPS Übelkeit (30s) |
| Scopolamin | 5 min | Delirium, Fake-Mobs | 3 DPS Verwirrung |
| Salvinorin | 1.5 min | Extreme Wahrnehmung | Keiner |
| Khat | 3 min | +10% Speed | Keiner |
| Ibogain | 30 min | Entfernt ALLE Drogeneffekte | Ataxie |
| LSD | 12 min | Texturen vertauscht, Himmel verzerrt | Keiner |
| Kava | 4 min | -10% Speed, Anti-Angst | Keiner |
| Überdosis | 1 min | Lähmung, 10 DPS | **TOD** |

**Notfall:** Naloxon craften (Alchemist's T2) — entfernt Opiat-Effekte und Überdosis!

---

## 🏪 KWEEBECK DEALER

- **Spawn:** 50% Wahrscheinlichkeit pro Kweebec-Dorf
- **Währung:** Essence of Shadow (NICHT Essence of Life!)
- **Kauft:** Dried Cannabis (3💰), Hashish (8💰), Raw Opium (12💰), Mushroom Powder (6💰), Joints (5💰), Blunts (7💰)
- **Verkauft:** Sativa Seeds (3💰), Indica Seeds (4💰), Poppy Seeds (4💰), Empty Bottles (2💰), Paper (1💰)

---

## 🎲 LOOT-TABELLEN

### Schmugglerversteck 1 (Trork Camp, Zone 1)
Cannabis-Seeds, Essence of Shadow (5-15), Boom Powder, Paper, Dried Cannabis, Poppy Seeds

### Schmugglerlabor 2 (Emerald Grove Ruins, Zone 2+)
Ether, Sulfuric Acid, Empty Bottles, Motes of Light, Essence of Shadow (10-25), Coca Paste, Acetone, Filter Paper, Lithium Powder

---

## 📝 ENTWICKLUNG

```bash
# JSON-Syntax validieren
find . -name "*.json" -exec python3 -c "import json; json.load(open('{}'))" \;

# Items zählen
ls Server/Item/Items/orbis_underground/*.json | wc -l

# Effekte zählen
ls Server/Assets/EntityEffect/*.json | wc -l

# Alle Dateien
find . -type f ! -path './.git/*' | wc -l
```

---

## 📄 Credits
- **Get Hy!** by DaemonPalace (MIT) — Cannabis-Modelle
- **Hytale** by Hypixel Studios — Vanilla-Assets als Basis
- Dieses Projekt ist MIT-lizenziert. Siehe [CREDITS.md](CREDITS.md)
