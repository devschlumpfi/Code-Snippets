client.on('messageCreate', (message) => {
    if (message.content === '!tts') {
      message.channel.send('This is a text-to-speech message', { tts: true });
    }
  });
  