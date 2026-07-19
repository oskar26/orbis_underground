# 🌿 Orbis Underground — Hytale Drogen-Mod

**Version 1.1.0 | Lizenz: MIT | Alle 3 Phasen implementiert**

> Eine umfassende Drogen-Mod für Hytale mit realistischen Crafting-Ketten, 26 Status-Effekten und einem Kweebec-Dealer-Handelssystem. **Die Pflanzenverarbeitung und Chemie laufen über zwei eigene, auf Tier 2 aufrüstbare Custom-Werkbänke.**

---

## 📋 Schnellübersicht

| Phase | Name | Drogen | Effekte |
|---|---|---|---|
| **1.0** | Green Harvest | Cannabis (3 Sorten), Haschisch, Psilocybin, Amanita, Rohopium | 6 |
| **2.0** | Hard Stuff | Kokain, Crack, Morphium, Heroin, Meth, MDMA, Meskalin, Scopolamin, Salvinorin, Khat | 15 |
| **3.0** | Full Trip | Ibogain, Ephedrin, Betel, Kava, LSD, Überdosis | 6 |

**94 Items/Blöcke | 26 EntityEffects | 1 Dealer-NPC | 13 Worldgen-Pflanzen | EN + DE Übersetzungen**

---

## 🏗️ ARCHITEKTUR: Zwei Custom-Werkbänke

| Werkbank | Bench-ID | Verwendung in der Mod |
|---|---|---|
| **Botanischer Tisch** | `OrbisUnderground_Botanybench` | Trocknen, Mahlen, Pressen, Papier, Joints, pflanzliche Extrakte und Pillen |
| **Chemie-Labor** | `OrbisUnderground_Chemistrybench` | Säuren, Lösungsmittel, Kokain, Crack, Morphium, Heroin, Meth, MDMA, Lysergsäure und Naloxon |
| **Chef's Stove** | `Cookingbench` | Ethanol-Fermentation, Coca-Tee und Cannabis-Butter |
| **Farmer's Workbench** | `Farmingbench` | Samen craften |

Beide Custom-Bänke besitzen **Tier 1 und Tier 2**. Tier 2 schaltet komplexe Pflanzenextrakte bzw. harte Drogen frei. Die Weltgenerierung nutzt die konfliktarmen `Server/WorldGen/Modifier`-Assets des WorldGen-v1-Modifier-Systems, anstatt Vanilla-Biome-Dateien vollständig zu überschreiben.

> **ID-Hinweis:** Hytale-Asset-IDs sind global und werden aus dem Dateinamen abgeleitet. Darum heißen die runtimefähigen Item-IDs z. B. `bench_botany` und `essence_shadow`; die Paketidentität bleibt `orbis_underground:Orbis Underground`. Minecraft-artige Item-IDs wie `orbis_underground:bench_botany` sind im Hytale-Item-AssetStore nicht gültig.

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
    │   ├── Blocks\orbis_underground\       ← Werkbank-Modelle
    │   ├── BlockTextures\orbis_underground\← Werkbank-Texturen
    │   ├── Icons\ItemsGenerated\           ← Item- und Werkbank-Icons
    │   └── Icons\ItemCategories\           ← Kategorie-Icons
    └── Server\
        ├── Item\Items\orbis_underground\   ← Items, Werkbänke und Wildpflanzen
        ├── Assets\EntityEffect\            ← 26 Effekte
        ├── WorldGen\Modifier\              ← 13 WorldGen-v1-Injections
        ├── NPC\Roles\                      ← Kweebec-Dealer
        ├── NPC\Spawn\Markers\              ← 50%-Dorfspawn
        ├── BarterShops\                     ← Dealer-Handel
        ├── Languages\en-US\server.lang     ← Englische Texte
        └── Languages\de-DE\server.lang     ← Deutsche Texte
```

### Schritt 2: Texturen generieren (empfohlene Methode = Original-Assets recolorn)
Die saubere Methode ist **nicht** die Platzhalter-Generierung, sondern das **Umfärben der originalen Hytale-Assets**. Genau dafür ist `scripts/recolor.py` jetzt gedacht.

#### Empfohlenes Setup
- Lege deinen Hytale-Asset-Ordner als `Assets/` direkt **in den Repo-Hauptordner**.
- Lege die entpackte **Get Hy!**-Mod irgendwo lokal ab, z. B. `/home/oskar/Downloads/get_hy`.
- Dann sucht `scripts/recolor.py` rekursiv selbst nach den benötigten Dateien.

#### Ein-Kommando-Variante
```bash
cd /home/oskar/hytale_underground
python3 -m pip install Pillow
python3 scripts/recolor.py \
  --assets-dir /home/oskar/hytale_underground/Assets \
  --get-hy-dir /home/oskar/Downloads/get_hy
```

#### Wenn `Assets/` schon im Repo-Hauptordner liegt
Dann reicht meistens schon:
```bash
cd /home/oskar/hytale_underground
python3 -m pip install Pillow
python3 scripts/recolor.py
python3 scripts/check_missing.py
```

> Falls `python3 -m pip install Pillow` auf deinem Linux mit `externally-managed-environment` scheitert:
> ```bash
> python3 -m venv .venv
> source .venv/bin/activate
> pip install Pillow
> python scripts/recolor.py
> python scripts/check_missing.py
> ```

#### Was das Script automatisch macht
- sucht die Vanilla-Basisdateien rekursiv in `Assets/`
- recolort daraus die benötigten Mod-Icons
- erstellt Kategorie-Icons und Status-Effekt-Icons
- erstellt/kopiert die Werkbank-Texturen
- kopiert Cannabis-Bud-/Joint-/Blunt-/Spliff-Icons aus **Get Hy!**, wenn vorhanden
- kopiert optionale Cannabis-Bud-Modelle nach `Common/Items/Cannabis/`, wenn vorhanden

#### Platzhalter bewusst deaktiviert
Standardmäßig erzeugt `recolor.py` **keine** hässlichen Platzhalter. Falls du sie trotzdem willst, musst du es explizit mit `--allow-placeholders` einschalten.

#### Falls etwas fehlt
```bash
python3 scripts/check_missing.py
```
Das Script zeigt dir danach genau, welche Dateien noch fehlen.

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

### Schritt 3: Kategorie-Icons
Diese 32×32-Kategorie-Icons werden durch `scripts/recolor.py` automatisch erzeugt:
```
Common/Icons/ItemCategories/OrbisUnderground.png
Common/Icons/ItemCategories/OrbisUnderground_Currency.png
Common/Icons/ItemCategories/OrbisUnderground_Seeds.png
Common/Icons/ItemCategories/OrbisUnderground_Materials.png
Common/Icons/ItemCategories/OrbisUnderground_Consumables.png
Common/Icons/ItemCategories/OrbisUnderground_Chemicals.png
Common/Icons/ItemCategories/OrbisUnderground_Tools.png
```
Wenn danach noch etwas fehlt: `python3 scripts/check_missing.py`

### Schritt 4: Status-Effekt-Icons
Auch diese Icons werden beim Recolor-Lauf automatisch gebaut:
```
Common/Icons/UI/StatusEffects/drug_cannabis.png
Common/Icons/UI/StatusEffects/drug_hashish.png
Common/Icons/UI/StatusEffects/drug_psilocybin.png
Common/Icons/UI/StatusEffects/drug_amanita.png
Common/Icons/UI/StatusEffects/drug_cocaine.png
Common/Icons/UI/StatusEffects/drug_crack.png
Common/Icons/UI/StatusEffects/drug_morphine.png
Common/Icons/UI/StatusEffects/drug_heroin.png
Common/Icons/UI/StatusEffects/drug_meth.png
Common/Icons/UI/StatusEffects/drug_mdma.png
Common/Icons/UI/StatusEffects/drug_mescaline.png
Common/Icons/UI/StatusEffects/drug_scopolamine.png
Common/Icons/UI/StatusEffects/drug_salvinorin.png
Common/Icons/UI/StatusEffects/drug_khat.png
Common/Icons/UI/StatusEffects/drug_ibogaine.png
Common/Icons/UI/StatusEffects/drug_ephedrin.png
Common/Icons/UI/StatusEffects/drug_betel.png
Common/Icons/UI/StatusEffects/drug_kava.png
Common/Icons/UI/StatusEffects/drug_lsd.png
Common/Icons/UI/StatusEffects/drug_overdose.png
Common/Icons/UI/StatusEffects/drug_crash.png
```

### Schritt 5: Mod aktivieren und testen
```
1. Starte Hytale
2. Gehe zum "Worlds"-Tab
3. Rechtsklick auf deine Welt → Pack "Orbis Underground" einschalten
4. Welt betreten
5. /op self (um Cheats zu aktivieren)
6. /give essence_shadow 64
7. /give cannabis_seed_sativa 10
8. Baue einen Botanischen Tisch und ein Chemie-Labor
9. Rüste beide Bänke auf Tier 2 auf und teste die Rezepte!
```

---

## 🔧 ALLE CRAFTING-REZEPTE

### 🌿 Botanischer Tisch (Pflanzenverarbeitung)
| Output | Input | Zeit |
|---|---|---|
| Dried Cannabis | 1× Cannabis Bud + 1× Plant Fiber | 6s |
| Mushroom Powder | 1× Blue Glowing Mushroom | 4s |
| Amanita Powder | 1× Bloodcap Mushroom | 4s |
| Poppy Pods (×2) | 1× Poppy Flower | 4s |
| Lithium Powder | 1× Iron Ingot + 1× Charcoal | 10s |
| Ephedrine Powder | 4× Ephedra Stem + 1× Plant Fiber | 10s |

### ⚗️ Chemie-Labor (Extraktionen & Synthesen)
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

### 🌿 Botanischer Tisch (Weiterverarbeitung)
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
