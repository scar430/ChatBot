# Chat Bot Py v1.0

Chat Bot is an AI capable of intelligent speech, this was combined with a Discord Bot so Discord users would be able to interact with it, more of a fun toy than anything else. There are plans in the future to expand this bot, like adding more datasets and allowing it to learn from conversations.

## Proper use for Chat Bot Py v1.0
In order to communicate with the bot your message must start with the Mention of the bot.
Input :
`@ChatBot Hello!`
Output : 
`hello ... `

## Notes for collaborators
- py/Main/config.json (not included in the repository) contains two variables, "token" and "loadFromFile".
- "token" is a string which acts as a login token for a discord bot.
- "loadFromFile" is a bool. If false, training will begin, this is mandatory if py/Main/data/save/ is absent or empty. If true, it will load data it already trained on.
- If you plan on running this bot from your own computer then you will have to train it since I could not upload pretrained data due to it's size.

### Prerequisites

The pip commands below are only recommended if you are using Python 3.7, Windows, and plan on training on your CPU. 
You can try other versions/install methods but I can not guarentee these will work.

```
pip3 install https://download.pytorch.org/whl/cpu/torch-1.1.0-cp37-cp37m-win_amd64.whl
pip3 install https://download.pytorch.org/whl/cpu/torchvision-0.3.0-cp37-cp37m-win_amd64.whl
```

## Built With

* [Pytorch](https://pytorch.org/get-started/locally/) - Analytical lib for Python.

## Authors

* **Seth Banker** - *Initial work* - [scar430](https://github.com/scar430)

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/scar430/ChatBot/blob/master/LISCENSE.md) file for details

## Acknowledgments

* Hat tip to Pytorch for making this easy AF.

