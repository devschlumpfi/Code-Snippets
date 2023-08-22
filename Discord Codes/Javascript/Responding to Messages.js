client.on('messageCreate', (message) => {
    if (message.content === '!ping') {
      message.reply('Pong!');
    }
  });
  