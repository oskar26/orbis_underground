package orbis_underground.interaction;

import com.hypixel.hytale.codec.builder.BuilderCodec;
import com.hypixel.hytale.component.CommandBuffer;
import com.hypixel.hytale.component.Ref;
import com.hypixel.hytale.protocol.InteractionState;
import com.hypixel.hytale.protocol.InteractionType;
import com.hypixel.hytale.server.core.Message;
import com.hypixel.hytale.server.core.entity.InteractionContext;
import com.hypixel.hytale.server.core.modules.entity.effect.EffectControllerComponent;
import com.hypixel.hytale.server.core.modules.interaction.interaction.CooldownHandler;
import com.hypixel.hytale.server.core.modules.interaction.interaction.config.SimpleInstantInteraction;
import com.hypixel.hytale.server.core.universe.Player;
import com.hypixel.hytale.server.core.universe.world.storage.EntityStore;

import javax.annotation.Nonnull;

/**
 * RemoveAllDrugEffectsInteraction
 *
 * Used by Naloxone item.
 * Removes ALL active entity effects (drug-related and others) from the player.
 * This is the "antidote" mechanic.
 */
public class RemoveAllDrugEffectsInteraction extends SimpleInstantInteraction {

    public static final BuilderCodec<RemoveAllDrugEffectsInteraction> CODEC = BuilderCodec.builder(
            RemoveAllDrugEffectsInteraction.class,
            RemoveAllDrugEffectsInteraction::new,
            SimpleInstantInteraction.CODEC
    ).build();

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
        Player player = commandBuffer.getComponent(entityRef, Player.getComponentType());

        if (player == null) {
            interactionContext.getState().state = InteractionState.Failed;
            return;
        }

        // Get the effect controller and clear all effects
        EffectControllerComponent effectController = commandBuffer.getComponent(
                entityRef, EffectControllerComponent.getComponentType());

        if (effectController != null) {
            // Clear all active effects
            effectController.clearEffects(entityRef, commandBuffer);

            player.sendMessage(Message.raw(
                    "§b§l💉 Naloxone administered. §aAll drug effects have been purged."
            ));

            interactionContext.getState().state = InteractionState.Finished;
        } else {
            player.sendMessage(Message.raw("§7No active effects to remove."));
            interactionContext.getState().state = InteractionState.Failed;
        }
    }
}
