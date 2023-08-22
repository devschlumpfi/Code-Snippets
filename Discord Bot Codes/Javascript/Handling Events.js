client.on('guildCreate', (guild) => {
    console.log(`Added to server: ${guild.name}`);
  });
  
  client.on('guildDelete', (guild) => {
    console.log(`Removed from server: ${guild.name}`);
  });
  