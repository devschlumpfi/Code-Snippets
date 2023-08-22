// Create multiple select menus in the same row
const row = new MessageActionRow().addComponents(
    new MessageSelectMenuBuilder()
      .setCustomId('select1')
      .setPlaceholder('Select option 1')
      .addOption({
        label: 'Option A',
        value: 'optionA',
      })
      .addOption({
        label: 'Option B',
        value: 'optionB',
      }),
  
    new MessageSelectMenuBuilder()
      .setCustomId('select2')
      .setPlaceholder('Select option 2')
      .addOption({
        label: 'Option X',
        value: 'optionX',
      })
      .addOption({
        label: 'Option Y',
        value: 'optionY',
      })
  );
  
  // Handle interactions for multiple select menus
  client.on('interactionCreate', async (interaction) => {
    if (!interaction.isSelectMenu()) return;
  
    const selectedValue = interaction.values[0];
  
    switch (interaction.customId) {
      case 'select1':
        if (selectedValue === 'optionA') {
          await interaction.reply('You selected Option A from select menu 1.');
        } else if (selectedValue === 'optionB') {
          await interaction.reply('You selected Option B from select menu 1.');
        }
        break;
  
      case 'select2':
        if (selectedValue === 'optionX') {
          await interaction.reply('You selected Option X from select menu 2.');
        } else if (selectedValue === 'optionY') {
          await interaction.reply('You selected Option Y from select menu 2.');
        }
        break;
    }
  });
  