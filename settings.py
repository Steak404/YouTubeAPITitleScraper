from datetime import date
TODAY = date.today()
WIN_WIDTH = 1280
WIN_HEIGHT = 720

DEV_KEY = "You must put the key in here."
PLAYLIST_ID = "Put the playlist ID in here"

TEXT_D = {'intro_text':"""I was interested in the drinking habits of Japanese internet sensation
        **Hiroyuki Nishimura** So I figured I'd use the YouTube API to do some research.
        I compiled data about what drinks he drinks, and what days. This was done with a couple of modules, 
        which will be in the GitHub. I only looked for alphabetical (non japanese character) drinks, because it is hard for regex to discriminate between 
        a Japanese beverage and a Japanese name. Also it is difficult because he is not always consistent with titles, although he's gotten 
        better. Note I do not know much drink info, so some improper formats may have slipped through. Oh well. """,
        'beginning_text':"""Here is what I found.""",
        'day_freq_text':"""Here is a pie chart by day. The chart shows what day he uploads (and drinks). You can see the relative frequencies. How cool a dude!""",
        'drink_freq_text':"Here is a pie chart by drink frequency. A large variety, to the point where a pie chart is no good!",
        'transistion_1':"What are ALL of the things he drinks? (as of {})".format(TODAY),
        'transistion_2':"He does drink!",
        'transistion_3':'What is/are his FAVORITE drink(s)? (as of {})'.format(TODAY),
        'transistion_4':'Nice! How many videos are these drinks featured in? (as of {})'.format(TODAY),
        'end':"That's all!"
}