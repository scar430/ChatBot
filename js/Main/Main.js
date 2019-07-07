const Discord = require('discord.js');
const client = new Discord.Client();

//Chat Bot's login token is pulled from config.json which has also been included in the gitignore so as not to reveal Chat Bot's login token.
const { token } = require('./config.json');

client.once('ready', () => {
	console.log('Ready!');
});

client.on('message', message => {
	if (message.content === '!ping') {
        // send back "Pong." to the channel the message was sent in
        message.channel.send('Pong.');
    }    
});

client.login(token);
