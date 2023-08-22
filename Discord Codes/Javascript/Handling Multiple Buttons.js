const { Client, Intents, MessageActionRow, MessageButton } = require('discord.js');

const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES] });

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}`);
});

client.on('messageCreate', async (message) => {
  if (message.content === '!buttons') {
    const row = new MessageActionRow()
      .addComponents(
        new MessageButton()
          .setCustomId('button1')
          .setLabel('Button 1')
          .setStyle('PRIMARY'),
        new MessageButton()
          .setCustomId('button2')
          .setLabel('Button 2')
          .setStyle('SECONDARY')
      );

    await message.channel.send({ content: 'Click the buttons below:', components: [row] });
  }
});

client.on('interactionCreate', async (interaction) => {
  if (!interaction.isButton()) return;

  if (interaction.customId === 'button1') {
    await interaction.reply('Button 1 clicked!');
  } else if (interaction.customId === 'button2') {
    await interaction.reply('Button 2 clicked!');
  }
});

client.login('YOUR_BOT_TOKEN');
