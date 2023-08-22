client.on('messageCreate', (message) => {
    if (message.content === 'react') {
      message.react('👍');
      message.react('👎');
    }
  });
  