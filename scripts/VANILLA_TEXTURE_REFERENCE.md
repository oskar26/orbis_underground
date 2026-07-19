# Vanilla Hytale Texture Reference für Orbis Underground

## Benötigte Vanilla-Texturen

`recolor.py` sucht diese Dateien inzwischen **rekursiv** in deinem lokalen `Assets/`-Ordner.
Der alte Weg über `scripts/vanilla_textures/` funktioniert weiterhin als Fallback, ist aber nicht mehr nötig.

| Mod-Ziel | Vanilla-Dateiname (vermutet) | Quelle / Hinweis |
|---|---|---|
| **essence_shadow.png** | `essence_of_life.png` | Grün → Lila (Hue +180°) |
| **Flaschen-Basises** | `empty_potion_bottle.png` | Basis für alle Flüssigkeiten |
| **tree_sap.png** | `tree_sap.png` | Harz → Rohopium, Haschisch, Coca-Paste, Kava |
| **charcoal.png** | `charcoal.png` | Kohle → Alle Pulver |
| **plant_fiber.png** | `plant_fiber.png` | Faser → Papier, Blätter, Wurzeln |
| **wheat_seed_bag.png** | `wheat_seed_bag.png` | Samtüte → Alle Samen |
| **alchemist_workbench.png** | `alchemist_workbench.png` | → Chemistry Bench (violett, dunkler) |
| **blue_glowing_mushroom.png** | `blue_glowing_mushroom.png` | Psilocybin-Status-Icon |
| **bloodcap_mushroom.png** | `bloodcap_mushroom.png` | Amanita-Status-Icon |
| **iron_ingot.png** | `iron_ingot.png` | Tools-Kategorie (Spritze) |

---

## Extraction-Befehle (Fedora)

```bash
cd /home/oskar/hytale_underground

# 1. Assets.zip finden & entpacken
ASSETS_DIR="/home/oskar/.local/share/f2p-evo/games/ef4f5126-60ae-43ec-9cd6-a439e971a5d7"
mkdir -p scripts/vanilla_textures

# Assets.zip suchen (kann auch assets.pak oder .zip heißen)
find "$ASSETS_DIR" -type f \( -name "*.zip" -o -name "*.pak" -o -name "Assets*" \) 2>/dev/null

# Falls Assets.zip gefunden:
unzip -o "$ASSETS_DIR/Assets.zip" -d /tmp/hytale_assets/

# 2. Relevante Texturen kopieren (Pfade anpassen je nach Struktur)
# Typische Pfade in Hytale Assets:
# /tmp/hytale_assets/assets/hytale/textures/items/
# /tmp/hytale_assets/assets/hytale/textures/blocks/
# /tmp/hytale_assets/Common/Icons/Items/

cp /tmp/hytale_assets/**/essence_of_life.png scripts/vanilla_textures/ 2>/dev/null
cp /tmp/hytale_assets/**/empty_potion_bottle.png scripts/vanilla_textures/ 2>/dev/null
cp /tmp/hytale_assets/**/tree_sap.png scripts/vanilla_textures/ 2>/dev/null
cp /tmp/hytale_assets/**/charcoal.png scripts/vanilla_textures/ 2>/dev/null
cp /tmp/hytale_assets/**/plant_fiber.png scripts/vanilla_textures/ 2>/dev/null
cp /tmp/hytale_assets/**/wheat_seed_bag.png scripts/vanilla_textures/ 2>/dev/null
cp /tmp/hytale_assets/**/alchemist_workbench*.png scripts/vanilla_textures/ 2>/dev/null
cp /tmp/hytale_assets/**/blue_glowing_mushroom*.png scripts/vanilla_textures/ 2>/dev/null
cp /tmp/hytale_assets/**/bloodcap_mushroom*.png scripts/vanilla_textures/ 2>/dev/null
cp /tmp/hytale_assets/**/iron_ingot*.png scripts/vanilla_textures/ 2>/dev/null

# 3. Prüfen was da ist
ls -la scripts/vanilla_textures/
```

---

## Falls Assets.zip NICHT gefunden wird

Hytale speichert Assets evtl. in `.pak` Dateien. Nutze **Hytale Asset Extractor**:

```bash
# Option A: Hytale Asset Editor (im Spiel enthalten)
# 1. Spiel starten → Creative Mode → Asset Editor
# 2. Vanilla Pack öffnen → Texturen exportieren

# Option B: Community Tool
# https://github.com/HytaleModding/HytaleAssetExtractor (falls existiert)

# Option C: Manuell aus Game-Dateien
# Suche nach .png in den Game-Files:
find "$ASSETS_DIR" -name "*.png" | head -30
```

---

## Mapping-Tabelle: Mod-Item → Vanilla-Basis + Transformation

| Mod-Item | Vanilla-Basis | Transformation |
|---|---|---|
| `essence_shadow` | `essence_of_life` | Hue +180° |
| `ethanol` | `empty_potion_bottle` | Tint #DCDCF0 @55% |
| `schwefelsaeure` | `empty_potion_bottle` | Tint #C8B450 @70% |
| `salzsaeure` | `empty_potion_bottle` | Tint #96C878 @70% |
| `ammoniak` | `empty_potion_bottle` | Tint #E6E6F0 @50% |
| `ether` | `empty_potion_bottle` | Tint #96AADC @60% |
| `morphine` | `empty_potion_bottle` | Tint #E6E1D7 @60% |
| `cocaine` | `charcoal` | Tint #FFFFFF @50% |
| `crack` | `empty_potion_bottle` | Tint #FFF0B4 @65% |
| `heroin` | `empty_potion_bottle` | Tint #D2BE90 @70% |
| `mdma_powder` | `charcoal` | Tint #D2BEAA @65% |
| `mdma_pill` | `empty_potion_bottle` | Tint #FF64B4 @80% |
| `rohopium` | `tree_sap` | Tint #321E14 @85% |
| `haschisch` | `tree_sap` | Tint #503214 @80% |
| `coca_paste` | `tree_sap` | Tint #D2D2C8 @70% |
| `pilz_pulver` | `charcoal` | Tint #8C785A @75% |
| `amanita_pulver` | `charcoal` | Tint #B4643C @75% |
| `paper` | `plant_fiber` | Tint #F0F0EB @60% |
| `filter_paper` | `plant_fiber` | Tint #B4B4AF @65% |
| `coca_leaves` | `plant_fiber` | Tint #28641E @80% |
| `khat_leaves` | `plant_fiber` | Tint #8CD264 @75% |
| `cannabis_seed_*` | `wheat_seed_bag` | Tint (grün-variiert) @75% |
| `bench_chemistry` | `alchemist_workbench` | Hue +270°, Darken 0.85 |

---

## Get Hy! Assets (MIT-Lizenz)

**Download:** https://modrinth.com/mod/get-hy oder CurseForge

`recolor.py` versucht diese Dateien automatisch rekursiv aus dem angegebenen Get-Hy-Ordner zu kopieren.

**Benötigte Icons nach `Common/Icons/ItemsGenerated/`:**
```
cannabis_bud_sativa_junk.png          cannabis_bud_indica_junk.png          cannabis_bud_hybrid_junk.png
cannabis_bud_sativa_street.png        cannabis_bud_indica_street.png        cannabis_bud_hybrid_street.png
cannabis_bud_sativa_dispensary.png    cannabis_bud_indica_dispensary.png    cannabis_bud_hybrid_dispensary.png
cannabis_bud_sativa_exotic.png        cannabis_bud_indica_exotic.png        cannabis_bud_hybrid_exotic.png
cannabis_bud_sativa_god.png           cannabis_bud_indica_god.png           cannabis_bud_hybrid_god.png
joint.png                             blunt.png                              spliff.png
```

**Optionale Item-Modelle nach `Common/Items/Cannabis/`:**
```
cannabis_bud_sativa.blockymodel
cannabis_bud_indica.blockymodel
cannabis_bud_hybrid.blockymodel
```

Falls dein Get-Hy-Paket andere Dateinamen nutzt, musst du diese drei Modelldateien ggf. manuell zuordnen oder umbenennen.

---

## Ausführung

### Empfohlen für dein lokales Setup
```bash
cd /home/oskar/hytale_underground
python3 -m pip install Pillow
python3 scripts/recolor.py \
  --assets-dir /home/oskar/hytale_underground/Assets \
  --get-hy-dir /home/oskar/Downloads/get_hy
python3 scripts/check_missing.py
```

> Falls `python3 -m pip install Pillow` wegen `externally-managed-environment` fehlschlägt:
> ```bash
> python3 -m venv .venv
> source .venv/bin/activate
> pip install Pillow
> python scripts/recolor.py
> python scripts/check_missing.py
> ```

### Wenn `Assets/` schon im Repo-Hauptordner liegt
```bash
cd /home/oskar/hytale_underground
python3 -m pip install Pillow
python3 scripts/recolor.py
python3 scripts/check_missing.py
```

---

## Troubleshooting

| Problem | Lösung |
|---|---|
| `⚠ FEHLT: essence_of_life ...` in `recolor.py` | Assets-Ordner nicht gefunden oder falscher `--assets-dir` |
| `PIL.UnidentifiedImageError` | Datei korrupt / kein PNG |
| Farben stimmen nicht | Vanilla-Textur hat andere Farbwerte → `tint()` alpha anpassen |
| `amanita_pulver.png` fehlt | Wurde im Script neu hinzugefügt (nicht in altem generate_textures.py) |
| Kategorie-Icons 32x32 zu klein | `resize((32,32), Image.NEAREST)` nutzt Nearest-Neighbor für Pixel-Art |