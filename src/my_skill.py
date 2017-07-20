# coding=utf-8
import random
from all_voice.models import AllVoice

welcome_messages = [
    "I think so Brainini but arugula flavoured gelato?",
    "I think so, Brain, but where are we going to find a duck and a hose at this hour?",
    "I think so, but where will we find an open tattoo parlor at this time of night?",
    "Wuh, I think so, Brain, but if we didn't have ears, we'd look like weasels.",
    "Uh... yeah, Brain, but where are we going to find rubber pants our size?",
    "Uh, I think so, Brain, but balancing a family and a career ... ooh, it's all too much for me.",
    "Wuh, I think so, Brain, but isn't Regis Philbin already married?",
    "Wuh, I think so, Brain, but burlap chafes me so.",
    "Sure, Brain, but how are we going to find chaps our size?",
    "Uh, I think so, Brain, but we'll never get a monkey to use dental floss.",
    "Are you pondering cheesesticks?",
    "Uh, I think so Brain, but this time, you wear the tutu.",
    "I think so, Brain, but culottes have a tendency to ride up so.",
    "I think so, Brain, but if we covered the world in salad dressing wouldn't the asparagus feel left out?",
    "I think so, Brain, but if they called them 'Sad Meals', kids wouldn't buy them!",
    "I think so, Brain, but me and Pippi Longstocking -- I mean, what would the children look like?",
    "I think so, Brain, but what would Pippi Longstocking look like with her hair straight?",
    "I think so, Brain, but this time you put the trousers on the chimp.",
    "Well, I think so, Brain, but I can't memorize a whole opera in Yiddish.",
    "I think so, Brain, but there's still a bug stuck in here from last time.",
    "Uh, I think so, Brain, but I get all clammy inside the tent.",
    "I think so, Brain, but I don't think Kaye Ballard's in the union.",
    "I think so, Brain, but, the Rockettes? I mean, it's mostly girls, isn't it?",
    "I think so, Brain, but pants with horizontal stripes make me look chubby.",
    "Well, I think so -POIT- but where do you stick the feather and call it macaroni?",
    "Well, I think so, Brain, but pantyhose are so uncomfortable in the summertime.",
    "Well, I think so, Brain, but it's a miracle that this one grew back.",
    "Well, I think so, Brain, but first you'd have to take that whole bridge apart, wouldn't you?",
    "Well, I think so, Brain, but 'apply North Pole' to what?",
    "I think so, Brain, but 'Snowball for Windows'?",
    "Well, I think so, Brain, but snort no, no, it's too stupid!",
    "Umm, I think so, Don Cerebro, but, umm, why would Sophia Loren do a musical?",
    "Umm, I think so, Brain, but what if the chicken won't wear the nylons?",
    "I think so, Brain, but isn't that why they invented tube socks?",
    "Well, I think so Brain, but what if we stick to the seat covers?",
    "I think so Brain, but if you replace the 'P' with an 'O', my name would be Oinky, wouldn't it?",
    "Oooh, I think so Brain, but I think I'd rather eat the Macarena.",
    "Well, I think so hiccup, but Kevin Costner with an English accent?",
    "I think so, Brain, but don't you need a swimming pool to play Marco Polo?",
    "Well, I think so, Brain, but do I really need two tongues?",
    "I think so, Brain, but we're already naked.",
    "Well, I think so, Brain, but if Jimmy cracks corn, and no one cares, why does he keep doing it?",
    "I think so, Brain NARF, but don't camels spit a lot?",
    "I think so, Brain, but how will we get a pair of Abe Vigoda's pants?",
    "I think so, Brain, but Pete Rose? I mean, can we trust him?",
    "I think so, Brain, but why would Peter Bogdanovich?",
    "I think so, Brain, but isn't a cucumber that small called a gherkin?",
    "I think so, Brain, but if we get Sam Spade, we'll never have any puppies.",
    "I think so, Larry, and um, Brain, but how can we get seven dwarves to shave their legs?",
    "I think so, Brain, but calling it pu-pu platter? Huh, what were they thinking?",
    "I think so, Brain, but how will we get the Spice Girls into the paella?",
    "I think so, Brain, but if we give peas a chance, won't the lima beans feel left out?",
    "I think so, Brain, but I am running for mayor of Donkeytown and Tuesdays are booked.",
    "I think so, Brain, but if we had a snowmobile, wouldn't it melt before summer?",
    "I think so, Brain, but what kind of rides do they have in Fabioland?",
    "I think so, Brain, but can the Gummi Worms really live in peace with the Marshmallow Chicks?",
    "Wuh, I think so, Brain, but wouldn't anything lose its flavor on the bedpost overnight?",
    "I think so, Brain, but three round meals a day wouldn't be as hard to swallow.",
    "I think so, Brain, but if the plural of mouse is mice, wouldn't the plural of spouse be spice?",
    "Umm, I think so, Brain, but three men in a tub? Ooh, that's unsanitary!",
    "Yes, but why does the chicken cross the road, huh, if not for love? I do not know.",
    "Wuh, I think so, Brain, but I prefer Space Jelly.",
    "Yes Brain, but if our knees bent the other way, how would we ride a bicycle?",
    "Wuh, I think so, Brain, but how will we get three pink flamingos into one pair of Capri pants?",
    "I think so, Brain, but Tuesday Weld isn't a complete sentence.",
    "I think so, Brain, but why would anyone want to see Snow White and the Seven Samurai?",
    "I think so, Brain, but then my name would be Thumby.",
    "I think so, Brain, but I find scratching just makes it worse.",
    "I think so, Brain, but shouldn't the bat boy be wearing a cape?",
    "I think so, Brain, but why would anyone want a depressed tongue?",
    "Um, I think so, Brainie, but why would anyone want to Pierce Brosnan?",
    "Methinks so, Brain, verily, but dost thou think Pete Rose by any other name would still smell as sweaty?",
    "I think so, Brain, but wouldn't his movies be more suitable for children if he was named Jean-Claude van Darn?",
    "Wuh, I think so, Brain, but will they let the Cranberry Duchess stay in the Lincoln Bedroom?",
    "I think so, Brain, but why does a forklift have to be so big if all it does is lift forks?",
    "I think so, Brain, but if it was only supposed to be a three hour tour, why did the Howells bring all their money?",
    "I think so, Brain, but Zero Mostel times anything will still give you Zero Mostel.",
    "I think so, Brain, but if we have nothing to fear but fear itself, why does Eleanor Roosevelt wear that spooky mask?",
    "I think so, Brain, but what if the hippopotamus won't wear the beach thong?",
    "Um, I think so, Brain-2, but a show about two talking lab mice? Hoo! It'll never get on the air.",
    "I think so, Brain, but Lederhosen won't stretch that far.",
    "Yeah, but I thought Madonna already had a steady bloke!",
    "I think so, Brain, but what would goats be doing in red leather turbans?",
    "I think so, Brain... but how would we ever determine Sandra Bullock's shoe size?",
    "Yes, Brain, I think so. But how do we get Twiggy to pose with an electric goose?",
    "I think so, Brain. But if I put on two tutu's, would I really be wearing a four-by-four?",
    "I think so, Brain, but wouldn't mustard make it sting?",
    "I think so, Brain, but can you use the word 'asphalt' in polite society?",
    "I think so, Mr. Brain, but if the sun'll come out tomorrow, what's it doing right now?",
    "I think so, Brain, but aren't we out of shaving cream?",
    "Oh yes, Brain! Remind me to tape all our phone calls!",
    "Um, I think so, Brain, but I hear Hillary is the jealous type.",
    "I think so, Brain, but Madonna's stock is sinking.",
    "I think so, Brain. But does 'Chunk o' Cheesy's' deliver packing material?",
    "I think so, Brain wulf, but if we're Danish, where's the cream cheese? Narf!",
    "I think so, Bwain, but I don't think newspaper will fit in my underoos.",
    "Uh, I think so, Brain--but after eating newspaper all day, do I really need the extra fiber?",
    "I think so, Brain! But isn't a dreadlock hair extension awfully expensive?",
    "I think so, Brain. But will anyone other than Eskimos buy blubber-flavored chewing gum?",
    "I think so, Brain, but the ointment expired weeks ago!",
    "I think so, Brain. But would the villains really have gotten away with it, if it weren't for those pesky kids and their dog?",
    "Uh, I think so Brain, but how are we gonna teach a goat to dance with flippers on?",
    "Wuhh... I think so, Brain! But let's use safflower oil this time! It's ever so much healthier!",
    "Wuh... I think so, Brain. But Cream of Gorilla Soup—well, we'd have to sell it in awfully big cans, wouldn't we?",
    "I think so, Brain. But if he left chocolate bullets instead of silver, they'd get all runny and gooey!",
    "Yes, Brain, I think so, but do nuts go with pudding?",
    "I think so, Brain, but a codpiece made from a real fish would get smelly after a while, wouldn’t it?",
    "I think... so, Brain... *gag* ...but I didn't know Annette used peanut butter in that way.",
    "I think so, Brain, but do those roost in this neighborhood?",
    "I think so, Brain, but is the world ready for angora bellbottoms? I mean I can see wearing them inside out, but that would--",
    "I think so, Commander Brain from Outer Space! But do we have time to grease the rockets?",
    "I think so, Doctor. But are these really the legs of a show girl?",
    "Whuh... I think so, Brain. But this time I get to play the dishwasher repairman!",
    "I think so, Brainius. But what if a sudden wind were to blow up my toga?",
    "I think so, Brain. But Trojans won’t arrive on the scene for another 300 years.",
    "I think so, Brain... but where would a yak put PVC tubing?",
    "Whuh... I think so, Brain, but... but if Charlton Heston doesn't eat Soylent Green, what will he eat?",
    "Yes, I am! But where would you get a chicken, 20 yards of spandex and smelling salts at this hour?",
    "I think so, Brain, but Ben Vereen never answered our proposition.",
    "I think so, Brain, but wouldn't an itsy-bitsy, teeny-weenie, yellow polka-dot one-piece be better suited for my figure?",
    "I think so, Brain, but won't it go straight to my hips?!",
    "I think so, Ali-Brain! But isn't it cheating to use glue?",
    "Whuu... I think so, BrainPan! But if running shoes had little feet, wouldn't they need their own shoes?",
    "I think so, Brain. But what if the Earl of Essex doesn't like burlap pantaloons?",
    "I think so, Brain, but should we use dishwashing liquid or cooking oil?",
    "I think so, Brain! We'll dress up like biker dudes and infiltrate the Hades Ladies. Then we'll convince them to hold a meeting inside the corn palace. Narf! The resulting carbon-monoxide buildup will allow you to complete your energy-making device and shortly after, you will rule the world!",
    "I think so, Brain, but would Danish flies work just as well?",
    "We think so, Brain! But dressing like twins is so tacky.",
    "I think so, Brain, but practicing docking procedures with a goat at zero G's—it's never been done!",
    "I think so, Brain! But shouldn't we let the silk worms finish the boxer shorts before we put them on?",
    "I think so, Brain! You draw the bath and I'll fetch the alka-seltzers and candles!",
    "I think so, Brain. But the real trick will be getting Demi Moore out of the creamed corn!",
    "Wuhhh... I think so, Brain, but if a ham can operate a radio, why can't a pig set a VCR?",
    "I think so, Brain, you'd think [Lyndon Johnson would] have left room for baby-kissing, wouldn't you?",
    "I think so, Brain! But won't Mr. Hoover notice a missing evening gown?",
    "I think so, Brain! But what's the use of having a heart-shaped tattoo if it's going to be covered by hair?",
]


class PinkySkill(AllVoice):
    """
    Speech skill where function names are called as actions.
    """

    # ACTIONS
    def Pondering(self):
        return self.build_response(
            speech=random.choice(welcome_messages),
        )
