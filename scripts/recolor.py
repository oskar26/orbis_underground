#!/usr/bin/env python3
"""
Orbis Underground — Vanilla Texture Recolorer
Maps each mod item to its vanilla Hytale source texture and applies color transformations.
Run from: /home/user/orbis_underground/scripts/
Requires: Pillow (pip install Pillow)
"""

from PIL import Image
import os
import sys

# ─── CONFIG ──────────────────────────────────────────────────────────────
SRC_DIR = "vanilla_textures"          # Ordner mit extrahierten Vanilla-Texturen
DST_ITEMS = "../Common/Icons/ItemsGenerated"
DST_BLOCKS = "../Common/BlockTextures/orbis_underground"
DST_CATEGORIES = "../Common/Icons/ItemCategories"
DST_STATUS = "../Common/Icons/UI/StatusEffects"

os.makedirs(DST_ITEMS, exist_ok=True)
os.makedirs(DST_BLOCKS, exist_ok=True)
os.makedirs(DST_CATEGORIES, exist_ok=True)
os.makedirs(DST_STATUS, exist_ok=True)

# ─── HELPER: Farbtransformationen ────────────────────────────────────────

def hue_shift(img: Image.Image, degrees: int) -> Image.Image:
    """Hue-Shift in HSV-Farbraum (0-360°)."""
    hsv = img.convert("HSV")
    h, s, v = hsv.split()
    shift = int(degrees * 255 / 360)
    h = h.point(lambda x: (x + shift) % 256)
    return Image.merge("HSV", (h, s, v)).convert("RGBA")


def tint(img: Image.Image, rgb: tuple, alpha: float = 0.65) -> Image.Image:
    """Farbüberlagerung (Multiplikativ + Alpha)."""
    base = img.convert("RGBA")
    overlay = Image.new("RGBA", img.size, rgb + (int(255 * alpha),))
    return Image.alpha_composite(base, overlay)


def desaturate(img: Image.Image, factor: float = 0.3) -> Image.Image:
    """Entsättigen (0.0 = Graustufen, 1.0 = Original)."""
    hsv = img.convert("HSV")
    h, s, v = hsv.split()
    s = s.point(lambda x: int(x * factor))
    return Image.merge("HSV", (h, s, v)).convert("RGBA")


def darken(img: Image.Image, factor: float = 0.7) -> Image.Image:
    """Abdunkeln."""
    return img.convert("RGBA").point(lambda x: int(x * factor) if x > 0 else 0)


def lighten(img: Image.Image, factor: float = 1.3) -> Image.Image:
    """Aufhellen."""
    return img.convert("RGBA").point(lambda x: min(255, int(x * factor)))


def recolor_replace(img: Image.Image, target_hue: int, tolerance: int = 30) -> Image.Image:
    """Ersetzt einen Farbbereich (Hue) durch einen anderen."""
    hsv = img.convert("HSV")
    h, s, v = hsv.split()
    target = int(target_hue * 255 / 360)
    h = h.point(lambda x: target if abs(x - target) < tolerance else x)
    return Image.merge("HSV", (h, s, v)).convert("RGBA")


def load_vanilla(name: str) -> Image.Image | None:
    """Lädt Vanilla-Textur aus SRC_DIR (versucht .png und _icon.png)."""
    for suffix in (".png", "_icon.png", "_item.png", ""):
        path = os.path.join(SRC_DIR, f"{name}{suffix}")
        if os.path.exists(path):
            return Image.open(path).convert("RGBA")
    print(f"  ⚠ Vanilla nicht gefunden: {name}")
    return None


def save(img: Image.Image, dest_dir: str, filename: str):
    img.save(os.path.join(dest_dir, filename))
    print(f"  ✓ {dest_dir}/{filename}")


# ─── MAIN RECOLOR LOGIC ──────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("Orbis Underground — Vanilla Texture Recolorer")
    print("=" * 60)

    # ─── 1. ESSENCE OF SHADOW (Essence of Life → Hue +180°) ───────────────
    print("\n[1/8] Essence & Währung")
    img = load_vanilla("essence_of_life")
    if img:
        save(hue_shift(img, 180), DST_ITEMS, "essence_shadow.png")
        # Kategorie-Icon (32x32)
        cat = hue_shift(img.resize((32, 32), Image.NEAREST), 180)
        save(cat, DST_CATEGORIES, "OrbisUnderground_Currency.png")

    # ─── 2. FLASCHEN & FLÜSSIGKEITEN (Empty Potion Bottle Basis) ─────────
    print("\n[2/8] Flaschen & Flüssigkeiten")
    bottle = load_vanilla("empty_potion_bottle")
    if bottle:
        recipes = {
            # (output_name, rgb_tint, alpha)
            "ethanol.png":          ((220, 220, 240), 0.55),   # klar
            "schwefelsaeure.png":   ((200, 180,  80), 0.70),   # gelb
            "salzsaeure.png":       ((150, 200, 120), 0.70),   # grün
            "ammoniak.png":         ((230, 230, 240), 0.50),   # weiß-trüb
            "ether.png":            ((150, 170, 220), 0.60),   # blau
            "morphine.png":         ((230, 225, 215), 0.60),   # weiß
            "cocaine.png":          ((250, 250, 248), 0.55),   # rein weiß
            "crack.png":            ((255, 240, 180), 0.65),   # gelblich
            "heroin.png":           ((210, 190, 160), 0.70),   # bräunlich
            "mdma_powder.png":      ((210, 190, 170), 0.65),
            "mdma_pill.png":        ((255, 100, 180), 0.80),   # pink
            "meskalin_extract.png": ((180, 150, 110), 0.70),
            "scopolamin_extract.png":((100, 130,  90), 0.70),
            "salvinorin.png":       (( 70, 180,  70), 0.70),
            "ibogain_extract.png":  ((240, 235, 220), 0.65),
            "naloxon.png":          ((230, 240, 250), 0.60),
            "koka_tee.png":         ((100, 150,  80), 0.70),
            "cannabis_butter.png":  ((200, 200, 140), 0.75),
            "filled_syringe.png":   ((190, 160, 130), 0.75),
            "empty_syringe.png":    ((220, 220, 230), 0.50),
        }
        for name, (rgb, alpha) in recipes.items():
            save(tint(bottle, rgb, alpha), DST_ITEMS, name)

    # ─── 3. BAUMHARZ BASIS (Tree Sap → Rohopium, Haschisch, Coca-Paste) ──
    print("\n[3/8] Baumharz-Derivate")
    sap = load_vanilla("tree_sap")
    if sap:
        for name, rgb, alpha in [
            ("rohopium.png",        (50, 30, 20), 0.85),
            ("haschisch.png",       (80, 50, 20), 0.80),
            ("coca_paste.png",      (210, 210, 200), 0.70),
            ("kava_paste.png",      (170, 165, 150), 0.75),
        ]:
            save(tint(sap, rgb, alpha), DST_ITEMS, name)

    # ─── 4. KOHLE / CHARCOAL BASIS (Pulver) ──────────────────────────────
    print("\n[4/8] Pulver (Charcoal-Basis)")
    coal = load_vanilla("charcoal")
    if coal:
        for name, rgb, alpha in [
            ("pilz_pulver.png",     (140, 120,  90), 0.75),  # Psilocybin-Pulver
            ("amanita_pulver.png",  (180, 100,  60), 0.75),  # NEU: Amanita-Pulver (rötlich)
            ("cocaine.png",         (255, 255, 255), 0.50),  # reines Kokain (überschreibt bottle)
            ("heroin.png",          (210, 190, 160), 0.70),
            ("lithium_powder.png",  (200, 200, 210), 0.65),
            ("ephedrin_powder.png", (200, 220, 180), 0.65),
            ("mdma_powder.png",     (210, 190, 170), 0.65),
            ("mutterkorn.png",      (70, 50, 40), 0.80),
        ]:
            save(tint(coal, rgb, alpha), DST_ITEMS, name)

    # ─── 5. PFLANZENFASER BASIS (Plant Fiber → Papier, Blätter) ──────────
    print("\n[5/8] Papier & Blätter (Plant Fiber Basis)")
    fiber = load_vanilla("plant_fiber")
    if fiber:
        for name, rgb, alpha in [
            ("paper.png",           (240, 240, 235), 0.60),
            ("filter_paper.png",    (180, 180, 175), 0.65),
            ("coca_leaves.png",     (40, 100, 30), 0.80),
            ("khat_leaves.png",     (140, 210, 100), 0.75),
            ("datura_leaves.png",   (50, 90, 40), 0.80),
            ("salvia_leaves.png",   (60, 150, 60), 0.80),
            ("peyote_bud.png",      (160, 170, 140), 0.75),
            ("iboga_root.png",      (130, 90, 50), 0.80),
            ("kava_root.png",       (140, 110, 90), 0.80),
            ("ephedra_stem.png",    (170, 190, 130), 0.75),
            ("betel_nut.png",       (160, 110, 60), 0.80),
        ]:
            save(tint(fiber, rgb, alpha), DST_ITEMS, name)

    # ─── 6. WEIZEN-SAMENTÜTE BASIS (Wheat Seed Bag → Alle Samen) ─────────
    print("\n[6/8] Samen-Tüten (Wheat Seed Bag Basis)")
    seedbag = load_vanilla("wheat_seed_bag")
    if seedbag:
        for name, rgb, alpha in [
            ("cannabis_seed_sativa.png", (80, 160, 60), 0.75),
            ("cannabis_seed_indica.png", (60, 130, 50), 0.75),
            ("cannabis_seed_hybrid.png", (70, 150, 70), 0.75),
            ("coca_seed.png",            (60, 140, 50), 0.75),
            ("peyote_seed.png",          (120, 100, 70), 0.75),
            ("khat_seed.png",            (100, 160, 70), 0.75),
            ("datura_seed.png",          (40, 70, 30), 0.80),
            ("salvia_seed.png",          (40, 110, 40), 0.80),
            ("iboga_seed.png",           (100, 70, 30), 0.80),
            ("ephedra_seed.png",         (130, 150, 90), 0.75),
            ("betel_seed.png",           (120, 80, 40), 0.80),
        ]:
            save(tint(seedbag, rgb, alpha), DST_ITEMS, name)

    # ─── 7. CANNABIS BUDS & JOINTS (Get Hy! Assets — NICHT recoloren!) ────
    print("\n[7/8] Cannabis Buds & Joints — Get Hy! Assets erwartet")
    print("  ⚠ Diese werden NICHT generiert — kopiere Get Hy! Assets manuell nach:")
    print(f"     {DST_ITEMS}/")
    print("  Benötigt: 15 Buds (3 Strains × 5 Tiers) + joint/blunt/spliff Varianten")

    # Platzhalter falls Get Hy! fehlt (einfache Icons)
    bud_colors = {
        "sativa":  [(70,120,40), (85,140,50), (100,155,60), (115,170,70), (130,190,80)],
        "indica":  [(50,100,30), (60,115,40), (70,130,50), (85,150,60), (100,170,70)],
        "hybrid":  [(60,115,50), (75,130,60), (90,145,70), (105,160,80), (120,180,90)],
    }
    tiers = ["junk", "street", "dispensary", "exotic", "god"]
    for strain, colors in bud_colors.items():
        for tier, rgb in zip(tiers, colors):
            name = f"cannabis_bud_{strain}_{tier}.png"
            path = os.path.join(DST_ITEMS, name)
            if not os.path.exists(path):
                # Einfacher Kreis als Fallback
                img = Image.new("RGBA", (16, 16), (0,0,0,0))
                p = img.load()
                cx, cy, r = 8, 8, 6
                for y in range(16):
                    for x in range(16):
                        if (x-cx)**2 + (y-cy)**2 <= r**2:
                            shade = 1.0 - ((x-cx)**2 + (y-cy)**2)**0.5 / r * 0.3
                            p[x,y] = (int(rgb[0]*shade), int(rgb[1]*shade), int(rgb[2]*shade), 255)
                save(img, DST_ITEMS, name)

    # Joint/Blunt/Spliff Fallbacks
    for name, rgb in [
        ("joint.png",    (200, 180, 150)),
        ("blunt.png",    (140, 100,  60)),
        ("spliff.png",   (180, 160, 130)),
    ]:
        path = os.path.join(DST_ITEMS, name)
        if not os.path.exists(path):
            img = Image.new("RGBA", (16, 16), (0,0,0,0))
            p = img.load()
            for y in range(4, 12):
                for x in range(6, 10):
                    p[x,y] = rgb + (255,)
            save(img, DST_ITEMS, name)

    # ─── 8. WERKBANK-TEXTUREN ────────────────────────────────────────────
    print("\n[8/8] Werkbank-Texturen")
    # Botanischer Tisch: bereits via generate_textures.py
    # Chemie-Labor: Alchemist Workbench → Hue-Shift + Dunkel
    alch = load_vanilla("alchemist_workbench") or load_vanilla("alchemy_workbench") or load_vanilla("alchemist_bench")
    if alch:
        chem = darken(hue_shift(alch, 270), 0.85)  # Violett + dunkler
        save(chem, DST_BLOCKS, "bench_chemistry.png")
        save(chem.resize((16,16), Image.NEAREST), DST_ITEMS, "bench_chemistry.png")
    else:
        print("  ⚠ alchemist_workbench nicht gefunden — nutze Platzhalter")

    # Botanischer Tisch Textur kopieren falls vorhanden
    botany_src = "../Common/BlockTextures/bench_botany.png"
    if os.path.exists(botany_src):
        img = Image.open(botany_src).convert("RGBA")
        save(img, DST_BLOCKS, "bench_botany.png")
        save(img.resize((16,16), Image.NEAREST), DST_ITEMS, "bench_botany.png")

    # ─── KATEGORIE-ICONS (32x32) ─────────────────────────────────────────
    print("\n[+] Kategorie-Icons (32x32)")
    cat_recipes = {
        "OrbisUnderground.png":         (hue_shift(load_vanilla("essence_of_life").resize((32,32)), 180) if load_vanilla("essence_of_life") else None, "lila Essence"),
        "OrbisUnderground_Seeds.png":   (tint(load_vanilla("wheat_seed_bag").resize((32,32)), (80,160,60), 0.7) if load_vanilla("wheat_seed_bag") else None, "Samen-Tüte"),
        "OrbisUnderground_Materials.png": (tint(load_vanilla("plant_fiber").resize((32,32)), (60,130,40), 0.7) if load_vanilla("plant_fiber") else None, "Blatt"),
        "OrbisUnderground_Consumables.png": (tint(load_vanilla("empty_potion_bottle").resize((32,32)), (255,100,180), 0.8) if load_vanilla("empty_potion_bottle") else None, "Pille"),
        "OrbisUnderground_Chemicals.png": (tint(load_vanilla("empty_potion_bottle").resize((32,32)), (150,170,220), 0.7) if load_vanilla("empty_potion_bottle") else None, "Flasche"),
        "OrbisUnderground_Tools.png":   (tint(load_vanilla("iron_ingot").resize((32,32)), (190,160,130), 0.7) if load_vanilla("iron_ingot") else None, "Spritze"),
    }
    for name, (img, desc) in cat_recipes.items():
        if img:
            save(img, DST_CATEGORIES, name)
        else:
            print(f"  ⚠ {name} ({desc}) — Vanilla-Basis fehlt")

    # ─── STATUS-EFFEKT-ICONS (16x16) ─────────────────────────────────────
    print("\n[+] Status-Effekt-Icons (16x16)")
    status_map = {
        "drug_cannabis.png":      ("plant_fiber", (60,130,40)),
        "drug_hashish.png":       ("charcoal", (80,50,20)),
        "drug_psilocybin.png":    ("blue_glowing_mushroom", (70,70,200)),
        "drug_amanita.png":       ("bloodcap_mushroom", (180,60,40)),
        "drug_cocaine.png":       ("charcoal", (255,255,255)),
        "drug_crack.png":         ("charcoal", (255,240,180)),
        "drug_morphine.png":      ("empty_potion_bottle", (230,225,215)),
        "drug_heroin.png":        ("empty_potion_bottle", (210,190,160)),
        "drug_meth.png":          ("charcoal", (180,200,240)),
        "drug_mdma.png":          ("empty_potion_bottle", (255,100,180)),
        "drug_mescaline.png":     ("empty_potion_bottle", (180,150,110)),
        "drug_scopolamine.png":   ("empty_potion_bottle", (100,130,90)),
        "drug_salvinorin.png":    ("empty_potion_bottle", (70,180,70)),
        "drug_khat.png":          ("plant_fiber", (140,210,100)),
        "drug_ibogaine.png":      ("plant_fiber", (130,90,50)),
        "drug_ephedrin.png":      ("charcoal", (200,220,180)),
        "drug_betel.png":         ("plant_fiber", (160,110,60)),
        "drug_kava.png":          ("tree_sap", (170,165,150)),
        "drug_lsd.png":           ("empty_potion_bottle", (255,80,220)),
        "drug_overdose.png":      ("charcoal", (200,40,40)),
        "drug_crash.png":         ("charcoal", (220,60,60)),
    }
    for name, (vanilla_base, rgb) in status_map.items():
        base = load_vanilla(vanilla_base)
        if base:
            icon = tint(base.resize((16,16), Image.NEAREST), rgb, 0.75)
            save(icon, DST_STATUS, name)
        else:
            print(f"  ⚠ {name} — Basis '{vanilla_base}' nicht gefunden")

    print("\n" + "=" * 60)
    print("FERTIG!")
    print(f"Items:     {len(os.listdir(DST_ITEMS))} Dateien in {DST_ITEMS}")
    print(f"Blocks:    {len(os.listdir(DST_BLOCKS))} Dateien in {DST_BLOCKS}")
    print(f"Kategorien: {len(os.listdir(DST_CATEGORIES))} Dateien in {DST_CATEGORIES}")
    print(f"StatusFX:  {len(os.listdir(DST_STATUS))} Dateien in {DST_STATUS}")
    print("=" * 60)
    print("\n⚠ NACHBearbeitung nötig:")
    print("1. Get Hy! Assets für Cannabis Buds (15) + Joints (5) manuell kopieren")
    print("2. Fehlende Vanilla-Texturen in scripts/vanilla_textures/ ablegen")
    print("3. Prüfen: python3 scripts/check_missing.py")


if __name__ == "__main__":
    main()