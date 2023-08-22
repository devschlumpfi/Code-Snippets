const prefix = '!';

client.on('messageCreate', (message) => {
  if (!message.content.startsWith(prefix) || message.author.bot) return;

  const args = message.content.slice(prefix.length).trim().split(/ +/);
  const command = args.shift().toLowerCase();

  if (command === 'ping') {
    message.reply('Pong!');
  } else if (command === 'hello') {
    message.channel.send('Hello!');
  }
});
