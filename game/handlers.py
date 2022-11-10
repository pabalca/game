import click

from game import app
from game.models import Question, db


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Question=Question)


@app.cli.command()
@click.option("--drop", is_flag=True, help="Create after drop.")
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("Initialized datagame.")

    for question in questions:
        q = Question(text=question)
        db.session.add(q)
    db.session.commit()



questions = [
    "how did you spend your summer breaks as a kid?",
    "when was the last time you cried?",
    "act is your favourite animal at the zoo?",
    "are you allergic to anything?",
    "what do you think about before you fall asleep?",
    "name one thing that most people don‚Äôt know about you?",
    "do you want your organs to be donated when you die?",
    "how important is having a clean and tidy home for you?",
    "do you know what your name would have been if you had been born opposite sex?",
    "if you were hiring someone, what would the three most important criteria be?",
    "have you ever had a crush on a celebrity? who?",
    "what brand are you loyal to simply out of habit and not because of its quality?",
    "what is the most intelligent animal?",
    "are you picky eater?",
    "would you rather lose all your memories from the past or lose the ability to form new memories?",
    "is it ok to not leave a tip when you receive bad service?",
    "do you like talking to strangers on planes?",
    "what is the least important subject in school?",
    "does your family have a lot of inside jokes?",
    "what is the best trait you inherited from your mother and what is the best one you inherited from your father?",
    "are people kind or selfish by nature?",
    "what is the most enjoyable way to spend 50 dollars?",
    "is it ok to lie to avoid hurting someone's feelings?",
    "do you know how both sets of your grandparents met?",
    "would you enjoy sharing a meal with your clone?",
    "what is the one key trait that makes successful people successful?",
    "what was the name of your first serious crush?",
    "when was the last time you felt really proud of someone in your family?",
    "do you have any irrational phobias?",
    "what product do you think people will still use 500 years from now?",
    "how many languages can you say: 'I love you'?",
    "now costing a house or car, what is the most expensive thing you have ever bought?",
    "what job would you personally find most boring?",
    "what is the most meaningful gift you have ever received?",
    "would you tell people if you won the lottery or keep it a secret?",
    "do you prefer paper books or electronic books?",
    "if you could change one thing about your body, what would it be?",
    "who was your idol when you were growing up?",
    "you have just won a free car of your choice: what car would you choose?",
    "do you think people ever really change?",
    "if you had enough money to retire tomorrow, what would you do for the rest of your life?",
    "are you more romantic or less romantic than most people?",
    "how would the world be different if the majority of presidents and CEOs were women?",
    "would you rather be stuck on a reset island with your mom or dad? why?",
    "what would you do if you won the lottery?",
    "are you good with kids?",
    "what makes you really angry?",
    "researchers say that it is impossible to change your level of happiness; even if you won the lottery, you would be soon back to the same level of happiness as before. Do you think this is true?",
    "if you had an extra room in your home, what would you use it for?",
    "how would you define intelligence?",
    "what do you think your parents would answer if asked what the crazies thing you did as a child was?",
    "what part of your body do you like best?",
    "have you ever lied about your job to seem more interesting?",
    "do you think there would be fewer conflicts in the world if we all spoke the same language?",
    "have you ever gone on a fad diet?",
    "if you had to name one thing others could possible envy about you, what would it be?",
    "what is likely the most common ting that couples fight about?",
    "did you ever have a really bad haircut or hairstyle? what did it look like?",
    "what personal quality do you know people appreciate about you?",
    "if you could live anywhere, where would you live and why?",
    "who is the most interesting person you have ever met?",
    "if you could only have one app on your phone, what would it be?",
    "act city really exceeded your expectations the first time you visited at?",
    "in what ways do you make other people's lives better?",
    "which of your family member do you look like the most?",
    "describe a time when you helped a stranger.",
    "why do you think so many marriages end in divorce?",
    "do you think you have the right personality for sales?",
    "what invention has had the greatest impact on human culture and civilisation?",
    "what is the ideal retirement age?",
    "if you had the whole world's attention for 30 seconds, what would you say or or?",
    "have you ever won or been chose for something despite thinking you had no change?",
    "what kind of people do you most admire?",
    "what is the most annoying sound?",
    "is there any sort or hobby whose appeal you struggle to understand?",
    "what name would you never give your child?",
    "have you ever declined someone's friend request on Facebook? Why?",
    "of all the famous people alive today, who do you think will still be discussed in 500 years?",
    "what actor or actress would play you in the movie version of your life?",
    "is there anything your parent did not let you do as kid that you would or do let your own children do?",
    "do you like to buy and use secondhand items?",
    "what outfit or accessories that you had in the past did you think was the coolest ever?",
    "what do you consider to be your most productive time of the day?",
    "have you ever bought something you were really embarrassed to buy? what was it?",
    "do you always sleep on the same side of the bed?",
    "who in your family has a personality that is the least like everyone else‚Äôs?",
    "if you could be reincarnated as any animal, what animal would you choose?",
    "what is the biggest difference between your parents?",
    "do people pay too much or too little attention to their appearances these days?",
    "is it better to grow up in a large family or a small family?",
    "do you have any facebook friends that you would not enjoy spending time with?",
    "would you be willing to work hard to learn a foreign language if it would double your salary?",
    "have you ever committed or come close to committing a crime?",
    "was there any one rule in your house growing up that was excessively strict?",
    "if you could see into the future, how far ahead would you want to see?",
    "can you name one good and one bad thing about the American way of life?",
    "have you ever had a really strange or memorable neighbour or roommate?",
    "has there ever been a time when you thought: it doesn't get any better than this?",
    "what book changed your life?",
    "what compliment have you received and never forgotten?",
    "why do so many people live alone today compared to in the past?",
    "would you move to the other side of the world?",
    "what song tend to make you tear up?",
    "what are the two most important things for people to be happy?",
    "describe a time when you did something truly kind for another person.",
    "what item on your long-term to-do list you never seem to get to?",
    "are you glad to be living in the modern day and age, or do you wish you had lived during a past era?",
    "if there were suddenly 28 hours in a day, how would you spend the extra hours?",
    "describe a time when you felt like a terrible person.",
    "do you go easy on people in games or sports when you know that your skill level is much higher than theirs?",
    "who has been the biggest role model in your life?",
    "as you get older, do you find that you act more and more like your parents?",
    "is life easier for kids or adults in general?",
    "was there any period of your life that was difficult but that ultimately made you a stronger or better person?",
    "would you get a tattoo of your partner's name?",
    "do you prefer white walls, painted walls, or wallpaper in your home?",
    "are there any recurring themes in your dreams?",
    "are school uniforms a good or bad idea?",
    "what expensive activity would you like to try or do if you could afford it?",
    "what do you do differently from most people?",
    "what is the most romantic Valentine's day gift you have ever received?",
    "when was the last time you went out of your way to thank someone?",
    "do you think it would be possible for you to meet and become close friends with a celebrity?",
    "what word of phrase do you tend to overuse?",
    "if you could be guaranteed an honest answer, what would you ask and to whom?",
    "at what age would you say people are generally happiest?",
    "if you could go back and relive one day of your life, what day would it be?",
    "describe a time when you did something reckless and daring.",
    "what can we learn from children?",
    "what low-paid job or profession deserves to be better compensated?",
    "name something you look back at and think: I can't believe I was afraid of that.",
    "who is the most likeable person you know?",
    "what would you like to be better at?",
    "not counting your partner or family members, who in your life has been the kindest to you?",
    "if you could take a week-long vacation anywhere in the world by yourself, where would you go?",
    "what movie do you wish they would make a sequel to?",
    "should students get to grade their teachers?",
    "shat is the strangest thing you have ever eaten?",
    "if you could change your age, would you choose to be younger, older, or stay the same?",
    "what is your favourite way of wasting time?",
    "name a time when you felt really proud of yourself.",
    "what two things would you grab if your house were on fire?",
    "have you ever prayed on an airplane?",
    "have you ever done something that only a few people in the world have done?",
    "if only one picture of you could survive after you die, which one would you choose?",
    "how would you summarise yourself on a dating site in just three worlds?",
    "do you have any major scars? if you, how did you get them?",
    "have you ever experience a natural disaster or crisis situation?",
    "what websites do you visit multiple times a day?",
    "which are smarter, cat or dogs?",
    "describe a time when your first impression of a person was completely wrong.",
    "do you believe in good luck charms?",
    "was there anything that you were exceptionally good at when you were younger?",
]

