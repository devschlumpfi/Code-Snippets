client.on('messageCreate', (message) => {
    if (message.content === '!checkrole') {
      const member = message.member;
      const roleName = 'YourRoleName'; // Replace with the role you want to check
      
      if (member.roles.cache.some((role) => role.name === roleName)) {
        message.reply(`You have the ${roleName} role.`);
      } else {
        message.reply(`You do not have the ${roleName} role.`);
      }
    }
  });
  