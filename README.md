## MTG Online - Sort Bot Prices Script

This is a python script that sorts your MTGO trade binder based on the current price offered to you by bots through trade. I've been using this to maximise my trades for months, so if it can help me then I hope it can help you too.

This script is only compatable with bots in the ManaTraders network.

### How to use the script

-Download pricer.py and open it with your preferred text editor or IDE (I've used [Jupyter Notebook](https://jupyter.org/))

-Begin a trade with a bot on MTGO. If they don't automatically search your collection, message "sell"

-Copy and paste the trade messages from the MTGO client to a text editor

![Image](https://i.imgur.com/CQEXME5.jpg)


-Remove timestamps, bot names, and 'YOU GIVE' from the text (Ctrl+F) and paste it into the script in the section titled Edited_Text


![Image](https://i.imgur.com/RUo4IgP.jpg)


-Run the script. The result looks like this:


![Image](https://i.imgur.com/9noZdzB.jpg)

### Options

By default, the script sorts by card price using this line:

  `l.sort(key = lambda x: x[2], reverse=True)`

You can change this to sort by card price times the amount of copies in your collection by commenting out the previous line and uncommenting this line:

  `l.sort(key = lambda x: x[2]*x[1], reverse=True)`

### Next Update

-Automatic removal of bot names and timestamps

### Support or Contact

Having issues running the script? Feel free to [contact me](mikeds@live.com.au), I'd be happy to help with issues or receive general feedback.
