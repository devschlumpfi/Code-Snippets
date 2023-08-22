client.on('messageCreate', (message) => {
    if (message.content === 'react') {
      message.react('👍').then(() => {
        message.react('👎');
      });
    }
  });
  
  client.on('messageReactionAdd', (reaction, user) => {
    if (reaction.emoji.name === '👍') {
      reaction.message.channel.send(`${user.username} liked the message.`);
    }
  });
  