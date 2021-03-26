import random 
tarot_cards = ["The Fool: Fresh hope, take chances, new paths and adventures await.",
 "The Magician: Focussed creativity, turning visions into reality, sudden solutions may appear.",
"The High Priestess: Secrets and hidden circumstances stand in the way, trust yourself.", 
"The Empress: A gentle almost unnoticed power, rarely opposed.", 
"The Emperor: You're up against real power, respect its leadership.", 
"The Hierophant: Dependency on approval from elevated dignity.", 
"The Lovers: Deeply felt mutual attraction or partnership.", 
"The Chariot: Triumph! but beware of its consequences.",
"Strength: Strength of a kind that's superior because of clever application.", 
"The Hermit: A lesson and reward, but also misfortune of solitude.", 
"Wheel of Fortune: An uncertain outcome, with n aftermath to be considered.", 
"Justice: Justice without blinfold is not always fair.", 
"The Hanged Man: Great personal sacrifice that still doesn't hurt much.", 
"Death: A costly loss, big changes to move on from and transform.", 
"Temperance: Balance and harmony, self control is strong.", 
"The Devil: The pain and delight of giving in to temptation.", 
"The Tower: A spectacular ambition that ends with disaster.", 
"The Star: Time to pause and reflect, contemplate what's precious and what's not.",
"The Moon: Longing for the sake of longing, hoping for fulfillment.",
"The sun: Great resources at your disposal, but constrain yourself, it's possible to have too much.",
"Judgement: Ultimate judgement, whether we welcome it or not.",
"The world: Success in anything worldy, but not for free."]

intro = "Welcome to Anna's Mystical Tarot Reading!"
player_input = input("Please choose which area of your life you would like to learn about:\nFamily, Work, Romantic, Friendship, or anything else\n")
loading_str = "...carefully choosing your cards..."
ending = "Thank you for letting me read you, please take this information with care :)"

def random_cards1():
    card_one = random.choice(tarot_cards)
    tarot_cards.remove(card_one)
    return card_one

def random_cards2():
    card_two = random.choice(tarot_cards)
    tarot_cards.remove(card_two)
    return card_two

def random_cards3():
    card_three = random.choice(tarot_cards)
    return card_three

game_str = ("Your card representing your past is " + random_cards1() + "\nYour card representing your present is " + random_cards2() + "\nYour card representing your future is " + random_cards3())

#the game
print(intro)
print("You chose "+ player_input + " as the area of your life you would like to be read on")
print(loading_str)
print(game_str)
print(ending)





 
