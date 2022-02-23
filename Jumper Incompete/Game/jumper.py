import random


class Jumper:
    
    def __init__(self):
        print(self._word)

    def word_list(self):
        word_list = ["airplane", "boat", "baby", "ears", "scissors", "cough", "cold", "phone", "laugh", "blink", "hairbrush", "sneeze", "spin", "hammer", "book", "phone", "toothbrush", "jump", "clap", "slap", "archer", "ghost", "balance", "sick", "balloon", "banana", "monster", "hiccup", "stomp", "hurt", "hungry", "slip", "ladder", "scare", "fish", "dizzy", "read", "hot", "birthday", "president", "apartment", "cradle", "coffee", "trampoline", "waterfall", "window", "proud", "flashlight", "marry", "overwhelm", "judge", "shadow", "halo", "measure", "clown", "slither", "whale", "snake", "elephant", "dog", "cat", "ant", "rabbit", "shark", "monkey", "rooster", "jaguar", "starter", "theory", "gamble", "badminton", "necktie", "replay", "pinball"]

      
        list_total = len(word_list)
        i = random.randint(1,list_total)
        self._word = word_list[i]
        return self._word
