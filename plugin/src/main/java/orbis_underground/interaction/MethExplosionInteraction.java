package orbis_underground.interaction;

import com.hypixel.hytale.codec.builder.BuilderCodec;
import com.hypixel.hytale.component.CommandBuffer;
import com.hypixel.hytale.component.Ref;
import com.hypixel.hytale.protocol.InteractionState;
import com.hypixel.hytale.protocol.InteractionType;
import com.hypixel.hytale.server.core.Message;
import com.hypixel.hytale.server.core.entity.InteractionContext;
import com.hypixel.hytale.server.core.modules.entity.component.HealthComponent;
import com.hypixel.hytale.server.core.modules.entity.component.TransformComponent;
import com.hypixel.hytale.server.core.modules.interaction.interaction.CooldownHandler;
import com.hypixel.hytale.server.core.modules.interaction.interaction.config.SimpleInstantInteraction;
import com.hypixel.hytale.server.core.universe.world.World;
import com.hypixel.hytale.server.core.universe.world.storage.EntityStore;

import javax.annotation.Nonnull;
import java.util.concurrent.ThreadLocalRandom;

/**
 * MethExplosionInteraction
 * 
 * When the player crafts meth, there is a 20% chance of an explosion.
 * The explosion:
 * - Deals 8-15 damage to the player
 * - Sends a warning message
 * - Creates a visual explosion effect at the player's position
 * 
 * On success (80% chance):
 * - The meth item is crafted normally
 * - The player gets the drug_meth effect applied
 */
public class MethExplosionInteraction extends SimpleInstantInteraction {

    public static final BuilderCodec<MethExplosionInteraction> CODEC = BuilderCodec.builder(
            MethExplosionInteraction.class,
            MethExplosionInteraction::new,
            SimpleInstantInteraction.CODEC
    ).build();

    /** Chance of explosion (0.0 - 1.0) */
    private static final double EXPLOSION_CHANCE = 0.20;
    /** Minimum damage on explosion */
    private static final float MIN_DAMAGE = 8.0f;
    /** Maximum damage on explosion */
    private static final float MAX_DAMAGE = 15.0f;

    @Override
    protected void firstRun(@Nonnull InteractionType interactionType,
                            @Nonnull InteractionContext interactionContext,
                            @Nonnull CooldownHandler cooldownHandler) {

        CommandBuffer<EntityStore> commandBuffer = interactionContext.getCommandBuffer();
        if (commandBuffer == null) {
            interactionContext.getState().state = InteractionState.Failed;
            return;
        }

        Ref<EntityStore> entityRef = interactionContext.getEntity();
        com.hypixel.hytale.server.core.universe.Player player =
                commandBuffer.getComponent(entityRef, com.hypixel.hytale.server.core.universe.Player.getComponentType());

        if (player == null) {
            interactionContext.getState().state = InteractionState.Failed;
            return;
        }

        double roll = ThreadLocalRandom.current().nextDouble();

        if (roll < EXPLOSION_CHANCE) {
            // === EXPLOSION! ===
            float damage = MIN_DAMAGE + (float) (ThreadLocalRandom.current().nextDouble() * (MAX_DAMAGE - MIN_DAMAGE));

            // Apply damage to the player
            HealthComponent health = commandBuffer.getComponent(entityRef, HealthComponent.getComponentType());
            if (health != null) {
                health.subtractStatValue(
                        com.hypixel.hytale.server.core.modules.entitystats.Predictable.ALL,
                        health.getHealthIndex(),
                        damage
                );
            }

            // Get player position for explosion
            TransformComponent transform = commandBuffer.getComponent(entityRef, TransformComponent.getComponentType());
            World world = commandBuffer.getExternalData().getWorld();

            if (transform != null && world != null) {
                // Spawn explosion particles/sound at player position
                world.spawnParticle(
                        "OrbisUnderground:Meth_Explosion",
                        transform.getPosition().x,
                        transform.getPosition().y,
                        transform.getPosition().z
                );
            }

            // Send dramatic message to player
            player.sendMessage(Message.raw(
                    "§c§l💥 EXPLOSION! §eThe meth lab erupted! §cYou took " + 
                    String.format("%.0f", damage) + " damage! §4(Meth destroyed)"
            ));

            // Mark as "succeeded" but the item is NOT given (handled by removing from output)
            // The interaction failed = item not produced
            interactionContext.getState().state = InteractionState.Failed;

        } else {
            // === Success — meth crafted safely ===
            player.sendMessage(Message.raw("§a§l⚗ Methamphetamine cooked successfully. §7(Lucky this time...)"));
            interactionContext.getState().state = InteractionState.Finished;
        }
    }
}
