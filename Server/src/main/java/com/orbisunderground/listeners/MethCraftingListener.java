package com.orbisunderground.listeners;

import com.orbisunderground.OrbisUndergroundPlugin;
import hytale.server.event.EventHandler;
import hytale.server.event.crafting.ItemCraftedEvent;
import hytale.server.entity.Player;
import hytale.server.world.Location;
import hytale.server.world.Explosion;
import hytale.server.world.ParticleEffect;

import java.util.Random;

/**
 * Listens for item crafting events.
 * When a player crafts 'orbis_underground:meth', triggers a 20% random chance
 * for a hazardous chemical explosion at the crafting location.
 */
public class MethCraftingListener {

    private final OrbisUndergroundPlugin plugin;
    private final Random random = new Random();
    private static final String METH_ITEM_ID = "orbis_underground:meth";
    private static final float EXPLOSION_CHANCE = 0.20f; // 20% chance

    public MethCraftingListener(OrbisUndergroundPlugin plugin) {
        this.plugin = plugin;
    }

    @EventHandler
    public void onItemCrafted(ItemCraftedEvent event) {
        if (event == null || event.getCraftedItem() == null) {
            return;
        }

        String itemId = event.getCraftedItem().getId();
        if (METH_ITEM_ID.equalsIgnoreCase(itemId)) {
            float roll = random.nextFloat();
            if (roll < EXPLOSION_CHANCE) {
                Player player = event.getPlayer();
                Location loc = player != null ? player.getLocation() : event.getCraftingBenchLocation();

                plugin.getLogger().warning("💥 METH SYNTHESIS EXPLOSION TRIGGERED at " + (loc != null ? loc.toString() : "Unknown") + " for player " + (player != null ? player.getName() : "Unknown"));

                // 1. Cancel crafting output and destroy reactants
                event.setCancelled(true);
                event.setRefundIngredients(false);

                // 2. Trigger chemical explosion at bench/player location
                if (loc != null) {
                    Explosion explosion = new Explosion.Builder(loc)
                            .power(3.5f)
                            .damage(45.0f) // Deal severe chemical damage
                            .fire(true)
                            .particle(ParticleEffect.CHEMICAL_SMOKE_BURST)
                            .build();
                    explosion.explode();
                }

                // 3. Notify player in chat
                if (player != null) {
                    player.sendMessage("§c⚠️ DIE METH-SYNTHESE IST EXPLODIERT! Chemical reaction failed! 💥");
                }
            }
        }
    }
}
