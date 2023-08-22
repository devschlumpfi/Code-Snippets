client.on('messageCreate', (message) => {
    if (message.content === '!userinfo') {
      const user = message.author;
      const userInfo = `Username: ${user.username}\nID: ${user.id}\nTag: ${user.tag}`;
      message.channel.send(userInfo);
    }
  });
  