const { Client, Intents, MessageActionRow, MessageButton } = require('discord.js');

const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES] });

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}`);
});

client.on('messageCreate', async (message) => {
  if (message.content === '!button') {
    const row = new MessageActionRow().addComponents(
      new MessageButton()
        .setCustomId('button')
        .setLabel('Click Me!')
        .setStyle('PRIMARY')
    );

    await message.channel.send({ content: 'Click the button below:', components: [row] });
  }
});

client.on('interactionCreate', async (interaction) => {
  if (!interaction.isButton()) return;

  if (interaction.customId === 'button') {
    await interaction.reply('Button clicked!');
  }
});

client.login('YOUR_BOT_TOKEN');
