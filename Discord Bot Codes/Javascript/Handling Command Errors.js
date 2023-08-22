client.on('messageCreate', (message) => {
    if (message.content === '!error') {
      // Simulate an error (for testing purposes)
      throw new Error('This is a test error.');
    }
  });
  
  // Handling errors globally
  client.on('error', (error) => {
    console.error('An error occurred:', error);
  });
  