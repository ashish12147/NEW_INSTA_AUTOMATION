"""Deterministic caption and hashtag packs for the @44.o0 meme automation.

No AI is used at runtime.  The rotation is deliberately controlled so that
72-hour performance can be compared by caption strategy and hashtag pack.
"""
from __future__ import annotations

ROTATION = ("MEME", "WEIRD", "MEME", "ENGAGEMENT", "WEIRD")

MEME_CAPTIONS = (
    "bro had exactly one job",
    "nah this cannot be real",
    "the confidence made it ten times worse",
    "everything was fine for approximately two seconds",
    "no thoughts. just consequences.",
    "this escalated with zero warning",
    "the last second got me",
    "why did that actually work",
    "the timing is criminal",
    "somebody explain the thought process here",
    "the plot changed immediately",
    "he really committed to the bit",
    "this is the kind of decision you make once",
    "I was not prepared for the ending",
    "the second-hand embarrassment is undefeated",
    "there was definitely a better way to do this",
    "watching the plan leave the chat in real time",
    "that pause before disaster says everything",
    "the recovery attempt somehow made it worse",
    "zero hesitation was the first mistake",
    "the camera person knew exactly what was coming",
    "every frame somehow gets worse",
    "we all know one person who would do this",
    "the unnecessary confidence is sending me",
    "this deserves a frame-by-frame investigation",
    "that was not in the tutorial",
    "the ending changed the entire video",
    "a completely normal sequence of events",
    "the silence afterwards is the funniest part",
    "this is why instructions exist",
)

ENGAGEMENT_CAPTIONS = (
    "send this to the friend who would absolutely do this",
    "rate the decision making from 1 to 10",
    "tag the person who needs to see this with no context",
    "who in your group is doing this first",
    "be honest: would you have tried it too",
    "which second made you lose it",
    "send this to someone who laughs at the worst possible moment",
    "what would you even do after this",
    "name the friend who would make this situation worse",
    "would you help or start recording",
    "one word for this entire situation",
    "who is surviving this: you or your best friend",
    "tell me you have a friend like this without naming them",
    "what was the exact moment the plan failed",
    "save this for the next group chat argument",
    "who needs to be banned from trying this",
    "would you admit this happened or take it to the grave",
    "send it to the person whose ideas always start like this",
    "how many times did you replay the ending",
    "pick a side: genius or absolute disaster",
)

# Intentionally unrelated explainer/fact captions.  This mirrors the current
# meme-page "why is THAT the caption?" format without relying on one stale
# copypasta.  Facts are kept broad and non-medical/non-financial.
WEIRD_CAPTIONS = (
    "A black box on an aircraft is usually bright orange, not black. The color makes the recorder easier to locate after an accident, while the name comes from older engineering terminology rather than its appearance.",
    "QR codes can still work when part of the image is damaged because they include error-correction data. The three large squares help a scanner identify the code's orientation before it reads the smaller pattern.",
    "Bananas are botanically classified as berries, while strawberries are not true berries. Botanical names are based on how the fruit develops from the flower, not on how people group fruit in everyday language.",
    "Octopuses have three hearts. Two mainly move blood through the gills, while another circulates it through the rest of the body. Their blood also uses a copper-containing protein that gives it a bluish appearance.",
    "Airplane windows are rounded because sharp corners concentrate stress. As aircraft cabins repeatedly pressurize and depressurize, a rounded shape distributes that stress more smoothly through the fuselage.",
    "The tiny hole near the bottom of many airplane windows is called a breather hole. It helps balance pressure between layers of the window so the outer pane carries most of the pressure load.",
    "A day on Venus is longer than a year on Venus. The planet rotates extremely slowly on its axis, while its trip around the Sun takes less time than one complete Venusian rotation.",
    "Traffic lights did not begin with today's familiar three-color electronic systems. Early versions were inspired by railway signals, and electric traffic lights developed as cities needed safer ways to manage growing road traffic.",
    "The word 'robot' comes from the Czech word 'robota', associated with forced labor or work. It became widely known after appearing in Karel Capek's 1920 play R.U.R.",
    "A standard deck of 52 cards can be shuffled into more possible orders than there are stars in the observable universe by many estimates. The number of arrangements is 52 factorial, an unimaginably large value.",
    "The Eiffel Tower can become slightly taller in hot weather. Metal expands as its temperature rises, so thermal expansion can change the height of the iron structure by several centimeters across seasonal conditions.",
    "Sharks existed long before trees. The earliest shark-like animals appeared hundreds of millions of years ago, while the first true trees evolved much later in Earth's history.",
    "The dot over a lowercase i or j has a name: a tittle. The word has been used for centuries for a small distinguishing mark in writing or printing.",
    "The smell after rain has a name: petrichor. The term describes the earthy scent associated with rain hitting dry ground, including compounds released from soil and plant material.",
    "Some turtles can absorb oxygen through specialized tissues near the rear of their bodies while underwater. The adaptation helps certain species remain submerged for long periods, especially in cold conditions.",
    "The first computer mouse prototype was made from wood. Early designs used mechanical wheels to track movement, long before the optical and laser sensors common in modern mice.",
    "The Moon is slowly moving away from Earth by a few centimeters each year. Measurements made with lasers bounced off reflectors left on the lunar surface allow scientists to track the change very precisely.",
    "Honey can remain edible for an exceptionally long time when sealed and stored properly because it has very little available water and is naturally acidic, conditions that make it difficult for many microorganisms to grow.",
    "The small pocket on many pairs of jeans was originally designed for a pocket watch. Its purpose dates back to nineteenth-century workwear, even though it is now mostly used for tiny modern objects.",
    "Wombat droppings are famously cube-shaped. Their intestines compress material unevenly as it dries, producing the unusual shape before it leaves the body.",
    "今日もなんとか生き延びた。特に理由はない。 Translation: somehow survived today too. No particular reason.",
    "「あとでやる」は、ときどき一番長い予定になる。 Translation: 'I'll do it later' sometimes becomes the longest plan of all.",
    "The ampersand symbol, &, developed from a stylized combination of the Latin letters e and t, forming the word 'et', which means 'and'. Its modern shape is the result of centuries of handwriting and typography.",
    "Bluetooth is named after Harald 'Bluetooth' Gormsson, a tenth-century Scandinavian king. The technology's logo combines runic characters representing his initials.",
)

HASHTAG_PACKS = (
    ("CORE_A", ("#memes", "#funnyreels", "#funnymemes", "#relatable", "#reels")),
    ("CORE_B", ("#memesdaily", "#funny", "#reelsinstagram", "#comedy", "#viralreels")),
    ("REACTION_A", ("#meme", "#reaction", "#funnyvideos", "#lol", "#reels")),
    ("DISCOVERY_A", ("#funnymemes", "#explorepage", "#memepage", "#reelitfeelit", "#funnyreels")),
    ("CORE_C", ("#memes", "#comedyreels", "#relatablememes", "#funnyvideo", "#reels")),
    ("DISCOVERY_B", ("#viral", "#memesdaily", "#funnyreels", "#explore", "#reelsinstagram")),
    ("REACTION_B", ("#funny", "#memevideo", "#reactionmemes", "#comedy", "#reels")),
    ("CORE_D", ("#funnymemes", "#memes", "#dailyhumor", "#funnyclips", "#reels")),
    ("EXPERIMENT_A", ("#meme", "#viralreels", "#explorepage", "#funny", "#reelsvideo")),
    ("EXPERIMENT_B", ("#memepage", "#reels", "#funnyreels", "#trendingreels", "#relatable")),
    ("CORE_E", ("#memesdaily", "#funnyvideos", "#comedyreels", "#meme", "#reels")),
    ("DISCOVERY_C", ("#reelsinstagram", "#funny", "#memes", "#viralvideo", "#comedy")),
)


def build_caption(order_index: int) -> tuple[str, str, str, str]:
    """Return (caption, strategy, caption_key, hashtag_pack_key)."""
    n = max(1, int(order_index))
    strategy = ROTATION[(n - 1) % len(ROTATION)]
    cycle = (n - 1) // len(ROTATION)

    if strategy == "MEME":
        pool = MEME_CAPTIONS
    elif strategy == "ENGAGEMENT":
        pool = ENGAGEMENT_CAPTIONS
    else:
        pool = WEIRD_CAPTIONS

    # Different multipliers keep the caption and hashtag cycles from lining up
    # too quickly while remaining completely deterministic.
    caption_index = (cycle * 7 + n * 3) % len(pool)
    tag_index = (n * 7 + cycle * 5) % len(HASHTAG_PACKS)
    pack_key, tags = HASHTAG_PACKS[tag_index]
    base = pool[caption_index]
    caption = f"{base}\n\n{' '.join(tags)}"
    caption_key = f"{strategy}:{caption_index}"
    return caption, strategy, caption_key, pack_key
