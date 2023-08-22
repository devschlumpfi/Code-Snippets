client.on('messageCreate', (message) => {
    if (message.content === '!typing') {
      message.channel.sendTyping();
      setTimeout(() => {
        message.reply('I am typing!');
      }, 1000); // Delay for 1 second
    }
  });
  