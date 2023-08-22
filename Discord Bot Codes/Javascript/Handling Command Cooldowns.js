const cooldowns = new Map();

client.on('messageCreate', (message) => {
  if (message.content === '!cooldown') {
    const { author } = message;
    if (!cooldowns.has(author.id)) {
      // Set a 10-second cooldown for this command
      cooldowns.set(author.id, Date.now() + 10000);

      // Your command logic here
      message.reply('This command has a 10-second cooldown.');
      
      setTimeout(() => {
        cooldowns.delete(author.id);
      }, 10000);
    } else {
      const timeLeft = (cooldowns.get(author.id) - Date.now()) / 1000;
      message.reply(`Please wait ${timeLeft.toFixed(1)} more seconds before using this command.`);
    }
  }
});
