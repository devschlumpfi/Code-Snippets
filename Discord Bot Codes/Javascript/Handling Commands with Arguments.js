client.on('messageCreate', (message) => {
    if (message.content.startsWith('!say')) {
      const args = message.content.slice(5).trim().split(/ +/);
      const text = args.join(' ');
  
      message.channel.send(text);
    }
  });
  