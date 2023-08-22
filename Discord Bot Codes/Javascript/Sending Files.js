client.on('messageCreate', (message) => {
    if (message.content === '!sendfile') {
      const attachment = new MessageAttachment('path-to-your-file.png');
      message.channel.send({ files: [attachment] });
    }
  });
  