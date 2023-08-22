const responses = ['Response 1', 'Response 2', 'Response 3'];

client.on('messageCreate', (message) => {
  if (message.content === '!randomresponse') {
    const randomIndex = Math.floor(Math.random() * responses.length);
    const randomResponse = responses[randomIndex];
    message.reply(randomResponse);
  }
});
