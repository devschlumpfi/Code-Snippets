const { MessageActionRow, MessageButton } = require('discord.js');

client.on('messageCreate', (message) => {
  if (message.content === '!buttons') {
    const row = new MessageActionRow()
      .addComponents(
        new MessageButton()
          .setCustomId('primary')
          .setLabel('Primary Button')
          .setStyle('PRIMARY'),
        new MessageButton()
          .setCustomId('secondary')
          .setLabel('Secondary Button')
          .setStyle('SECONDARY')
      );

    message.channel.send({ content: 'Click a button:', components: [row] });
  }
});

// Handling button interactions
client.on('interactionCreate', async (interaction) => {
  if (!interaction.isButton()) return;

  const { customId } = interaction;

  if (customId === 'primary') {
    await interaction.reply('You clicked the Primary Button!');
  } else if (customId === 'secondary') {
    await interaction.reply('You clicked the Secondary Button!');
  }
});
