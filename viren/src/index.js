require('dotenv').config();
const fetch = require('node-fetch');
const { Client,IntentsBitField} =require('discord.js');
const client =new Client({
    intents:[
        IntentsBitField.Flags.Guilds,
        IntentsBitField.Flags.GuildMembers,
        IntentsBitField.Flags.GuildMessages,
        IntentsBitField.Flags.MessageContent,
    ]
})

client.on('ready',(c)=>{
console.log(`👀 ${c.user.tag} is online`)
})


client.on('messageCreate',(message)=>{
    if(message.content === 'hello'){
        message.reply('Hey there 👀')
    }
})

client.on('messageCreate',gifmsg)
 async function gifmsg(msg){
    if(msg.channel.id == '1068939915422871642'){
        if(msg.content === '!gif'){
            msg.channel.send('gif!')
            let url = `https://tenor.googleapis.com/v2/search?q=dualipa&key=${process.env.tenor}&client_key=my_test_app&limit=8`
            let response = await fetch(url)
            let json =await response.json()
            console.log(json)
            const index = Math.floor(Math.random() * json.results.length)
            
            msg.channel.send(json.results[index].url);

        }
    }

}

client.login(process.env.token);
