#!/usr/bin/env python3
"""Check which required textures are missing vs. README/bibel.md spec."""

import os

# ─── REQUIRED FROM README.md ─────────────────────────────────────────────
REQUIRED_ITEMS = [
    # Währung
    "essence_shadow.png",
    # Seeds
    "cannabis_seed_sativa.png", "cannabis_seed_indica.png", "cannabis_seed_hybrid.png",
    # Buds (15)
    "cannabis_bud_sativa_junk.png", "cannabis_bud_sativa_street.png", "cannabis_bud_sativa_dispensary.png",
    "cannabis_bud_sativa_exotic.png", "cannabis_bud_sativa_god.png",
    "cannabis_bud_indica_junk.png", "cannabis_bud_indica_street.png", "cannabis_bud_indica_dispensary.png",
    "cannabis_bud_indica_exotic.png", "cannabis_bud_indica_god.png",
    "cannabis_bud_hybrid_junk.png", "cannabis_bud_hybrid_street.png", "cannabis_bud_hybrid_dispensary.png",
    "cannabis_bud_hybrid_exotic.png", "cannabis_bud_hybrid_god.png",
    # Verarbeitetes Cannabis
    "dried_cannabis.png", "haschisch.png", "joint.png", "blunt.png", "spliff.png",
    # Pilze
    "pilz_pulver.png", "psilocybin_tinktur.png", "amanita_pulver.png",
    # Mohn
    "mohn_kapsel.png", "mohn_samen.png", "rohopium.png",
    # Papier
    "paper.png", "filter_paper.png",
    # Coca
    "coca_leaves.png", "coca_seed.png", "coca_paste.png", "cocaine.png", "crack.png",
    # Opiate
    "morphine.png", "heroin.png",
    # Meth/Stimulanzien
    "meth.png", "mdma_powder.png", "mdma_pill.png",
    # Kakteen/Psychedelika
    "peyote_bud.png", "peyote_seed.png", "meskalin_extract.png",
    # Khat
    "khat_leaves.png", "khat_seed.png",
    # Nachtschatten
    "datura_leaves.png", "datura_seed.png", "scopolamin_extract.png",
    # Salvia
    "salvia_leaves.png", "salvia_seed.png", "salvinorin.png",
    # Chemikalien
    "ethanol.png", "aceton.png", "schwefelsaeure.png", "salzsaeure.png", "ammoniak.png", "ether.png",
    "lithium_powder.png", "pill_press_form.png",
    # Spritzen
    "empty_syringe.png", "filled_syringe.png",
    # Getränke/Essen
    "koka_tee.png", "cannabis_butter.png",
    # Phase 3
    "iboga_root.png", "iboga_seed.png", "ibogain_extract.png",
    "ephedra_stem.png", "ephedra_seed.png", "ephedrin_powder.png",
    "betel_nut.png", "betel_seed.png",
    "kava_root.png", "kava_paste.png",
    "mutterkorn.png", "lysergsaeure.png", "lsd_tab.png", "naloxon.png",
]

REQUIRED_CATEGORIES = [
    "OrbisUnderground.png",
    "OrbisUnderground_Currency.png",
    "OrbisUnderground_Seeds.png",
    "OrbisUnderground_Materials.png",
    "OrbisUnderground_Consumables.png",
    "OrbisUnderground_Chemicals.png",
    "OrbisUnderground_Tools.png",
]

REQUIRED_STATUS = [
    "drug_cannabis.png", "drug_hashish.png", "drug_psilocybin.png", "drug_amanita.png",
    "drug_cocaine.png", "drug_crack.png", "drug_morphine.png", "drug_heroin.png",
    "drug_meth.png", "drug_mdma.png", "drug_mescaline.png", "drug_scopolamine.png",
    "drug_salvinorin.png", "drug_khat.png", "drug_ibogaine.png", "drug_ephedrin.png",
    "drug_betel.png", "drug_kava.png", "drug_lsd.png", "drug_overdose.png", "drug_crash.png",
]

REQUIRED_BLOCKS = [
    "bench_botany.png",
    "bench_chemistry.png",
]

def check_folder(folder: str, required: list, label: str):
    if not os.path.exists(folder):
        print(f"\n{label}: ORDNER FEHLT ({folder})")
        return len(required)
    existing = set(os.listdir(folder))
    missing = [f for f in required if f not in existing]
    extra = [f for f in existing if f not in required and not f.startswith('.')]
    print(f"\n{label} ({len(existing)}/{len(required)}):")
    if missing:
        print(f"  FEHLEND ({len(missing)}):")
        for m in missing:
            print(f"    - {m}")
    else:
        print("  ✓ Alle vorhanden")
    if extra:
        print(f"  EXTRA ({len(extra)}): {', '.join(extra[:10])}{'...' if len(extra)>10 else ''}")
    return len(missing)

def main():
    base = "/home/user/orbis_underground"
    total_missing = 0
    total_missing += check_folder(f"{base}/Common/Icons/ItemsGenerated", REQUIRED_ITEMS, "ITEMS (16x16)")
    total_missing += check_folder(f"{base}/Common/Icons/ItemCategories", REQUIRED_CATEGORIES, "KATEGORIEN (32x32)")
    total_missing += check_folder(f"{base}/Common/Icons/UI/StatusEffects", REQUIRED_STATUS, "STATUS-EFFEKTE (16x16)")
    total_missing += check_folder(f"{base}/Common/BlockTextures/orbis_underground", REQUIRED_BLOCKS, "BLOCK-TEXTUREN")
    
    print(f"\n{'='*50}")
    print(f"GESAMT FEHLEND: {total_missing}")
    if total_missing == 0:
        print("🎉 ALLE TEXTUREN VORHANDEN!")
    else:
        print("⚠ Führe recolor.py aus und kopiere Get Hy! Assets")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()