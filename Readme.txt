This Discord Do evaluation bot is not intended to be used by anyone else other than myself as it has integration with my raspberry pi allowing me to reboot from discord.
special note: this is the first program I wrote as I was learning coding. Many components of this were updated and upgraded over time as I learned new things.
for example, the first and second versions of this bot did not have a database.

How it works:
1) A Discord user will input their name with the command "!my name is [name]"
- the bot will use this as a primary key in the database keeping track of all records this user changes
-- this is done by using their discord name as a primary key and looking up the value of their "name"
2) Discord user issues the command !eval [name] or !test [name]
- evaluations are the main work of this bot
-- these evaluations are performed by scraping the html data from http://users.nexustk.com/webreport/Do.htm or an individuals user page.
--- The script running will parse the data of a users "legend" and do a series of tests and comparisons to add up "points" for a series of categories like as follows.
note: Points are based on specific strings in a user's legend.
note: The script file structure is built similar to these circles for organization.

Life Breath Circle    |   5 Chambers
[ ] 99th Insight       * This circle is never used to
[ ] Il San               evaluate Do Titles.
[ ] Ee San
[ ] Sam San
[ ] Sa San

3) many values are not held on the user's page or in the index, so the Discord user may be prompted to fill in these records in the evaluation report.
-example: if no karma records are found, the report will prompt the user to add one by asking them to issue the command !add karma [user] [level]
--all of these values are held in a local database
---error reporting is built into these commands. for example if a user tries to input a karma rank that does not exist the bot will inform them.
note: A user trying to trick the bot by changing their name by issuing "!my name is [new name]" and reverting it back will not trick the bot
These records are stored with the user's discord name as foreign key referencing the primary key that points to their "name"
this means any record created or changed by the user will follow them regardless of their namechange.
4) records are queried each time an evaluation is run.
5) some records have a 'log' of their events - such as name changes. This enforces record reliability because it is another layer of protection against
someone trying to trick the bot.
6) future versions of hte bot will integrate an external database into record keeping. This will help augment a "public facing site" https://www.dojong.com/
