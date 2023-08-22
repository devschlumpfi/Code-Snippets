const channelId = 'YOUR_CHANNEL_ID';

client.on('ready', () => {
  const channel = client.channels.cache.get(channelId);
  if (channel) {
    channel.send('Hello, channel!');
  }
});
