client.once('ready', () => {
    // Set bot status
    client.user.setPresence({
      status: 'online', // 'online', 'idle', 'dnd', 'invisible'
      activities: [
        {
          name: 'with Discord.js',
          type: 'PLAYING', // 'PLAYING', 'WATCHING', 'LISTENING', 'STREAMING'
        },
      ],
    });
  });
  