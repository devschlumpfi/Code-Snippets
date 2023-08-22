client.on('messageCreate', (message) => {
    if (message.content === '!clear') {
      const channel = message.channel;
      channel.bulkDelete(5); // Delete the last 5 messages, adjust the number as needed.
    }
  });
  