const { MessageEmbed } = require('discord.js');

client.on('messageCreate', (message) => {
  if (message.content === '!embed') {
    const embed = new MessageEmbed()
      .setTitle('Embed Title')
      .setDescription('This is an example embed.')
      .setColor('#3498db');

    message.reply({ embeds: [embed] });
  }
});
