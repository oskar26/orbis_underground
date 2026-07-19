#!/usr/bin/env python3
"""
Orbis Underground — asset-first texture prep script

Ziel:
- Nimmt die ORIGINALEN Hytale-Assets aus einem lokalen Assets-Ordner.
- Recolort nur die Texturen, die für Orbis Underground gebraucht werden.
- Kopiert optionale Get-Hy-Assets (Cannabis-Buds / Joints / Modelle) automatisch.
- Vermeidet Platzhalter standardmäßig. Platzhalter sind nur per Flag erlaubt.

Beispiel:
    python3 scripts/recolor.py \
        --assets-dir /home/oskar/hytale_underground/Assets \
        --get-hy-dir /home/oskar/Downloads/get_hy

Falls dein Repo selbst in /home/oskar/hytale_underground liegt und dort ein
Unterordner Assets existiert, reicht meistens schon:
    python3 scripts/recolor.py
"""

from __future__ import annotations

import argparse
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

from PIL import Image


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent

DST_ITEMS = REPO_ROOT / "Common" / "Icons" / "ItemsGenerated"
DST_BLOCKS = REPO_ROOT / "Common" / "BlockTextures" / "orbis_underground"
DST_CATEGORIES = REPO_ROOT / "Common" / "Icons" / "ItemCategories"
DST_STATUS = REPO_ROOT / "Common" / "Icons" / "UI" / "StatusEffects"
DST_BUD_MODELS = REPO_ROOT / "Common" / "Items" / "Cannabis"

for folder in (DST_ITEMS, DST_BLOCKS, DST_CATEGORIES, DST_STATUS, DST_BUD_MODELS):
    folder.mkdir(parents=True, exist_ok=True)


# ─────────────────────────────────────────────────────────────────────────────
# Farb-Helfer
# ─────────────────────────────────────────────────────────────────────────────

def hue_shift(img: Image.Image, degrees: int) -> Image.Image:
    hsv = img.convert("HSV")
    h, s, v = hsv.split()
    shift = int(degrees * 255 / 360)
    h = h.point(lambda x: (x + shift) % 256)
    return Image.merge("HSV", (h, s, v)).convert("RGBA")


def tint(img: Image.Image, rgb: tuple[int, int, int], alpha: float = 0.65) -> Image.Image:
    base = img.convert("RGBA")
    overlay = Image.new("RGBA", img.size, rgb + (int(255 * alpha),))
    return Image.alpha_composite(base, overlay)


def darken(img: Image.Image, factor: float = 0.85) -> Image.Image:
    base = img.convert("RGBA")
    out = Image.new("RGBA", base.size)
    in_px = base.load()
    out_px = out.load()
    for y in range(base.height):
        for x in range(base.width):
            r, g, b, a = in_px[x, y]
            out_px[x, y] = (int(r * factor), int(g * factor), int(b * factor), a)
    return out


def resize_nearest(img: Image.Image, size: tuple[int, int]) -> Image.Image:
    return img.resize(size, Image.NEAREST)


# ─────────────────────────────────────────────────────────────────────────────
# Placeholder-Helfer (nur optional)
# ─────────────────────────────────────────────────────────────────────────────

def create_simple_icon(color_rgb: tuple[int, int, int], shape: str = "circle", size: int = 16) -> Image.Image:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    p = img.load()
    cx, cy = size // 2, size // 2
    r = size // 2 - 2
    r_c, g_c, b_c = color_rgb

    for y in range(size):
        for x in range(size):
            dx, dy = x - cx, y - cy
            dist = (dx * dx + dy * dy) ** 0.5
            if shape == "circle":
                if dist <= r:
                    shade = 1.0 - (dist / r) * 0.3
                    p[x, y] = (int(r_c * shade), int(g_c * shade), int(b_c * shade), 255)
                elif dist <= r + 1:
                    p[x, y] = (int(r_c * 0.5), int(g_c * 0.5), int(b_c * 0.5), 200)
            elif shape == "square":
                if 2 <= x <= size - 3 and 2 <= y <= size - 3:
                    p[x, y] = (r_c, g_c, b_c, 255)
    return img


def create_botanical_table_texture() -> Image.Image:
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    p = img.load()

    WOOD_DARK = (82, 57, 38, 255)
    WOOD_MED = (125, 85, 55, 255)
    WOOD_LIGHT = (158, 112, 75, 255)
    STONE_GRAY = (128, 128, 128, 255)
    STONE_DARK = (90, 90, 90, 255)
    STONE_LIGHT = (160, 160, 160, 255)
    PESTLE = (140, 120, 100, 255)
    LEAF_GREEN = (60, 130, 50, 255)
    LEAF_DARK = (40, 90, 30, 255)
    METAL = (180, 170, 160, 255)

    for y in range(5, 14):
        for x in range(16):
            if y < 7:
                p[x, y] = WOOD_LIGHT
            elif y < 12:
                p[x, y] = WOOD_MED
            else:
                p[x, y] = WOOD_DARK

    for y in range(5, 16):
        for x in [0, 1, 2, 13, 14, 15]:
            p[x, y] = WOOD_DARK

    for y in range(2, 6):
        for x in range(10, 14):
            if y == 2:
                p[x, y] = STONE_LIGHT
            elif y == 5:
                if x in [11, 12]:
                    p[x, y] = STONE_DARK
            else:
                p[x, y] = STONE_GRAY if x in [10, 13] else STONE_DARK

    p[9, 2] = PESTLE
    p[9, 3] = PESTLE
    p[10, 1] = PESTLE

    p[2, 1] = METAL
    p[4, 1] = METAL

    for ly in range(2, 5):
        p[2, ly] = LEAF_GREEN
        p[3, ly] = LEAF_DARK
        p[4, ly] = LEAF_GREEN

    for y in range(8, 10):
        for x in range(6, 9):
            p[x, y] = (230, 225, 210, 255)

    return img


# ─────────────────────────────────────────────────────────────────────────────
# Datenmodell / Suche
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class RunContext:
    assets_roots: list[Path]
    get_hy_roots: list[Path]
    allow_placeholders: bool = False
    verbose: bool = False
    _asset_index: dict[str, list[Path]] = field(default_factory=dict)
    _get_hy_index: dict[str, list[Path]] = field(default_factory=dict)
    missing_sources: list[str] = field(default_factory=list)
    copied_get_hy: list[str] = field(default_factory=list)
    generated_files: list[Path] = field(default_factory=list)

    def build_index(self, roots: list[Path]) -> dict[str, list[Path]]:
        index: dict[str, list[Path]] = {}
        for root in roots:
            if not root.exists():
                continue
            for path in root.rglob("*"):
                if not path.is_file():
                    continue
                key = path.name.lower()
                index.setdefault(key, []).append(path)
        return index

    @property
    def asset_index(self) -> dict[str, list[Path]]:
        if not self._asset_index:
            self._asset_index = self.build_index(self.assets_roots)
        return self._asset_index

    @property
    def get_hy_index(self) -> dict[str, list[Path]]:
        if not self._get_hy_index:
            self._get_hy_index = self.build_index(self.get_hy_roots)
        return self._get_hy_index


def default_assets_candidates() -> list[Path]:
    return [
        REPO_ROOT / "Assets",
        SCRIPT_DIR / "vanilla_textures",
    ]


def default_get_hy_candidates() -> list[Path]:
    home = Path.home()
    return [
        REPO_ROOT / "get_hy",
        REPO_ROOT.parent / "get_hy",
        home / "Downloads" / "get_hy",
        home / "Downloads" / "get-hy",
        home / "Downloads" / "GetHy",
        home / "Downloads" / "Get Hy",
    ]


def normalize_existing(paths: list[Path]) -> list[Path]:
    seen: set[Path] = set()
    out: list[Path] = []
    for path in paths:
        expanded = path.expanduser().resolve()
        if expanded.exists() and expanded not in seen:
            out.append(expanded)
            seen.add(expanded)
    return out


def choose_best(paths: list[Path]) -> Path:
    def score(path: Path) -> tuple[int, int, str]:
        parts = {p.lower() for p in path.parts}
        bonus = 0
        if "icons" in parts:
            bonus += 3
        if "items" in parts:
            bonus += 2
        if "textures" in parts:
            bonus += 2
        if "common" in parts:
            bonus += 1
        if "assets" in parts:
            bonus += 1
        return (-bonus, len(path.parts), str(path).lower())

    return sorted(paths, key=score)[0]


def find_by_names(index: dict[str, list[Path]], *names: str) -> Path | None:
    matches: list[Path] = []
    for name in names:
        matches.extend(index.get(name.lower(), []))
    return choose_best(matches) if matches else None


def load_png(index: dict[str, list[Path]], label: str, *candidate_names: str) -> Image.Image | None:
    source = find_by_names(index, *candidate_names)
    if not source:
        return None
    print(f"  ✓ Quelle {label}: {source}")
    return Image.open(source).convert("RGBA")


def save_image(img: Image.Image, dest: Path, ctx: RunContext):
    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest)
    ctx.generated_files.append(dest)
    print(f"  ✓ {dest.relative_to(REPO_ROOT)}")


def record_missing(ctx: RunContext, label: str, candidates: list[str]):
    msg = f"{label} (gesucht: {', '.join(candidates)})"
    ctx.missing_sources.append(msg)
    print(f"  ⚠ FEHLT: {msg}")


def ensure_botany_textures(ctx: RunContext):
    root_block = REPO_ROOT / "Common" / "BlockTextures" / "bench_botany.png"
    if root_block.exists():
        img = Image.open(root_block).convert("RGBA")
    else:
        img = create_botanical_table_texture()
        save_image(img, root_block, ctx)
    save_image(img, DST_BLOCKS / "bench_botany.png", ctx)
    save_image(resize_nearest(img, (16, 16)), DST_ITEMS / "bench_botany.png", ctx)


def maybe_save_placeholder(ctx: RunContext, dest: Path, color: tuple[int, int, int], shape: str = "circle"):
    if not ctx.allow_placeholders:
        return
    save_image(create_simple_icon(color, shape), dest, ctx)


# ─────────────────────────────────────────────────────────────────────────────
# Recolor-Mapping
# ─────────────────────────────────────────────────────────────────────────────

def process_vanilla_recolors(ctx: RunContext):
    print("\n[2/5] Recolors aus Hytale-Assets")
    assets = ctx.asset_index

    # 1) Essence
    essence_candidates = ["essence_of_life.png", "essence_of_life_icon.png", "essence_of_life_item.png"]
    essence = load_png(assets, "essence_of_life", *essence_candidates)
    if essence:
        shifted = hue_shift(essence, 180)
        save_image(shifted, DST_ITEMS / "essence_shadow.png", ctx)
        save_image(resize_nearest(shifted, (32, 32)), DST_CATEGORIES / "OrbisUnderground_Currency.png", ctx)
        save_image(resize_nearest(shifted, (32, 32)), DST_CATEGORIES / "OrbisUnderground.png", ctx)
    else:
        record_missing(ctx, "essence_of_life", essence_candidates)
        maybe_save_placeholder(ctx, DST_ITEMS / "essence_shadow.png", (140, 70, 200))

    # 2) Bottle base
    bottle_candidates = ["empty_potion_bottle.png", "empty_potion_bottle_icon.png", "empty_potion_bottle_item.png"]
    bottle = load_png(assets, "empty_potion_bottle", *bottle_candidates)
    bottle_recipes = {
        "ethanol.png": ((220, 220, 240), 0.55),
        "aceton.png": ((240, 220, 140), 0.65),
        "schwefelsaeure.png": ((200, 180, 80), 0.70),
        "salzsaeure.png": ((150, 200, 120), 0.70),
        "ammoniak.png": ((230, 230, 240), 0.50),
        "ether.png": ((150, 170, 220), 0.60),
        "morphine.png": ((230, 225, 215), 0.60),
        "crack.png": ((255, 240, 180), 0.65),
        "mdma_pill.png": ((255, 100, 180), 0.80),
        "meskalin_extract.png": ((180, 150, 110), 0.70),
        "scopolamin_extract.png": ((100, 130, 90), 0.70),
        "salvinorin.png": ((70, 180, 70), 0.70),
        "ibogain_extract.png": ((240, 235, 220), 0.65),
        "naloxon.png": ((230, 240, 250), 0.60),
        "koka_tee.png": ((100, 150, 80), 0.70),
        "cannabis_butter.png": ((200, 200, 140), 0.75),
        "filled_syringe.png": ((190, 160, 130), 0.75),
        "empty_syringe.png": ((220, 220, 230), 0.50),
        "psilocybin_tinktur.png": ((70, 70, 200), 0.75),
        "lysergsaeure.png": ((220, 200, 140), 0.70),
    }
    if bottle:
        for name, (rgb, alpha) in bottle_recipes.items():
            save_image(tint(bottle, rgb, alpha), DST_ITEMS / name, ctx)
    else:
        record_missing(ctx, "empty_potion_bottle", bottle_candidates)
        if ctx.allow_placeholders:
            for name in bottle_recipes:
                maybe_save_placeholder(ctx, DST_ITEMS / name, (200, 200, 230))

    # 3) Tree sap base
    sap_candidates = ["tree_sap.png", "tree_sap_icon.png", "tree_sap_item.png"]
    sap = load_png(assets, "tree_sap", *sap_candidates)
    sap_recipes = [
        ("rohopium.png", (50, 30, 20), 0.85),
        ("haschisch.png", (80, 50, 20), 0.80),
        ("coca_paste.png", (210, 210, 200), 0.70),
        ("kava_paste.png", (170, 165, 150), 0.75),
    ]
    if sap:
        for name, rgb, alpha in sap_recipes:
            save_image(tint(sap, rgb, alpha), DST_ITEMS / name, ctx)
    else:
        record_missing(ctx, "tree_sap", sap_candidates)
        if ctx.allow_placeholders:
            for name, rgb, _ in sap_recipes:
                maybe_save_placeholder(ctx, DST_ITEMS / name, rgb, "square")

    # 4) Charcoal base
    charcoal_candidates = ["charcoal.png", "charcoal_icon.png", "charcoal_item.png"]
    charcoal = load_png(assets, "charcoal", *charcoal_candidates)
    charcoal_recipes = [
        ("pilz_pulver.png", (140, 120, 90), 0.75),
        ("amanita_pulver.png", (180, 100, 60), 0.75),
        ("cocaine.png", (255, 255, 255), 0.50),
        ("heroin.png", (210, 190, 160), 0.70),
        ("lithium_powder.png", (200, 200, 210), 0.65),
        ("ephedrin_powder.png", (200, 220, 180), 0.65),
        ("mdma_powder.png", (210, 190, 170), 0.65),
        ("mutterkorn.png", (70, 50, 40), 0.80),
        ("meth.png", (180, 200, 240), 0.70),
    ]
    if charcoal:
        for name, rgb, alpha in charcoal_recipes:
            save_image(tint(charcoal, rgb, alpha), DST_ITEMS / name, ctx)
    else:
        record_missing(ctx, "charcoal", charcoal_candidates)
        if ctx.allow_placeholders:
            for name, rgb, _ in charcoal_recipes:
                maybe_save_placeholder(ctx, DST_ITEMS / name, rgb)

    # 5) Plant fiber base
    fiber_candidates = ["plant_fiber.png", "plant_fiber_icon.png", "plant_fiber_item.png"]
    fiber = load_png(assets, "plant_fiber", *fiber_candidates)
    fiber_recipes = [
        ("paper.png", (240, 240, 235), 0.60),
        ("filter_paper.png", (180, 180, 175), 0.65),
        ("lsd_tab.png", (255, 80, 220), 0.78),
        ("coca_leaves.png", (40, 100, 30), 0.80),
        ("khat_leaves.png", (140, 210, 100), 0.75),
        ("datura_leaves.png", (50, 90, 40), 0.80),
        ("salvia_leaves.png", (60, 150, 60), 0.80),
        ("peyote_bud.png", (160, 170, 140), 0.75),
        ("iboga_root.png", (130, 90, 50), 0.80),
        ("kava_root.png", (140, 110, 90), 0.80),
        ("ephedra_stem.png", (170, 190, 130), 0.75),
        ("betel_nut.png", (160, 110, 60), 0.80),
        ("dried_cannabis.png", (100, 140, 70), 0.80),
        ("mohn_kapsel.png", (100, 120, 80), 0.80),
    ]
    if fiber:
        for name, rgb, alpha in fiber_recipes:
            save_image(tint(fiber, rgb, alpha), DST_ITEMS / name, ctx)
    else:
        record_missing(ctx, "plant_fiber", fiber_candidates)
        if ctx.allow_placeholders:
            for name, rgb, _ in fiber_recipes:
                maybe_save_placeholder(ctx, DST_ITEMS / name, rgb)

    # 6) Seed bag base
    seedbag_candidates = ["wheat_seed_bag.png", "wheat_seed_bag_icon.png", "wheat_seed_bag_item.png"]
    seedbag = load_png(assets, "wheat_seed_bag", *seedbag_candidates)
    seed_recipes = [
        ("cannabis_seed_sativa.png", (80, 160, 60), 0.75),
        ("cannabis_seed_indica.png", (60, 130, 50), 0.75),
        ("cannabis_seed_hybrid.png", (70, 150, 70), 0.75),
        ("coca_seed.png", (60, 140, 50), 0.75),
        ("peyote_seed.png", (120, 100, 70), 0.75),
        ("khat_seed.png", (100, 160, 70), 0.75),
        ("datura_seed.png", (40, 70, 30), 0.80),
        ("salvia_seed.png", (40, 110, 40), 0.80),
        ("iboga_seed.png", (100, 70, 30), 0.80),
        ("ephedra_seed.png", (130, 150, 90), 0.75),
        ("betel_seed.png", (120, 80, 40), 0.80),
        ("mohn_samen.png", (40, 40, 40), 0.80),
    ]
    if seedbag:
        for name, rgb, alpha in seed_recipes:
            save_image(tint(seedbag, rgb, alpha), DST_ITEMS / name, ctx)
        save_image(resize_nearest(tint(seedbag, (80, 160, 60), 0.70), (32, 32)), DST_CATEGORIES / "OrbisUnderground_Seeds.png", ctx)
    else:
        record_missing(ctx, "wheat_seed_bag", seedbag_candidates)

    # 7) Iron ingot -> Tools category
    iron_candidates = ["iron_ingot.png", "iron_ingot_icon.png", "iron_ingot_item.png"]
    iron = load_png(assets, "iron_ingot", *iron_candidates)
    if iron:
        save_image(tint(iron, (160, 150, 140), 0.65), DST_ITEMS / "pill_press_form.png", ctx)
        save_image(resize_nearest(tint(iron, (190, 160, 130), 0.70), (32, 32)), DST_CATEGORIES / "OrbisUnderground_Tools.png", ctx)
    else:
        record_missing(ctx, "iron_ingot", iron_candidates)
        maybe_save_placeholder(ctx, DST_ITEMS / "pill_press_form.png", (160, 150, 140), "square")

    # 8) Category icons from existing bases
    if fiber:
        save_image(resize_nearest(tint(fiber, (60, 130, 40), 0.70), (32, 32)), DST_CATEGORIES / "OrbisUnderground_Materials.png", ctx)
    if bottle:
        save_image(resize_nearest(tint(bottle, (255, 100, 180), 0.80), (32, 32)), DST_CATEGORIES / "OrbisUnderground_Consumables.png", ctx)
        save_image(resize_nearest(tint(bottle, (150, 170, 220), 0.70), (32, 32)), DST_CATEGORIES / "OrbisUnderground_Chemicals.png", ctx)

    # 9) Status effect icons
    blue_mushroom_candidates = ["blue_glowing_mushroom.png", "blue_glowing_mushroom_icon.png"]
    bloodcap_candidates = ["bloodcap_mushroom.png", "bloodcap_mushroom_icon.png"]
    blue_mushroom = load_png(assets, "blue_glowing_mushroom", *blue_mushroom_candidates)
    bloodcap = load_png(assets, "bloodcap_mushroom", *bloodcap_candidates)

    status_map: dict[str, tuple[Image.Image | None, tuple[int, int, int]]] = {
        "drug_cannabis.png": (fiber, (60, 130, 40)),
        "drug_hashish.png": (charcoal, (80, 50, 20)),
        "drug_psilocybin.png": (blue_mushroom, (70, 70, 200)),
        "drug_amanita.png": (bloodcap, (180, 60, 40)),
        "drug_cocaine.png": (charcoal, (255, 255, 255)),
        "drug_crack.png": (charcoal, (255, 240, 180)),
        "drug_morphine.png": (bottle, (230, 225, 215)),
        "drug_heroin.png": (bottle, (210, 190, 160)),
        "drug_meth.png": (charcoal, (180, 200, 240)),
        "drug_mdma.png": (bottle, (255, 100, 180)),
        "drug_mescaline.png": (bottle, (180, 150, 110)),
        "drug_scopolamine.png": (bottle, (100, 130, 90)),
        "drug_salvinorin.png": (bottle, (70, 180, 70)),
        "drug_khat.png": (fiber, (140, 210, 100)),
        "drug_ibogaine.png": (fiber, (130, 90, 50)),
        "drug_ephedrin.png": (charcoal, (200, 220, 180)),
        "drug_betel.png": (fiber, (160, 110, 60)),
        "drug_kava.png": (sap, (170, 165, 150)),
        "drug_lsd.png": (bottle, (255, 80, 220)),
        "drug_overdose.png": (charcoal, (200, 40, 40)),
        "drug_crash.png": (charcoal, (220, 60, 60)),
    }
    for name, (base, rgb) in status_map.items():
        if base is not None:
            save_image(tint(resize_nearest(base, (16, 16)), rgb, 0.75), DST_STATUS / name, ctx)
        elif ctx.verbose:
            print(f"  ⚠ Status-Icon übersprungen: {name}")

    # 10) Chemistry bench from alchemist workbench
    alch_candidates = [
        "alchemist_workbench.png",
        "alchemist_workbench_icon.png",
        "alchemy_workbench.png",
        "alchemist_bench.png",
    ]
    alch = load_png(assets, "alchemist_workbench", *alch_candidates)
    if alch:
        chem = darken(hue_shift(alch, 270), 0.85)
        save_image(chem, DST_BLOCKS / "bench_chemistry.png", ctx)
        save_image(resize_nearest(chem, (16, 16)), DST_ITEMS / "bench_chemistry.png", ctx)
    else:
        record_missing(ctx, "alchemist_workbench", alch_candidates)


def copy_get_hy_assets(ctx: RunContext):
    print("\n[3/5] Get Hy! Assets übernehmen")
    if not ctx.get_hy_roots:
        print("  ⚠ Kein Get-Hy-Ordner gefunden/angegeben. Überspringe Kopien.")
        return

    index = ctx.get_hy_index

    bud_icons = [
        "cannabis_bud_sativa_junk.png",
        "cannabis_bud_sativa_street.png",
        "cannabis_bud_sativa_dispensary.png",
        "cannabis_bud_sativa_exotic.png",
        "cannabis_bud_sativa_god.png",
        "cannabis_bud_indica_junk.png",
        "cannabis_bud_indica_street.png",
        "cannabis_bud_indica_dispensary.png",
        "cannabis_bud_indica_exotic.png",
        "cannabis_bud_indica_god.png",
        "cannabis_bud_hybrid_junk.png",
        "cannabis_bud_hybrid_street.png",
        "cannabis_bud_hybrid_dispensary.png",
        "cannabis_bud_hybrid_exotic.png",
        "cannabis_bud_hybrid_god.png",
        "joint.png",
        "blunt.png",
        "spliff.png",
    ]

    for filename in bud_icons:
        src = find_by_names(index, filename)
        if src:
            dest = DST_ITEMS / filename
            shutil.copy2(src, dest)
            ctx.copied_get_hy.append(filename)
            print(f"  ✓ kopiert: {src} -> {dest.relative_to(REPO_ROOT)}")
        else:
            record_missing(ctx, f"Get Hy icon {filename}", [filename])
            fallback_colors = {
                "joint.png": (200, 180, 150),
                "blunt.png": (140, 100, 60),
                "spliff.png": (180, 160, 130),
            }
            if filename.startswith("cannabis_bud_"):
                maybe_save_placeholder(ctx, DST_ITEMS / filename, (95, 145, 60))
            elif filename in fallback_colors:
                maybe_save_placeholder(ctx, DST_ITEMS / filename, fallback_colors[filename], "square")

    # Optionale Bud-Modelle, falls im Get-Hy-Paket vorhanden
    bud_models = [
        "cannabis_bud_sativa.blockymodel",
        "cannabis_bud_indica.blockymodel",
        "cannabis_bud_hybrid.blockymodel",
    ]
    for filename in bud_models:
        src = find_by_names(index, filename)
        if src:
            dest = DST_BUD_MODELS / filename
            shutil.copy2(src, dest)
            ctx.copied_get_hy.append(filename)
            print(f"  ✓ kopiert: {src} -> {dest.relative_to(REPO_ROOT)}")
        else:
            print(f"  • optional nicht gefunden: {filename}")


def ensure_static_assets(ctx: RunContext):
    print("\n[1/5] Statische Mod-Assets sichern")
    ensure_botany_textures(ctx)


def summarize(ctx: RunContext):
    print("\n[4/5] Zusammenfassung")
    print(f"  Ausgabedateien aktualisiert: {len(ctx.generated_files)}")
    print(f"  Get-Hy-Dateien kopiert:      {len(ctx.copied_get_hy)}")
    print(f"  Fehlende Quellen:            {len(ctx.missing_sources)}")
    if ctx.assets_roots:
        print("  Asset-Quellen:")
        for root in ctx.assets_roots:
            print(f"    - {root}")
    if ctx.get_hy_roots:
        print("  Get-Hy-Quellen:")
        for root in ctx.get_hy_roots:
            print(f"    - {root}")

    if ctx.missing_sources:
        print("\n  Fehlende Quellen im Detail:")
        for item in ctx.missing_sources:
            print(f"    - {item}")


def print_next_steps():
    print("\n[5/5] Nächste Schritte")
    print("  1. python3 scripts/check_missing.py")
    print("  2. Fehlt noch etwas? Dann die fehlenden Dateien im Assets- oder Get-Hy-Ordner suchen.")
    print("  3. Danach den ganzen Mod-Ordner nach Hytale/UserData/Packs kopieren.")
    print("  4. In Hytale Pack aktivieren und mit /give essence_shadow 64 testen.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Recolor Hytale-Assets und übernehme Get-Hy-Assets automatisch.")
    parser.add_argument(
        "--assets-dir",
        action="append",
        default=[],
        help="Pfad zu einem Hytale-Assets-Ordner. Kann mehrfach angegeben werden.",
    )
    parser.add_argument(
        "--get-hy-dir",
        action="append",
        default=[],
        help="Pfad zum entpackten Get-Hy-Ordner. Kann mehrfach angegeben werden.",
    )
    parser.add_argument(
        "--allow-placeholders",
        action="store_true",
        help="Erlaubt einfache Platzhalter für nicht gefundene Dateien. Standardmäßig AUS.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Mehr Logs ausgeben.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    asset_candidates = [Path(p) for p in args.assets_dir] if args.assets_dir else default_assets_candidates()
    get_hy_candidates = [Path(p) for p in args.get_hy_dir] if args.get_hy_dir else default_get_hy_candidates()

    ctx = RunContext(
        assets_roots=normalize_existing(asset_candidates),
        get_hy_roots=normalize_existing(get_hy_candidates),
        allow_placeholders=args.allow_placeholders,
        verbose=args.verbose,
    )

    print("=" * 72)
    print("Orbis Underground — Asset-first Recolor Setup")
    print("=" * 72)
    print(f"Repo: {REPO_ROOT}")
    print(f"Placeholders erlaubt: {'JA' if ctx.allow_placeholders else 'NEIN'}")

    if not ctx.assets_roots:
        print("⚠ Kein Assets-Ordner gefunden.")
        print("  Standardmäßig gesucht wurde nach:")
        for p in default_assets_candidates():
            print(f"    - {p}")
        print("  Nutze sonst: python3 scripts/recolor.py --assets-dir /pfad/zu/Assets")
    else:
        print("Asset-Ordner:")
        for root in ctx.assets_roots:
            print(f"  - {root}")

    if ctx.get_hy_roots:
        print("Get-Hy-Ordner:")
        for root in ctx.get_hy_roots:
            print(f"  - {root}")
    else:
        print("Get-Hy-Ordner: keiner gefunden (optional, aber für Cannabis empfohlen)")

    ensure_static_assets(ctx)
    process_vanilla_recolors(ctx)
    copy_get_hy_assets(ctx)
    summarize(ctx)
    print_next_steps()

    print("\n" + "=" * 72)
    if ctx.missing_sources and not ctx.allow_placeholders:
        print("FERTIG MIT WARNUNGEN: Es fehlen noch Originalquellen. Keine Platzhalter erzeugt.")
        print("=" * 72)
        return 2

    print("FERTIG")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main())
