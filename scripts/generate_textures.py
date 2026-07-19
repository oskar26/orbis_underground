#!/usr/bin/env python3
"""
Orbis Underground — Texture Generator
Generates textures for all custom blocks and items.
Uses PIL to create pixel-art textures programmatically.
"""

from PIL import Image
import os

OUTPUT = "../Common"

def create_botanical_table_texture():
    """
    Generate a 16x16 pixel art texture for the Botanical Table.
    Design: Wooden table surface with mortar (gray bowl + pestle) on the right
    and a small drying rack with hanging green leaves on the left.
    Color palette borrowed from Alchemist's Workbench vibes.
    """
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    p = img.load()

    # Colors
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

    # Table top surface (rows 4-13, columns 0-15)
    for y in range(5, 14):
        for x in range(16):
            if y < 7:
                p[x, y] = WOOD_LIGHT  # top edge
            elif y < 12:
                p[x, y] = WOOD_MED  # middle
            else:
                p[x, y] = WOOD_DARK  # bottom shadow

    # Table legs (columns 0-3 and 12-15, rows 5-15)
    for y in range(5, 16):
        for x in [0, 1, 2, 13, 14, 15]:
            p[x, y] = WOOD_DARK

    # Mortar bowl (right side, columns 10-13, rows 2-5)
    for y in range(2, 6):
        for x in range(10, 14):
            if y == 2:  # rim
                p[x, y] = STONE_LIGHT
            elif y == 5:  # bottom
                if x in [11, 12]:
                    p[x, y] = STONE_DARK
            else:
                if x in [10, 13]:
                    p[x, y] = STONE_GRAY
                else:
                    p[x, y] = STONE_DARK

    # Pestle (diagonal stick above mortar)
    p[9, 2] = PESTLE
    p[9, 3] = PESTLE
    p[10, 1] = PESTLE

    # Drying rack hooks (left side, columns 2-4)
    p[2, 1] = METAL
    p[4, 1] = METAL

    # Hanging leaves from rack
    for ly in range(2, 5):
        p[2, ly] = LEAF_GREEN
        p[3, ly] = LEAF_DARK
        p[4, ly] = LEAF_GREEN

    # Paper/parchment on table (center-left)
    for y in range(8, 10):
        for x in range(6, 9):
            p[x, y] = (230, 225, 210, 255)

    os.makedirs(os.path.join(OUTPUT, "BlockTextures"), exist_ok=True)
    img.save(os.path.join(OUTPUT, "BlockTextures", "bench_botany.png"))
    print("  ✓ Common/BlockTextures/bench_botany.png")

    # Also save as item icon
    os.makedirs(os.path.join(OUTPUT, "Icons", "ItemsGenerated"), exist_ok=True)
    img.save(os.path.join(OUTPUT, "Icons", "ItemsGenerated", "bench_botany.png"))
    print("  ✓ Common/Icons/ItemsGenerated/bench_botany.png")


def create_simple_icon(filename, color_rgb, shape="circle", size=16):
    """Create a simple colored icon for placeholder use."""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
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
                    alpha = 255
                    p[x, y] = (int(r_c * shade), int(g_c * shade), int(b_c * shade), alpha)
                elif dist <= r + 1:
                    p[x, y] = (int(r_c * 0.5), int(g_c * 0.5), int(b_c * 0.5), 200)
            elif shape == "square":
                if 2 <= x <= size - 3 and 2 <= y <= size - 3:
                    p[x, y] = (r_c, g_c, b_c, 255)

    os.makedirs(os.path.join(OUTPUT, "Icons", "ItemsGenerated"), exist_ok=True)
    img.save(os.path.join(OUTPUT, "Icons", "ItemsGenerated", filename))
    print(f"  ✓ Common/Icons/ItemsGenerated/{filename}")


def generate_all_icons():
    """Generate all placeholder icons with distinct colors."""
    icons = {
        # Phase 1
        "essence_shadow.png": ((140, 70, 200), "circle"),
        "cannabis_seed_sativa.png": ((80, 160, 60), "circle"),
        "cannabis_seed_indica.png": ((60, 130, 50), "circle"),
        "cannabis_seed_hybrid.png": ((70, 150, 70), "circle"),
        "dried_cannabis.png": ((100, 140, 70), "circle"),
        "haschisch.png": ((80, 50, 20), "square"),
        "joint.png": ((200, 180, 150), "circle"),
        "blunt.png": ((140, 100, 60), "circle"),
        "spliff.png": ((180, 160, 130), "circle"),
        "pilz_pulver.png": ((140, 120, 90), "circle"),
        "psilocybin_tinktur.png": ((70, 70, 200), "circle"),
        "mohn_kapsel.png": ((100, 120, 80), "circle"),
        "mohn_samen.png": ((40, 40, 40), "circle"),
        "rohopium.png": ((50, 30, 20), "square"),
        "paper.png": ((240, 240, 235), "square"),
        "filter_paper.png": ((180, 180, 175), "square"),
        # Buds (5 tiers x 3 strains)
        "cannabis_bud_sativa_junk.png": ((70, 120, 40), "circle"),
        "cannabis_bud_sativa_street.png": ((85, 140, 50), "circle"),
        "cannabis_bud_sativa_dispensary.png": ((100, 155, 60), "circle"),
        "cannabis_bud_sativa_exotic.png": ((115, 170, 70), "circle"),
        "cannabis_bud_sativa_god.png": ((130, 190, 80), "circle"),
        "cannabis_bud_indica_junk.png": ((50, 100, 30), "circle"),
        "cannabis_bud_indica_street.png": ((60, 115, 40), "circle"),
        "cannabis_bud_indica_dispensary.png": ((70, 130, 50), "circle"),
        "cannabis_bud_indica_exotic.png": ((85, 150, 60), "circle"),
        "cannabis_bud_indica_god.png": ((100, 170, 70), "circle"),
        "cannabis_bud_hybrid_junk.png": ((60, 115, 50), "circle"),
        "cannabis_bud_hybrid_street.png": ((75, 130, 60), "circle"),
        "cannabis_bud_hybrid_dispensary.png": ((90, 145, 70), "circle"),
        "cannabis_bud_hybrid_exotic.png": ((105, 160, 80), "circle"),
        "cannabis_bud_hybrid_god.png": ((120, 180, 90), "circle"),
        # Phase 2
        "coca_leaves.png": ((40, 100, 30), "circle"),
        "coca_seed.png": ((60, 140, 50), "circle"),
        "coca_paste.png": ((210, 210, 200), "square"),
        "cocaine.png": ((250, 250, 248), "circle"),
        "crack.png": ((255, 240, 180), "circle"),
        "morphine.png": ((230, 225, 215), "circle"),
        "heroin.png": ((210, 190, 160), "circle"),
        "meth.png": ((180, 200, 240), "circle"),
        "mdma_powder.png": ((210, 190, 170), "circle"),
        "mdma_pill.png": ((255, 100, 180), "circle"),
        "peyote_bud.png": ((160, 170, 140), "circle"),
        "peyote_seed.png": ((120, 100, 70), "circle"),
        "meskalin_extract.png": ((180, 150, 110), "circle"),
        "khat_leaves.png": ((140, 210, 100), "circle"),
        "khat_seed.png": ((100, 160, 70), "circle"),
        "datura_leaves.png": ((50, 90, 40), "circle"),
        "datura_seed.png": ((40, 70, 30), "circle"),
        "salvia_leaves.png": ((60, 150, 60), "circle"),
        "salvia_seed.png": ((40, 110, 40), "circle"),
        "scopolamin_extract.png": ((100, 130, 90), "circle"),
        "salvinorin.png": ((70, 180, 70), "circle"),
        "ethanol.png": ((220, 220, 240), "circle"),
        "aceton.png": ((240, 220, 140), "circle"),
        "schwefelsaeure.png": ((200, 180, 80), "circle"),
        "salzsaeure.png": ((150, 200, 120), "circle"),
        "ammoniak.png": ((230, 230, 240), "circle"),
        "ether.png": ((150, 170, 220), "circle"),
        "lithium_powder.png": ((200, 200, 210), "circle"),
        "pill_press_form.png": ((160, 150, 140), "square"),
        "empty_syringe.png": ((220, 220, 230), "circle"),
        "filled_syringe.png": ((190, 160, 130), "circle"),
        "koka_tee.png": ((100, 150, 80), "circle"),
        "cannabis_butter.png": ((200, 200, 140), "square"),
        # Phase 3
        "iboga_root.png": ((130, 90, 50), "square"),
        "iboga_seed.png": ((100, 70, 30), "circle"),
        "ibogain_extract.png": ((240, 235, 220), "circle"),
        "ephedra_stem.png": ((170, 190, 130), "circle"),
        "ephedra_seed.png": ((130, 150, 90), "circle"),
        "ephedrin_powder.png": ((200, 220, 180), "circle"),
        "betel_nut.png": ((160, 110, 60), "circle"),
        "betel_seed.png": ((120, 80, 40), "circle"),
        "kava_root.png": ((140, 110, 90), "square"),
        "kava_paste.png": ((170, 165, 150), "square"),
        "mutterkorn.png": ((70, 50, 40), "square"),
        "lysergsaeure.png": ((220, 200, 140), "circle"),
        "lsd_tab.png": ((255, 80, 220), "square"),
        "naloxon.png": ((230, 240, 250), "circle"),
    }
    for filename, (rgb, shape) in icons.items():
        create_simple_icon(filename, rgb, shape)


if __name__ == "__main__":
    print("Orbis Underground — Texture Generator")
    print("=" * 50)
    print("\n[1/2] Generating Botanical Table texture...")
    create_botanical_table_texture()
    print("\n[2/2] Generating item icons...")
    generate_all_icons()
    print("\n" + "=" * 50)
    print("All textures generated!")
    print("NOTE: These are BASIC placeholder icons.")
    print("For final quality, use Get Hy! assets + AI generation.")
