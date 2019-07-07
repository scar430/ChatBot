*** HOW TO USE Chat Bot ***
- In order to communicate with Chat Bot you must FIRST mention Chat Bot and then follow up with you message (e.g. "@ChatBot Hello!").
- The mention MUST come first since the messages contents (message.content) is split and the first element in the array is removed then the rest of the message is plugged in as the input.
- Chat Bot's current data pool is very small, currently only consisting of 4000 data sets (In comparison, most advanced Chat Bots contain 1,000,000+ data sets.).

*** IMPORTANT INFORMATION ABOUT Main/config.json ***
- config.json (not included in the repository) contains two variables, "token" and "loadFromFile".
- "token" is a login token for a discord bot.
- "loadFromFile" is a bool. If false, training will begin, this is mandatory if py/Main/data/save/ is absent. If true, it will load data it already trained on.