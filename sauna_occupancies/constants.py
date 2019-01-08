import datetime

SONG_CHOICES = (
    ('Rock', (
        (101, 'Play All'),
        (102, 'America - A Horse with no Name'),
        (103, 'Alphaville - Big in Japan'),
        (104, 'Arctic Monkeys - Do I Wanna Know'),
        (105, 'Crystal Waters - Gypsy Woman'),
        (106, 'David Bowie - Heroes'),
        (107, 'David Bowie - Look Back in Anger'),
        (108, 'David Bowie - Ashes to Ashes'),
        (109, 'Dire Straits - Sultans of Swing'),
        (110, 'Gnarls Barkley - Crazy'),
        (111, 'Grateful Dead - Box of Rain'),
        (112, 'Jefferson Airplane - White Rabbit'),
        (113, 'Jefferson Airplane - Somebody to Love'),
        (114, 'Led Zeppelin - Kashmir'),
        (115, 'MGMT - Kids'),
        (116, 'Nirvana - Smells Like Teen Spirit'),
        (117, 'Pink Floyd - Comfortably Numb'),
        (118, 'Beach Boys - Kokomo'),
        (119, 'Beach Boys - Pet Sounds'),
        (120, 'Beatles - Lucy in the Sky with Diamonds'),
        (121, 'Beatles - Yesterday'),
        (122, 'The Cranberries - Zombie'),
        (123, 'The Eagles - Hotel California'),
        (124, 'Toto - Hold the Line'),
        (125, 'War - Low Rider'),
        (126, 'Westbam - You Need the Drugs'),
    )
     ),
    ('Techno', (
        (201, 'Play All'),
        (202, 'Marek Hemmann - Moments (Full Album)'),
        (203, 'Ben C & Kalsx - Odysseus'),
        (204, 'Dominik Eulberg - Dream Machine'),
        (205, 'Kormac - Wash my Hands'),
        (206, 'Marek Hemmann - Joker'),
        (207, 'Marek Hemmann - You Know'),
        (208, 'N\'to - 1825'),
        (209, 'Oliver Koletzki - Arrow & Bow'),
        (210, 'Paul Kalkbrenner - Sky and Sand'),
        (211, 'Rimini Sunset - Sunrise'),
        (212, 'Romulus - Chacruna'),
        (213, 'Ruederich - Top Of The World'),
        (214, 'Vini Vici - Alteza'),
        (215, 'Vini Vici - The Tribe'),
    )
     ),
    ('Reggae', (
        (301, 'Play All'),
        (302, 'Manu Chao - Clandestino (Full Album)'),
        (303, 'Bob Marley - I Smoke Two Joints'),
        (304, 'Bob Marley - Sunshine Reggae'),
        (305, 'Green Car Motel - Destino de Abril'),
        (306, 'Manu Chao - Bongo Bong'),
        (307, 'Manu Chao - Me Gustas Tu'),
        (308, 'Manu Chao - Mentira'),
        (309, 'Manu Chao - Mr. Bobby'),
        (310, 'Manu Chao - Welcome to Tijuana'),
        (311, 'Mr. President - Coco Jambo'),
    )
     ),
    ('Party', (
        (401, 'Play All'),
        (402, 'Alligatoah - Willst Du'),
        (403, 'Flume - You and Me'),
        (404, 'Falco - Der Mann mit dem Koks'),
        (405, 'Gigi d\'Agostino - L\'amour Toujours'),
        (406, 'KIZ - Neuruppin'),
        (407, 'Liquido - Narcotic'),
        (408, 'Marsimoto - Angst'),
        (409, 'Mickie Krause - Biste braun kriegste Fraun'),
        (410, 'Tim Toupet - Fliegerlied'),
        (411, 'The Bloodhound Gang - The Bad Touch'),
        (412, 'Trailerpark - Bleib in der Schule'),
        (413, 'Trailerpark - Koks auf Hawaii'),
        (414, 'Udo Jürgens - Griechischer Wein'),
        (415, 'Europe - The Final Countdown'),
    )
     ),
    ('Klassik', (
        (501, 'Play All'),
        (502, 'Mix - Klassische Musik'),
        (503, 'Bizet - Habanera (Remix)'),
        (504, 'Xavier de Maistre - Die Moldau (Smetana)'),
        (505, 'Shostakovich - The Second Waltz'),
        (506, 'James Bond Theme - All Time High'),
        (507, 'James Bond Theme - You Only Live Twice'),
    )
     ),

    ('Klänge', (
        (601, 'Play All'),
        (602, 'Gewitter & Regen'),
        (603, 'Meeresrauschen'),
        (604, 'Vogelgezwitscher'),
        (605, 'Tibetanische Klänge'),
        (606, 'Solfeggio 852Hz'),
    )
     ),
    ('False', 'Ich will in Ruhe saunieren'),
)

SAUNA_HEATING_TIME = datetime.timedelta(minutes=90)
