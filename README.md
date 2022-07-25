# af-bot

A bot to automate keeping track of bumps on Disboard for the Action Fiction community's Discord server, and possibly more if things pop up.

Uses the disnake wrapper for Discord API calls.

Only meant to run for single servers, you'll need to specify which server you're trying to do a thing for as well as your Discord developer token in a .env file in the top level of the repo. Something like:

~/af-bot/.env:
```
GUILD=111111111111111
TOKEN=222222222222222
```

By default this is logging to a "discord.log" file in the top level of the repo. Could prolly grow really huge if you let it. Might wanna comment that bit out if you don't want to deal with it. I'll prolly make it a flag at some point.
