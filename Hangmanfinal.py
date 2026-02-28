import random

words = {
    "Fruits": ["apple", "banana", "chikoo", "pineapple", "grapes", "strawberry", "blackberry", "kiwi", "dragonfruit", "custard apple", "coconut", "blueberry", "fig", "mango", "papaya", "watermelon", "cantaloupe", "honeydew", "cherry", "plum", "peach", "pear", "apricot", "pomegranate", "grapefruit", "lemon", "lime", "tangerine", "clementine", "raspberry", "cranberry", "nectarine", "passionfruit", "guava", "lychee", "persimmon", "starfruit", "boysenberry", "mulberry", "quince"],
    "Animals": ["dog", "cat", "horse", "cow", "pig", "sheep", "goat", "chicken", "duck", "rabbit", "lion", "tiger", "elephant", "giraffe", "zebra", "monkey", "gorilla", "bear", "kangaroo", "rhinoceros", "dolphin", "whale", "shark", "octopus", "penguin", "seal", "walrus", "crab", "lobster", "stingray", "eagle", "owl", "parrot", "snake", "crocodile", "alligator", "turtle", "frog", "toad", "lizard"],
    "Bollywood Movies": ["sholay", "dangal", "pk", "lagaan", "swades", "barfi", "andhadhun", "drishyam", "jawan", "pathaan", "animal", "stree", "war", "don", "sanju", "border", "gadar", "sultan", "queen", "tamasha", "udaan", "haider", "dhoom", "krrish", "raazi", "dostana", "agneepath", "fanaa", "ghajini", "ludo", "yeh jawaani hai deewani", "jab we met", "om shanti om", "chennai express", "bajrangi bhaijaan", "chak de india", "munna bhai mbbs", "dil chahta hai", "bhool bhulaiyaa", "hera pheri"],
    "Hollywood Movies": ["inception", "avatar", "gladiator", "the matrix", "interstellar", "jurassic park", "titanic", "the godfather", "pulp fiction", "the dark knight", "forrest gump", "star wars", "the avengers", "the terminator", "alien", "jaws", "back to the future", "indiana jones", "rocky", "die hard", "the lord of the rings", "harry potter", "spider man", "iron man", "toy story", "finding nemo", "the lion king", "frozen", "shrek", "the shawshank redemption", "fight club", "goodfellas", "the silence of the lambs", "the truman show", "mad max", "the martian", "gravity", "dune", "oppenheimer", "barbie"],
    "Indian Actors": ["amitabh bachchan", "shah rukh khan", "salman khan", "aamir khan", "hrithik roshan", "akshay kumar", "ajay devgn", "ranbir kapoor", "ranveer singh", "shahid kapoor", "varun dhawan", "tiger shroff", "ayushmann khurrana", "rajkummar rao", "vicky kaushal", "kartik aaryan", "john abraham", "saif ali khan", "suniel shetty", "anil kapoor", "sanjay dutt", "nana patekar", "allu arjun", "ram charan", "ntr jr", "prabhas", "mahesh babu", "pawan kalyan", "vijay", "ajith kumar", "rajinikanth", "kamal haasan", "suriya", "dhanush", "yash", "rishab shetty", "dulquer salmaan", "fahadh faasil", "mohanlal", "mammootty"],
    "Indian Actresses": ["deepika padukone", "alia bhatt", "katrina kaif", "priyanka chopra", "kareena kapoor", "anushka sharma", "shraddha kapoor", "kiara advani", "kriti sanon", "disha patani", "taapsee pannu", "vidya balan", "kangana ranaut", "aishwarya rai", "sushmita sen", "madhuri dixit", "kajol", "rani mukerji", "preity zinta", "juhi chawla", "karisma kapoor", "tabu", "nayanthara", "samantha ruth prabhu", "anushka shetty", "tamannaah bhatia", "kajal aggarwal", "pooja hegde", "rashmika mandanna", "shruti haasan", "trisha krishnan", "mrunal thakur", "sreeleela", "keerthy suresh", "sai pallavi", "radhika apte", "bhumi pednekar", "sanya malhotra", "yami gautam", "sonam kapoor"],
    "Languages": ["english", "mandarin", "hindi", "spanish", "french", "arabic", "bengali", "russian", "portuguese", "urdu", "indonesian", "german", "japanese", "marathi", "telugu", "turkish", "tamil", "vietnamese", "tagalog", "korean", "persian", "swahili", "javanese", "italian", "punjabi", "gujarati", "thai", "amharic", "kannada", "bhojpuri", "burmese", "yoruba", "uzbek", "odia", "maithili", "sindhi", "malayalam", "romanian", "dutch", "greek"],
    "Hollywood Stars": ["leonardo dicaprio", "brad pitt", "tom cruise", "denzel washington", "tom hanks", "robert de niro", "al pacino", "morgan freeman", "johnny depp", "will smith", "keanu reeves", "christian bale", "matthew mcconaughey", "joaquin phoenix", "harrison ford", "samuel l jackson", "ryan gosling", "chris evans", "chris hemsworth", "robert downey jr", "meryl streep", "scarlett johansson", "angelina jolie", "jennifer lawrence", "emma stone", "natalie portman", "charlize theron", "cate blanchett", "nicole kidman", "julia roberts", "sandra bullock", "anne hathaway", "margot robbie", "zendaya", "florence pugh", "viola davis", "halle berry", "kate winslet", "anya taylor joy", "emily blunt"],
    "Online Games": ["valorant", "counter strike", "apex legends", "fortnite", "pubg", "call of duty", "overwatch", "rainbow six siege", "team fortress", "league of legends", "dota", "smite", "heroes of the storm", "world of warcraft", "final fantasy xiv", "runescape", "guild wars", "black desert online", "the elder scrolls online", "lost ark", "minecraft", "rust", "ark survival evolved", "roblox", "dayz", "palworld", "lethal company", "among us", "rocket league", "fall guys", "hearthstone", "teamfight tactics", "brawlhalla", "dead by daylight", "sea of thieves", "genshin impact", "warframe", "destiny", "path of exile", "escape from tarkov"],
    "Cities": ["nashik", "pune", "mumbai", "rameshwaram", "delhi", "bangalore", "chennai", "kolkata", "hyderabad", "ahmedabad", "jaipur", "surat", "lucknow", "kanpur", "nagpur", "indore", "bhopal", "patna", "agra", "varanasi", "london", "tokyo", "paris", "new york", "dubai", "singapore", "sydney", "toronto", "berlin", "rome", "madrid", "amsterdam", "seoul", "beijing", "istanbul", "moscow", "bangkok", "cairo", "cape town", "rio de janeiro"],
    "Superheroes": ["spider man", "iron man", "captain america", "thor", "hulk", "black widow", "hawkeye", "black panther", "doctor strange", "ant man", "captain marvel", "wolverine", "deadpool", "cyclops", "storm", "star lord", "groot", "rocket raccoon", "drax", "gamora", "daredevil", "moon knight", "ghost rider", "silver surfer", "superman", "batman", "wonder woman", "flash", "aquaman", "green lantern", "cyborg", "martian manhunter", "green arrow", "nightwing", "supergirl", "batgirl", "shazam", "plastic man", "blue beetle", "invincible"],
    "Mythological Characters": ["rama", "sita", "lakshmana", "hanuman", "ravana", "surpanakha", "jatayu", "shiva", "vishnu", "brahma", "saraswati", "lakshmi", "parvati", "ganesha", "kartikeya", "indra", "agni", "varuna", "yama", "vayu", "krishna", "radha", "balarama", "arjuna", "bhima", "yudhishthira", "nakula", "sahadeva", "draupadi", "karna", "duryodhana", "bhishma", "drona", "ashwatthama", "prahlada", "hiranyakashipu", "narasimha", "vamana", "parasurama", "kalki"],
    "Historical Characters": ["shivaji maharaj", "bhagat singh", "mahatma gandhi", "rani lakshmibai", "subhas chandra bose", "sardar patel", "br ambedkar", "chandragupta maurya", "ashoka", "akbar", "tipu sultan", "baji rao", "tatya tope", "mangal pandey", "maharana pratap", "chhatrapati sambhaji", "ahilyabai holkar", "raja ram mohan roy", "swami vivekananda", "rabindranath tagore", "jawaharlal nehru", "lal bahadur shastri", "sarojini naidu", "dadabhai naoroji", "lala lajpat rai", "bal gangadhar tilak", "bipin chandra pal", "chandrashekhar azad", "ashfaqulla khan", "savitribai phule", "jyotirao phule", "samudragupta", "krishnadevaraya", "harsha", "rani padmini", "prithviraj chauhan", "bahadur shah zafar", "rajendra chola", "rajaraja chola", "rani durgavati"],
    "Hindi Dialogues": ["kitne aadmi the", "mogambo khush hua", "rishte mein toh hum tumhare baap lagte hain", "bade bade deshon mein aisi choti choti baatein hoti rehti hai", "rahul naam toh suna hoga", "pushpa jhukega nahi saala", "don ko pakadna mushkil hi nahi namumkin hai", "mere paas maa hai", "baad mein baad mein chai thandi ho jaati he", "tareekh pe tareekh", "ek chutki sindoor ki keemat tum kya jano ramesh babu", "mere karan arjun aayenge", "jaa simran jaa jee le apni zindagi", "haar kar jeetne wale ko baazigar kehte hain", "aap purush hi nahi mahapurush hain", "life is race run or get trampled", "picture abhi baaki hai mere dost", "all is well", "mhari chhoriyan chhoron se kam hai ke", "babumoshai zindagi badi honi chahiye lambi nahi", "rehman dakeit ki di hui maut badi kasainuma hoti he ", "main udna chahta hoon daudna chahta hoon", "hows the josh", "ghaayal hu isliye ghaatak hu", "parampara pratishtha anushasan", "thappar se darr nahi lagta sahab pyar se lagta hai", "ye baburao ka style he", "padhai likhai karo ias yas bano", "tension lene ka nahi sirf dene ka", "ek baar jo maine commitment kar di", "swagat nahi karoge hamara", "sirkate ka sir kata hua he", "kuch kuch hota hai anjali tum nahi samjhogi", "kabhi kabhi lagta hai apunich bhagwan hai", "apna time aayega", "aao kabhi haveli pe", "cheete ki chaal baaz ki nazar aur bajirao ki talvaar", "hum tummein itne ched karenge", "jo dar gaya samjho mar gaya", "kaun kambakht bardaasht karne ko peeta hai"],
    "Sports": ["football", "basketball", "cricket", "tennis", "baseball", "rugby", "golf", "volleyball", "table tennis", "badminton", "swimming", "athletics", "boxing", "wrestling", "gymnastics", "cycling", "skiing", "snowboarding", "surfing", "hockey", "ice hockey", "american football", "water polo", "rowing", "sailing", "fencing", "archery", "weightlifting", "judo", "taekwondo", "karate", "polo", "squash", "snooker", "billiards", "darts", "bowling", "kabaddi", "kho kho", "kickboxing"]
}

hangman_draw = {
    0: ("___", 
        " | ", 
        "   ", 
        "   ", 
        "   "),
    1: ("___", 
        " | ", 
        " O ", 
        "   ", 
        "   "),
    2: ("___", 
        " | ", 
        " O ", 
        " | ", 
        "   "),
    3: ("___", 
        " | ", 
        " O ", 
        "/| ", 
        "   "),
    4: ("___", 
        " | ", 
        " O ", 
        "/|\\", 
        "   "),
    5: ("___", 
        " | ", 
        " O ", 
        "/|\\", 
        "/  "),
    6: ("___", 
        " | ", 
        " O ", 
        "/|\\", 
        "/ \\")
}

def display_hangman(wrong_guesses):
    print("***************")
    for line in hangman_draw[wrong_guesses]:
        print(line)
    print("***************")

def display_answer(answer):
    print(" ".join(answer))

def display_hint(hint):
    print(" ".join(hint))

def play_round():
    print("\nChoose a Genre:")
    genres = list(words.keys())
    
    for index, genre in enumerate(genres):
        print(f"{index + 1}. {genre}")
        
    while True:
        choice = input("\nEnter the number of your choice: ")
        if choice.isdigit() and 1 <= int(choice) <= len(genres):
            selected_genre = genres[int(choice) - 1]
            print(f"\nAwesome! You chose {selected_genre}. Let's play!")
            break
        else:
            print("Invalid Input!!! Please enter a valid number.")

    answer = random.choice(words[selected_genre])
    wrong_guesses = 0
    hint = [" " if char == " " else "_" for char in answer]
    guessed_letters = set()
    is_running = True

    while is_running:
        display_hangman(wrong_guesses)
        display_hint(hint)
        guess = input("Guess a Letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Kuch Dhang ka Likho,IAS YAS bano!!!")
            continue

        if guess in guessed_letters:
            print(f"'{guess}' ho to gya ek baar kitne baar daalega.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print("JEET GAYA LAADLE\nMEOOOOW\nGHOP GHOP GHOP!!!")
            is_running = False
            
        elif wrong_guesses >= len(hangman_draw) - 1:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print("YE SAB KYA DEKHNA PAD RAHA HE\nACCHA HE ME ANDHA HOON")
            is_running = False

def main():
    print("=== WELCOME TO HANGMAN ===")
    
    while True:
        play_round()
        
        replay = input("\nAAJA LADLE AA? (y/n): ").lower()
        if replay != 'y':
            print("CHAL BHOSADIKE!!!")
            break

if __name__ == "__main__":
    main()





