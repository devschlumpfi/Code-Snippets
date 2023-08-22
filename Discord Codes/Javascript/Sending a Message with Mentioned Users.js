client.on('messageCreate', (message) => {
    if (message.content === '!mention') {
      const mentionedUser = message.mentions.users.first();
      message.channel.send(`You mentioned ${mentionedUser}`);
    }
  });
  