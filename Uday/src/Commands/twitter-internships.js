const { SlashCommandBuilder } = require("@discordjs/builders");

module.exports = {
	data: new SlashCommandBuilder()
		.setName("Twitter Internships")
		.setDescription("Scrapers and returns the latest Twitter Internships!"),
	execute: async (interaction, client) => {
		return interaction.reply("Hey! Here are the latest Twitter Internships!");
	},
};