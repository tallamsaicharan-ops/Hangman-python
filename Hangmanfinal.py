import random

# Dictionary of { "word": "hint" }
words = {
    "Fruits": {
        "apple": "Newton",
        "banana": "Monkeys",
        "watermelon": "Summers' Best Friend",
        "kiwi": "New Zealand",
        "chikoo": "Virat Kohli",
        "pineapple": "Spiky",
        "grapes": "Wine",
        "strawberry": "Pairs with Chocolate",
        "blackberry": "Phone Brand",
        "dragonfruit": "Name relating Bhutan",
        "custard apple": "In Hindi it is named after a mythological figure.",
        "coconut": "Hydration",
        "blueberry": "Thanos' favorite fruit",
        "fig": "Myth was birds lays eggs in it.",
        "mango": "Langda",
        "papaya": "Abortions",
        "cantaloupe": "A type of melon with a rough, netted skin and sweet orange flesh.",
        "honeydew": "Can be related to Bees",
        "cherry": "on top of a cake",
        "peach": "Emoji Not used as a Fruit",
        "pear": "Confuse me with a guava.",
        "apricot": "Fuzzy Nectarine",
        "pomegranate": "Dabeli",
        "grapefruit": "My name consists a fruit related to wine.",
        "lemon": "Salad.",
        "lime": "Identity Crisis with Lemon.",
        "tangerine": "Identity Crisis with Orange.",
        "clementine": "Identity Crisis with Tangerine.",
        "raspberry": "Identity Crisis with Blackberry.",
        "nectarine": "Essentially a peach with smooth, fuzz-free skin.",
        "guava": "Why are there so many Seeds in it?",
        "lychee": "Juice is Good Though...",
        "starfruit": "Looks like a kind of fish.",
    },
    "Animals": {
        "dog": "Uska bhi Din aata he",
        "cat": "Has 9 Lives",
        "horse": "Lakdi ki kaathi",
        "cow": "Winkin'",
        "pig": "Muddy",
        "sheep": "Baa Baa",
        "goat": "MSD,Virat,Rohit.",
        "chicken": "It's finger lickin' Good.",
        "duck": "Donald.",
        "rabbit": "Looney Tunes.",
        "lion": "Hakuna Matata.",
        "tiger": "Bengal",
        "elephant": "Dumbo.",
        "giraffe": "Khali.",
        "zebra": "Crossing",
        "monkey": "Boots.",
        "gorilla": "Godzilla",
        "bear": "Hibernation.",
        "kangaroo": "Australia.",
        "rhinoceros": "Horn.",
        "dolphin": "One of the Smartest Animal.",
        "whale": "Largest Mammal.",
        "shark": "I'm the reason Steven Spielberg made everyone afraid of the beach in 1975.",
        "octopus": "2 Hearts and 3 Brains.",
        "penguin": "He wouldn't go to the feeding grounds neither return to the colony.",
        "seal": "Football",
        "crab": "Sideways.",
        "lobster": "A marine crustacean with a muscular tail and large claws that turns red when cooked.",
        "eagle": "He is Mighty in the Angry Birds",
        "owl": "Hogwarts",
        "parrot": "Speaks like Humans.",
        "snake": "Your Ex.",
        "crocodile": "Lacoste",
        "alligator": "Identity Crisis.",
        "turtle": "Slow and Steady",
        "frog": "Kisses the Princess.",
        "toad": "Similar to a frog but typically has dry, warty skin and shorter legs.",
        "lizard": "Sticky and Yuck."
    },
    "Bollywood Movies": {
        "sholay": "Samba",
        "dangal": "Chhoriyan",
        "pk": "Yellow Helmet.",
        "lagaan": "Kachra.",
        "swades": "Shah Rukh in a Boat.",
        "barfi": "Falling of a Light Pole.",
        "andhadhun": "Blind.",
        "drishyam": "Gaitonde.",
        "jawan": "Bald and Bold.",
        "animal": "Jamal Kudu.",
        "stree": "Kal aana.",
        "war": "Ghoongroo Toot Gye.",
        "don": "Pakadna mushkil hi nahi...",
        "border": "Battle of Longewala.",
        "gadar": "Ye Dhai Kilo Ka Haath.",
        "sultan": "Dhobi Pachaad.",
        "koi mil gya": "Aila Jaadoo.",
        "agneepath": "Kancha Cheena.",
        "fanaa": "Kadhaksingh ke Khadakne se Khadkti he Khidkiya.",
        "ghajini": "Kalpana was Killed.",
        "yeh jawaani hai deewani": "Me jeena chahta hu,udna chahta hu aur daudna bhi chahta hu.",
        "jab we met": "An Epic Train Journey.",
        "om shanti om": "Picture abhi baaki he mere dost.",
        "chennai express": "Goa is On.",
        "bajrangi bhaijaan": "Maaamaaaaaaan!!!",
        "chak de india": "Sattar Minute.",
        "munna bhai mbbs": "Chinki.",
        "bhool bhulaiyaa": "Aa Beti Pushpa kaha jaa rahi ho",
        "hera pheri": "Sone ka Lota"
    },
    "Online Games": {
        "valorant": "Omen,Wayley and Reyna.",
        "counter strike": "The classic tactical shooter with Terrorists and Counter-Terrorists.",
        "apex legends": "A fast-paced hero battle royale set in the Titanfall universe.",
        "fortnite": "A popular battle royale where you build structures to survive.",
        "pubg": "Enemies ahead.",
        "call of duty": "A massive first-person shooter franchise known for its fast-paced multiplayer and Warzone.",
        "overwatch": "Blizzard's colorful team-based hero shooter featuring characters like Tracer.",
        "rainbow six siege": "A tactical shooter focusing on environmental destruction and operator gadgets.",
        "team fortress": "Valve's classic class-based shooter with a cartoonish art style and lots of hats.",
        "league of legends": "The most popular MOBA game, featuring Champions battling on Summoner's Rift.",
        "dota": "Valve's complex MOBA featuring heroes defending their Ancients.",
        "smite": "A third-person MOBA where you play as mythological gods.",
        "heroes of the storm": "Blizzard's crossover MOBA featuring characters from their various universes.",
        "world of warcraft": "The legendary MMORPG set in Azeroth, pitting the Alliance against the Horde.",
        "final fantasy xiv": "Square Enix's critically acclaimed MMORPG set in Eorzea.",
        "runescape": "A classic, long-running browser-based MMORPG by Jagex.",
        "guild wars": "An MMORPG known for its lack of subscription fees and dynamic events.",
        "black desert online": "An MMORPG famous for its incredibly detailed character creator and action combat.",
        "the elder scrolls online": "An MMORPG set in the same universe as Skyrim and Oblivion.",
        "lost ark": "An action-RPG MMO with isometric combat similar to Diablo.",
        "minecraft": "Pig with a Crown.",
        "rust": "A brutal multiplayer survival game where waking up naked on a beach with a rock is just the beginning.",
        "ark survival evolved": "A survival game where you can tame and ride dinosaurs.",
        "roblox": "A massive platform where players can create and play millions of user-generated games.",
        "dayz": "A gritty multiplayer zombie survival game born from an Arma 2 mod.",
        "palworld": "Often described as 'Pokemon with guns', an open-world survival and crafting game.",
        "lethal company": "A co-op horror game where you collect scrap from abandoned moons for 'The Company'.",
        "among us": "I did Trash.",
        "rocket league": "Car soccer. Boost, jump, and score massive goals.",
        "fall guys": "A colorful battle royale where jellybeans compete in chaotic obstacle courses.",
        "hearthstone": "Blizzard's popular digital collectible card game based on the Warcraft universe.",
        "teamfight tactics": "Riot's auto-battler game featuring League of Legends champions.",
        "brawlhalla": "A free-to-play platform fighter similar to Super Smash Bros.",
        "dead by daylight": "An asymmetrical horror game where one killer hunts four survivors.",
        "sea of thieves": "A co-op pirate adventure game where you sail ships, loot treasure, and fight skeletons.",
        "genshin impact": "A hugely popular gacha action-RPG with elemental combat and an anime aesthetic.",
        "warframe": "Play as space ninjas in this fast-paced, free-to-play looter shooter.",
        "destiny": "Bungie's sci-fi looter shooter featuring Guardians fighting the Darkness.",
        "path of exile": "A dark, free-to-play action RPG known for its massive passive skill tree.",
        "escape from tarkov": "A hardcore, realistic extraction shooter set in a fictional Russian region."
    },
    "Hollywood Movies": {
        "inception": "A thief steals corporate secrets by entering the subconscious minds of his targets.",
        "avatar": "Pandora ",
        "gladiator": "A betrayed Roman general seeks revenge against the corrupt emperor who murdered his family.",
        "the matrix": "A computer hacker learns the true nature of his reality and his role in the war against its machine controllers.",
        "interstellar": "A team of explorers travels through a wormhole in space in an attempt to ensure humanity's survival.",
        "jurassic park": "Steven Spielberg's Epic Depiction.",
        "titanic": "Tip of an Ice Berg.",
        "the godfather": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
        "pulp fiction": "The lives of two mob hitmen, a boxer, a gangster, and his wife intertwine in four tales of violence and redemption.",
        "the dark knight": "Joker in Gotham City.",
        "forrest gump": "Laal Singh Chaddha.",
        "star wars": "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee, and two droids.",
        "the avengers": "Earth's mightiest heroes must come together and learn to fight as a team to stop the mischievous Loki.",
        "the terminator": "A cyborg assassin is sent back in time to 1984 to kill Sarah Connor.",
        "alien": "The crew of a commercial spacecraft encounters a deadly lifeform after investigating an unknown transmission.",
        "jaws": "When a killer shark unleashes chaos on a beach community, it's up to a local sheriff, a marine biologist, and an old seafarer to hunt it down.",
        "back to the future": "A 17-year-old high school student is accidentally sent thirty years into the past in a time-traveling DeLorean.",
        "indiana jones": "An adventurous archeologist races against a band of Nazis to find a unique religious relic.",
        "rocky": "A small-time Philadelphia boxer gets a supremely rare chance to fight the world heavyweight champion.",
        "die hard": "An NYPD officer tries to save his wife and others taken hostage by German terrorists during a Christmas party at the Nakatomi Plaza.",
        "the lord of the rings": "A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring.",
        "harry potter":"z",
        "spider man": "tune churaya mere dil ka chain.",
        "iron man": "After being held captive in an Afghan cave, a billionaire engineer creates a unique weaponized suit of armor.",
        "toy story": "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
        "finding nemo": "After his son is captured in the Great Barrier Reef, a timid clownfish sets out on a journey to bring him home.",
        "the lion king": "A young cub flees his kingdom after his father's death, only to return years later to reclaim his throne from his evil uncle.",
        "frozen": "A newly crowned queen accidentally uses her power to turn things into ice to curse her home in infinite winter.",
        "shrek": "A grumpy ogre's swamp is overrun by fairytale creatures, leading him on a quest to rescue a princess.",
        "the shawshank redemption": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
        "fight club": "An insomniac office worker and a devil-may-care soap maker form an underground society with strict rules. (First rule: don't talk about it).",
        "goodfellas": "The story of Henry Hill and his life in the mob, covering his relationship with his wife and his mob partners.",
        "the silence of the lambs": "A young F.B.I. cadet must receive the help of an incarcerated and manipulative cannibal killer to catch another serial killer.",
        "the truman show": "An insurance salesman discovers his whole life is actually a reality TV show.",
        "mad max": "In a post-apocalyptic wasteland, a drifter helps a rebel woman flee from a tyrannical warlord.",
        "the martian": "An astronaut becomes stranded on the red planet and must rely on his ingenuity to find a way to signal to Earth.",
        "gravity": "Two astronauts work together to survive after an accident leaves them stranded in space.",
        "dune": "A noble family becomes embroiled in a war for control over the galaxy's most valuable asset on a dangerous desert planet.",
        "oppenheimer": "The story of the American scientist and his role in the development of the atomic bomb.",
        "barbie": "She suffers a crisis that leads her to question her world and her existence in a perfect, pink plastic land."
    },
    "Indian Actors": {
        "amitabh bachchan": "Samay Samapti ki Ghoshna!",
        "shah rukh khan": "Hakla",
        "salman khan": "Farmhouse",
        "aamir khan": "Mr. Perfectionist.",
        "hrithik roshan": "Chhati Ungli.",
        "akshay kumar": "Kya Rupa Naha Liya...?",
        "ajay devgn": "Vimal Cinematic Universe",
        "ranbir kapoor": "Beef Lover.",
        "ranveer singh": "Daboo Ratnani Photoshoot.",
        "shahid kapoor": "Anda Maang raha he.",
        "varun dhawan": "Tedha muh kya bana raha he.",
        "tiger shroff": "Only strength is Martial Arts.",
        "ayushmann khurrana": "The undisputed king of playing middle-class men with highly specific medical or social embarrassments.",
        "rajkummar rao": "Will ask you 'O Stree kal aana' while giving an absolute acting masterclass.",
        "vicky kaushal": "How's the Josh.",
        "kartik aaryan": "Paedophilia.",
        "john abraham": "Lifts heavy motorcycles instead of dumbbells and permanently rides a Hayabusa in our heads.",
        "saif ali khan": "The royal Nawab of Bollywood who somehow says 'Wow' in the most posh way possible.",
        "suniel shetty": "Anna who will constantly remind you that 'Dhadkan' is still hurting his heart.",
        "anil kapoor": "Jhakaas!",
        "sanjay dutt": "Prisoner to a Superstar.",
        "nana patekar": "Kaanda Lelo...",
        "allu arjun": "Lucky.",
        "brahmanandam": "Kilbil Pandey.",
        "prabhas": "Current Flopstar of Tollywood.",
        "mahesh babu": "No Expressions.",
        "pawan kalyan": "The 'Power Star' who can make his fans go absolutely crazy just by rubbing his neck.",
        "vijay": "Thalapathy",
        "ajith kumar":"Thala who loves racing cars and making a salt-and-pepper beard look incredibly cool.",
        "rajinikanth": "Mind it!",
        "kamal haasan": "Can play 10 completely different characters in the same movie and you wouldn't even notice.",
        "suriya": "Played a fiery cop with a massive mustache in Singam and has a jawline sharper than a knife.",
        "dhanush": "Made the entire country sing about a 'Kolaveri Di' soup song.",
        "yash": "Daddy's Home.",
        "rishab shetty": "Screamed his way to a blockbuster while performing a mesmerizing, divine Panjurli Daiva dance.",
        "dulquer salmaan": "The ultimate Malayalam heartthrob who can pull off a vintage car road trip like nobody else.",
        "fahadh faasil": "Can act better with just a stare from his bulging eyes than most actors can with their whole bodies.",
        "mohanlal": "The complete actor 'Lalettan' who can effortlessly twitch his shoulder and make theaters erupt.",
        "mammootty": "The legendary Malayalam megastar who looks younger at 70 than most 30-year-olds."
    },
    "Indian Actresses": {
        "deepika padukone": "Mere appa ki gaadi.",
        "alia bhatt": "Dhoptengi na usko.",
        "katrina kaif": "Salman Khan.",
        "priyanka chopra": "The girl who made us all fall for her in 'The Namesake'.",
        "kareena kapoor": "Main apni Favourite hoon!.",
        "anushka sharma": "Chikoo.",
        "shraddha kapoor": "Chhatri.",
        "kriti sanon": "Played a robot and a surrogate mother, proving she's more than just a tall glass of water.",
        "disha patani": "Calvin Klein.",
        "taapsee pannu": "Gulabi.",
        "vidya balan": "Dirty Picture.",
        "kangana ranaut": "Hrithik Roshan.",
        "aishwarya rai": "Salman Khan.",
        "sushmita sen": "Indian Miss Universe.",
        "madhuri dixit": "Nimbooda.",
        "kajol": "Eyeroll.",
        "rani mukerji": "The husky-voiced queen of the 2000s, whether she's a con artist or a tough cop.",
        "preity zinta": "Aloo Parathe.",
        "juhi chawla": "KKR.",
        "karisma kapoor": "Lolo, who danced with Govinda in outfits brighter than the sun.",
        "tabu": "Ajay Devgn.",
        "nayanthara": "The 'Lady Superstar' of South India who recently debuted in Bollywood with 'Jawan'.",
        "samantha ruth prabhu": "Danced to 'Oo Antava' and single-handedly broke the internet.",
        "anushka shetty": "Devasena, who shot arrows better than Baahubali himself.",
        "tamannaah bhatia": "The 'Milky Beauty' who danced in the rain in 'Kaavaalaa'.",
        "kajal aggarwal": "The wide-eyed beauty who was everyone's favorite 'Darling' in Telugu cinema.",
        "pooja hegde": "Often found playing the extremely glamorous lead in massive Pan-Indian blockbusters.",
        "rashmika mandanna": "The 'National Crush' who made hand-heart signs very, very popular.",
        "shruti haasan": "The rockstar daughter of a legend, known for her gothic aesthetic off-screen.",
        "trisha krishnan": "Jessie from VTV who broke a million hearts just by wearing a cotton saree.",
        "mrunal thakur": "Sita Mahalaxmi, whose single tear is enough to make the audience weep.",
        "sreeleela": "The current sensation of Tollywood whose dance speed can rival any hero's.",
        "keerthy suresh": "Won a National Award for flawlessly bringing the legendary actress Savitri back to life.",
        "sai pallavi": "The 'Rowdy Baby' who refuses to wear makeup on screen and still looks flawless.",
        "radhika apte": "At one point, it felt like she was starring in every single Netflix India original.",
        "bhumi pednekar": "Specializes in playing strong-willed women from small towns in socially relevant films.",
        "sanya malhotra": "Broke stereotypes (and bones) as a wrestler in 'Dangal'.",
        "yami gautam": "Started by selling fairness cream, now delivers critically acclaimed thrillers.",
        "sonam kapoor": "Bollywood's resident fashionista who is always ready for a Vogue cover."
    },
    "Cities": {
        "nashik": "Cheetah.",
        "pune": "Porsche.",
        "mumbai": "Wadapav.",
        "rameshwaram": "A peaceful island city at the very tip of India, famous for its grand temple.",
        "delhi": "Pollution.",
        "bangalore": "What ra sudeep!!!",
        "chennai": "Filter Coffee.",
        "kolkata": "Babu Moshaay.",
        "hyderabad": "Baingan baataan.",
        "ahmedabad": "The largest city in Gujarat, known for the Sabarmati Ashram and dhokla.",
        "jaipur": "The Pink City, full of royal palaces, forts, and vibrant bazaars.",
        "surat": "The diamond city of India, also famous for its textile industries.",
        "lucknow": "The city of Nawabs, known for adab (manners) and amazing kebabs.",
        "kanpur": "A major industrial city in UP, historically known as the Manchester of the East.",
        "nagpur": "Ho na bey!!!.",
        "indore": "Sarafa.",
        "bhopal": "The city of lakes, tragically known for the 1984 gas tragedy.",
        "patna": "The ancient city of Pataliputra, located on the southern bank of the Ganges.",
        "agra": "Home to the magnificent Taj Mahal.",
        "varanasi": "One of the oldest living cities in the world, known for its spiritual ghats along the Ganges.",
        "london": "A foggy city famous for a big clock tower and a royal family.",
        "tokyo": "A neon-lit metropolis known for anime, sushi, and the Shibuya crossing.",
        "paris": "The city of love, croissants, and a very famous iron tower.",
        "new york": "The Big Apple, a city so nice they named it twice, featuring a green lady with a torch.",
        "dubai": "A desert city known for luxury shopping, artificial islands, and the tallest building in the world.",
        "singapore": "A squeaky-clean island city-state with a massive ship-shaped hotel on top of three towers.",
        "sydney": "An Australian city famous for its sail-shaped opera house.",
        "toronto": "A Canadian city marked by the towering CN Tower.",
        "berlin": "A German city known for its history, techno clubs, and a wall that came down in 1989.",
        "rome": "An ancient city where you can throw coins in a fountain and visit the Colosseum.",
        "madrid": "The capital of Spain, known for its royal palace and a famous football team in white.",
        "amsterdam": "A city full of canals, bicycles, and very liberal coffee shops.",
        "seoul": "A bustling South Korean city known for K-pop and high-tech subways.",
        "beijing": "The capital of China, home to the Forbidden City.",
        "istanbul": "A city that physically bridges Europe and Asia.",
        "moscow": "The capital of Russia, famous for the colorful domes of St. Basil's Cathedral.",
        "bangkok": "A bustling Thai city known for ornate shrines and vibrant street life.",
        "cairo": "A sprawling Egyptian city resting near the Giza pyramid complex.",
        "cape town": "A port city on South Africa's southwest coast, nestled beneath Table Mountain.",
        "rio de janeiro": "A vibrant Brazilian city known for Copacabana beach and a giant Christ statue."
    },
    "Superheroes": {
        "spider man": "_________ tune churaya mere dil ka chain!!.",
        "iron man": "Maximoff hates him.",
        "captain america": "Frisbee.",
        "thor": "Godbod.",
        "hulk": "Smaaasshhh!!!.",
        "black widow": "Romanoff.",
        "hawkeye": "Lucky for the Team.",
        "black panther": "Vibranium.",
        "doctor strange": "14,000,605.",
        "ant man": "Could have been more useful to kill Thanos.",
        "captain marvel": "Punch through spaceships.",
        "wolverine": "Knuckles.",
        "deadpool": "Desert Eagle Mark XIX pistols.",
        "cyclops": "An X-Men leader who really needs to keep his special ruby-quartz sunglasses on.",
        "storm": "A mutant goddess who can ruin your picnic with a lightning strike.",
        "star lord": "Dance-off.",
        "groot": "Three words - We are _____.",
        "rocket raccoon": "Being called a Rodent.",
        "drax": "Invisible.",
        "gamora": "Where is ______?,Who is ______?,Why is ______?.",
        "daredevil": "Hell's Kitchen.",
        "moon knight": "A man with dissociative identity disorder who wears white so the bad guys can see him coming.",
        "ghost rider": "A stunt motorcyclist who doesn't BURN.",
        "silver surfer": "A shiny cosmic herald who glides space on a board.",
        "superman": "An alien reporter who disguises himself by simply wearing glasses.",
        "batman": "Gotham.",
        "wonder woman": "An Amazonian princess armed with a glowing lasso of truth.",
        "flash": "A forensic scientist who got struck by lightning and is now chronically late despite being the fastest man alive.",
        "aquaman": "The King of Atlantis who is constantly mocked for talking to fish.",
        "green lantern": "Wears a ring powered by willpower that constructs anything he imagines, as long as it's green.",
        "cyborg": "A former college athlete who is now more machine than man.",
        "martian manhunter": "A shape-shifting, telepathic alien who really loves Choco cookies.",
        "green arrow": "A billionaire mayor who decided to fight crime with a bow, a hood, and a goatee.",
        "nightwing": "Batman's original sidekick who grew up, moved to Bludhaven, and got a much cooler costume.",
        "supergirl": "The Man of Steel's older cousin who arrived on Earth a little late.",
        "batgirl": "The police commissioner's daughter who fights crime in Gotham.",
        "shazam": "A teenager who turns into a magical adult superhero by shouting a single word.",
        "plastic man": "A former crook who gained the ability to stretch and contort his body into anything.",
        "blue beetle": "A teenager who bonded with an alien scarab that gives him a high-tech suit of armor.",
        "invincible": "Mark Grayson, the teenage son of Omni-Man, who learns that taking a punch really hurts."
    },
    "Sports": {
        "football": "Chase a Ball and kick it.",
        "basketball": "Curry.",
        "cricket": "Gentleman.",
        "tennis": "A sport where 'love' actually means you have zero points.",
        "baseball": "Hit a small white ball with a wooden stick and run in a diamond shape.",
        "rugby": "Like American football, but without the helmets or forward passes.",
        "golf": "An expensive excuse to walk a long distance and hit a tiny ball into a tiny hole.",
        "volleyball": "Don't let the ball touch the floor on your side of the net.",
        "table tennis": "Ping pong.",
        "badminton": "Hitting a feathered cone over a net with a racket.",
        "swimming": "Trying not to drown as fast as possible in a pool.",
        "athletics": "Running, jumping, or throwing things very far.",
        "boxing": "Punching another person with padded gloves until someone falls down.",
        "wrestling": "Grappling an opponent to the mat in a singlet.",
        "gymnastics": "Flipping, tumbling, and balancing gracefully.",
        "cycling": "Pedaling a two-wheeled machine very fast, often in a pack.",
        "skiing": "Sliding down a snowy mountain on two long planks attached to your feet.",
        "snowboarding": "Surfing down a snowy mountain on a single board.",
        "surfing": "Riding a board on the face of a moving ocean wave.",
        "hockey": "Using sticks to hit a ball into a goal on a field.",
        "ice hockey": "Using sticks to hit a rubber puck into a goal while skating on ice.",
        "american football": "A game with a pointy ball where throwing it forward is actually allowed.",
        "water polo": "Like handball, but you're treading water in a deep pool.",
        "rowing": "Moving a boat backward using oars.",
        "sailing": "Using the wind to propel a boat across the water.",
        "fencing": "Sword fighting, but with wires and a beeping machine.",
        "archery": "Shooting arrows at a target with a bow.",
        "weightlifting": "Picking up very heavy metal plates attached to a bar.",
        "judo": "A martial art focused on throwing your opponent to the ground.",
        "taekwondo": "A Korean martial art famous for fast, high spinning kicks.",
        "karate": "A Japanese martial art focusing on striking with hands and feet.",
        "polo": "Hitting a small ball with a mallet while riding a horse.",
        "squash": "Hitting a rubber ball against a wall in an enclosed court.",
        "snooker": "A cue sport played on a green baize table with 22 colored balls.",
        "billiards": "A general term for cue sports, often referring to carom or pocket games.",
        "darts": "Throwing small pointy missiles at a round board in a pub.",
        "bowling": "Rolling a heavy ball down a wooden lane to knock down 10 pins.",
        "kabaddi": "A contact team sport where you raid the enemy half while chanting a single word.",
        "kho kho": "A traditional Indian tag game involving sitting and chasing.",
        "kickboxing": "A combat sport combining punches and kicks."
    }
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
    print(f"The answer was: {answer.upper()}😊")

def display_blanks(blanks):
    print(" ".join(blanks))

def play_round():
    print("\nChoose a Genre😎:")
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
            print("Invalid Input!!! Please enter a valid number.😒")

    genre_dict = words[selected_genre]
    answer = random.choice(list(genre_dict.keys()))
    text_hint = genre_dict[answer]

    wrong_guesses = 0
    blanks = [" " if char == " " else "_" for char in answer]
    guessed_letters = set()

    while True:
        display_hangman(wrong_guesses)
        print(f"HINT: {text_hint}")
        display_blanks(blanks)
        
        print() # Adding a blank line for breathing room before input
        guess = input("Guess a Letter😁: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input!!!😩 Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"'{guess}' has already been guessed😒. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    blanks[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in blanks:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print("\nCONGRATS!!! YOU WIN!!!😍")
            return True
            
        elif wrong_guesses >= len(hangman_draw) - 1:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print("\nGAME OVER!!! BETTER LUCK NEXT TIME!!!😭")
            return False

def main():
    print("=== 🙌WELCOME TO HANGMAN🙌 ===")
    
    streak = 0  
    
    while True:
        won_round = play_round() 
        
        if won_round:
            streak += 1
            print(f"🔥 Current Winning Streak: {streak} 🔥")
        else:
            streak = 0
            print(f"❄️ Streak broken! Back to 0. ❄️")
            
        replay = input("\nWanna Play Again?😏 (y/n): ").lower()
        if replay != 'y':
            print(f"\nTHANK YOU FOR PLAYING!!! You finished with a streak of {streak}.😣")
            break

if __name__ == "__main__":
    main()





