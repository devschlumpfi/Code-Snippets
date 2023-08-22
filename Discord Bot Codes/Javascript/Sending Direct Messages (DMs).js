client.on('messageCreate', (message) => {
    if (message.content === '!dm') {
      const user = message.author;
      user.send('This is a direct message!');
    }
  });
  