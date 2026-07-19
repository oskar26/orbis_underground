package orbis_underground;

import com.hypixel.hytale.plugin.JavaPlugin;
import com.hypixel.hytale.plugin.JavaPluginInit;
import orbis_underground.interaction.MethExplosionInteraction;
import orbis_underground.interaction.RemoveAllDrugEffectsInteraction;
import javax.annotation.Nonnull;

/**
 * Orbis Underground — Plugin
 *
 * Registers custom interactions:
 * - orbis_underground:meth_explosion: 20% chance explosion when crafting meth
 * - orbis_underground:RemoveAllDrugEffects: Naloxone removes all drug effects
 */
public class OrbisUndergroundPlugin extends JavaPlugin {

    private static OrbisUndergroundPlugin instance;

    public OrbisUndergroundPlugin(@Nonnull JavaPluginInit init) {
        super(init);
        instance = this;
    }

    public static OrbisUndergroundPlugin get() {
        return instance;
    }

    @Override
    protected void setup() {
        // Register custom interactions
        getCodecRegistry(com.hypixel.hytale.server.core.modules.interaction.interaction.Interaction.CODEC)
            .register("orbis_underground:meth_explosion", MethExplosionInteraction.class, MethExplosionInteraction.CODEC);

        getCodecRegistry(com.hypixel.hytale.server.core.modules.interaction.interaction.Interaction.CODEC)
            .register("orbis_underground:RemoveAllDrugEffects", RemoveAllDrugEffectsInteraction.class, RemoveAllDrugEffectsInteraction.CODEC);

        getLogger().info("[Orbis Underground] Plugin loaded — Meth explosion & Naloxone interactions registered.");
    }
}
