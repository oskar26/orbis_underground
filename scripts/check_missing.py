#!/usr/bin/env python3
"""Prüft fehlende Assets für Orbis Underground (repo-relativ, portabel)."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_ITEMS = [
    "essence_shadow.png",
    "cannabis_seed_sativa.png", "cannabis_seed_indica.png", "cannabis_seed_hybrid.png",
    "cannabis_bud_sativa_junk.png", "cannabis_bud_sativa_street.png", "cannabis_bud_sativa_dispensary.png",
    "cannabis_bud_sativa_exotic.png", "cannabis_bud_sativa_god.png",
    "cannabis_bud_indica_junk.png", "cannabis_bud_indica_street.png", "cannabis_bud_indica_dispensary.png",
    "cannabis_bud_indica_exotic.png", "cannabis_bud_indica_god.png",
    "cannabis_bud_hybrid_junk.png", "cannabis_bud_hybrid_street.png", "cannabis_bud_hybrid_dispensary.png",
    "cannabis_bud_hybrid_exotic.png", "cannabis_bud_hybrid_god.png",
    "dried_cannabis.png", "haschisch.png", "joint.png", "blunt.png", "spliff.png",
    "pilz_pulver.png", "psilocybin_tinktur.png", "amanita_pulver.png",
    "mohn_kapsel.png", "mohn_samen.png", "rohopium.png",
    "paper.png", "filter_paper.png",
    "coca_leaves.png", "coca_seed.png", "coca_paste.png", "cocaine.png", "crack.png",
    "morphine.png", "heroin.png",
    "meth.png", "mdma_powder.png", "mdma_pill.png",
    "peyote_bud.png", "peyote_seed.png", "meskalin_extract.png",
    "khat_leaves.png", "khat_seed.png",
    "datura_leaves.png", "datura_seed.png", "scopolamin_extract.png",
    "salvia_leaves.png", "salvia_seed.png", "salvinorin.png",
    "ethanol.png", "aceton.png", "schwefelsaeure.png", "salzsaeure.png", "ammoniak.png", "ether.png",
    "lithium_powder.png", "pill_press_form.png",
    "empty_syringe.png", "filled_syringe.png",
    "koka_tee.png", "cannabis_butter.png",
    "iboga_root.png", "iboga_seed.png", "ibogain_extract.png",
    "ephedra_stem.png", "ephedra_seed.png", "ephedrin_powder.png",
    "betel_nut.png", "betel_seed.png",
    "kava_root.png", "kava_paste.png",
    "mutterkorn.png", "lysergsaeure.png", "lsd_tab.png", "naloxon.png",
    "bench_botany.png", "bench_chemistry.png",
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

OPTIONAL_BUT_RECOMMENDED_MODELS = [
    "cannabis_bud_sativa.blockymodel",
    "cannabis_bud_indica.blockymodel",
    "cannabis_bud_hybrid.blockymodel",
]


def check_folder(folder: Path, required: list[str], label: str) -> int:
    if not folder.exists():
        print(f"\n{label}: ORDNER FEHLT ({folder})")
        return len(required)

    existing = {p.name for p in folder.iterdir() if p.is_file()}
    missing = [name for name in required if name not in existing]
    extra = [name for name in sorted(existing) if name not in required and not name.startswith('.')]

    print(f"\n{label} ({len(existing)}/{len(required)} Dateien im Ordner):")
    if missing:
        print(f"  FEHLEND ({len(missing)}):")
        for item in missing:
            print(f"    - {item}")
    else:
        print("  ✓ Alle vorhanden")

    if extra:
        preview = ", ".join(extra[:12])
        suffix = "..." if len(extra) > 12 else ""
        print(f"  EXTRA ({len(extra)}): {preview}{suffix}")

    return len(missing)


def check_optional(folder: Path, files: list[str], label: str) -> int:
    if not folder.exists():
        print(f"\n{label}: ORDNER FEHLT ({folder})")
        return len(files)

    existing = {p.name for p in folder.iterdir() if p.is_file()}
    missing = [name for name in files if name not in existing]

    print(f"\n{label}:")
    if missing:
        print(f"  EMPFOHLEN ABER FEHLT ({len(missing)}):")
        for item in missing:
            print(f"    - {item}")
    else:
        print("  ✓ Alle empfohlenen Modelle vorhanden")

    return len(missing)


def main() -> None:
    items = REPO_ROOT / "Common" / "Icons" / "ItemsGenerated"
    categories = REPO_ROOT / "Common" / "Icons" / "ItemCategories"
    status = REPO_ROOT / "Common" / "Icons" / "UI" / "StatusEffects"
    blocks = REPO_ROOT / "Common" / "BlockTextures" / "orbis_underground"
    bud_models = REPO_ROOT / "Common" / "Items" / "Cannabis"

    total_missing = 0
    total_missing += check_folder(items, REQUIRED_ITEMS, "ITEM-ICONS (16x16)")
    total_missing += check_folder(categories, REQUIRED_CATEGORIES, "KATEGORIE-ICONS (32x32)")
    total_missing += check_folder(status, REQUIRED_STATUS, "STATUS-EFFEKT-ICONS (16x16)")
    total_missing += check_folder(blocks, REQUIRED_BLOCKS, "BLOCK-TEXTUREN")
    missing_optional_models = check_optional(bud_models, OPTIONAL_BUT_RECOMMENDED_MODELS, "CANNABIS-BUD-MODELLE (empfohlen)")

    print(f"\n{'=' * 64}")
    print(f"PFLICHT-ASSETS FEHLEND: {total_missing}")
    print(f"EMPFOHLENE MODELLE FEHLEND: {missing_optional_models}")
    if total_missing == 0:
        print("✓ Alle Pflicht-Texturen sind vorhanden.")
    else:
        print("⚠ Erst recolor.py mit deinen lokalen Assets ausführen.")
    if missing_optional_models:
        print("⚠ Für schönere Cannabis-Items zusätzlich Get-Hy-Modelle kopieren.")
    print(f"{'=' * 64}")


if __name__ == "__main__":
    main()
