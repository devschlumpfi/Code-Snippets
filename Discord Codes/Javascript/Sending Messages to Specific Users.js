client.on('messageCreate', (message) => {
    if (message.content === '!sendtouser') {
      const userId = 'USER_ID'; // Replace with the user's ID
      const user = client.users.cache.get(userId);
      
      if (user) {
        user.send('This is a message sent directly to a user!');
      } else {
        message.reply('User not found.');
      }
    }
  });
  