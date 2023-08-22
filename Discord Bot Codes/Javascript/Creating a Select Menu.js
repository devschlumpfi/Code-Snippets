const { Client, Intents, MessageActionRow, MessageSelectMenuBuilder } = require('discord.js');

const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES] });

client.on('messageCreate', async (message) => {
  if (message.content === '!selectmenu') {
    const row = new MessageActionRow().addComponents(
      new MessageSelectMenuBuilder()
        .setCustomId('select')
        .setPlaceholder('Select an option')
        .addOption({
          label: 'Option 1',
          value: 'option1',
        })
        .addOption({
          label: 'Option 2',
          value: 'option2',
        })
    );

    await message.channel.send({ content: 'Please select an option:', components: [row] });
  }
});

client.on('interactionCreate', async (interaction) => {
  if (!interaction.isSelectMenu()) return;

  const selectedValue = interaction.values[0];

  if (selectedValue === 'option1') {
    await interaction.reply('You selected Option 1.');
  } else if (selectedValue === 'option2') {
    await interaction.reply('You selected Option 2.');
  }
});

client.login('YOUR_BOT_TOKEN');
