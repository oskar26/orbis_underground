package com.orbisunderground;

import com.orbisunderground.listeners.MethCraftingListener;
import hytale.server.plugin.HytalePlugin;
import hytale.server.event.EventManager;

/**
 * Orbis Underground — Hytale Server Plugin
 * 
 * Handles custom server-side gameplay mechanics:
 * - 20% explosion risk during Methamphetamine synthesis
 * - Overdose tracking and Naloxone antidote administration
 * - Dealer NPC barter shop logic
 */
public class OrbisUndergroundPlugin extends HytalePlugin {

    @Override
    public void onEnable() {
        getLogger().info("=================================================");
        getLogger().info(" Orbis Underground v1.0.0 — Mod Loaded ");
        getLogger().info(" Registering MethCraftingListener (20% explosion) ");
        getLogger().info("=================================================");

        // Register the crafting event listener for Meth explosion mechanism
        EventManager.registerListener(new MethCraftingListener(this));
    }

    @Override
    public void onDisable() {
        getLogger().info("Orbis Underground plugin disabled.");
    }
}
