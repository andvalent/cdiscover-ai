import json
import re

# Your raw copy-pasted data
raw_data = """
1EMBNB 	JACK: Black and Blue034571100708
1EMBOT 	BRYARS/PITTS: Burden of Truth028947562931
1EMCDA 	MESSIAEN: Harawi034571102405
1EMCOV 	HILDEGARD: Ordo Virtutum034571102368
# ... (and so on for the rest of your list) ...
# I will use a small sample here for demonstration
CDA66450 	BANTOCK: Hebridean & Celtic Symphonies034571164502
CDA66451 	BYRD: Gradualia  Superseded by CDH55047034571164519
CDA66452 	The Romantic Piano Concerto, Vol. 01 – Moszkowski & Paderewski034571164526
CDA66453 	BARTÓK: 44 Duos for two violinsPreviously issued on CDH55267034571164533
"""

# For the real run, copy your full text inside the triple quotes above.

def extract_catalogue_codes(text_block):
    """
    Parses the raw text block to extract just the catalogue codes.
    """
    catalogue_codes = []
    print("Parsing raw text to find catalogue codes...")
    
    # Process each line in the text block
    for line in text_block.strip().splitlines():
        # Clean up the line by removing extra whitespace
        clean_line = line.strip()
        
        if not clean_line:
            continue # Skip any empty lines

        # The catalogue code is the very first part of the string before any space or tab.
        # We can split the line by whitespace and take the first element.
        parts = clean_line.split()
        if parts:
            code = parts[0]
            # A simple check to ensure it looks like a valid code (avoids junk lines)
            if re.match(r'^[A-Z0-9/]+$', code):
                catalogue_codes.append(code)

    return catalogue_codes

if __name__ == '__main__':
    # You would paste your full text data into the raw_data variable
    # For this example, I'll use the small sample above plus some of your list
    full_text_data = """
    1EMBNB 	JACK: Black and Blue034571100708
1EMBOT 	BRYARS/PITTS: Burden of Truth034571102283
1EMCDA 	MESSIAEN: Harawi034571102405
1EMCOV 	HILDEGARD: Ordo Virtutum034571102368
1EMEYE 	Known Unknown034571102375
1EMFTH 	Songs From The Heart034571102702
1EMHDUS 	Harmonies d'un Soir034571100753
1EMIIT 	In illo tempore034571101583
1EMIPM08 	PITTS J: Airs & Fantasias034571100678
1EMJY2 	PITTS: Jerusalem-Yerushalayim034571102498
1EMRZW 	MOZART/BARBER/ROSENZWEIG: Elegy034571102757
1EMTSC 	Tracks034571102696
1EMVEM 	Vinum et Musica034571102351
1EMXIX 	Nineteen to the dozen034571102566
4750112 	Janine Jansen028947501121
4756293 	VIVALDI: The Four Seasons028947562931
4758328 	MENDELSSOHN/BRUCH: Violin Concertos & Romance028947583288
4780651 	TCHAIKOVSKY: Violin Concerto & Souvenir d'un lieu cher028947806516
4781530 	BEETHOVEN/BRITTEN: Violin Concertos028947815303
4782256 	Beau Soir028947822561
4783206 	CHOPIN/LISZT/RAVEL: Benjamin Grosvenor Chopin, Lizst & Ravel028947832065
4783527 	SAINT-SAËNS/RAVEL/GERSHWIN: Rhapsody in blue028947835271
4783546 	PROKOFIEV: Violin Concerto No. 2 & Sonatas028947835462
4783551 	SCHUBERT/SCHOENBERG: String Quintet & Verklärte Nacht028947835516
4785334 	Dances028947853343
4785362 	BACH: Violin Concertos & Sonatas028947853626
4830255 	Homages028948302550
4834722 	Baroque Journey028948347223
4850365 	CHOPIN: Piano Concertos028948503650
4851156 	SAINT-SAËNS: Carnival028948511563
4851450 	LISZT: Benjamin Grosvenor plays Liszt028948514502
4851605 	12 Stradivari028948516056
4852256 	SIBELIUS: The Symphonies028948522569
4853192 	Origins028948531929
4853945 	SCHUMANN/BRAHMS: Benjamin Grosvenor plays Schumann & Brahms028948539451
4853946 	STRAVINSKY: The Rite of Spring & The Firebird028948539468
4854624 	BEETHOVEN: Triple Concerto & Folk Songs Arrangements028948546244
4854637 	SHOSTAKOVICH: Symphonies Nos. 4, 5 & 6028948546374
4854748 	SIBELIUS/PROKOFIEV: Violin Concertos028948547487
4870122 	CHOPIN: Études028948701223
4870146 	STRAVINSKY/DEBUSSY: Petrushka & Jeux028948701469
4870262 	Aigul028948702626
4870360 	TCHAIKOVSKY: Violin Concerto & other works028948703609
4870458 	Nightfall028948704583
4870642 	The Frans Brüggen Project028948706426
4870791 	PALESTRINA: The Golden Renaissance – Palestrina028948707911
4870835 	SHOSTAKOVICH/BRITTEN: Cello Concerto & Sonatas028948708352
4870877 	KHACHATURIAN: Piano Concerto & works for solo piano028948708772
4870952 	WAGNER: The Flying Dutchman028948709526
4870958 	CHOPIN: Piano Sonatas Nos. 2 & 3028948709588
4870959 	BERLIOZ/RAVEL: Symphonie fantastique & La valse028948709595
4871023 	RACHMANINOV: Piano Concerto No. 3 – Live from the 2022 Cliburn Competition028948710232
A66007 	The Virtuoso Mandolin  Deleted034571160078
A66018 	English Cathedral Music of the 20th Century  Deleted034571160184
A66059 	The Light Blues' Tour de France  Deleted034571160597
A66092 	BAX: Choral Music  Deleted034571160924
A66109 	FINZI/BERKELEY: Music for Oboe & String Quartet  Deleted034571161099
A66128 	KERN: The Light Blues sing Jerome Kern  Deleted034571161280
A66149 	Le Bestiaire  Deleted034571161495
APR5501 	BRAILOWSKY: The 1938 London HMV recordings5024709155019
APR5502 	FISCHER: First Beethoven Sonata recordings5024709155026
APR5503 	SOLOMON: First HMV recordings (Brahms/Beethoven)5024709155033
APR5504 	LAMOND: The complete Liszt recordings HMV 1919-365024709155040
APR5505 	MOISEIWITSCH: The complete Rachmaninov recordings 1937-435024709155057
APR5506 	HUBERMAN: The 1934 Szell/Vienna Philharmonic recordings5024709155064
APR5519 	HOROWITZ/BARBIROLLI: Tchaikovsky & Rachmaninov concertos5024709155194
APR5528 	BUSCH-SERKIN DUO: Unpublished recordings5024709155286
APR5531 	THE PIANO G&T's Vol.1: Pachmann, Michalowski, Ronald5024709155316
APR5532 	THE PIANO G&T's Vol.2: Grunfeld, Pugno, Janotha5024709155323
APR5533 	THE PIANO G&T's Vol.3: Chaminade & Saint-Saens5024709155330
APR5534 	THE PIANO G&T's Vol.4: Diémer, Eibenschütz, Hofmann, Backhaus5024709155347
APR5546 	MEDTNER: The complete solo piano recordings, Vol. 15024709155460
APR5547 	MEDTNER: The complete solo piano recordings, Vol. 25024709155477
APR5548 	MEDTNER: The complete solo piano recordings, Vol. 35024709155484
APR5571 	CORTOT: Late recordings Vol.15024709155712
APR5572 	CORTOT: Late recordings Vol.25024709155729
APR5573 	CORTOT: Late recordings Vol.35024709155736
APR5574 	CORTOT: Late recordings Vol.45024709155743
APR5579 	KATHLEEN FERRIER: Das Lied von der Erde, Alto Rhapsody5024709155798
APR5595 	VALERIE TRYON: Mendelssohn5024709155958
APR5614 	KENTNER: Liszt Recordings, Vol. 25024709156146
APR5621 	BARERE: At Carnegie Hall Vol.15024709156214
APR5622 	BARERE: At Carnegie Hall Vol.25024709156221
APR5623 	BARERE: At Carnegie Hall Vol.35024709156238
APR5624 	BARERE: At Carnegie Hall Vol.45024709156245
APR5625 	BARERE: At Carnegie Hall Vol.55024709156252
APR5630 	STEVENSON: The Transcendental Tradition5024709156306
APR5636 	PADEREWSKI: The HMV recordings 1937 & 19385024709156368
APR5639 	ELLY NEY: Brahms & Schubert5024709156399
APR5640 	VALERIE TRYON: Mozart Piano Concertos5024709156405
APR5643 	BACHAUER: HMV recordings 1949-19515024709156436
APR5646 	HESS: Historic broadcast recordings5024709156467
APR5647 	CHAMINADE: Chaminade & her contemporaries play Chaminade5024709156474
APR5650 	STEVENSON: Passacaglia on DSCH5024709156504
APR5655 	ALFRED BRENDEL: Busoni & Liszt - The 1950s SPA recordings5024709156559
APR5660 	NEUHAUS: Beethoven, Scriabin & Chopin5024709156603
APR5661 	GOLDENWEISER: Piano music5024709156610
APR5662 	IGUMNOV: Piano music5024709156627
APR5663 	GILELS: Schumann, Beethoven, Liszt, Prokofiev, etc5024709156634
APR5664 	GILELS and ZAK: Mozart, Mozart-Busoni, Saint-Saëns5024709156641
APR5665 	FLIER: Piano music5024709156658
APR5666 	NIKOLAYEVA: Tchaikovsky5024709156665
APR5667 	GINZBURG: His Early Recordings, Vol. 15024709156672
APR5668 	OBORIN: Beethoven, Chopin & Liszt5024709156689
APR5669 	RICHTER: Schubert Sonatas5024709156696
APR5670 	YUDINA: Beethoven Sonatas5024709156702
APR5671 	MERZHANOV: Chopin, Liszt & Scriabin5024709156719
APR5672 	GINZBURG: His Early Recordings, Vol. 25024709156726
APR6001 	HOROWITZ/TOSCANINI: Three Live Brahms Concertos5024709160013
APR6002 	BARERE: HMV recordings 1934-365024709160020
APR6004 	VLADIMIR HOROWITZ: Solo European Recordings 1930-36Previously issued on APR5516, APR55175024709160044
APR6005 	RICHTER, OBORIN & ZAK: The first Soviet Rachmaninov Recordings5024709160051
APR6006 	PADEREWSKI: His earliest recordings5024709160068
APR6007 	YORK BOWEN: The complete solo 78-rpm recordings5024709160075
APR6008 	MICHAEL ZADORA: The complete recordings 1922-19385024709160082
APR6009 	JORGE BOLET: His earliest recordings5024709160099
APR6010 	IRENE SCHARRER: The electric & selected acoustic recordings5024709160105
APR6011 	MOURA LYMPANY: HMV Recordings, 1947-19525024709160112
APR6012 	BARTLETT & ROBERTSON: Selected recordings, 1927-19475024709160129
APR6013 	WALTER GIESEKING: The complete Homocord recordings & rarities5024709160136
APR6014 	A MATTHAY MISCELLANY: Rare and unissued recordings5024709160143
APR6015 	GUIOMAR NOVAES: The complete published 78-rpm recordings5024709160150
APR6016 	VASSILY SAPELLNIKOFF & XAVER SCHARWENKA: The complete recordings5024709160167
APR6017 	ANATOLE KITAIN: The complete Columbia recordings 1936-395024709160174
APR6020 	LOUIS KENTNER: Balakirev, Lyapunov & the Liszt Sonata5024709160204
APR6032 	DINU LIPATTI: The complete Columbia recordings, 1947-19485024709160327
APR6044 	OLGA SAMAROFF & FRANK LA FORGE: The complete recordings5024709160440
APR6046 	ALFRED CORTOT: The 1942-3 Paris Chopin recordings  September 2025 release5024709160464
APR7038 	DOHNANYI: Complete HMV solo recordings 1929-565024709270385
APR7040 	MARK HAMBOURG: Liszt Hungarian Rhapsodies5024709170401
APR7302 	HAROLD BAUER: The complete recordings5024709173020
APR7303 	EDWIN FISCHER: Mozart Piano Concertos5024709173037
APR7304 	HARRIET COHEN: The complete solo studio recordings5024709173044
APR7305 	WANDA LANDOWSKA: The complete piano recordings5024709173051
APR7306 	MYRA HESS: Live from the University of Illinois, 19495024709173068
APR7314 	EDWIN FISCHER: The complete Brahms, Schubert & Schumann – studio recordings 1934-19505024709173143
APR7316 	SHURA CHERKASSKY: The complete 78-rpm recordings 1923-19505024709173167
APR7317 	WILHELM BACKHAUS: The complete acoustic & selected – early electric recordings5024709173174
APR7318 	The earliest French piano recordings5024709173181
APR7319 	French School Pianists play French Concertos5024709173198
APR7401 	ARTHUR DE GREEF: Solo and concerto recordings5024709174010
APR7501 	PERCY GRAINGER: The complete 78-rpm solo recordings5024709175017
APR7502 	EILEEN JOYCE: The complete Parlophone & Columbia recordings5024709175024
APR7503 	MORIZ ROSENTHAL: The complete recordings5024709175031
APR7504 	MYRA HESS: 78-rpm solo and concerto recordings5024709175048
APR7701 	EGON PETRI: The complete Columbia & Electrola recordings5024709177011
BKS44201/40 	SCHUBERT: The Complete Song Texts  Deleted034571142029
BSP1 	Baroque String Playing034571102870
CCR0001-D 	REICH: Drumming811043030165
CCR0002-D 	The scene of the crime811043030264
CCR0003-D 	REICH: Live at Fondation Louis Vuitton811043030363
CCR0004-D 	GRUBER: Percussion Concertos811043030462
CCR0006-D 	REICH: Music for 18 musicians811043030660
CDA30001/2 	BACH: Cello Suites  Superseded by CDA67541/2034571300016
CDA30002 	BACH: Goldberg Variations  Superseded by CDS44421/35034571300023
CDA30003 	BACH: Keyboard Concertos Nos. 1, 5 & 7  Superseded by CDA67307034571300030
CDA30004 	BACH: Toccatas & Fugues  Superseded by CDA66434034571300047
CDA30005 	BRAHMS: Cello Sonatas  Superseded by CDA67529034571300054
CDA30006 	CHOPIN: Piano Sonatas Nos. 2 & 3  Superseded by CDA67706034571300061
CDA30007 	FAURÉ: Piano Quartets  Superseded by CDA66166034571300078
CDA30008 	FAURÉ: Requiem & other choral music  Superseded by CDA66292034571300085
CDA30009 	HILDEGARD: A feather on the breath of God  Superseded by CDA66039034571300092
CDA30010 	MOZART: Clarinet Concerto & Quintet  Superseded by CDA66199034571300108
CDA30011 	MOZART: Piano Quartets  Superseded by CDA67373034571300115
CDA30012 	MOZART: Exsultate jubilate!  Superseded by CDA67560034571300122
CDA30013 	PÄRT: Triodion & other choral works  Superseded by CDA67375034571300139
CDA30014/2 	RACHMANINOV: Piano Concertos  Superseded by CDA67501/2034571300146
CDA30015 	RACHMANINOV: 24 Preludes  Superseded by CDA67700034571300153
CDA30016 	RACHMANINOV: Vespers034571300160
CDA30017 	RUTTER: Requiem & other choral works  Superseded by CDA66947034571300177
CDA30018 	SAINT-SAËNS: Piano Concertos Nos. 2, 4 & 5  Superseded by CDA67331/2034571300184
CDA30019 	SCHUBERT: Death & the Maiden  Superseded by CDA67585034571300191
CDA30020 	SCHUBERT: Die schöne MüllerinPreviously issued on CDJ33025034571300207
CDA30021 	SCHUBERT: Winterreise034571300214
CDA30022 	SCHUMANN: Piano TriosPreviously issued on CDA67063034571300221
CDA30023 	SHOSTAKOVICH/SHCHEDRIN: Piano Concertos  Superseded by CDA67425034571300238
CDA30024 	TALLIS: Spem in alium & other choral works  Superseded by CDA66400034571300245
CDA30025 	VAUGHAN WILLIAMS: Serenade to Music, Flos Campi, Mystical Songs  Superseded by CDA66420034571300252
CDA30026 	VICTORIA: Requiem  Superseded by CDA66250034571300269
CDA30027 	VIVALDI: Lute & Mandolin Concertos  Superseded by CDA66160034571300276
CDA30028 	WHITACRE: Cloudburst & other choral works  Superseded by CDA67543034571300283
CDA30029 	Three French Piano Trios034571300290
CDA30030 	New World Symphonies034571300306
CDA66001 	FINZI/STANFORD: Clarinet Concertos  Superseded by CDH55101034571160016
CDA66003 	English Ayres & Duets034571160030
CDA66004 	SCHUBERT: Piano Sonata in B flat major034571160047
CDA66008 	How The World Wags  Superseded by CDH55013034571160085
CDA66009 	RACHMANINOV: Variations034571160092
CDA66010 	DOWLAND: Consort Music034571160108
CDA66014 	Music for clarinet & piano  Superseded by CDD22027034571160146
CDA66015 	Finzi & His Friends  Superseded by CDH55084034571160153
CDA66017 	RUBINSTEIN: Piano Sonatas Nos. 1 & 3  Superseded by CDD22007034571160177
CDA66019 	Madrigals & Wedding Songs for Diana034571160191
CDA66021 	MONTEVERDI: Sacred Vocal Music  Temporarily out of stockPreviously issued on CDH55345034571160214
CDA66022 	The Clarinet in Concert, Vol. 1  Superseded by CDD22017034571160221
CDA66030 	STANFORD: Cathedral Music034571160306
CDA66031 	English Clarinet Concertos, Vol. 1Previously issued on CDH55069034571160313
CDA66032 	MUFFAT: Armonico Tributo  Superseded by CDH55191034571160320
CDA66036 	BACH: Cantatas 82 & 202  Superseded by CDD22041034571160368
CDA66038 	Echoes of a Waterfall  Superseded by CDH55128034571160382
CDA66039 	HILDEGARD: A feather on the breath of God034571160399
CDA66044 	Music for clarinet & piano  Superseded by CDD22027034571160443
CDA66045 	HAHN: Chansons Grises & other songs  Superseded by CDH55040034571160450
CDA66047 	RACHMANINOV: Piano Sonatas034571160474
CDA66050 	PANUFNIK/SESSIONS: Sinfonia votiva & Concerto for Orchestra  Superseded by CDH55100034571160504
CDA66053 	BRAHMS/SCHUMANN: Voices of the Night034571160535
CDA66055 	CRUSELL: Clarinet Concertos Nos. 1 & 3  Superseded by CDH55203034571160559
CDA66056 	PURCELL: Songs & Dialogues  Superseded by CDH55065034571160566
CDA66062 	BRUCKNER: Motets034571160627
CDA66065 	HAYDN: String Quartets, Op. 71/1 & Op. 71/2034571160658
CDA66066 	LASSUS: Requiem  Rights no longer controlled by Hyperion034571160665
CDA66067 	English Virginal Music of the 17th century034571160672
CDA66070 	PURCELL: Music for a while034571160702
CDA66071/2 	HANDEL: The Triumph of Time & Truth  Superseded by CDD22050034571160719
CDA66073 	FAYRFAX: Missa Albanus034571160733
CDA66074 	German Consort Music, 1660-1710034571160740
CDA66076 	HOWELLS/VAUGHAN WILLIAMS: Requiem & Mass  Superseded by CDH55220034571160764
CDA66077 	CRUSELL: Clarinet Quartets  Superseded by CDH55031034571160771
CDA66078 	English Choral & Organ Music  Superseded by CDH55009034571160788
CDA66081 	RACHMANINOV: Preludes, Op. 23034571160818
CDA66082 	RACHMANINOV: Preludes, Op. 32034571160825
CDA66084 	MARTINU: La Revue de Cuisine  Superseded by CDD22039034571160849
CDA66087 	MACHAUT: The Mirror of Narcissus034571160870
CDA66088 	CRUSELL/WEBER: Clarinet Concertos034571160887
CDA66089 	Renaissance Fantasias034571160894
CDA66090 	Rare Piano Encores  Superseded by CDH55109034571160900
CDA66091 	RACHMANINOV: Études-tableaux  Superseded by CDH55403034571160917
CDA66093 	MOZART: Piano Trios, K 254 & K 548034571160931
CDA66094 	Troubadour Songs & Medieval Lyrics034571160948
CDA66098 	HAYDN: String Quartets, Op. 71/3 & Op. 74/1034571160986
CDA66099 	HOLST: Savitri & The Dream City  Superseded by CDH55042034571160993
CDA66100 	MAHLER: Songs of Youth  Superseded by CDH55160034571161006
CDA66101/2 	BOUGHTON: The Immortal Hour  Superseded by CDD22040034571161013
CDA66104 	HAYDN: The Rising of the Lark034571161044
CDA66105 	RUBINSTEIN: Piano Sonatas Nos. 2 & 4  Superseded by CDD22007034571161051
CDA66106 	MONTEVERDI/INDIA: Olympia's Lament034571161068
CDA66107 	BRAHMS: Clarinet Quintet & Trio034571161075
CDA66108 	Purcell's London034571161082
CDA66112 	Souvenirs de VenisePreviously issued on CDH55217034571161129
CDA66114 	VICTORIA: O quam gloriosum & Ave maris stella034571161143
CDA66115 	STOCKHAUSEN: Stimmung034571161150
CDA66116 	Arabesque  Superseded by CDH55129034571161167
CDA66117 	SIMPSON: String Quartets Nos. 7 & 8034571161174
CDA66118 	HANDEL: Aminta e Fillide  Superseded by CDH55077034571161181
CDA66121 	Organ Fireworks, Vol. 01034571161211
CDA66123 	BURGON: Cathedral Music034571161235
CDA66124 	HAYDN: String Quartets, Op. 74/2 & Op. 74/3034571161242
CDA66125 	MOZART: Piano Trios, K 502 & K 564034571161259
CDA66126 	BRITTEN: A Boy was Born  Superseded by CDH55307034571161266
CDA66127 	SIMPSON: String Quartet No. 9034571161273
CDA66129 	VICTORIA: Missa Vidi speciosam & motets  Superseded by CDH55358034571161297
CDA66130 	FERGUSON: Sonata & Partita034571161303
CDA66133 	MARTINU: Madrigals  Superseded by CDD22039034571161334
CDA66134 	TAVERNER: Missa Gloria tibi Trinitas  Superseded by CDH55052034571161341
CDA66135 	LAWES: Sitting by the Streams034571161358
CDA66136 	Shakespeare's Kingdom034571161365
CDA66137 	BLISS: Rout & Rhapsody034571161372
CDA66139 	HOWELLS/DYSON: Rhapsodies & In GloucestershirePreviously issued on CDH55045034571161396
CDA66141 	SPOHR: Double Quartets Nos. 1 & 2  Superseded by CDD22014034571161419
CDA66142 	SPOHR: Double Quartets Nos. 3 & 4  Superseded by CDD22014034571161426
CDA66143 	CRUSELL/KREUTZER/REICHA: Oboe Quintets  Superseded by CDH55015034571161433
CDA66144 	The Garden of Zephirus  Superseded by CDH55289034571161440
CDA66145 	BIBER: Twelve Sonatas (1676)  Superseded by CDH55041034571161457
CDA66147 	POULENC: Voyage à Paris  Superseded by CDH55366034571161471
CDA66148 	MOZART: Piano Trios, K 496 & K 542034571161488
CDA66150 	DYSON: Hierusalem  Superseded by CDH55046034571161501
CDA66153 	17th-Century Bel Canto  Rights no longer controlled by Hyperion034571161532
CDA66156 	The Symphony in Europe, 1785034571161563
CDA66157 	PARRY: Violin Sonatas  Superseded by CDH55266034571161570
CDA66159 	BRAHMS: Cello Sonatas034571161594
CDA66160 	VIVALDI: Lute & Mandolin Concertos034571161600
CDA66161/2 	FINZI: Earth & Air & Rain  Superseded by CDD22070034571161617
CDA66163 	GLINKA/RIMSKY-KORSAKOV: Grand Sextet & Quintet  Superseded by CDH55173034571161631
CDA66165 	The Sea034571161655
CDA66166 	FAURÉ: Piano Quartets  Temporarily out of stockPreviously issued on CDA30007034571161662
CDA66167 	JANACEK/STRAVINSKY: Capriccio & Piano Concerto034571161679
CDA66168 	Treasures of the Spanish Renaissance  Superseded by CDH55430034571161686
CDA66169 	BACH: Hunt Cantata  Superseded by CDD22041034571161693
CDA66170 	MOZART: String Quartets, Vol. 1  Superseded by CDS44001/3034571161709
CDA66171 	ARNOLD: Chamber Music, Vol. 1  Superseded by CDH55071034571161716
CDA66172 	ARNOLD: Chamber Music, Vol. 2  Superseded by CDH55072034571161723
CDA66173 	ARNOLD: Chamber Music, Vol. 3  Temporarily out of stockPreviously issued on CDH55073034571161730
CDA66175 	HOLST/BRITTEN/BLISS: Lie Strewn The White Flocks  Superseded by CDH55050034571161754
CDA66176 	España!034571161761
CDA66177 	BRUCKNER: Mass in E minor  Superseded by CDH55277034571161778
CDA66178 	BLISS: Quartets  Rights no longer controlled by Hyperion034571161785
CDA66181 	WIDOR: Symphony No. 5  Superseded by CDH55144034571161815
CDA66182 	SCARLATTI D: Stabat Mater  Superseded by CDH55172034571161822
CDA66184 	RACHMANINOV: Moments Musicaux034571161846
CDA66185 	For Children  Temporarily out of stockPreviously issued on CDH55194034571161853
CDA66186 	Time stands still  Superseded by CDH55462034571161860
CDA66187 	SOMERVELL: Maud & A Shropshire Lad  Superseded by CDH55089034571161877
CDA66188 	MOZART: String Quartets, Vol. 2  Superseded by CDS44001/3034571161884
CDA66189 	Music for Brass & Percussion  Deleted034571161891
CDA66190 	VICTORIA: O magnum mysterium & Ascendens Christus034571161907
CDA66191 	DURUFLÉ: Requiem & Quatre motets034571161914
CDA66192 	FERGUSON: Octet034571161921
CDA66193 	VIVALDI: Variations on La Folia  Superseded by CDH55231034571161938
CDA66194 	The Castle of Fair Welcome  Superseded by CDH55274034571161945
CDA66195 	TELEMANN: Chamber Music  Superseded by CDH55108034571161952
CDA66196 	MENDELSSOHN: String Symphonies Nos 9, 10 & 12  Superseded by CDS44081/3034571161969
CDA66197 	BEETHOVEN: Piano Trios034571161976
CDA66198 	RACHMANINOV: The Early Piano Works034571161983
CDA66199 	MOZART: Clarinet Concerto & Quintet034571161990
CDA66200 	PRAETORIUS: Christmas Music  Temporarily out of stockPreviously issued on CDH55446034571162003
CDA66201 	LISZT: The complete music for solo piano, Vol. 01 – Waltzes  Temporarily out of stock034571162010
CDA66202 	BRAHMS: Clarinet Sonatas  Superseded by CDH55158034571162027
CDA66204 	DVORAK: Slavonic Dances034571162041
CDA66205 	DUPRE: Organ Music, Vol. 1  Superseded by CDD22059034571162058
CDA66209 	BRITTEN: Winter Words  Superseded by CDH55067034571162096
CDA66210 	FIORILLO/VIOTTI: Violin ConcertosPreviously issued on CDH55062034571162102
CDA66211 	BERNART DE VENTADORN: The Testament of Tristan034571162119
CDA66212 	PURCELL: Ayres for the Theatre  Superseded by CDH55010034571162126
CDA66214 	MONTEVERDI: Masses & Motets  Superseded by CDH55145034571162140
CDA66215 	Clarinet ConcertosPreviously issued on CDH55068034571162157
CDA66216 	The Grand Organ034571162164
CDA66217 	SCHUBERT: Grand Duo034571162171
CDA66218 	LOBO/MAGALHAES: Requiem & Missa dilectus meus  Superseded by CDH55138034571162188
CDA66219 	American Choral Music034571162195
CDA66220 	BRITTEN: A Ceremony of Carols034571162201
CDA66221/2 	MENDELSSOHN: Songs without words  Superseded by CDD22020034571162218
CDA66223 	REGER: Organ Music034571162232
CDA66224 	BACH: Bach-Vivaldi Concertos034571162249
CDA66225 	SIMPSON: String Quartets Nos. 10 & 11034571162256
CDA66226 	CORELLI: La Folia & other sonatas  Superseded by CDH55240034571162263
CDA66227 	The Emma Kirkby Collection  Deleted034571162270
CDA66228 	Ancient Airs & DancesPreviously issued on CDH55146034571162287
CDA66229 	Harp Music of the Italian Renaissance  Superseded by CDH55162034571162294
CDA66230 	MESSIAEN: La Nativité du Seigneur034571162300
CDA66231/2 	NIELSEN: Complete Piano Music  Rights no longer controlled by Hyperion034571162317
CDA66233 	La Compagna  Rights no longer controlled by Hyperion034571162331
CDA66234 	MOZART: String Quartets, Vol. 3  Superseded by CDS44001/3034571162348
CDA66235 	FAURÉ: Cello Sonata No. 2 & other cello music  Deleted034571162355
CDA66236 	BOCCHERINI: Symphonies Nos. 6, 8 & 14034571162362
CDA66237 	ARNE: Dr. Arne at Vauxhall Gardens034571162379
CDA66238 	The Service of Venus & Mars  Superseded by CDH55290034571162386
CDA66239 	BACH C P E: Variations on La Folia  Superseded by CDH55232034571162393
CDA66240 	PHILIPS: Consort Music034571162409
CDA66243 	KOECHLIN: Le cortège d'AmphitritePreviously issued on CDH55163034571162430
CDA66244 	Il Ballarino  Superseded by CDH55059034571162447
CDA66245 	BRUCKNER: Requiem034571162454
CDA66247 	VIVALDI: Concertos, Cantatas, Magnificat  Superseded by CDH55190034571162478
CDA66248 	La Procession034571162485
CDA66249 	My soul doth magnify the Lord  Superseded by CDH55401034571162492
CDA66250 	VICTORIA: Requiem034571162508
CDA66251/2 	HANDEL: Messiah  Temporarily out of stockPreviously issued on CDD22019034571162515
CDA66253 	BLOW/PURCELL: Countertenor duets  Superseded by CDH55447034571162539
CDA66254 	SCARLATTI A: Variations on La Folia  Superseded by CDH55233034571162546
CDA66255 	Italian Baroque Trumpet Music  Temporarily out of stockPreviously issued on CDH55192034571162553
CDA66256 	WARD: Sweet Philomel & other madrigals034571162560
CDA66257 	VILLA-LOBOS: Bachianas brasileiras Nos. 1 & 5  Superseded by CDH55316034571162577
CDA66258 	Organ Fireworks, Vol. 02034571162584
CDA66259 	SHEPPARD: Church Music, Vol. 1034571162591
CDA66260 	HOWELLS: St Paul's Service & other musicPreviously issued on CDD22038034571162607
CDA66261/2 	War's Embers034571162614
CDA66263 	Christmas Music from Medieval Europe034571162638
CDA66264 	GEMINIANI: La Folia Concerto Grosso  Superseded by CDH55234034571162645
CDA66265 	Concert Pieces for Organ034571162652
CDA66266 	PALESTRINA: Missa Papae Marcelli034571162669
CDA66267 	BACH/TELEMANN: Oboe & Oboe d'amore Concertos  Superseded by CDH55269034571162676
CDA66268 	REICHA: Wind Quintets, Vol. 1  Superseded by CDD22006034571162683
CDA66269 	MONDONVILLE: De Profundis & Venite, exsultemusPreviously issued on CDH55038034571162690
CDA66270 	LANGLAIS: Missa Salve regina & Messe solennelle  Superseded by CDH55444034571162706
CDA66271/2 	ELGAR: The Complete Choral Songs034571162713
CDA66273 	PARRY: Songs of Farewell & Jerusalem034571162737
CDA66274 	BRITTEN: Cello Suites034571162744
CDA66275 	Heroic & Ceremonial Music for Brass & Organ034571162751
CDA66276 	BRAHMS: String Sextets034571162768
CDA66277 	FAURÉ: Violin Sonatas  Superseded by CDH55030034571162775
CDA66278 	TELEMANN: Musique de Table  Superseded by CDH55278034571162782
CDA66279 	BRIDGE: Piano Trio No. 2  Superseded by CDH55063034571162799
CDA66280 	SIMPSON: Symphonies Nos. 6 & 7034571162805
CDA66281 	BEETHOVEN: Complete Cello Music, Vol. 1  Superseded by CDD22004034571162812
CDA66282 	BEETHOVEN: Complete Cello Music, Vol. 2  Superseded by CDD22004034571162829
CDA66283 	Bella Domna  Temporarily out of stockPreviously issued on CDH55207034571162836
CDA66284 	VIERNE: Symphony No. 2 & Les Angélicus  Superseded by CDH55044034571162843
CDA66285 	MOZART: Serenade in B flat major, K361  Superseded by CDH55093034571162850
CDA66286 	A Song for Francesca  Superseded by CDH55291034571162867
CDA66287 	DVORÁK: Piano Quartets034571162874
CDA66288 	PURCELL: Mr Henry Purcell's Most Admirable Composures  Superseded by CDH55303034571162881
CDA66289 	Blah blah blah & other trifles  Superseded by CDH55422034571162898
CDA66290 	MARTUCCI/RESPIGHI: La Canzone dei Ricordi & Il TramontoPreviously issued on CDH55049034571162904
CDA66291 	PARRY/STANFORD: NonetsPreviously issued on CDH55061034571162911
CDA66292 	FAURÉ: Requiem & other choral music  Temporarily out of stock034571162928
CDA66294 	PERGOLESI: Stabat Mater034571162942
CDA66295 	VILLA-LOBOS: Music for Flute  Superseded by CDH55057034571162959
CDA66296 	MARTINU: Three Cello Sonatas  Superseded by CDH55185034571162966
CDA66297 	HAYDN: Piano Trios Nos. 38-40034571162973
CDA66298 	Flute Music of the 16th and 17th Centuries  Superseded by CDH55096034571162980
CDA66299 	SIMPSON: Symphony No. 9034571162997
CDA66300 	The Clarinet in Concert, Vol. 2  Superseded by CDD22017034571163000
CDA66301 	LISZT: The complete music for solo piano, Vol. 02 – Ballades, Legends & Polonaises034571163017
CDA66302 	LISZT: The complete music for solo piano, Vol. 03 – Konzertsolo & Odes funèbres034571163024
CDA66303 	STROZZI: Songs034571163031
CDA66304 	VICTORIA: Tenebrae Responsories034571163048
CDA66305 	My spirit hath rejoiced  Superseded by CDH55402034571163055
CDA66306 	VAUGHAN WILLIAMS: Five Mystical Songs & Five Tudor Portraits  Temporarily out of stockPreviously issued on CDH55004034571163062
CDA66307 	My mind to me a kingdom is034571163079
CDA66308 	DVORÁK: String Quintet & String Sextet  Superseded by CDH55405034571163086
CDA66309 	VIVALDI: La Pastorella  Superseded by CDH55102034571163093
CDA66310 	MARAIS: Les folies d'Espagne  Superseded by CDH55235034571163109
CDA66311/2 	MONTEVERDI: VespersPreviously issued on CDD22028034571163116
CDA66313 	ELGAR: Cathedral Music  Superseded by CDH55147034571163130
CDA66314 	PURCELL: Odes 1 Royal and Ceremonial Odes034571163147
CDA66315 	HANDEL: Music for Royal Occasions034571163154
CDA66316 	PALESTRINA: O rex gloriae & Viri Galilaei  Superseded by CDH55335034571163161
CDA66317 	VERDI/STRAUSS: String Quartets  Superseded by CDH55012034571163178
CDA66318 	MENDELSSOHN: String Symphonies Nos. 5, 7 & 8  Superseded by CDS44081/3034571163185
CDA66319 	MUNDY: Sacred Choral Music  Superseded by CDH55086034571163192
CDA66320 	FAURÉ: La Chanson d'Ève & other songs  Temporarily out of stock034571163208
CDA66323 	DUPARC: Songs034571163239
CDA66324 	CHOPIN: Preludes, Fantaisie & Berceuse034571163246
CDA66325 	TAVERNER: Missa O Michael  Temporarily out of stockPreviously issued on CDH55054034571163253
CDA66326 	BACH: Cantatas Nos. 54, 169 & 170Previously issued on CDH55312034571163260
CDA66327 	Spanish Music of the Golden Age  Superseded by CDH55098034571163277
CDA66328 	VIVALDI: Recorder Concertos  Superseded by CDH55016034571163284
CDA66329 	HOLST: The Evening Watch  Temporarily out of stockPreviously issued on CDH55170034571163291
CDA66330 	Masterpieces of Mexican Polyphony  Superseded by CDH55317034571163307
CDA66331 	SCHUMANN/MENDELSSOHN: Piano Trios  Temporarily out of stockPreviously issued on CDH55078034571163314
CDA66332 	ARNOLD: Sinfoniettas & Concertos034571163321
CDA66333 	BRITTEN: St Nicolas & Hymn to St Cecilia  Superseded by CDH55378034571163338
CDA66334 	BRIAN: Symphony No. 3  Superseded by CDH55029034571163345
CDA66335 	A Musicall Dreame034571163352
CDA66336 	Music for the Lion-hearted KingPreviously issued on CDH55292034571163369
CDA66337 	HAYDN: Seven Last Words of our Saviour on the Cross034571163376
CDA66338 	STANLEY: 6 Concertos in 7 parts, Op. 2  Superseded by CDH55361034571163383
CDA66339 	VIVALDI: The Four Seasons034571163390
CDA66340 	Caprices & Fantasies  Superseded by CDH55130034571163406
CDA66341/2 	CHOPIN: Nocturnes  Temporarily out of stockPreviously issued on CDD22013034571163413
CDA66343 	BOUGHTON: Symphony No. 3  Superseded by CDH55019034571163437
CDA66344 	SATIE: Piano Music  Superseded by CDH55175034571163444
CDA66345 	TOMKINS: Cathedral Music  Temporarily out of stockPreviously issued on CDH55066034571163451
CDA66346 	LISZT: The complete music for solo piano, Vol. 05 – Saint-Saëns, Chopin & Berlioz Transcriptions034571163468
CDA66347 	POULENC/HAHN: Aubade, Sinfonietta & Bal de Béatrice d'Este  Superseded by CDH55167034571163475
CDA66348 	HAYDN: Haydn's Last String Quartets034571163482
CDA66349 	PURCELL: Hail! bright Cecilia & Who can from joy?  Superseded by CDH55327034571163499
CDA66350 	HANDEL: Fireworks Music & Coronation Anthems034571163505
CDA66351/4 	BACH: The Well-tempered Clavier034571163529
CDA66355 	MOZART: String Quartets, K575 & K590034571163550
CDA66356 	MENDELSSOHN: Octet & Bargiel  Superseded by CDH55043034571163567
CDA66357 	LISZT: The complete music for solo piano, Vol. 04 – Transcendental Studies  Temporarily out of stock034571163574
CDA66358 	MACHAUT: Messe de Notre Dame034571163581
CDA66359 	MENDELSSOHN: Hear my prayer  Superseded by CDH55268034571163598
CDA66360 	TAVERNER: Missa Corona spinea  Temporarily out of stockPreviously issued on CDH55051034571163604
CDA66361/2 	HANDEL: Acis and Galatea034571163611
CDA66363 	LOCATELLI: Violin Sonatas034571163635
CDA66364 	PALESTRINA: Missa De beata virgine & Missa Ave Maria  Superseded by CDH55420034571163642
CDA66365 	SATIE: Theatre Music  Superseded by CDH55176034571163659
CDA66366 	ROTT: Symphony in E major  Superseded by CDH55140034571163666
CDA66367 	The Courts of Love  Superseded by CDH55186034571163673
CDA66368 	DURUFLÉ: The Complete Organ Music  Superseded by CDH55475034571163680
CDA66369 	BACH: The Six Motets  Temporarily out of stockPreviously issued on CDH55417034571163697
CDA66370 	Sacred & Secular Music  Superseded by CDH55148034571163703
CDA66371/2 	LISZT: The complete music for solo piano, Vol. 06 – Liszt at the Opera I034571163710
CDA66373 	LOCKE: Anthems  Superseded by CDH55250034571163734
CDA66374 	The English Anthem, Vol. 1034571163741
CDA66375 	RACHMANINOV: Music for two pianos  Superseded by CDH55209034571163758
CDA66376 	SIMPSON: String Quartets Nos. 3 & 6 & Trio034571163765
CDA66377 	MOZART: Epistle Sonatas  Superseded by CDH55314034571163772
CDA66378 	BOYCE: Solomon034571163789
CDA66379 	REICHA: Wind Quintets, Vol. 2  Superseded by CDD22006034571163796
CDA66380 	BACH: Violin Concertos  Superseded by CDH55347034571163802
CDA66381/2 	CORELLI: Violin Sonatas  Superseded by CDD22047034571163819
CDA66383 	ALBINONI/VIVALDI: Oboe Concertos  Superseded by CDH55349034571163833
CDA66385 	GURNEY/VAUGHAN WILLIAMS: Ludlow & Teme & On Wenlock Edge  Superseded by CDH55187034571163857
CDA66386 	SIMPSON: String Quartets Nos. 2 & 5034571163864
CDA66387 	LE JEUNE: Missa Ad placitum, Benedicite & Magnificat034571163871
CDA66388 	LISZT: The complete music for solo piano, Vol. 08 – Christmas Tree & Via Crucis034571163888
CDA66389 	BRAHMS: Motets  Superseded by CDH55346034571163895
CDA66390 	BACH: Six Trio Sonatas034571163901
CDA66391 	MOZART: Flute Sonatas034571163918
CDA66392 	MOZART: Flute Quartets, Adagio & Rondo034571163925
CDA66393 	MOZART: Flute Concertos034571163932
CDA66394 	HOWELLS: Psalm-Preludes & RhapsodiesPreviously issued on CDD22038034571163949
CDA66395 	GIBBONS/LUPO: Music for Prince Charles034571163956
CDA66396 	HUMMEL: Septets  Superseded by CDH55214034571163963
CDA66397 	MENDELSSOHN: String Quartets, Vol. 1034571163970
CDA66398 	SCHÜTZ/GABRIELI: The Christmas Story & Motets  Superseded by CDH55310034571163987
CDA66399 	RIMSKY-KORSAKOV: Antar  Temporarily out of stockPreviously issued on CDH55137034571163994
CDA66400 	TALLIS: Spem in alium & other choral works034571164007
CDA66401 	BEETHOVEN: String Quartets, Op. 18 Nos 1 & 2034571164014
CDA66402 	BEETHOVEN: String Quartets, Op. 18 Nos 3, 4 & 6034571164021
CDA66403 	BEETHOVEN: String Quartets, Op. 18 No 5 & Op. 59 No 1034571164038
CDA66404 	BEETHOVEN: String Quartets, Op. 59 Nos 2 & 3034571164045
CDA66405 	BEETHOVEN: String Quartets, Op. 74 & 131034571164052
CDA66406 	BEETHOVEN: String Quartets, Op. 95 & 132034571164069
CDA66407 	BEETHOVEN: String Quartet, Op. 130 & Grosse Fuge034571164076
CDA66408 	BEETHOVEN: String Quartets, Op. 127 & 135034571164083
CDA66409 	SZYMANOWSKI: Piano Music  Superseded by CDH55081034571164090
CDA66410 	STRAVINSKY: Les Noces & other choral music  Superseded by CDH55467034571164106
CDA66411 	MOZART/KROMMER: Oboe Concertos  Superseded by CDH55080034571164113
CDA66412 	PURCELL: Odes 3 Fly, bold rebellion034571164120
CDA66413 	TELEMANN: Recorder Concertos  Superseded by CDH55091034571164137
CDA66414 	KOECHLIN: Music for FlutePreviously issued on CDH55107034571164144
CDA66415 	BARTOK: Sonata for Solo Violin  Superseded by CDH55149034571164151
CDA66416 	DEBUSSY: Preludes Book 1034571164168
CDA66417 	ANERIO: Requiem  Superseded by CDH55213034571164175
CDA66418 	SHEPPARD: Church Music, Vol. 2034571164182
CDA66419 	SIMPSON: String Quartets Nos. 1 & 4  Temporarily out of stock034571164199
CDA66420 	VAUGHAN WILLIAMS: Serenade to Music, Flos Campi, Mystical SongsPreviously issued on CDA30025034571164205
CDA66421/2 	LISZT: The complete music for solo piano, Vol. 07 – Harmonies poétiques et religieuses034571164212
CDA66423 	The Marriage of Heaven & Hell  Superseded by CDH55273034571164236
CDA66424 	TYE: Missa Euge bone  Temporarily out of stockPreviously issued on CDH55079034571164243
CDA66425 	KORNGOLD/SCHOENBERG: Sextet & Verklärte Nacht  Superseded by CDH55466034571164250
CDA66426 	ZELENKA: Lamentations  Temporarily out of stockPreviously issued on CDH55106034571164267
CDA66427 	TAVERNER: Missa Sancti WilhelmiPreviously issued on CDH55055034571164274
CDA66428 	FRANKEL/HOLBROOKE: Clarinet Quintets  Superseded by CDH55105034571164281
CDA66429 	LISZT: The complete music for solo piano, Vol. 09 – Sonata, Elegies & Consolations034571164298
CDA66430 	TARTINI: The Devil's Trill  Superseded by CDD22061034571164304
CDA66431 	MOZART: String Quintets, K 515 & K 519  Superseded by CDD22005034571164311
CDA66432 	MOZART: String Quintets, K 516 & K 614  Superseded by CDD22005034571164328
CDA66433 	LISZT: The complete music for solo piano, Vol. 10 – Hexaméron  Temporarily out of stock034571164335
CDA66434 	BACH: Toccatas & Fugues  Temporarily out of stock034571164342
CDA66435 	SIMPSON T: An Englishman Abroad034571164359
CDA66436 	Three English Ballets  Temporarily out of stockPreviously issued on CDH55099034571164366
CDA66437 	STRAVINSKY: Mass & Symphony of Psalms034571164373
CDA66438 	LISZT: The complete music for solo piano, Vol. 13 – À la Chapelle Sixtine034571164380
CDA66439 	Hear my prayer  Superseded by CDH55445034571164397
CDA66440 	HANDEL: Italian DuetsPreviously issued on CDH55262034571164403
CDA66441/3 	SHOSTAKOVICH: Preludes & Fugues  Temporarily out of stock034571164410
CDA66444 	BRAHMS: Elly Ameling sings Brahms034571164441
CDA66445 	LISZT: The complete music for solo piano, Vol. 11 – The Late Pieces034571164458
CDA66446 	WESLEY: Anthems, Vol. 1034571164465
CDA66447 	Awake, sweet love  Superseded by CDH55241034571164472
CDA66448 	LISZT: The complete music for solo piano, Vol. 12 – 3e Année de pèlerinage  Temporarily out of stock034571164489
CDA66449 	SIMPSON: Music for Brass034571164496
CDA66450 	BANTOCK: Hebridean & Celtic Symphonies034571164502
CDA66451 	BYRD: Gradualia  Superseded by CDH55047034571164519
CDA66452 	The Romantic Piano Concerto, Vol. 01 – Moszkowski & Paderewski034571164526
CDA66453 	BARTÓK: 44 Duos for two violinsPreviously issued on CDH55267034571164533
CDA66454 	From a Spanish Palace Songbook  Superseded by CDH55097034571164540
CDA66455 	BACH: Partitas & Canonic Variations034571164557
CDA66456 	PURCELL: Odes 4 Ye tuneful Muses034571164564
CDA66457 	Organ Fireworks, Vol. 03034571164571
CDA66458 	MOZART: String Quartets, K499 & K589Previously issued on CDH55094034571164588
CDA66459 	GOTTSCHALK: Piano Music, Vol. 1034571164595
CDA66460 	RACHMANINOV: Vespers  Superseded by CDA30016034571164601
CDA66461/2 	HANDEL: Joshua  Temporarily out of stock034571164618
CDA66463 	The Medieval Romantics  Superseded by CDH55293034571164632
CDA66464 	TAVENER: Sacred Music  Temporarily out of stockPreviously issued on CDH55414034571164649
CDA66465 	BRAHMS: Violin Sonatas  Superseded by CDH55087034571164656
CDA66466 	LISZT: The complete music for solo piano, Vol. 14 – Christus & St Elisabeth034571164663
CDA66467 	BOND: Six Concertos in seven parts034571164670
CDA66468 	DEBUSSY: The complete music for two pianosPreviously issued on CDH55014034571164687
CDA66469 	WESLEY: Anthems, Vol. 2034571164694
CDA66470 	Original 19th-century music for brass034571164700
CDA66471/2 	A Shropshire Lad  Superseded by CDD22044034571164717
CDA66473 	MARTINU/MILHAUD/PROKOFIEV: Music for 2 violins  Deleted034571164731
CDA66474 	COUPERIN F: Leçons de Ténèbres  Superseded by CDH55455034571164748
CDA66475 	MONTEVERDI: Balli  Superseded by CDH55165034571164755
CDA66476 	PURCELL: Odes 5 Welcome glorious morn034571164762
CDA66477 	WEELKES: Anthems  Superseded by CDH55259034571164779
CDA66478 	MENDELSSOHN: Cello Music  Superseded by CDH55064034571164786
CDA66479 	ROMBERG/FUCHS: Clarinet Quintets  Temporarily out of stockPreviously issued on CDH55076034571164793
CDA66480 	Songs to Shakespeare034571164809
CDA66481/2 	LISZT: The complete music for solo piano, Vol. 15 – Song Transcriptions034571164816
CDA66483 	HANDEL: James Bowman sings Heroic Arias  Superseded by CDH55370034571164830
CDA66484 	ENESCU: Violin Sonatas  Superseded by CDH55103034571164847
CDA66485 	TARTINI: Violin Sonatas, Vol. 2  Superseded by CDD22061034571164854
CDA66486 	RACHMANINOV: The Transcriptions  Superseded by CDH55458034571164861
CDA66487 	DEBUSSY: Preludes Book 2034571164878
CDA66488 	HOWELLS: Hymnus Paradisi & An English Mass  Temporarily out of stock034571164885
CDA66489 	LEIGHTON: Cathedral Music by Kenneth Leighton  Superseded by CDH55195034571164892
CDA66490 	PALESTRINA: Missa Aeterna Christi munera & MotetsPreviously issued on CDH55368034571164908
CDA66491/2 	MENDELSSOHN: Organ Music  Superseded by CDD22029034571164915
CDA66493 	BALAKIREV: Symphony No. 1 & Russia  Superseded by CDD22030034571164939
CDA66494 	PURCELL: Odes 6 Love's goddess sure034571164946
CDA66495 	DEBUSSY: Estampes, Children's Corner, Pour le piano034571164953
CDA66496 	GODOWSKY: Piano Music by Leopold Godowsky  Superseded by CDH55206034571164960
CDA66497 	O tuneful voice034571164977
CDA66498 	BRITTEN: Five CanticlesPreviously issued on CDH55244034571164984
CDA66499 	PROKOFIEV: Music for Children  Superseded by CDH55177034571164991
CDA66500 	Jill Gomez South of the Border034571165004
CDA66501 	BACH: Orchestral Suites Nos. 1 & 2  Superseded by CDD22002034571165011
CDA66502 	BACH: Orchestral Suites Nos. 3 & 4  Superseded by CDD22002034571165028
CDA66503 	SIMPSON: String Quartet No. 12 & String Quintet034571165035
CDA66504 	SUSSMAYR/TAUSCH: Clarinet Concertos  Superseded by CDH55188034571165042
CDA66505 	SIMPSON: Symphonies Nos. 2 & 4034571165059
CDA66506 	LISZT: The complete music for solo piano, Vol. 16 – Bunte Reihe034571165066
CDA66507 	TAVERNER: The Western Wynde Mass  Superseded by CDH55056034571165073
CDA66508 	HAYDN: Harmonie & Little Organ Masses  Superseded by CDH55208034571165080
CDA66509 	ARNE: Six Favourite Concertos  Superseded by CDH55251034571165097
CDA66510 	SIMPSON: Symphony No. 10034571165103
CDA66511 	VAUGHAN WILLIAMS: The Pilgrim's Progress034571165110
CDA66512 	Masterpieces of Portuguese Polyphony  Superseded by CDH55229034571165127
CDA66513 	BEETHOVEN: Septet & Sextet  Temporarily out of stockPreviously issued on CDH55189034571165134
CDA66514 	CHOPIN: The Four Scherzi  Superseded by CDH55181034571165141
CDA66515 	Victorian Concert Overtures  Superseded by CDH55088034571165158
CDA66516 	MARTINU/SCHULHOFF: String SextetsPreviously issued on CDH55321034571165165
CDA66517 	From The Steeples & The Mountains  Superseded by CDH55018034571165172
CDA66518 	The Harp of Luduvico  Superseded by CDH55264034571165189
CDA66519 	The English Anthem, Vol. 2034571165196
CDA66520 	HAYDN: Symphonies Nos. 73, 74 & 75  Superseded by CDH55121034571165202
CDA66521 	HAYDN: Symphonies Nos. 90, 91 & 92  Superseded by CDH55125034571165219
CDA66522 	HAYDN: Symphonies Nos. 45, 46 & 47  Superseded by CDH55118034571165226
CDA66523 	HAYDN: Symphonies Nos. 6, 7 & 8  Superseded by CDH55112034571165233
CDA66524 	HAYDN: Symphonies Nos. 1, 2, 3, 4 & 5  Superseded by CDH55111034571165240
CDA66525 	HAYDN: Symphonies Nos. 76, 77 & 78  Superseded by CDH55122034571165257
CDA66526 	HAYDN: Symphonies Nos. 70, 71 & 72  Superseded by CDH55120034571165264
CDA66527 	HAYDN: Symphonies Nos. 82, 83 & 84Previously issued on CDH55123034571165271
CDA66528 	HAYDN: Symphonies Nos. 101 & 102 & Windsor Castle  Superseded by CDH55127034571165288
CDA66529 	HAYDN: Symphonies Nos. 9, 10, 11 & 12  Superseded by CDH55113034571165295
CDA66530 	HAYDN: Symphonies Nos. 42, 43 & 44  Superseded by CDH55117034571165301
CDA66531 	HAYDN: Symphonies Nos. 48, 49 & 50  Superseded by CDH55119034571165318
CDA66532 	HAYDN: Symphonies Nos. 93, 94 & 95  Superseded by CDH55126034571165325
CDA66533 	HAYDN: Symphonies Nos. 17, 18, 19, 20 & 21  Superseded by CDH55115034571165332
CDA66534 	HAYDN: Symphonies Nos. 13, 14, 15 & 16  Superseded by CDH55114034571165349
CDA66535 	HAYDN: Symphonies Nos. 85, 86 & 87  Superseded by CDH55124034571165356
CDA66536 	HAYDN: Symphonies Nos. 22, 23, 24 & 25  Superseded by CDH55116034571165363
CDA66551/7 	BYRD: The Complete Keyboard Music  Superseded by CDS44461/7034571165516
CDA66558 	BYRD: Keyboard Music  Deleted034571165585
CDA66561/3 	MENDELSSOHN: Twelve String Symphonies  Superseded by CDS44081/3Previously issued on CDA66196, CDA66318034571165615
CDA66564 	ROSEINGRAVE: Keyboard Music034571165646
CDA66565 	LAMBERT: Summer's Last Will & Testament  Superseded by CDH55388034571165653
CDA66566 	BACH: Piano Transcriptions, Vol. 01 – Ferruccio Busoni  Temporarily out of stock034571165660
CDA66567 	The Romantic Piano Concerto, Vol. 03 – Mendelssohn Double Concertos034571165677
CDA66568 	HUMMEL: Three String Quartets  Superseded by CDH55166034571165684
CDA66569 	VAUGHAN WILLIAMS: The Shepherds of the Delectable Mountains034571165691
CDA66570 	SHEPPARD: Church Music, Vol. 3034571165707
CDA66571/2 	LISZT: The complete music for solo piano, Vol. 17 – Liszt at the Opera II  Temporarily out of stock034571165714
CDA66573 	PROKOFIEV: String Quartets  Superseded by CDH55032034571165738
CDA66574 	PEÑALOSA: The Complete MotetsPreviously issued on CDH55357034571165745
CDA66575 	LISZT: The complete music for solo piano, Vol. 18 – Liszt at the Theatre034571165752
CDA66576 	THOMSON: Louisiana Story  Superseded by CDH55169034571165769
CDA66577 	CHOPIN: Demidenko plays Ballades & Sonata No. 3  Superseded by CDH55182034571165776
CDA66578 	Odes on the death of Henry Purcell034571165783
CDA66579 	MENDELSSOHN: String Quartets, Vol. 2034571165790
CDA66580 	The Romantic Piano Concerto, Vol. 02 – Medtner 2 & 3  Temporarily out of stock034571165806
CDA66581/2 	BARTOK: String Quartets  Superseded by CDD22003034571165813
CDA66583 	English 18th-century Violin Sonatas034571165837
CDA66584 	CHAMINADE: Piano Music, Vol. 1Previously issued on CDH55197034571165844
CDA66585 	PURCELL: Anthems & Services, Vol. 01034571165851
CDA66586 	BALAKIREV: Symphony No. 2 & Tamara  Superseded by CDD22030034571165868
CDA66587 	PURCELL: Odes 7 Yorkshire Feast Song034571165875
CDA66588 	Lancaster & Valois  Superseded by CDH55294034571165882
CDA66589 	BACH: Goldberg Variations034571165899
CDA66590 	WOLF: Goethe & Mörike Songs034571165905
CDA66591/2 	GAY: The Beggar's Opera034571165912
CDA66593 	LISZT: The complete music for solo piano, Vol. 19 – Liebesträume & the Songbooks  Temporarily out of stock034571165936
CDA66594 	MILHAUD: Le Carnaval d'Aix & other works  Superseded by CDH55168034571165943
CDA66595 	ROSSINI: String Sonatas  Superseded by CDH55200034571165950
CDA66596 	SCHUMANN: Kerner Lieder & Liederkreis  Superseded by CDH55011034571165967
CDA66597 	CHOPIN: Demidenko plays ChopinPreviously issued on CDH55183034571165974
CDA66598 	PURCELL: Odes 8 Come ye sons of Art034571165981
CDA66599 	BRUCKNER: Mass in F minor  Superseded by CDH55332034571165998
CDA66600 	Rondeaux Royaux  Superseded by CDH55020034571166001
CDA66601/2 	LISZT: The complete music for solo piano, Vol. 20 – Album d'un voyageur  Temporarily out of stock034571166018
CDA66603 	SHEPPARD: Church Music, Vol. 4034571166032
CDA66604 	JENKINS: Late Consort Music034571166049
CDA66605 	Organ Fireworks, Vol. 04034571166056
CDA66606 	CROFT: Te Deum & Burial Service  Temporarily out of stockPreviously issued on CDH55252034571166063
CDA66607 	SCRIABIN: The Complete Études  Superseded by CDH55242034571166070
CDA66608 	DIBDIN: Ephesian Matron, Brickdust Man & Grenadier034571166087
CDA66609 	PURCELL: Anthems & Services, Vol. 02034571166094
CDA66610 	HOWELLS: Concertos & Dances  Superseded by CDH55205034571166100
CDA66611 	BACH: Brandenburg Concertos Nos. 1, 2 & 3  Superseded by CDD22001034571166117
CDA66612 	BACH: Brandenburg Concertos Nos. 4, 5 & 6  Superseded by CDD22001034571166124
CDA66613 	LINLEY: Ode on the Fairies of Shakespeare  Superseded by CDH55253034571166131
CDA66614 	JOSQUIN: Missa Pange lingua & Vultum tuum  Superseded by CDH55374034571166148
CDA66615 	MENDELSSOHN: String Quartets, Vol. 3034571166155
CDA66616 	LISZT: Demidenko plays Liszt  Temporarily out of stockPreviously issued on CDH55184034571166162
CDA66617 	TCHAIKOVSKY: Songs  Superseded by CDH55331034571166179
CDA66618 	The English Anthem, Vol. 3034571166186
CDA66619 	The Study of Love  Superseded by CDH55295034571166193
CDA66620 	SHOSTAKOVICH: Fantastic Dances, Preludes & Sonata No. 2034571166209
CDA66621 	HAYDN: Sun Quartets Nos. 1, 2 & 3034571166216
CDA66622 	HAYDN: Sun Quartets Nos. 4, 5 & 6034571166223
CDA66623 	PURCELL: Anthems & Services, Vol. 03034571166230
CDA66624 	The Romantic Piano Concerto, Vol. 04 – Arensky & Bortkiewicz034571166247
CDA66625 	The sweet look & the loving manner034571166254
CDA66626 	SIMPSON: String Quartets Nos. 14 & 15034571166261
CDA66627 	The Last Rose of Summer  Superseded by CDH55210034571166278
CDA66628 	RAFF: Symphonies Nos. 3 & 4  Superseded by CDH55017034571166285
CDA66629 	PEÑALOSA: Masses  Superseded by CDH55326034571166292
CDA66630 	BANTOCK: Pagan Symphony034571166308
CDA66631/2 	BACH: The Art of Fugue034571166315
CDA66633 	HANDEL: Concerti Grossi, Op. 3  Superseded by CDH55075034571166339
CDA66634 	English Clarinet Concertos, Vol. 2  Superseded by CDH55060034571166346
CDA66635 	MORALES: Missa Queramus cum pastoribus  Superseded by CDH55276034571166353
CDA66636 	MEDTNER: Demidenko plays Medtner  Superseded by CDH55315034571166360
CDA66637 	DOWLAND: Lachrimae  Superseded by CDH55339034571166377
CDA66638 	VILLA-LOBOS: Missa São Sebastião & other sacred musicPreviously issued on CDH55470034571166384
CDA66639 	TAVERNER: Missa Mater Christi sanctissima  Superseded by CDH55053034571166391
CDA66640 	The Romantic Piano Concerto, Vol. 05 – Balakirev & Rimsky-Korsakov034571166407
CDA66641/2 	HANDEL: Judas Maccabaeus  Temporarily out of stock034571166414
CDA66643 	PHILIPS: Motets  Superseded by CDH55254034571166438
CDA66644 	PURCELL: Anthems & Services, Vol. 04034571166445
CDA66645 	ELGAR: Quintet & Violin Sonata  Superseded by CDH55301034571166452
CDA66646 	BLOW: Fairest work of happy Nature034571166469
CDA66647 	CHOPIN: Two Piano Concertos  Superseded by CDH55180034571166476
CDA66648 	ARENSKY/TCHAIKOVSKY: String Quartet & Souvenir  Superseded by CDH55426034571166483
CDA66649 	BENDA: Cephalus & Aurora034571166490
CDA66650 	BRUCKNER: Mass in D minor & Te Deum  Superseded by CDS44071/3034571166506
CDA66651 	BRAHMS: String Quartets, Op. 51  Superseded by CDD22018034571166513
CDA66652 	BRAHMS: String Quartet, Op. 67 & Piano Quintet  Superseded by CDD22018034571166520
CDA66653 	The Voice in the GardenPreviously issued on CDH55298034571166537
CDA66654 	MEDTNER/RACHMANINOV: Music for two pianos  Superseded by CDH55337034571166544
CDA66655 	VAUGHAN WILLIAMS: Dona nobis pacem & other works034571166551
CDA66656 	PURCELL: Anthems & Services, Vol. 05034571166568
CDA66657 	SCHUMANN: Piano Quartet & Piano Quintet034571166575
CDA66658 	BLOW: Awake my lyre034571166582
CDA66659 	STRAUSS R: SongsPreviously issued on CDH55202034571166599
CDA66660 	HOLST: Choral Symphony  Superseded by CDH55104034571166605
CDA66661/2 	LISZT: The complete music for solo piano, Vol. 21 – Soirées musicales  Temporarily out of stock034571166612
CDA66663 	PURCELL: Anthems & Services, Vol. 06034571166636
CDA66664 	POULENC: Mass & Motets  Superseded by CDH55448034571166643
CDA66665 	HOWELLS: Music for violin & piano  Superseded by CDH55139034571166650
CDA66666 	MENDELSSOHN: On Wings of Song  Superseded by CDH55150034571166667
CDA66667 	Four & Twenty Fiddlers034571166674
CDA66668 	Adeste fideles  Temporarily out of stock034571166681
CDA66669 	Panis angelicus034571166698
CDA66670 	WASSENAER: Concerti Armonici  Superseded by CDH55155034571166704
CDA66671/5 	LISZT: The complete music for solo piano, Vol. 22 – The Beethoven Symphonies034571166711
CDA66676 	Organ Fireworks, Vol. 05034571166766
CDA66677 	PURCELL: Anthems & Services, Vol. 07034571166773
CDA66678 	The English Anthem, Vol. 4034571166780
CDA66679 	DVORÁK: String Quartet, Quintet & Notturno034571166797
CDA66680 	SCRIABIN/TCHAIKOVSKY: Piano Concertos  Superseded by CDH55304034571166803
CDA66681 	HAYDN: String Quartets, Op. 33/1-3034571166810
CDA66682 	HAYDN: String Quartets, Op. 33/4-6 & Op. 42034571166827
CDA66683 	LISZT: The complete music for solo piano, Vol. 23 – Harold in Italy034571166834
CDA66684 	The Romantic Piano Concerto, Vol. 06 – Dohnányi034571166841
CDA66685 	Gabriel's Greeting  Superseded by CDH55151034571166858
CDA66686 	PURCELL: Anthems & Services, Vol. 08034571166865
CDA66687 	English Viola Music  Superseded by CDH55085034571166872
CDA66688 	LASSUS: Missa Bell' Amfitrit' alteraPreviously issued on CDH55212034571166889
CDA66689 	HOWELLS: Howells' & Lambert's Clavichord  Superseded by CDH55152034571166896
CDA66690 	BOUGHTON: Bethlehem034571166902
CDA66691/2 	BALAKIREV: Orchestral Music  Superseded by CDD22030034571166919
CDA66693 	PURCELL: Anthems & Services, Vol. 09034571166933
CDA66694 	LISZT: The complete music for solo piano, Vol. 25 – The Canticle of the Sun  Temporarily out of stock034571166940
CDA66695 	SIMPSON: Horn Quartet & Horn Trio034571166957
CDA66697 	GOTTSCHALK: Piano Music, Vol. 2034571166971
CDA66698 	Enchanting Harmonist034571166988
CDA66699 	SPOHR: Octet & Nonet034571166995
CDA66700 	English 18th-century Keyboard Concertos  Superseded by CDH55341034571167008
CDA66701/2 	BACH: 4 Orchestral Suites  Superseded by CDD22002034571167015
CDA66703 	RACHMANINOV: The Divine Liturgy of St John Chrysostom  Superseded by CDH55318034571167039
CDA66704 	BRUCKNER/STRAUSS R: Quintet & CapriccioPreviously issued on CDH55372034571167046
CDA66705 	HOLST: This have I done for my true love  Temporarily out of stockPreviously issued on CDH55171034571167053
CDA66706 	CHAMINADE: Piano Music, Vol. 2Previously issued on CDH55198034571167060
CDA66707 	PURCELL: Anthems & Services, Vol. 10034571167077
CDA66708 	CRUSELL: Three Clarinet Concertos  Superseded by CDH55203Previously issued on CDA66055, CDA66088034571167084
CDA66709 	In praise of Woman, English women composers  Superseded by CDH55159034571167091
CDA66710 	PURCELL: Secular solo songs, Vol. 1034571167107
CDA66711/2 	BACH: Brandenburg Concertos  Superseded by CDD22001Previously issued on CDA66611, CDA66612034571167114
CDA66713 	RACHMANINOV: Demidenko plays Rachmaninov  Superseded by CDH55239034571167138
CDA66714 	DANYEL: The Complete Songs & Lute Music034571167145
CDA66715 	MELGÁS/MORAGO: Music of the Portuguese Renaissance034571167152
CDA66716 	PURCELL: Anthems & Services, Vol. 11034571167169
CDA66717 	The Romantic Piano Concerto, Vol. 07 – Alkan & Henselt034571167176
CDA66718 	Bridge, Elgar, Walton  Superseded by CDH55218034571167183
CDA66719 	BOCCHERINI: Double Cello Sonatas  Superseded by CDH55219034571167190
CDA66720 	PURCELL: Secular solo songs, Vol. 2034571167206
CDA66721/3 	LOCATELLI: L'Arte del Violino  Superseded by CDS44391/3034571167213
CDA66724 	SCHUBERT: String Quintet & String Trio  Superseded by CDH55305034571167244
CDA66725 	Masters of The Royal Chapel, Lisbon034571167251
CDA66726 	BOULANGER: Clairières dans le ciel  Temporarily out of stockPreviously issued on CDH55153034571167268
CDA66727 	LOCKE: The Broken Consort  Superseded by CDH55255034571167275
CDA66728 	SIMPSON: Symphonies Nos. 3 & 5034571167282
CDA66729 	The Romantic Piano Concerto, Vol. 10 – Weber034571167299
CDA66730 	PURCELL: Secular solo songs, Vol. 3034571167305
CDA66731/2 	STRAUSS: Complete Music for WindsPreviously issued on CDD22015034571167312
CDA66733 	PALESTRINA: The Song of Songs  Temporarily out of stockPreviously issued on CDH55095034571167336
CDA66734 	PHILIPS: Keyboard Music034571167343
CDA66735 	Music from Renaissance Coimbra034571167350
CDA66736 	WARLOCK: Songs  Superseded by CDH55442034571167367
CDA66737 	SIMPSON: Violin Sonata & Piano Trio034571167374
CDA66738 	VICTORIA: Missa Trahe me post te & Motets  Superseded by CDH55376034571167381
CDA66739 	The Spirits of England & France, Vol. 1  Superseded by CDH55281034571167398
CDA66740 	The Romantic Muse034571167404
CDA66741/2 	CORELLI: Concerti Grossi, Op. 6  Temporarily out of stockPreviously issued on CDD22011034571167411
CDA66743 	LISZT: Music for Violin034571167435
CDA66744 	The Romantic Piano Concerto, Vol. 08 – Medtner 1 & Quintet034571167442
CDA66745 	VIVALDI: Opera Arias & Sinfonias  Superseded by CDH55279034571167459
CDA66746 	BACH: The Inventions034571167466
CDA66747 	The Romantic Piano Concerto, Vol. 09 – d'Albert034571167473
CDA66748 	BEETHOVEN: The Creatures of Prometheus  Superseded by CDH55196034571167480
CDA66749 	TIPPETT: Songs034571167497
CDA66750 	PURCELL: Hark how the wild musicians sing034571167503
CDA66751/3 	HANDEL: Ottone  Superseded by CDS44511/3034571167510
CDA66754 	LAMBERT: Piano Concerto & other works  Superseded by CDH55397034571167541
CDA66755 	ARENSKY: Complete Suites for two pianos034571167558
CDA66756 	BACH: Orgelbüchlein034571167565
CDA66757 	DURUFLÉ: Requiem  Temporarily out of stock034571167572
CDA66758 	The English Anthem, Vol. 5034571167589
CDA66759 	LAMPE: Pyramus & Thisbe034571167596
CDA66760 	WOLF: Italienisches Liederbuch  Superseded by CDH55385Previously issued on CDA66760S034571167602
CDA66761/2 	LISZT: The complete music for solo piano, Vol. 24 – Beethoven & Hummel Septets034571167619
CDA66763 	BEETHOVEN: Diabelli Variations  Superseded by CDH55082034571167633
CDA66764 	MACKENZIE: Orchestral Music  Superseded by CDH55395034571167640
CDA66765 	Marc-André Hamelin Live034571167657
CDA66766 	FAURÉ: Piano Quintets034571167664
CDA66767 	LINLEY: Cantatas & Theatre Music  Temporarily out of stockPreviously issued on CDH55256034571167671
CDA66768 	AMNER: Cathedral Music034571167688
CDA66769 	VIVALDI: Sacred Music, Vol. 01  Temporarily out of stock034571167695
CDA66770 	BLOW/DRAGHI: Odes for St Cecilia  Superseded by CDH55257034571167701
CDA66771/2 	LISZT: The complete music for solo piano, Vol. 26 – The Young Liszt034571167718
CDA66773 	The Spirits of England & France, Vol. 2  Temporarily out of stockPreviously issued on CDH55282034571167732
CDA66774 	Moore's Irish Melodies034571167749
CDA66775 	MUSSORGSKY: Song Cycles034571167756
CDA66776 	BRITTEN: Music for Oboe and Piano  Superseded by CDH55154034571167763
CDA66777 	VAUGHAN WILLIAMS: Over hill, over dale034571167770
CDA66778 	Organ Fireworks, Vol. 06034571167787
CDA66779 	VIVALDI: Sacred Music, Vol. 02034571167794
CDA66780 	Quartet in 18th-century England034571167800
CDA66781/2 	Demidenko Live at the Wigmore Hall  Superseded by CDD22024034571167817
CDA66783 	The Spirits of England & France, Vol. 3  Superseded by CDH55283034571167831
CDA66784 	HOLST: Choral Ballets034571167848
CDA66785 	Virtuoso Strauss Transcriptions  Superseded by CDH55238034571167855
CDA66786 	DOHNÁNYI: Piano Quintets & Serenade  Temporarily out of stockPreviously issued on CDH55412034571167862
CDA66787 	LISZT: The complete music for solo piano, Vol. 27 – Fantasies on National Songs034571167879
CDA66788 	WOLF: Songs034571167886
CDA66789 	VIVALDI: Sacred Music, Vol. 03  Temporarily out of stock034571167893
CDA66790 	The Romantic Piano Concerto, Vol. 11 – Sauer & Scharwenka034571167909
CDA66791/2 	BACH: Great Fantasias, Preludes & Fugues  Superseded by CDD22062034571167916
CDA66793 	GRAINGER/GRIEG: At Twilight  Superseded by CDH55236034571167930
CDA66794 	ALKAN: Marc-André Hamelin plays Alkan034571167947
CDA66795 	VIVALDI: Viola d'amore Concertos  Temporarily out of stockPreviously issued on CDH55178034571167954
CDA66796 	DVORÁK: Piano Quintet & String Quintet  Superseded by CDH55472034571167961
CDA66797 	HANDEL: English AriasPreviously issued on CDH55419034571167978
CDA66798 	POULENC: Secular Choral MusicPreviously issued on CDH55179034571167985
CDA66799 	VIVALDI: Sacred Music, Vol. 05034571167992
CDA66800 	ARRIAGA/VORISEK: Symphonies034571168005
CDA66801/2 	GOUNOD: Songs034571168012
CDA66803 	CHABRIER: Briséïs  Superseded by CDH55428034571168036
CDA66804 	BRAHMS: String Quintets  Superseded by CDH55369034571168043
CDA66805 	CHERUBINI: Requiem034571168050
CDA66806 	A High-Priz'd Noise034571168067
CDA66807 	BAX: Nonet & other chamber music034571168074
CDA66808 	CLEMENTI: Demidenko plays ClementiPreviously issued on CDH55227034571168081
CDA66809 	VIVALDI: Sacred Music, Vol. 06034571168098
CDA66810 	BANTOCK: The Cyprian Goddess & Helena Variations034571168104
CDA66811/2 	LISZT: The complete music for solo piano, Vol. 28 – Dances & Marches  Temporarily out of stock034571168111
CDA66813 	BACH: The Italian Connection034571168135
CDA66814 	In the Cradle of the Renaissance034571168142
CDA66815 	MACCUNN: Land of the Mountain & the Flood034571168159
CDA66816 	DAQUIN: Douze NoëlsPreviously issued on CDH55319034571168166
CDA66817 	Sound the Trumpet  Superseded by CDH55258034571168173
CDA66818 	Bird Songs at Eventide  Superseded by CDH55156034571168180
CDA66819 	VIVALDI: Sacred Music, Vol. 07034571168197
CDA66820 	The Romantic Piano Concerto, Vol. 12 – Parry & Stanford  Temporarily out of stock034571168203
CDA66821 	HAYDN: Prussian Quartets Nos. 1, 2 & 3034571168210
CDA66822 	HAYDN: Prussian Quartets Nos. 4, 5 & 6034571168227
CDA66823 	BRITTEN: The Red Cockatoo & other songs  Temporarily out of stock034571168234
CDA66824 	HINDEMITH: Ludus Tonalis & Suite 1922  Superseded by CDH55413034571168241
CDA66825 	BRITTEN: Christ's Nativity034571168258
CDA66826 	The English Anthem, Vol. 6034571168265
CDA66827 	SIMPSON: The Complete Solo Piano Music034571168272
CDA66828 	GOMBERT: Credo & other sacred musicPreviously issued on CDH55247034571168289
CDA66829 	VIVALDI: Sacred Music, Vol. 08034571168296
CDA66830 	BEETHOVEN: Mass in C major  Superseded by CDH55263034571168302
CDA66831/2 	ALBINONI: Sonate & Trattenimenti  Superseded by CDD22048034571168319
CDA66833 	GLAZUNOV: The Complete Solo Piano Music, Vol. 1  Superseded by CDH55221034571168333
CDA66834 	BERWALD: Chamber Music, Vol. 1  Superseded by CDD22053034571168340
CDA66835 	BERWALD: Chamber Music, Vol. 2  Superseded by CDD22053034571168357
CDA66836 	Hark! hark! the lark034571168364
CDA66837 	BYRD: Mass for five voices  Superseded by CDH55348034571168371
CDA66838 	BOWEN: Piano Music034571168388
CDA66839 	VIVALDI: Sacred Music, Vol. 09034571168395
CDA66840 	Violin ConcertosPreviously issued on CDH55157034571168401
CDA66841/2 	HANDEL: Deborah034571168418
CDA66843 	BACH: Six Trio Sonatas transcribed034571168432
CDA66844 	GLAZUNOV: The Complete Solo Piano Music, Vol. 2  Superseded by CDH55222034571168449
CDA66845 	BRITTEN: Phaedra & other chamber music  Superseded by CDH55225034571168456
CDA66846 	CHAMINADE: Piano Music, Vol. 3Previously issued on CDH55199034571168463
CDA66847 	His Majestys Sagbutts & Cornetts Grand Tour  Superseded by CDH55344034571168470
CDA66848 	WALLACE: Symphonic Poems  Superseded by CDH55461034571168487
CDA66849 	VIVALDI: Sacred Music, Vol. 10034571168494
CDA66850 	Exultate Deo034571168500
CDA66851/2 	LISZT: The complete music for solo piano, Vol. 29 – Magyar Dalok & Magyar Rapszódiák034571168517
CDA66853 	IRELAND: The complete music for violin & pianoPreviously issued on CDH55164034571168531
CDA66854 	DUFAY: Music for St Anthony of Padua  Superseded by CDH55271034571168548
CDA66855 	GLAZUNOV: The Complete Solo Piano Music, Vol. 3  Superseded by CDH55223034571168555
CDA66856 	SAINT-SAËNS: Songs  Temporarily out of stock034571168562
CDA66857 	The Spirits of England & France, Vol. 4  Superseded by CDH55284034571168579
CDA66858 	PROKOFIEV: Piano Concertos Nos. 2 & 3  Superseded by CDH55440034571168586
CDA66860 	HANDEL: Opera Arias & Overtures, Vol. 1034571168609
CDA66861/2 	LISZT: The complete music for solo piano, Vol. 30 – Liszt at the Opera III  Temporarily out of stock034571168616
CDA66863 	GRAINGER: Jungle Book & other choral works  Superseded by CDH55433034571168630
CDA66864 	SCHUMANN: Piano Sonatas  Temporarily out of stockPreviously issued on CDH55300034571168647
CDA66865 	Classical Violin Concertos  Superseded by CDH55260034571168654
CDA66866 	GLAZUNOV: The Complete Solo Piano Music, Vol. 4  Superseded by CDH55224034571168661
CDA66867 	Holy Week at the Chapel of the Braganza Dukes034571168678
CDA66868 	British Light Music Classics, Vol. 1034571168685
CDA66870 	Royal Eurostar034571168708
CDA66871/3 	VERACINI: Sonate accademiche  Superseded by CDS44241/3034571168715
CDA66874 	LISZT: Marc-André Hamelin plays Liszt034571168746
CDA66875 	SCARLATTI/HASSE: Salve regina, Cantatas & Motets  Superseded by CDH55354034571168753
CDA66876 	FINZI: Intimations of Immortality & Dies natalis  Superseded by CDH55432034571168760
CDA66877 	The Romantic Piano Concerto, Vol. 13 – Glazunov & Goedicke034571168777
CDA66878 	QUILTER: Songs034571168784
CDA66880 	BEETHOVEN: Early Cantatas  Superseded by CDH55479034571168807
CDA66881/2 	VIVALDI: The Complete Cello Sonatas  Superseded by CDD22065034571168814
CDA66883 	RHEINBERGER: Suites for Organ, Violin & Cello  Superseded by CDH55211034571168838
CDA66884 	GRAINGER: Piano Music034571168845
CDA66885 	SCHNITTKE: Chamber Music034571168852
CDA66886 	VICTORIA: Missa Dum complerentur, Hymns & Sequences  Superseded by CDH55452034571168869
CDA66887 	MOZART: Wind Serenades & OverturesPreviously issued on CDH55092034571168876
CDA66888 	BOELLMANN/GODARD: Cello Sonatas034571168883
CDA66889 	The Romantic Piano Concerto, Vol. 14 – Litolff Concertos Symphoniques 2 & 4  Temporarily out of stock034571168890
CDA66890 	SIMPSON: Symphonies Nos. 1 & 8034571168906
CDA66891/2 	AVISON: Concerti Grossi after Scarlatti  Superseded by CDD22060034571168913
CDA66893 	JANÁCEK: Choral Music  Superseded by CDH55398034571168937
CDA66894 	For His Majestys Sagbutts & Cornetts  Superseded by CDH55406034571168944
CDA66895 	DVORÁK: Piano Trios Nos. 3 & 4034571168951
CDA66896 	Early English Clarinet Concertos  Superseded by CDH55261034571168968
CDA66897 	The Romantic Piano Concerto, Vol. 15 – Hahn & Massenet034571168975
CDA66898 	Vierne, Widor & Dupré  Temporarily out of stock034571168982
CDA66899 	BANTOCK: Sappho & Sapphic Poem034571168999
CDA66900 	Indian Classical Music034571169002
CDA66901/2 	VAUGHAN WILLIAMS: Hugh The Drover  Superseded by CDD22049034571169019
CDA66903 	BOCCHERINI: Six Symphonies034571169033
CDA66904 	BOCCHERINI: Four Symphonies034571169040
CDA66905 	SIMPSON: String Quartet No. 13, & Quintet No. 2034571169057
CDA66906 	MENDELSSOHN: Songs & Duets, Vol. 1034571169064
CDA66907 	CHAUSSON: Concert & Piano Quartet034571169071
CDA66908 	GABRIELI G: Sacrae Symphoniae034571169088
CDA66909 	WOLF: Eichendorff-Lieder  Superseded by CDH55435034571169095
CDA66910 	GUERRERO: Missa Sancta et immaculata  Superseded by CDH55313034571169101
CDA66911/4 	FAURÉ: The Complete Music for Piano  Superseded by CDS44601/4034571169118
CDA66915 	GOTTSCHALK: Piano Music, Vol. 3034571169156
CDA66916 	Passiontide at St Paul'sPreviously issued on CDH55436034571169163
CDA66917 	Organ Fireworks, Vol. 07034571169170
CDA66918 	FRANCK: Piano Music034571169187
CDA66919 	The Spirits of England & France, Vol. 5  Superseded by CDH55285034571169194
CDA66920 	Sure on this shining night034571169200
CDA66921/3 	HANDEL: 20 Sonatas, Op. 1  Superseded by CDS44411/3034571169217
CDA66924 	While Shepherds Watched  Superseded by CDH55325034571169248
CDA66925 	O magnum misteriumPreviously issued on CDH55216034571169255
CDA66926 	ROSLAVETS: Piano Music034571169262
CDA66927 	QUANTZ: Flute Concertos034571169279
CDA66928 	Ikon, Vol. 1034571169286
CDA66929 	Musique of Violenze034571169293
CDA66930 	HOLLOWAY/SCHUMANN: Serenade & Liederkreis034571169309
CDA66931/2 	HANDEL: Harpsichord Suites  Superseded by CDD22045034571169316
CDA66933 	BORTKIEWICZ: Piano Music, Vol. 1  Superseded by CDD22054034571169330
CDA66934 	DVORÁK: Music for violin & piano  Superseded by CDH55365034571169347
CDA66935 	BOYCE: Peleus & Thetis034571169354
CDA66936 	BOUGHTON: String Quartets & Oboe Quartet No. 1Previously issued on CDH55174034571169361
CDA66937 	My Garden034571169378
CDA66938 	WARLOCK: Curlew, Capriol, Serenade, Songs034571169385
CDA66939 	TCHAIKOVSKY: Piano SonatasPreviously issued on CDH55215034571169392
CDA66940 	YSAYE: Violin Music  Superseded by CDH55226034571169408
CDA66941/2 	BRITTEN: Complete Folk Song Arrangements034571169415
CDA66943 	GOMBERT: Missa Tempore paschali & Motets  Temporarily out of stockPreviously issued on CDH55323034571169439
CDA66944 	LÉONIN: Magister Leoninus, Vol. 1  Temporarily out of stockPreviously issued on CDH55328034571169446
CDA66945 	ALBERT: Solo Piano Music  Superseded by CDH55411034571169453
CDA66946 	Music for viola & piano034571169460
CDA66947 	RUTTER: Requiem & other choral works034571169477
CDA66948 	TCHAIKOVSKY: Liturgy of St John Chrysostom  Superseded by CDH55437034571169484
CDA66949 	The Romantic Piano Concerto, Vol. 16 – Huss & Schelling034571169491
CDA66950 	HANDEL: The Rival Queens034571169507
CDA66951/3 	LISZT: The complete music for solo piano, Vol. 31 – The Schubert Transcriptions I034571169514
CDA66954/6 	LISZT: The complete music for solo piano, Vol. 32 – The Schubert Transcriptions II034571169545
CDA66957/9 	LISZT: The complete music for solo piano, Vol. 33 – The Schubert Transcriptions III034571169576
CDA66960 	PÄRT: Berliner Messe & MagnificatPreviously issued on CDH55408034571169606
CDA66961/2 	HANDEL: The Occasional Oratorio034571169613
CDA66963 	MOMPOU: Piano music034571169637
CDA66964 	STANFORD: Sacred Choral Music, Vol. 1  Superseded by CDS44311/3034571169644
CDA66965 	STANFORD: Sacred Choral Music, Vol. 2  Superseded by CDS44311/3034571169651
CDA66966 	LIEBERMANN: Piano Concertos034571169668
CDA66967 	HANDEL/TELEMANN: Water Music034571169675
CDA66968 	British Light Music Classics, Vol. 2034571169682
CDA66969 	The Romantic Piano Concerto, Vol. 17 – Mendelssohn034571169699
CDA66970 	CAVALLI: Messa Concertata  Superseded by CDH55193034571169705
CDA66971 	HAYDN: Tost I Quartets034571169712
CDA66972 	HAYDN: Tost II Quartets034571169729
CDA66973 	LISZT: The complete music for solo piano, Vol. 34 – Douze Grandes Études034571169736
CDA66974 	STANFORD: Sacred Choral Music, Vol. 3  Superseded by CDS44311/3034571169743
CDA66975 	MACKENZIE: Violin Concerto & Pibroch  Temporarily out of stockPreviously issued on CDH55343034571169750
CDA66976 	BIZET: Songs034571169767
CDA66977 	The Age of Extravagance034571169774
CDA66978 	Organ Fireworks, Vol. 08034571169781
CDA66979 	KOECHLIN/PIERNÉ: Cello Sonatas034571169798
CDA66980 	XENAKIS: Choral Music034571169804
CDA66981/2 	LOCATELLI: Concerti Grossi, Op. 1  Superseded by CDD22066034571169811
CDA66983 	SÉVERAC: Songs034571169835
CDA66984 	LISZT: The complete music for solo piano, Vol. 35 – Arabesques034571169842
CDA66985 	Early Italian Violin Sonatas034571169859
CDA66986 	LIADOV: Solo Piano Music  Superseded by CDH55309034571169866
CDA66987 	WALLACE: Creation Symphony & other works  Temporarily out of stockPreviously issued on CDH55465034571169873
CDA66988 	Land of Heart's Desire  Superseded by CDH55204034571169880
CDA66989 	MOZART: Songs  Superseded by CDH55371034571169897
CDA66990 	The Romantic Piano Concerto, Vol. 18 – Korngold & Marx034571169903
CDA66991/2 	BERLIOZ: The Childhood of Christ  Superseded by CDD22067034571169910
CDA66993 	MENDELSSOHN: String Quintets  Superseded by CDH55377034571169934
CDA66994 	Advent at St Paul's  Temporarily out of stockPreviously issued on CDH55463034571169941
CDA66995 	LISZT: The complete music for solo piano, Vol. 36 – Excelsior!034571169958
CDA66996 	REGER: Piano Music  Temporarily out of stock034571169965
CDA66997 	DUFAY: Music for St James the Greater  Superseded by CDH55272034571169972
CDA66998 	European Light Music Classics  Superseded by CDH55477034571169989
CDA66999 	MOODY: Passion & Resurrection034571169996
CDA67000 	SCHUBERT: Symphony No. 10034571170008
CDA67001/3 	PURCELL: The Complete Ayres for the Theatre  Superseded by CDS44381/3034571170015
CDA67004 	LISZT: The complete music for solo piano, Vol. 37 – Tanzmomente  Temporarily out of stock034571170046
CDA67005 	New York Variations034571170053
CDA67006 	JONES: The Geisha  Temporarily out of stockPreviously issued on CDH55245034571170060
CDA67007 	CLERK: The Lion of Scotland  Temporarily out of stock034571170077
CDA67008 	LLOYD WEBBER W: Chamber music & songs034571170084
CDA67009 	Music for St Paul's  Superseded by CDH55359034571170091
CDA67010 	LA RUE: Missa De Feria & Missa Sancta Dei genitrix  Superseded by CDH55296034571170107
CDA67011 	HAYDN: Tost III Quartets 1 2 3034571170121
CDA67012 	HAYDN: Tost III Quartets 4 5 6034571170114
CDA67013 	CASTELLO/PICCHI: The Floating City  Temporarily out of stockPreviously issued on CDH55320034571170138
CDA67014 	MILHAUD: Music for two pianists034571170145
CDA67015 	LISZT: The complete music for solo piano, Vol. 38 – Les Préludes  Temporarily out of stock034571170152
CDA67016 	SIMPSON: Complete Choral & Organ Music034571170169
CDA67017 	MARTIN/PIZZETTI: Mass & Messa di Requiem034571170176
CDA67018 	MUSORGSKY/PROKOFIEV: Pictures from an Exhibition & Romeo  Superseded by CDH55306034571170183
CDA67019 	ELGAR: Choral Songs034571170190
CDA67020 	Vital Spark of Heav'nly Flame034571170206
CDA67021/2 	LOCATELLI: Sonatas, Op. 8  Superseded by CDD22057034571170213
CDA67023 	The Romantic Piano Concerto, Vol. 19 – Mackenzie & Tovey034571170237
CDA67024 	STANFORD: Music for violin & pianoPreviously issued on CDH55362034571170244
CDA67025 	PARRY: Job034571170251
CDA67026 	LISZT: The complete music for solo piano, Vol. 39 – 1e Année de pèlerinage034571170268
CDA67027 	SCHUBERT: Piano Sonatas, D613, 784 & 960034571170275
CDA67028 	CHAUSSON: Chamber Music034571170282
CDA67029 	PROKOFIEV: Piano Concertos Nos. 1, 4 & 5034571170299
CDA67030 	MAGNARD: Symphonies Nos. 1 & 2  Superseded by CDD22068034571170305
CDA67031/2 	BLOW: Anthems  Superseded by CDD22055034571170312
CDA67033 	LECLAIR: Sonatas, Vol. 1034571170336
CDA67034 	LISZT: The complete music for solo piano, Vol. 40 – Gaudeamus igitur034571170343
CDA67035 	La Folia034571170350
CDA67036 	FRANÇAIX: À huit & Divertissement034571170367
CDA67037 	SAINT-SAËNS: The Complete Études034571170374
CDA67038 	LINLEY: The Song of Moses & Let God Arise  Superseded by CDH55302034571170381
CDA67039 	Jerusalem, Vision of Peace034571170398
CDA67040 	MAGNARD: Symphonies Nos. 3 & 4  Superseded by CDD22068034571170404
CDA67041/2 	LOCATELLI: Sonatas, Op. 4  Superseded by CDD22064034571170411
CDA67043 	Stephen Hough's New Piano Album034571170435
CDA67044 	PARRY: English Lyrics & Songs034571170442
CDA67045 	LISZT: The complete music for solo piano, Vol. 41 – The Recitations with piano034571170459
CDA67046 	Mortuus est Philippus Rex  Superseded by CDH55248034571170466
CDA67047 	DUPRE: Organ Music, Vol. 2  Superseded by CDD22059034571170473
CDA67048 	Lo Sposalizio  Superseded by CDD22072034571170480
CDA67049 	LAMBERT: Tiresias & Pomona034571170497
CDA67050 	The Composer-Pianists034571170503
CDA67051/2 	ARNE: ArtaxerxesPreviously issued on CDD22073034571170510
CDA67053 	HANDEL: Handel in Hamburg  Temporarily out of stockPreviously issued on CDH55324034571170534
CDA67054 	MESSIAEN: Piano Music034571170541
CDA67055 	BEETHOVEN: Songs034571170558
CDA67056 	PADEREWSKI: Symphony 'Polonia'  Temporarily out of stockPreviously issued on CDH55351034571170565
CDA67057/8 	SCRIABIN: The Complete Preludes034571170572
CDA67059 	KUHNAU: Sacred Music  Superseded by CDH55394034571170596
CDA67060 	Organ Dreams, Vol. 1034571170602
CDA67061/2 	BRITTEN: Complete Purcell Realizations  Superseded by CDD22058034571170619
CDA67063 	SCHUMANN: Piano Trios  Superseded by CDA30022034571170633
CDA67064 	FAURÉ: Piano Music034571170640
CDA67065 	English Orchestral Songs034571170657
CDA67066 	ARENSKY: Piano Music  Superseded by CDH55311034571170664
CDA67067 	American Light Music Classics034571170671
CDA67068 	LECLAIR: Sonatas, Vol. 2034571170688
CDA67069 	The Romantic Piano Concerto, Vol. 20 – Brüll034571170695
CDA67070 	DURUFLÉ/FAURÉ: Requiems034571170701
CDA67071/2 	BACH: Wachet auf!034571170718
CDA67073 	VIVALDI: Concerti con molti istromenti  Temporarily out of stockPreviously issued on CDH55439034571170732
CDA67074 	The Romantic Violin Concerto, Vol. 01 – Saint-Saëns034571170749
CDA67075 	GUERRERO: Missa De la batalla escoutez & other works  Superseded by CDH55340034571170756
CDA67076 	All in the April Evening  Superseded by CDH55243034571170763
CDA67077 	RZEWSKI: The People United Will Never Be Defeated!034571170770
CDA67078 	MCCABE: String Quartets Nos. 3, 4 & 5034571170787
CDA67079 	German 17th-Century Church Music  Superseded by CDH55230034571170794
CDA67080 	GRECHANINOV: Vespers  Superseded by CDH55352034571170800
CDA67081/2 	BERWALD: Symphonies & Overtures  Superseded by CDD22043034571170817
CDA67083 	HANDEL: Trio SonatasPreviously issued on CDH55280034571170831
CDA67084 	PIZZETTI: Orchestral Music  Superseded by CDH55329034571170848
CDA67085 	LISZT: Sonata, Ballades & Polonaises034571170855
CDA67086 	The Romantic Piano Concerto, Vol. 21 – Dreyschock & Kullak034571170862
CDA67087 	The English Anthem, Vol. 7034571170879
CDA67088 	The Noble Bass Viol034571170886
CDA67089 	MCCABE: Symphony No. 4 & Flute Concerto034571170893
CDA67090 	CATOIRE: Piano MusicPreviously issued on CDH55425034571170909
CDA67091/2 	SCHUBERT: Impromptus & other piano music034571170916
CDA67093 	GIBBS: Dale & Fell034571170930
CDA67094 	BORTKIEWICZ: Piano Music, Vol. 2  Superseded by CDD22054034571170947
CDA67095 	SAINT-SAËNS: Cello Sonatas  Superseded by CDH55342034571170954
CDA67096 	SAMMONS: The English Kreisler034571170961
CDA67097 	CHAUSSON/INDY: String Quartets  Superseded by CDH55457034571170978
CDA67098 	Masters of the Rolls  Superseded by CDH55364034571170985
CDA67099 	PALESTRINA: Missa Ecce ego Johannes & other sacred music  Temporarily out of stockPreviously issued on CDH55407034571170992
CDA67100 	SAINT-SAËNS: Music for Violin034571171005
CDA67101/2 	LISZT: The complete music for solo piano, Vol. 42 – Liszt at the Opera IV034571171012
CDA67103 	SWEELINCK: Cantiones Sacrae, Vol. 1034571171036
CDA67104 	SWEELINCK: Cantiones Sacrae, Vol. 2034571171043
CDA67105 	Russian Images, Vol. 1034571171050
CDA67106 	Songs of Scotland  Superseded by CDH55336034571171067
CDA67107 	LISZT: The complete music for solo piano, Vol. 43 – 2e Année de pèlerinage034571171074
CDA67108 	ASTORGA/BOCCHERINI: Stabat Mater  Superseded by CDH55287034571171081
CDA67109 	GYROWETZ: Three String Quartets034571171098
CDA67110 	MENDELSSOHN: Songs  Superseded by CDH55360034571171104
CDA67111/3 	LISZT: The complete music for solo piano, Vol. 44 – The Early Beethoven Transcriptions034571171111
CDA67114 	Three French Piano Trios  Superseded by CDA30029034571171142
CDA67115 	Fairest Isle034571171159
CDA67116 	GIBBONS: Anthems & Verse Anthems  Superseded by CDH55228034571171166
CDA67117 	GRIEG: String Quartets Nos. 1 & 2  Superseded by CDH55299034571171173
CDA67118 	GOTTSCHALK: Piano Music, Vol. 4034571171180
CDA67119 	Antique Brasses034571171197
CDA67120 	SCHUMANN: Carnaval, Fantasiestücke, Papillons034571171203
CDA67121/2 	BACH: The French Suites  Temporarily out of stock034571171210
CDA67123 	STANFORD: Songs, Vol. 1034571171234
CDA67124 	STANFORD: Songs, Vol. 2034571171241
CDA67125 	CHOPIN: Polish SongsPreviously issued on CDH55270034571171258
CDA67126 	English Lute Songs  Superseded by CDH55249034571171265
CDA67127 	The Romantic Piano Concerto, Vol. 23 – Holbrooke & Wood034571171272
CDA67128 	HANDEL: Opera Arias & Overtures, Vol. 2034571171289
CDA67129 	A Marriage of England & Burgundy034571171296
CDA67130 	WOLF: Goethe Lieder034571171302
CDA67131/2 	SCRIABIN: The Complete Piano Sonatas034571171319
CDA67133/4 	CHABRIER: Musique adorable!034571171333
CDA67135/6 	MCCABE: Edward II034571171357
CDA67137 	MENDELSSOHN: Songs & Duets, Vol. 2  Temporarily out of stock034571171371
CDA67138 	BACH/SIMPSON: The Art of Fugue034571171388
CDA67139 	BACH: Organ Cornucopia  Temporarily out of stock034571171395
CDA67140 	BRITTEN: Sacred and Profane & other choral works  Temporarily out of stockPreviously issued on CDH55438034571171401
CDA67141/2 	HAHN: Songs034571171418
CDA67143 	The Romantic Piano Concerto, Vol. 22 – Busoni  Temporarily out of stock034571171432
CDA67145 	LISZT: The complete music for solo piano, Vol. 45 – Rapsodie espagnole034571171456
CDA67146 	Organ Dreams, Vol. 2  Temporarily out of stock034571171463
CDA67147 	JANÁCEK/KODÁLY: Masses034571171470
CDA67148 	British Light Music Classics, Vol. 3034571171487
CDA67149 	SCRIABIN: The Early Scriabin  Superseded by CDH55286034571171494
CDA67150 	Haydn & his English Friends034571171500
CDA67151/2 	BOYCE: Trio Sonatas  Superseded by CDD22063034571171517
CDA67153 	SHOSTAKOVICH: String Quartets Nos. 2 & 3034571171531
CDA67154 	SHOSTAKOVICH: String Quartets Nos. 4, 6 & 8034571171548
CDA67155 	SHOSTAKOVICH: String Quartets Nos. 5, 7 & 9034571171555
CDA67156 	SHOSTAKOVICH: String Quartets Nos. 10, 12 & 14034571171562
CDA67157 	SHOSTAKOVICH: String Quartets Nos. 11, 13 & 15034571171579
CDA67158 	SHOSTAKOVICH: Quartet No. 1, Quintet & Trio No. 2034571171586
CDA67159 	KAPUSTIN: Piano Music, Vol. 1034571171593
CDA67160 	KNÜPFER: Sacred Music  Temporarily out of stockPreviously issued on CDH55393034571171609
CDA67161/2 	LISZT: The complete music for solo piano, Vol. 46 – Meditations034571171616
CDA67163 	The Romantic Piano Concerto, Vol. 24 – Vianna da Motta034571171630
CDA67164 	COUPERIN M R N: Livre de Tablature de Clavescin034571171647
CDA67165 	The Romantic Piano Concerto, Vol. 25 – MacDowell034571171654
CDA67166 	SCHUMANN: Piano Music034571171661
CDA67167 	GABRIELI A: Missa Pater Peccavi  Superseded by CDH55265034571171678
CDA67168 	VAUGHAN WILLIAMS: Songs034571171685
CDA67169 	STRAUSS J: Strauss Dances034571171692
CDA67170 	BERNSTEIN/BOLCOM: The Age of Anxiety & Concerto034571171708
CDA67171/3 	HANDEL: Joseph & his Brethren  Temporarily out of stock034571171715
CDA67174 	HAYDN: Songs  Superseded by CDH55355034571171746
CDA67175 	SCHUMANN: Fantasiestücke, Piano Trio & Piano Quartet034571171753
CDA67176 	VILLA-LOBOS: Piano Music034571171760
CDA67177 	The Earliest Songbook in England  Superseded by CDH55297034571171777
CDA67178 	RACHMANINOV: Piano Trios  Superseded by CDH55431034571171784
CDA67179 	DITTERSDORF/VANHAL: Double Bass Concertos  Temporarily out of stock034571171791
CDA67180 	SCHUMANN: Violin Sonatas & Three Romances034571171807
CDA67181/2 	BRIDGE: Songs  Superseded by CDD22071034571171814
CDA67183 	JOSQUIN: Josquin & his contemporaries034571171838
CDA67184 	Smörgasbord034571171845
CDA67185 	BOUGHTON: Aylesbury Games & Concertos034571171852
CDA67186 	Canciones amatorias034571171869
CDA67187 	LISZT: The complete music for solo piano, Vol. 47 – Litanies de Marie034571171876
CDA67188/9 	BLISS: Knot of Riddles & other songs034571171883
CDA67190 	FRASER-SIMSON: The Maid of the Mountains  Superseded by CDH55246034571171906
CDA67191/2 	BACH: The Six Partitas034571171913
CDA67193 	LISZT: The complete music for solo piano, Vol. 48 – The Complete Paganini Études034571171937
CDA67194 	EBEN: Organ Music, Vol. 1034571171944
CDA67195 	EBEN: Organ Music, Vol. 2034571171951
CDA67196 	EBEN: Organ Music, Vol. 3034571171968
CDA67197 	EBEN: Organ Music, Vol. 4  Temporarily out of stock034571171975
CDA67198 	EBEN: Organ Music, Vol. 5034571171982
CDA67199 	LISZT: Missa Choralis & Via Crucis034571171999
CDA67200 	BRUCKNER: Symphony No. 3  Superseded by CDH55474034571172002
CDA67201/2 	BACH: Mass in B minor  Superseded by CDD22051034571172019
CDA67203 	LISZT: The complete music for solo piano, Vol. 49 – Schubert & Weber Transcriptions034571172033
CDA67204 	L'Album des Six  Superseded by CDH55386034571172040
CDA67205 	Russian Images, Vol. 2034571172057
CDA67206 	CORNELIUS: The Three Kings034571172064
CDA67207 	TALLIS: Missa Salve intemerata & AntiphonsPreviously issued on CDH55400034571172071
CDA67208 	The Romantic Violin Concerto, Vol. 02 – Stanford034571172088
CDA67209 	SABATA: Orchestral Music034571172095
CDA67210 	The Romantic Piano Concerto, Vol. 26 – Litolff Concertos Symphoniques 3 & 5  Temporarily out of stock034571172101
CDA67211/2 	BACH: Organ Miniatures034571172118
CDA67213/4 	BACH: The Clavierübung Chorales034571172132
CDA67215 	BACH: Neumeister Chorales034571172156
CDA67216 	GLINKA/TCHAIKOVSKY: Piano Trios  Superseded by CDH55322034571172163
CDA67217 	TAVENER: The World & Diódia  Temporarily out of stock034571172170
CDA67218 	ALKAN: Symphony for solo piano034571172187
CDA67219 	MACMILLAN: Mass & other sacred music034571172194
CDA67220 	GOLDMARK/WALTER: Violin Sonatas  Temporarily out of stock034571172200
CDA67221/4 	MEDTNER: The Complete Piano Sonatas034571172217
CDA67225 	Salve Regina034571172255
CDA67226 	BACH C P E: Flute Concertos034571172262
CDA67227 	On this Island034571172279
CDA67228 	Organ Fireworks, Vol. 09034571172286
CDA67229 	SCHUBERT: Opera Arias034571172293
CDA67230 	The Neapolitans034571172309
CDA67231/2 	LISZT: The complete music for solo piano, Vol. 50 – Liszt at the Opera V  Temporarily out of stock034571172316
CDA67233/4 	LISZT: The complete music for solo piano, Vol. 51 – Paralipomènes034571172330
CDA67235 	LISZT: The complete music for solo piano, Vol. 52 – Ungarischer Romanzero034571172354
CDA67236 	BUXTEHUDE: Seven Sonatas, Op. 1  Temporarily out of stock034571172361
CDA67237 	BRAHMS: Piano Sonata No. 3 & Four Ballades034571172378
CDA67238 	Violin Masters of the 17th Century034571172385
CDA67239 	WALTON: Façade034571172392
CDA67240 	PRAETORIUS: Music from Terpischore034571172408
CDA67241/2 	HANDEL: Alexander Balus034571172415
CDA67243 	GURNEY: Severn Meadows034571172439
CDA67244 	French Cello Music034571172446
CDA67245 	RUTTER: Music for Christmas034571172453
CDA67246 	MOZART: Divertimento, K563 & Duo, K424034571172460
CDA67247 	BACH: A Bach Album034571172477
CDA67248 	GOTTSCHALK: Piano Music, Vol. 5  Temporarily out of stock034571172484
CDA67249 	SCHUMANN C: Songs  Superseded by CDH55275034571172491
CDA67250 	BANTOCK: Thalaba the Destroyer034571172507
CDA67251/2 	BRAHMS: The Complete TriosPreviously issued on CDD22082034571172514
CDA67253 	BEETHOVEN: String Trio & Serenade034571172538
CDA67254 	BEETHOVEN: Three String Trios034571172545
CDA67255/6 	POULENC: The Complete Chamber Music034571172552
CDA67257 	DUREY: Songs034571172576
CDA67258 	HAHN/VIERNE: Piano Quintets034571172583
CDA67259 	RUTTER: Gloria & other sacred music034571172590
CDA67260 	SCHELLE: Sacred Music  Temporarily out of stockPreviously issued on CDH55373034571172606
CDA67261/2 	IRELAND: Songs034571172613
CDA67263 	BACH: Attributions034571172637
CDA67264/5 	BACH: The Complete Flute SonatasPreviously issued on CDD22077034571172644
CDA67266 	Classical Trumpet Concertos034571172668
CDA67267 	Stephen Hough's English Piano Album034571172675
CDA67268 	CAMPION: Move now with measured sound034571172682
CDA67269 	Epiphany at St Paul's  Superseded by CDH55443034571172699
CDA67270 	HOLST/MATTHEWS: The Planets & Pluto  Superseded by CDH55350034571172705
CDA67271/2 	LASSUS: Penitential Psalms  Superseded by CDD22056034571172712
CDA67273 	SCHUBERT: Piano Trio in B flat034571172736
CDA67274 	English Poets, Russian Romances034571172743
CDA67275 	Kaleidoscope034571172750
CDA67276 	The Romantic Piano Concerto, Vol. 29 – Moscheles 2 & 3034571172767
CDA67277 	MOZART: Oboe Quartet, Horn Quintet & other works  Superseded by CDH55390034571172774
CDA67278 	HANDEL: The Complete Flute Sonatas034571172781
CDA67279 	GRAINGER: Rambles & Reflections  Superseded by CDH55454034571172798
CDA67280 	SULLIVAN: The Golden Legend034571172804
CDA67281/2 	VIVALDI: Sacred Music, Vol. 04 - Juditha Triumphans034571172811
CDA67283/4 	HANDEL: L'Allegro, il Penseroso ed il Moderato034571172835
CDA67285 	SAINT-SAËNS/YSAYE: Rare transcriptions for violin & piano  Superseded by CDH55353034571172859
CDA67286 	The Coronation of King George II034571172866
CDA67287 	BOCCHERINI: Cello Quintets, Vol. 1034571172873
CDA67288 	Bassoon Concertos034571172880
CDA67289 	LÉONIN: Magister Leoninus, Vol. 2  Superseded by CDH55338034571172897
CDA67290 	Songs my father taught me034571172903
CDA67291/2 	HANDEL: Organ Concertos  Temporarily out of stockPreviously issued on CDD22052034571172910
CDA67293 	COLES: Music from Behind the lines  Temporarily out of stockPreviously issued on CDH55464034571172934
CDA67294 	Rare French works for violin & orchestra  Superseded by CDH55396034571172941
CDA67295 	GRECHANINOV: Piano Trios  Superseded by CDH55399034571172958
CDA67296 	The Romantic Piano Concerto, Vol. 39 – Delius & Ireland034571172965
CDA67297 	SCHNITTKE: Choir Concerto & Minnesang034571172972
CDA67298 	HANDEL: The Choice of Hercules034571172989
CDA67299 	A Scottish Lady Mass  Temporarily out of stock034571172996
CDA67300 	GODOWSKY: Sonata & Passacaglia034571173009
CDA67301/2 	BACH: The Well-tempered Clavier IPreviously issued on CDS44291/4034571173016
CDA67303/4 	BACH: The Well-tempered Clavier IIPreviously issued on CDS44291/4034571173030
CDA67305 	BACH: Goldberg Variations034571173054
CDA67306 	BACH: Italian Concerto & French Overture  Temporarily out of stock034571173061
CDA67307 	BACH: The Keyboard Concertos, Vol. 1034571173078
CDA67308 	BACH: The Keyboard Concertos, Vol. 2034571173085
CDA67309 	BACH: Bach Arrangements034571173092
CDA67310 	BACH: The Toccatas  Temporarily out of stock034571173108
CDA67311/2 	WOLF: Mörike Lieder034571173115
CDA67313 	VAUGHAN WILLIAMS: Chamber Music034571173139
CDA67314 	The Romantic Piano Concerto, Vol. 28 – Stojowski  Temporarily out of stock034571173146
CDA67315 	Of ladies & love  Temporarily out of stock034571173153
CDA67316 	Peacock Pie034571173160
CDA67317 	Organ Dreams, Vol. 3034571173177
CDA67318 	SIBELIUS: Songs  Superseded by CDH55471034571173184
CDA67319 	BUSNOIS/DOMARTO: Missa L'homme armé  Superseded by CDH55288034571173191
CDA67320 	ORNSTEIN: Piano Music034571173207
CDA67321/2 	CHAUSSON: Songs034571173214
CDA67323 	FRANÇAIX: Orchestral Music  Temporarily out of stock034571173238
CDA67324 	BACH: Piano Transcriptions, Vol. 02 – Ferruccio Busoni  Temporarily out of stock034571173245
CDA67325 	LALANDE: Music for The Sun King034571173252
CDA67326 	The Romantic Piano Concerto, Vol. 30 – Lyapunov034571173269
CDA67327 	BEETHOVEN: The Complete Music for Piano Trio, Vol. 1  Temporarily out of stock034571173276
CDA67328 	ALEXANDROV: Piano Music034571173283
CDA67329 	Soul and Landscape034571173290
CDA67330 	WALTON: Coronation Te Deum  Temporarily out of stock034571173306
CDA67331/2 	The Romantic Piano Concerto, Vol. 27 – Saint-Saëns034571173313
CDA67333 	FAURÉ: The Complete Songs, Vol. 1034571173337
CDA67334 	FAURÉ: The Complete Songs, Vol. 2  Temporarily out of stock034571173344
CDA67335 	FAURÉ: The Complete Songs, Vol. 3034571173351
CDA67336 	FAURÉ: The Complete Songs, Vol. 4034571173368
CDA67337 	GIBBS: Songs034571173375
CDA67338 	BORTKIEWICZ: Symphonies Nos. 1 & 2034571173382
CDA67339 	SCHUBERT: Octet  Superseded by CDH55460034571173399
CDA67340 	WALTON: Chamber Music034571173405
CDA67341/2 	RAVEL: The complete solo piano music034571173412
CDA67343 	WOLF: Lieder nach Heine & Lenau  Superseded by CDH55389034571173436
CDA67344 	BACH: Piano Transcriptions, Vol. 03 – Friedman, Grainger & Murdoch034571173443
CDA67345 	TARTINI: Violin Concertos  Temporarily out of stockPreviously issued on CDH55334034571173450
CDA67346 	LISZT: New Discoveries, Vol. 1  Temporarily out of stock034571173467
CDA67347 	SCHUBERT: Piano Trio in E flat034571173474
CDA67348 	The Romantic Piano Concerto, Vol. 34 – Pierné034571173481
CDA67349 	GOTTSCHALK: Piano Music, Vol. 6034571173498
CDA67350 	ZELENKA: Sacred Music  Temporarily out of stockPreviously issued on CDH55424034571173504
CDA67351/2 	MESSIAEN: Vingt Regards sur l'Enfant-Jésus034571173511
CDA67353 	PALESTRINA: Missa Dum complerentur & other sacred music  Superseded by CDH55449034571173535
CDA67354 	The Romantic Piano Concerto, Vol. 31 – Fuchs & Kiel034571173542
CDA67355 	Russian Songs034571173559
CDA67356 	Jerusalem on High  Last few remaining034571173566
CDA67357 	DEBUSSY: Songs, Vol. 1034571173573
CDA67358 	MOZART: Piano Concertos Nos. 11, 12 & 13  Superseded by CDH55333034571173580
CDA67359 	The fam'd Italian masters034571173597
CDA67360 	HOLLOWAY: Gilded Goldbergs034571173603
CDA67361/2 	VIVALDI: La Senna Festeggiante034571173610
CDA67363 	ELGAR: Enigma Variations & Organ Sonata  Temporarily out of stock034571173634
CDA67364 	BACH C P E: Die Auferstehung und Himmelfahrt Jesu  Superseded by CDH55478034571173641
CDA67365 	The Romantic Piano Concerto, Vol. 33 – Scharwenka 2 & 3034571173658
CDA67366 	MESSIAEN: Visions de l'Amen034571173665
CDA67367 	The Romantic Violin Concerto, Vol. 03 – Hubay 3 & 4034571173672
CDA67368 	DUFAY: Missa Puisque je vis & other works  Superseded by CDH55423034571173689
CDA67369 	BEETHOVEN: The Complete Music for Piano Trio, Vol. 2034571173696
CDA67370 	LISZT: Paganini Studies & Schubert Marches034571173702
CDA67371/2 	CHOPIN: Nocturnes & Impromptus034571173719
CDA67373 	MOZART: Piano Quartets034571173733
CDA67374 	More songs my father taught me034571173740
CDA67375 	PÄRT: Triodion & other choral works  Temporarily out of stock034571173757
CDA67376 	FRANCK/RACHMANINOV: Cello Sonatas034571173764
CDA67377 	ALKAN: Esquisses034571173771
CDA67378 	Songs of Travel034571173788
CDA67379 	The Maiden's Prayer  Superseded by CDH55410034571173795
CDA67380 	New World Symphonies  Superseded by CDA30030034571173801
CDA67381/2 	VAUGHAN WILLIAMS: The Early Chamber Music034571173818
CDA67383 	BOCCHERINI: Cello Quintets, Vol. 2034571173832
CDA67384 	FRANÇAIX: Ballet Music034571173849
CDA67385 	The Romantic Piano Concerto, Vol. 32 – Moscheles 1, 6 & 7034571173856
CDA67386 	MOZART: Divertimenti, K247 & K334034571173863
CDA67387 	LAMOND: Symphony in A major034571173870
CDA67388 	MENDELSSOHN: Songs & Duets, Vol. 3034571173887
CDA67389 	The Romantic Violin Concerto, Vol. 04 – Moszkowski & Karlowicz034571173894
CDA67390 	HUMMEL: Piano Sonatas034571173900
CDA67391 	HAHN: Chamber Music  Superseded by CDH55379034571173917
CDA67392 	MAHLER: Songs034571173924
CDA67393 	BEETHOVEN: The Complete Music for Piano Trio, Vol. 3034571173931
CDA67394 	MOSCHELES: Complete Concert Studies  Superseded by CDH55387034571173948
CDA67395 	BANTOCK: The Song of Songs034571173955
CDA67396 	PALESTRINA: Music for Advent & Christmas  Superseded by CDH55367034571173962
CDA67397 	BYRD: Consort Songs  Superseded by CDH55429034571173979
CDA67398 	Remembrance034571173986
CDA67399 	SZYMANOWSKI: The Complete Mazurkas034571173993
CDA67400 	British Light Music Classics, Vol. 4034571174006
CDA67401/2 	LISZT: The complete music for solo piano, Vol. 53a – Music for piano & orchestra I034571174013
CDA67403/4 	LISZT: The complete music for solo piano, Vol. 53b – Music for piano & orchestra II034571174037
CDA67406/7 	LISZT: The complete music for solo piano, Vol. 54 – Liszt at the Opera VI034571174068
CDA67408/10 	LISZT: The complete music for solo piano, Vol. 55 – Grande Fantaisie034571174082
CDA67411/2 	GODOWSKY: The Complete Studies on Chopin's Études034571174112
CDA67413 	TCHAIKOVSKY B: Chamber Symphony034571174136
CDA67414/7 	LISZT: The complete music for solo piano, Vol. 56 – Rarities & Curiosities034571174143
CDA67418/9 	LISZT: The complete music for solo piano, Vol. 57 – Hungarian Rhapsodies034571174181
CDA67420 	The Romantic Violin Concerto, Vol. 05 – Coleridge-Taylor & Somervell034571174204
CDA67421/2 	SWEELINCK: Keyboard Music034571174211
CDA67423 	SULLIVAN: The Prodigal Son034571174235
CDA67424 	LISZT: Années de pèlerinage, Suisse034571174242
CDA67425 	SHOSTAKOVICH/SHCHEDRIN: Piano Concertos034571174259
CDA67426 	BRIDGE: Early Chamber Music034571174266
CDA67427 	BRÉVILLE/CANTELOUBE: Violin Sonatas  Temporarily out of stock034571174273
CDA67428 	MONTEVERDI: The Sacred Music, Vol. 1034571174280
CDA67429 	Dohnányi, Martinu & Schoenberg Trios034571174297
CDA67430 	The Romantic Piano Concerto, Vol. 36 – Moscheles 4 & 5034571174303
CDA67431/2 	SAINT-SAËNS: Chamber Music034571174310
CDA67433 	KAPUSTIN: Piano Music, Vol. 2034571174334
CDA67434 	STANFORD: String Quartets  Superseded by CDH55459034571174341
CDA67435 	CHARPENTIER: Mass for four choirs  Temporarily out of stock034571174358
CDA67436 	Organ Dreams, Vol. 4034571174365
CDA67437 	STOJOWSKI: Piano Music034571174372
CDA67438 	MONTEVERDI: The Sacred Music, Vol. 2034571174389
CDA67439 	BLOCH: Violin Sonatas  Temporarily out of stock034571174396
CDA67440 	COUPERIN F: Keyboard Music, Vol. 1  Temporarily out of stock034571174402
CDA67441/2 	HUBAY: Scènes de la csárda034571174419
CDA67443 	Nativity034571174433
CDA67444 	MILFORD: Fishing by Moonlight034571174440
CDA67445 	LISZT: Harmonies poétiques et religieuses  Temporarily out of stock034571174457
CDA67446 	GRAUN: Der Tod Jesu034571174464
CDA67447 	RAMEAU: Règne Amour034571174471
CDA67448 	SUK: Piano Quintet & Piano Quartet  Temporarily out of stockPreviously issued on CDH55416034571174488
CDA67449 	LAURIDSEN: Lux aeterna034571174495
CDA67450 	Orpheus with his lute034571174501
CDA67451/2 	BACH: The English Suites034571174518
CDA67453 	The Playful Pachyderm  Temporarily out of stock034571174532
CDA67454 	MAXWELL DAVIES: Mass  Temporarily out of stock034571174549
CDA67455 	LISZT: New Discoveries, Vol. 2034571174556
CDA67456 	CHOPIN: Four Ballades & Four Scherzos034571174563
CDA67457 	London Pride034571174570
CDA67458 	Organ Fireworks, Vol. 10034571174587
CDA67459 	Songs by Britten, Finzi & Tippett034571174594
CDA67460 	MACMILLAN: Seven Last Words from the Cross  Temporarily out of stock034571174600
CDA67461/2 	TIPPETT: Piano Concerto034571174617
CDA67463 	HANDEL: St Cecilia's Day Ode034571174631
CDA67464 	WEBER: Complete Chamber Music034571174648
CDA67465 	The Romantic Piano Concerto, Vol. 35 – Herz 1, 7 & 8034571174655
CDA67466 	BEETHOVEN: The Complete Music for Piano Trio, Vol. 4034571174662
CDA67467 	VIVALDI: Six Violin Sonatas, Op. 2  Superseded by CDH55404034571174679
CDA67468 	BACH: Piano Transcriptions, Vol. 04 – Samuel Feinberg034571174686
CDA67469 	BARBER/IVES: Piano Sonatas  Temporarily out of stock034571174693
CDA67470 	WHITLOCK: Organ Sonata034571174709
CDA67471/2 	BRAHMS: Piano Quartets034571174716
CDA67474 	DUFAY: Mass for St Anthony Abbot034571174747
CDA67475 	TAVENER: Choral Works  Temporarily out of stock034571174754
CDA67476/7 	ALBÉNIZ: Iberia034571174761
CDA67478 	GOTTSCHALK: Piano Music, Vol. 7034571174785
CDA67479 	VICTORIA: Ave Regina caelorum034571174792
CDA67480 	COUPERIN F: Keyboard Music, Vol. 2  Temporarily out of stock034571174808
CDA67481/2 	BACH: Piano Transcriptions, Vol. 06 – Walter Rummel034571174815
CDA67483 	The English Anthem, Vol. 8034571174839
CDA67484 	ROSLAVETS: Chamber Symphony & The Hours Of The New Moon034571174846
CDA67485 	MENDELSSOHN: Piano Trios034571174853
CDA67486 	SULLIVAN: The Contrabandista & The Foresters034571174860
CDA67487 	MONTEVERDI: The Sacred Music, Vol. 3034571174877
CDA67488 	STRAUSS R: The Complete Songs, Vol. 1034571174884
CDA67489 	FRANÇAIX: Orchestral Music034571174891
CDA67490 	PEERSON: Latin Motets034571174907
CDA67491/2 	MEDTNER: The Complete Skazki034571174914
CDA67493 	SCHWANTNER: Angelfire & other works034571174938
CDA67494 	HOWELLS: Choral Music  Superseded by CDH55456034571174945
CDA67495 	HENSELT: Études034571174952
CDA67496 	VASKS/WEILL: Violin Concertos034571174969
CDA67497 	BAIRSTOW: Choral Music034571174976
CDA67498 	The Romantic Violin Concerto, Vol. 06 – Hubay 1 & 2034571174983
CDA67499 	BACH: Fantasia, Aria & other works034571174990
CDA67500 	SIMPSON: Symphony No. 11 & Nielsen Variations034571175003
CDA67501/2 	RACHMANINOV: Piano Concertos  Temporarily out of stock034571175010
CDA67503 	BINGHAM/VAUGHAN WILLIAMS: Mass034571175034
CDA67504 	GRIEG: Violin Sonatas034571175041
CDA67505 	STANFORD: Piano Quintet & String Quintet No. 1  Superseded by CDH55434034571175058
CDA67506 	BACH: Piano Transcriptions, Vol. 05 – Goedicke, Kabalevsky, Catoire & Siloti034571175065
CDA67507 	PITTS: Seven Letters & other sacred choral music034571175072
CDA67508 	The Romantic Piano Concerto, Vol. 38 – Rubinstein & Scharwenka034571175089
CDA67509 	SPOHR: Clarinet Concertos Nos. 1 & 2034571175096
CDA67510 	HAYDN M: Requiem034571175102
CDA67511 	The Romantic Piano Concerto, Vol. 37 – Nápravník & Blumenfeld034571175119
CDA67512 	CATOIRE: Chamber Music034571175126
CDA67513 	DUKAS/DECAUX: Piano Sonata034571175133
CDA67514 	PROKOFIEV: Violin Sonatas034571175140
CDA67515 	CHABRIER: Piano Music  Temporarily out of stock034571175157
CDA67516 	IVES: A Song - For Anything034571175164
CDA67517 	JANÁCEK: Orchestral Music034571175171
CDA67518 	BEETHOVEN: Piano Sonatas, Vol. 1034571175188
CDA67519 	MONTEVERDI: The Sacred Music, Vol. 4034571175195
CDA67520 	COUPERIN F: Keyboard Music, Vol. 3034571175201
CDA67521 	HUMMEL/MOSCHELES: Cello Sonatas  Temporarily out of stock034571175218
CDA67522 	Christmas Vespers at Westminster Cathedral034571175225
CDA67523 	L'invitation au voyage034571175232
CDA67524 	Moon, sun & all things  Temporarily out of stock034571175249
CDA67525 	IVES: Symphonies Nos. 2 & 3034571175256
CDA67526 	BEETHOVEN: Wind Quintet034571175263
CDA67527 	SCHUBERT: 'Trout' Quintet034571175270
CDA67528 	BARBER: Songs034571175287
CDA67529 	BRAHMS: Cello Sonatas034571175294
CDA67530 	DEBUSSY: Préludes034571175300
CDA67531/2 	MONTEVERDI: Vespers034571175317
CDA67533 	BYRD: The Great Service & other works034571175331
CDA67534 	SCHNITTKE/SHOSTAKOVICH: Cello Sonatas  Temporarily out of stock034571175348
CDA67535 	The Romantic Piano Concerto, Vol. 41 – Kalkbrenner 1 & 4034571175355
CDA67536 	GOTTSCHALK: Piano Music, Vol. 8034571175362
CDA67537 	The Romantic Piano Concerto, Vol. 40 – Herz 3, 4 & 5034571175379
CDA67538 	SAINT-SAËNS: Piano Trios034571175386
CDA67539 	VILLETTE: Choral Music034571175393
CDA67540 	IVES: Symphonies Nos. 1 & 4034571175409
CDA67541/2 	BACH: The Cello Suites034571175416
CDA67543 	WHITACRE: Cloudburst & other choral works034571175430
CDA67544 	The Romantic Cello Concerto, Vol. 1 – Dohnányi, Enescu & d'Albert034571175447
CDA67545 	LAMBERT: Romeo & Juliet  Temporarily out of stock034571175454
CDA67546 	BOWEN/FORSYTH: Viola Concertos034571175461
CDA67547 	HARTMANN: Concerto funebre034571175478
CDA67548 	TALLIS: Gaude gloriosa034571175485
CDA67549 	Delectatio angeli  Temporarily out of stock034571175492
CDA67550 	BRAHMS: Piano Concerto No. 2034571175508
CDA67551 	BRAHMS: String Quartet & Piano Quintet034571175515
CDA67552 	BRAHMS: String Quartets, Opp. 67 & 51/1034571175522
CDA67553 	VIVALDI: Cello Concertos034571175539
CDA67554 	HAYDN: Piano Sonatas, Vol. 1034571175546
CDA67555 	The Romantic Piano Concerto, Vol. 42 – Alnæs & Sinding034571175553
CDA67556 	MOZART: Piano Trios, K502, K542 & K564034571175560
CDA67557 	Trinity Sunday at Westminster Abbey  Temporarily out of stock034571175577
CDA67558 	MENDELSSOHN: Sacred choral music034571175584
CDA67559 	BRAHMS/RHEINBERGER: Mass034571175591
CDA67560 	MOZART: Exsultate jubilate!  Temporarily out of stock034571175607
CDA67561 	SPOHR: Clarinet Concertos Nos. 3 & 4034571175614
CDA67562 	PADEREWSKI: Sonata & Variations  Temporarily out of stock034571175621
CDA67563 	Women's lives & loves034571175638
CDA67564 	TSONTAKIS: Man of Sorrows034571175645
CDA67565 	Stephen Hough's Spanish Album  Temporarily out of stock034571175652
CDA67567 	BURGON: Choral MusicPreviously issued on CDH55421034571175676
CDA67568 	BYRD: Laudibus in sanctis034571175683
CDA67569 	ALKAN: Concerto for solo piano034571175690
CDA67570 	ROSSINI: Petite Messe solennelle034571175706
CDA67571 	BLOCH/BEN-HAÏM: Violin Music  Temporarily out of stock034571175713
CDA67572 	DVORÁK: Piano Trios Nos. 1 & 2034571175720
CDA67573 	TANEYEV: String Trios034571175737
CDA67574 	STRAUSS R: Metamorphosen, Capriccio034571175744
CDA67575 	Children of our time034571175751
CDA67576 	Christmas at St John's Cambridge034571175768
CDA67577 	Organ Fireworks, Vol. 11034571175775
CDA67578 	MEDTNER: Forgotten Melodies  Temporarily out of stock034571175782
CDA67579 	Music for the Court of Maximilian II034571175799
CDA67580 	LAURIDSEN: Nocturnes  Temporarily out of stock034571175805
CDA67581/2 	REGER: Cello Sonatas  Temporarily out of stock034571175812
CDA67583 	The Romantic Cello Concerto, Vol. 2 – Volkmann, Dietrich, Gernsheim & Schumann034571175836
CDA67584 	BRAHMS: Viola Sonatas034571175843
CDA67585 	SCHUBERT: Death & the Maiden034571175850
CDA67586 	The Feast of St Edward at Westminster Abbey034571175867
CDA67587 	RUBBRA/WALTON: Viola Concertos  Temporarily out of stock034571175874
CDA67588 	STRAUSS R: The Complete Songs, Vol. 2034571175881
CDA67589 	LAWES: Songs034571175898
CDA67590 	COLERIDGE-TAYLOR: Piano Quintet & Clarinet Quintet034571175904
CDA67591/2 	NIELSEN: Complete Piano Music034571175911
CDA67593 	ELGAR: Great is the Lord & other works034571175935
CDA67594 	DELIUS: Songs034571175942
CDA67595 	The Romantic Piano Concerto, Vol. 43 – Sterndale Bennett & Bache034571175959
CDA67596 	CRECQUILLON: Missa Mort m'a privé, motets & chansons034571175966
CDA67597 	RAMEAU: Keyboard Suites  Temporarily out of stock034571175973
CDA67598 	MOZART: Stephen Hough's Mozart Album  Temporarily out of stock034571175980
CDA67599 	SCHMITT: Orchestral Music034571175997
CDA67600 	Fire burning in snow034571176000
CDA67601 	TORMIS: Choral music  Temporarily out of stock034571176017
CDA67602 	STRAUSS R: The Complete Songs, Vol. 3034571176024
CDA67603 	JONGEN/PEETERS: Choral music034571176031
CDA67604 	MANCHICOURT: Missa Cuidez vous que Dieu034571176048
CDA67605 	BEETHOVEN: Piano Sonatas, Vol. 2034571176055
CDA67606 	HERZ: Piano Music034571176062
CDA67607/8 	BACH: The Keyboard Concertos034571176079
CDA67609 	MOZART: Piano Trios, K548, K254 & K496034571176093
CDA67610 	PALESTRINA: Lamentations034571176109
CDA67611 	HAYDN: String Quartets, Op. 9034571176116
CDA67612 	Organ Fireworks, Vol. 12034571176123
CDA67613 	SCARLATTI D: Sonatas  Temporarily out of stock034571176130
CDA67614 	GOMBERT: Tribulatio et angustia034571176147
CDA67615 	MAW: One foot in Eden still, I stand034571176154
CDA67616 	SPOHR: Symphonies Nos. 1 & 2034571176161
CDA67617 	STRADELLA: San Giovanni Battista034571176178
CDA67618 	SCHUMANN: Humoreske & Sonata Op. 11034571176185
CDA67619 	ERNST: Violin Music034571176192
CDA67621 	PORPORA: Or sì m’avveggio, oh Amore – Cantatas for soprano034571176215
CDA67622 	SPOHR: Symphonies Nos. 4 & 5  Temporarily out of stock034571176222
CDA67623 	POULENC: Gloria034571176239
CDA67624 	ALKAN/CHOPIN: Cello Sonatas034571176246
CDA67625 	BRITTEN: Piano Concerto034571176253
CDA67626 	GODOWSKY: Strauss transcriptions & other waltzes034571176260
CDA67627 	HANDEL: German Arias034571176277
CDA67628 	ABEL: Mr Abel's Fine Airs034571176284
CDA67629 	BRUCKNER: Mass & Motets034571176291
CDA67630 	The Romantic Piano Concerto, Vol. 44 – Melcer034571176307
CDA67631 	SCHUMANN: String Quartet & Piano Quintet034571176314
CDA67632 	CLEMENTI: The Complete Piano Sonatas, Vol. 1034571176321
CDA67633 	BEETHOVEN: Cello Sonatas, Vol. 1034571176338
CDA67634 	The Language of Love  Last few remaining034571176345
CDA67635 	The Romantic Piano Concerto, Vol. 53 – Reger & Strauss034571176352
CDA67636 	The Romantic Piano Concerto, Vol. 47 – Draeseke & Jadassohn034571176369
CDA67637 	ROSLAVETS: Violin Concertos034571176376
CDA67638 	BLOCH: Piano Quintets034571176383
CDA67639 	LUKASZEWSKI: Choral music034571176390
CDA67640 	REGNART: Missa Super Oeniades Nymphae034571176406
CDA67641 	LEIGHTON: The World's Desire  Temporarily out of stock034571176413
CDA67642 	The Romantic Violin Concerto, Vol. 07 – Taneyev & Arensky034571176420
CDA67643 	The Feast of Michaelmas at Westminster Abbey  Temporarily out of stock034571176437
CDA67644 	IVES: Romanzo di Central Park034571176444
CDA67645 	MAHLER: Des Knaben Wunderhorn034571176451
CDA67646 	BOCCHERINI: Flute Quintets, Op. 19034571176468
CDA67647 	ROSSINI: Soirées musicales034571176475
CDA67648 	DOWLAND/BRITTEN: Lute Songs034571176482
CDA67649 	RACHMANINOV: Piano Concertos Nos. 2 & 3  Superseded by CDA67501/2034571176499
CDA67650 	CHILCOTT: Requiem & other works034571176505
CDA67651/2 	BOWEN: The complete works for viola & piano034571176512
CDA67653 	BYRD: Hodie Simon Petrus034571176536
CDA67654 	MONCKTON: Songs from the shows034571176543
CDA67655 	The Romantic Piano Concerto, Vol. 45 – Hiller034571176550
CDA67656 	Marc-André Hamelin in a state of jazz034571176567
CDA67657 	SCHUBERT: Schwanengesang  Temporarily out of stock034571176574
CDA67658 	MONTE: Missa Ultimi miei sospiri034571176581
CDA67659 	The Romantic Piano Concerto, Vol. 46 – Bowen034571176598
CDA67660 	RUBINSTEIN: Cello Sonatas034571176604
CDA67661 	SCHUMANN: Music for cello & piano034571176611
CDA67662 	BEETHOVEN: Piano Sonatas – Moonlight, Pathétique & Waldstein034571176628
CDA67663 	BRAHMS/JOACHIM: Hungarian Dances034571176635
CDA67664 	FAURÉ/FRANCK: String Quartets  Temporarily out of stock034571176642
CDA67665 	SCHUBERT: Piano Duets034571176659
CDA67666 	BUXTEHUDE: The Complete Organ Works, Vol. 1034571176666
CDA67667 	STRAUSS R: The Complete Songs, Vol. 4034571176673
CDA67668 	PITTS: Alpha & Omega034571176680
CDA67669 	PRAETORIUS H: Magnificats & motets034571176697
CDA67670 	GRIEG: Songs034571176703
CDA67671 	MARTINU: Complete music for violin & orchestra, Vol. 1034571176710
CDA67672 	MARTINU: Complete music for violin & orchestra, Vol. 2034571176727
CDA67673 	MARTINU: Complete music for violin & orchestra, Vol. 3034571176734
CDA67674 	MARTINU: Complete music for violin & orchestra, Vol. 4  Temporarily out of stock034571176741
CDA67675 	BYRD: Assumpta est Maria034571176758
CDA67676 	SCHUMANN: Dichterliebe & other Heine Settings  Temporarily out of stock034571176765
CDA67677 	BUSONI: Fantasia contrappuntistica034571176772
CDA67678 	HANDEL: Dettingen Te Deum034571176789
CDA67679 	THOMPSON: The Peaceable Kingdom034571176796
CDA67680 	The Feast of Ascension at Westminster Abbey034571176802
CDA67681/2 	HANDEL: Il trionfo del Tempo e del Disinganno034571176819
CDA67683 	BACH: Piano Transcriptions, Vol. 07 – Max Reger034571176833
CDA67684 	SZYMANOWSKI/RÓZYCKI: String Quartets034571176840
CDA67685 	LIDARTI: Violin Concertos  Temporarily out of stock034571176857
CDA67686 	Stephen Hough in recital034571176864
CDA67687 	RÓZSA/BARTÓK: Viola Concertos034571176871
CDA67688 	HONEGGER: Une Cantate de Noël, Cello Concerto034571176888
CDA67689 	STENHAMMAR: Piano Music034571176895
CDA67690 	INDY: Wallenstein034571176901
CDA67691/2 	BACH: Sonatas & Partitas for solo violin034571176918
CDA67693 	BEETHOVEN: String Quintets, Opp. 4 & 29034571176932
CDA67694 	MORALES: Magnificat, Motets & Lamentations034571176949
CDA67695 	Music from the Chirk Castle Part-Books034571176956
CDA67696 	PHINOT: Missa Si bona suscepimus034571176963
CDA67697 	STRAVINSKY: The Fairy's Kiss & Scènes de ballet034571176970
CDA67698 	STRAVINSKY: Jeu de cartes, Agon & Orpheus034571176987
CDA67699 	DOHNÁNYI/JANÁCEK: Violin Sonatas034571176994
CDA67700 	RACHMANINOV: 24 PreludesPreviously issued on CDA30015034571177007
CDA67701/2 	HANDEL: Parnasso in Festa034571177014
CDA67703 	SZYMANOWSKI: The Complete Music for Violin & Piano  Temporarily out of stock034571177038
CDA67704 	Mary & Elizabeth at Westminster Abbey  Temporarily out of stock034571177045
CDA67705 	PROKOFIEV: Cello Concerto & Symphony-Concerto034571177052
CDA67706 	CHOPIN: Piano Sonatas Nos. 2 & 3034571177069
CDA67707 	From the vaults of Westminster Cathedral034571177076
CDA67708 	JACKSON: Not no faceless Angel034571177083
CDA67709 	BACH: Piano Transcriptions, Vol. 08 – Eugen d'Albert034571177090
CDA67710 	HAYDN: Piano Sonatas, Vol. 2034571177106
CDA67711/2 	The Romantic Piano Concerto, Vol. 50 – Tchaikovsky  Temporarily out of stock034571177113
CDA67713 	SAINT-SAËNS: Organ Music, Vol. 1034571177137
CDA67714 	SCARLATTI A: Davidis pugna et victoria034571177144
CDA67715 	DUFAY: The Court of Savoy034571177151
CDA67716 	A Christmas Caroll from Westminster Abbey034571177168
CDA67717 	CLEMENTI: The Complete Piano Sonatas, Vol. 2034571177175
CDA67719 	HAYDN: Piano Trios, Vol. 1034571177199
CDA67720 	The Romantic Piano Concerto, Vol. 48 – Benedict & Macfarren034571177205
CDA67721 	HINDEMITH: The Complete Viola Music, Vol. 1 – Sonatas034571177212
CDA67722 	HAYDN: String Quartets, Op. 17  Temporarily out of stock034571177229
CDA67723 	STRAVINSKY: Complete Music for Violin & Piano034571177236
CDA67724 	LUKASZEWSKI: Via Crucis  Temporarily out of stock034571177243
CDA67725 	Romantic Residues – Songs for tenor & harp034571177250
CDA67726 	BRIDGE: Piano Quintet, String Quartet & Idylls  Temporarily out of stock034571177267
CDA67727 	MACHAUT: Songs from Le Voir Dit034571177274
CDA67728 	RAVEL: Songs034571177281
CDA67729 	CLEMENTI: The Complete Piano Sonatas, Vol. 3034571177298
CDA67730 	Czech Piano Trios034571177304
CDA67731/2 	RAVEL: The complete solo piano music034571177311
CDA67733 	VAET: Missa Ego flos campi034571177335
CDA67734 	Organ Fireworks, Vol. 13034571177342
CDA67735 	WEINER: Violin Sonatas034571177359
CDA67736 	Angela Hewitt plays Handel & Haydn034571177366
CDA67737 	HANDEL: Chandos Anthems Nos 7, 9 & 11a034571177373
CDA67738 	CLEMENTI: The Complete Piano Sonatas, Vol. 4034571177380
CDA67739 	MENDELSSOHN: Songs & Duets, Vol. 4  Temporarily out of stock034571177397
CDA67740 	MATHIAS: Choral Music034571177403
CDA67741/4 	BACH: The Well-tempered Clavier – 2008 recording  Temporarily out of stock034571177410
CDA67745 	BEETHOVEN: Piano Quartet & String Quintet034571177458
CDA67746 	STRAUSS R: The Complete Songs, Vol. 5034571177465
CDA67747 	Baltic Exchange034571177472
CDA67748 	VICTORIA: Missa Gaudeamus & other music034571177489
CDA67749 	WILLAERT: Missa Mente tota & Motets034571177496
CDA67750 	The Romantic Piano Concerto, Vol. 49 – Stenhammar034571177502
CDA67751/2 	BOWEN: The Piano Sonatas034571177519
CDA67753 	MENDELSSOHN: Songs & Duets, Vol. 5  Temporarily out of stock034571177533
CDA67754 	The English Stage Jig034571177540
CDA67755 	BEETHOVEN: Cello Sonatas, Vol. 2  Temporarily out of stock034571177557
CDA67756 	Ikon, Vol. 2034571177564
CDA67757 	HAYDN: Piano Trios, Vol. 2034571177571
CDA67758 	Organ Fireworks, Vol. 14034571177588
CDA67759 	RAVEL/DEBUSSY: String Quartets  Temporarily out of stock034571177595
CDA67760 	LISZT: Piano Sonata034571177601
CDA67761 	MOULU: Missa Alma redemptoris & Missus est Gabriel034571177618
CDA67762 	REGER: Choral Music  Temporarily out of stock034571177625
CDA67763 	PAGANINI: 24 Caprices034571177632
CDA67764 	CHOPIN: Late Masterpieces034571177649
CDA67765 	The Romantic Piano Concerto, Vol. 51 – Taubert & Rosenhain  Temporarily out of stock034571177656
CDA67766 	MORTELMANS: Homerische symfonie & other orchestral works034571177663
CDA67767 	BACH: Piano Transcriptions, Vol. 09 – British Bach Transcriptions034571177670
CDA67768 	DOVE: Choral Music034571177687
CDA67769 	HINDEMITH: The Complete Viola Music, Vol. 2 – Solo Sonatas  Temporarily out of stock034571177694
CDA67770 	The Feast of St Peter at Westminster Abbey034571177700
CDA67771/2 	CESTI: Le disgrazie d'Amore034571177717
CDA67773 	Pushkin Romances034571177731
CDA67774 	HINDEMITH: The Complete Viola Music, Vol. 3 – Concertos034571177748
CDA67775 	BRAHMS: Zigeunerlieder034571177755
CDA67776 	Flying Horse – Music from the ML Lutebook034571177762
CDA67777 	BRAHMS: The Complete Variations  Temporarily out of stock034571177779
CDA67778 	BRITTEN: Songs & Proverbs of William Blake034571177786
CDA67779 	BYRD: Infelix ego034571177793
CDA67780 	SCHUMANN: Davidsbündlertänze, Kinderszenen, Sonata No 2  Temporarily out of stock034571177809
CDA67781 	HAYDN: String Quartets, Op. 74034571177816
CDA67782 	LISZT: The Complete Songs, Vol. 1034571177823
CDA67783 	BACEWICZ: Music for string orchestra034571177830
CDA67784 	Neapolitan Flute Concertos, Vol. 1034571177847
CDA67785 	PALESTRINA: Missa Tu es Petrus & Missa Te Deum laudamus034571177854
CDA67786 	BACH C P E: Keyboard Sonatas, Vol. 1034571177861
CDA67787 	RAUTAVAARA: Choral Music034571177878
CDA67788 	SPOHR: Symphonies Nos. 3 & 6  Temporarily out of stock034571177885
CDA67789 	HAMELIN: Études  Temporarily out of stock034571177892
CDA67790 	The Romantic Cello Concerto, Vol. 6 – Vieuxtemps  Temporarily out of stock034571177908
CDA67791 	The Romantic Piano Concerto, Vol. 52 – Goetz & Wieniawski034571177915
CDA67792 	O praise the Lord034571177922
CDA67793 	HAYDN: String Quartets, Op. 71034571177939
CDA67794 	WALTON: Symphonies034571177946
CDA67795 	MENDELSSOHN: Violin Concertos  Temporarily out of stock034571177953
CDA67796 	ESENVALDS: Passion & Resurrection & other choral music  Temporarily out of stock034571177960
CDA67797 	BEETHOVEN: Piano Sonatas, Vol. 3034571177977
CDA67798 	The Romantic Violin Concerto, Vol. 08 – Vieuxtemps 4 & 5034571177984
CDA67799 	DUBRA: Hail, Queen of Heaven & other choral works034571177991
CDA67800 	HANDEL: Messiah034571178004
CDA67801 	BRITTEN: Violin Concerto & Double Concerto034571178011
CDA67802 	SPOHR: Symphonies Nos. 8 & 10034571178028
CDA67803 	Hommage à Chopin  Temporarily out of stock034571178035
CDA67804 	The Romantic Violin Concerto, Vol. 09 – David  Temporarily out of stock034571178042
CDA67805 	DVORÁK: Piano Quintets034571178059
CDA67806 	BALAKIREV: Piano Sonata & other works034571178066
CDA67807 	ROGIER: Missa Ego sum qui sum & Motets034571178073
CDA67808 	BRIGGS: Mass for Notre Dame034571178080
CDA67809 	BUXTEHUDE: The Complete Organ Works, Vol. 2  Temporarily out of stock034571178097
CDA67810 	LISZT: New Discoveries, Vol. 3034571178103
CDA67811 	HUME: Passion & Division034571178110
CDA67812 	GÓRECKI: The Three String Quartets034571178127
CDA67813 	Echoes of Nightingales034571178134
CDA67814 	CLEMENTI: The Complete Piano Sonatas, Vol. 5  Temporarily out of stock034571178141
CDA67815 	SAINT-SAËNS: Organ Music, Vol. 2034571178158
CDA67816 	MESSIAEN: Turangalîla-Symphonie034571178165
CDA67817 	The Romantic Piano Concerto, Vol. 55 – Widor034571178172
CDA67818 	MISKINIS: Choral Music  Temporarily out of stock034571178189
CDA67819 	CLEMENTI: The Complete Piano Sonatas, Vol. 6034571178196
CDA67820 	RAVEL: Complete music for violin & piano034571178202
CDA67821/3 	MARTIN: Der Sturm034571178219
CDA67824 	GRIEG/LISZT: Piano Concertos034571178240
CDA67825 	PEETERS: Organ Music034571178257
CDA67826 	BACH/SITKOVETSKY: Goldberg Variations034571178264
CDA67827 	DALE: Piano Music034571178271
CDA67828 	The Romantic Piano Concerto, Vol. 57 – Wiklund034571178288
CDA67829 	KODÁLY: Cello Sonata & other works034571178295
CDA67830 	The Ballad Singer034571178301
CDA67831 	Casals Encores034571178318
CDA67832 	Beyond all mortal dreams034571178325
CDA67833 	SCHULHOFF: Violin Sonatas034571178332
CDA67834 	SHOSTAKOVICH: Piano Trios & Songs  Temporarily out of stock034571178349
CDA67835 	HARVEY: The Angels, Ashes Dance Back, Marahi034571178356
CDA67836 	GUERRERO: Missa Congratulamini mihi & other works034571178363
CDA67837 	The Romantic Piano Concerto, Vol. 54 – Somervell & Cowen034571178370
CDA67838 	The Romantic Violin Concerto, Vol. 10 – Cliffe & Erlanger034571178387
CDA67839 	VAUGHAN WILLIAMS/MCEWEN: Flos Campi / Viola Concerto034571178394
CDA67840 	MOZART: Piano Concertos Nos. 6, 8 & 9  Temporarily out of stock034571178400
CDA67841 	ACHRON: Complete Suites for Violin & Piano034571178417
CDA67842 	HANDEL: Finest Arias for Base Voice  Temporarily out of stock034571178424
CDA67843 	The Romantic Piano Concerto, Vol. 56 – Kalkbrenner 2 & 3034571178431
CDA67844 	STRAUSS R: The Complete Songs, Vol. 6034571178448
CDA67845 	SMETANA/SIBELIUS: String Quartets034571178455
CDA67846 	GRANADOS: Goyescas034571178462
CDA67847 	The Romantic Violin Concerto, Vol. 13 – Schumann034571178479
CDA67848 	CLEMENS: Requiem & Penitential Motets034571178486
CDA67849 	CHOPIN: The Complete Waltzes  Superseded by CDA68479034571178493
CDA67850 	CLEMENTI: Capriccios & Variations034571178509
CDA67851/2 	MEDTNER: Arabesques, Dithyrambs, Elegies034571178516
CDA67853 	HOWELLS: The Winchester Service & other late works034571178530
CDA67854 	SCHOENDORFF: The Complete Works034571178547
CDA67855 	BUXTEHUDE: The Complete Organ Works, Vol. 3034571178554
CDA67856 	LISZT: Funeral Odes034571178561
CDA67857 	ELGAR: Piano Quintet & String Quartet034571178578
CDA67858 	Music from the reign of King James I034571178585
CDA67859 	The Romantic Cello Concerto, Vol. 3 – Stanford034571178592
CDA67860 	ALLEGRI: Miserere & the music of Rome034571178608
CDA67861/3 	MOZART: String Quintets034571178615
CDA67864 	SCHUBERT: String Quintet & String Quartet D703034571178646
CDA67865 	SHOSTAKOVICH: Music for viola & piano034571178653
CDA67866 	LOEWE: Songs & Ballads034571178660
CDA67867 	MACMILLAN: Choral Music034571178677
CDA67868 	Music for Henry V & the House of Lancaster034571178684
CDA67869 	PIZZETTI/CASTELNUOVO-TEDESCO: Violin Sonatas034571178691
CDA67870 	STRAVINSKY: Complete music for piano & orchestra034571178707
CDA67871 	DOHNÁNYI: The Complete Solo Piano Music, Vol. 1034571178714
CDA67872 	FAURÉ: Cello Sonatas034571178721
CDA67873 	BACH: Piano Transcriptions, Vol. 10 – Saint-Saëns & Philipp034571178738
CDA67874 	PARSONS: Sacred Music034571178745
CDA67875 	FAURÉ: Piano Music034571178752
CDA67876 	BUXTEHUDE: The Complete Organ Works, Vol. 4034571178769
CDA67877 	HAYDN: String Quartets, Op. 20034571178776
CDA67878 	The Romantic Violin Concerto, Vol. 12 – Vieuxtemps 1 & 2034571178783
CDA67879 	BEETHOVEN: Bagatelles034571178790
CDA67880 	CHISHOLM: Piano Concertos034571178806
CDA67881 	HANSSON: Endless border & other choral works034571178813
CDA67882 	HAYDN: Piano Sonatas, Vol. 3034571178820
CDA67883 	DEBUSSY: Songs, Vol. 2034571178837
CDA67884 	Neapolitan Flute Concertos, Vol. 2034571178844
CDA67885 	SCHUMANN: Piano Concerto & Opp. 92 & 134034571178851
CDA67886 	SZYMANOWSKI: Piano Music  Temporarily out of stock034571178868
CDA67887 	LASSUS: Prophetiae Sibyllarum & Missa Amor ecco colei034571178875
CDA67888 	The Power of Love034571178882
CDA67889 	TURINA: Chamber Music034571178899
CDA67890 	Stephen Hough's French Album034571178905
CDA67891 	VICTORIA: De Beata Maria Virgine & Surge propera034571178912
CDA67892 	The Romantic Violin Concerto, Vol. 11 – Reger034571178929
CDA67893 	CHERUBINI: Arias & Overtures from Florence to Paris034571178936
CDA67894 	PORPORA: Cantatas034571178943
CDA67895 	SCRIABIN/JANÁCEK: Sonatas & Poems034571178950
CDA67896 	MUSORGSKY/PROKOFIEV: Pictures, Sarcasms & Visions034571178967
CDA67897 	BACH: Flute Sonatas034571178974
CDA67898 	DEBUSSY: Solo Piano Music034571178981
CDA67899 	HEAD: Songs  Temporarily out of stock034571178998
CDA67900 	BRAHMS: String Quintets034571179001
CDA67901/2 	BACH: St John Passion034571179018
CDA67903 	Homage to Paderewski034571179032
CDA67904 	18th-century Portuguese Love Songs  Temporarily out of stock034571179049
CDA67905 	ZAREBSKI/ZELENSKI: Piano Quintet & Piano Quartet034571179056
CDA67906 	The Romantic Cello Concerto, Vol. 4 – Pfitzner034571179063
CDA67907 	GRIFFES: Piano Music034571179070
CDA67908 	BACH C P E: Keyboard Sonatas, Vol. 2  Temporarily out of stock034571179087
CDA67909 	BINGHAM: Choral Music034571179094
CDA67910 	BLOCH/BRUCH: Schelomo, Kol Nidrei & other works  Temporarily out of stock034571179100
CDA67911/2 	SCHUBERT: Complete works for violin and piano034571179117
CDA67913 	RORE: Missa Doulce mémoire & Missa a note negre034571179131
CDA67914 	HOWELLS: Requiem & other works  Temporarily out of stock034571179148
CDA67915 	The Romantic Piano Concerto, Vol. 58 – Pixis & Thalberg034571179155
CDA67916 	BRUCKNER: Symphony No. 7034571179162
CDA67917 	DVORÁK: Cello Concertos034571179179
CDA67918 	The Romantic Piano Concerto, Vol. 65 – Albéniz & Granados034571179186
CDA67919 	MOZART: Piano Concertos Nos. 17 & 27034571179193
CDA67920 	DEBUSSY: Images & Préludes II034571179209
CDA67921 	MOZART: Missa solemnis & other works034571179216
CDA67922 	SAINT-SAËNS: Organ Music, Vol. 3034571179223
CDA67923 	SCHUMANN: Chamber Music  Temporarily out of stock034571179230
CDA67924 	Arias for Guadagni  Temporarily out of stock034571179247
CDA67925 	HAYDN: Piano Concertos Nos. 3, 4 & 11034571179254
CDA67926 	HANDEL: Chandos Anthems Nos. 5a, 6a & 8034571179261
CDA67927 	HARTY: String Quartets & Piano Quintet034571179278
CDA67928 	TYE: Missa Euge bone & Western Wynde Mass034571179285
CDA67929 	American Polyphony  Temporarily out of stock034571179292
CDA67930 	RESPIGHI: Violin Sonatas & Pieces034571179308
CDA67931 	The Romantic Piano Concerto, Vol. 60 – Dubois034571179315
CDA67932 	DOHNÁNYI: The Complete Solo Piano Music, Vol. 2034571179322
CDA67933 	MOUTON: Missa Tu es Petrus & other works034571179339
CDA67934 	LISZT: The Complete Songs, Vol. 2034571179346
CDA67935 	MENDELSSOHN: The Complete Solo Piano Music, Vol. 1034571179353
CDA67936 	MEDTNER/RACHMANINOV: Piano Sonatas034571179360
CDA67937 	BYRD: The Great Service & other English music034571179377
CDA67938 	Miserere034571179384
CDA67939 	SPOHR: Symphonies Nos. 7 & 9034571179391
CDA67940 	The Romantic Violin Concerto, Vol. 14 – Glazunov & Schoeck  Temporarily out of stock034571179407
CDA67941/2 	BRITTEN: Cello Symphony, Cello Sonata & Cello Suites034571179414
CDA67943 	PENDERECKI/LUTOSLAWSKI: String Quartets034571179438
CDA67944 	SCHUMANN: Liederkreis034571179445
CDA67945 	PHILIPS: Cantiones sacrae octonis vocibus034571179452
CDA67946 	BRITTEN: A Ceremony of Carols & Saint Nicolas034571179469
CDA67947 	SPOHR/ONSLOW: Piano Sonatas034571179476
CDA67948 	Lieux retrouvés – Music for cello & piano034571179483
CDA67949 	Conductus, Vol. 1034571179490
CDA67950 	The Romantic Piano Concerto, Vol. 61 – Döhler & Dreyschock  Temporarily out of stock034571179506
CDA67951/3 	BUSONI: Late Piano Music  Temporarily out of stock034571179513
CDA67954 	Canciones españolas034571179544
CDA67955 	HAYDN: String Quartets, Op. 33  Temporarily out of stock034571179551
CDA67956 	LISZT: The Complete Songs, Vol. 3034571179568
CDA67957 	GABRIELI G: Sacred Symphonies034571179575
CDA67958 	The Romantic Piano Concerto, Vol. 59 – Zarzycki & Zelenski034571179582
CDA67959 	RICHAFORT: Requiem & other sacred music034571179599
CDA67960 	STRAUSS R: Don Quixote & Till Eulenspiegel034571179605
CDA67961 	BRAHMS: The Piano Concertos034571179612
CDA67962 	L'heure exquise – A French Songbook034571179629
CDA67963 	MEDTNER: Violin Sonatas Nos. 1 & 3034571179636
CDA67964 	BUXTEHUDE: The Complete Organ Works, Vol. 5034571179643
CDA67965 	ARENSKY/TANEYEV: Piano Quintets034571179650
CDA67966 	TOMÁSEK: Songs  Last few remaining034571179667
CDA67967 	Piers Lane goes to town034571179674
CDA67968 	Kreek's Notebook034571179681
CDA67969 	BENJAMIN: Violin Sonatina, Viola Sonata & other works  Temporarily out of stock034571179698
CDA67970 	MacMILLAN: Tenebrae Responsories & other choral works  Temporarily out of stock034571179704
CDA67971/2 	BRIAN: Symphony No. 1 'The Gothic'034571179711
CDA67973 	Brundibár034571179735
CDA67974 	BEETHOVEN: Piano Sonatas, Vol. 4034571179742
CDA67975 	The Romantic Piano Concerto, Vol. 62 – The complete Gounod works for pedal piano034571179759
CDA67976 	JACKSON G: A ship with unfurled sails & other works034571179766
CDA67977 	HINDEMITH: Piano Sonatas034571179773
CDA67978 	PALESTRINA: Missa Ad coenam Agni & Eastertide motets034571179780
CDA67979 	HANDEL: Arias034571179797
CDA67980 	BACH: The Art of Fugue  Temporarily out of stock034571179803
CDA67981/2 	BEETHOVEN: Cello Sonatas034571179810
CDA67983 	SCHUMANN: Novelletten & Nachtstücke034571179834
CDA67984 	The Romantic Piano Concerto, Vol. 64 – Oswald & Napoleão034571179841
CDA67985 	ZEMLINSKY: Symphonies034571179858
CDA67986 	WALTON: Violin Concerto, Partita & Variations034571179865
CDA67987 	SHOSTAKOVICH: Piano Quintet & String Quartet No. 2034571179872
CDA67988 	SCRIABIN: Complete Poèmes034571179889
CDA67990 	The Romantic Violin Concerto, Vol. 15 – Mlynarski & Zarzycki  Temporarily out of stock034571179902
CDA67991/2 	BOWEN: The complete works for violin and piano034571179919
CDA67993 	YSAYE: Sonatas for solo violin034571179933
CDA67994 	TALLIS: Salve intemerata & other sacred music034571179940
CDA67995 	BACH C P E: Württemberg Sonatas034571179957
CDA67996 	In the Night  Temporarily out of stock034571179964
CDA67997 	JANÁCEK/SMETANA: String Quartets034571179971
CDA67998 	Conductus, Vol. 2034571179988
CDA67999 	KODÁLY: String Quartets, Intermezzo & Gavotte034571179995
CDA68002 	The Romantic Cello Concerto, Vol. 5 – Saint-Saëns034571280028
CDA68003 	BRIDGE: Phantasy Piano Quartet & Sonatas034571280035
CDA68004 	BRITTEN: String Quartets Nos. 1, 2 & 3034571280042
CDA68005 	The Romantic Violin Concerto, Vol. 18 – Jongen  Temporarily out of stock034571280059
CDA68006 	HINDEMITH: Symphonic Metamorphosis & other works034571280066
CDA68007 	DOWLAND: The Art of Melancholy034571280073
CDA68008 	MACHAUT: The dart of love  Temporarily out of stock034571280080
CDA68010 	SCHUBERT: Der Wanderer & other songs  Temporarily out of stock034571280103
CDA68011/2 	WILLIAMSON: The Complete Piano Concertos034571280110
CDA68013 	Rejoice, the Lord is king!  Temporarily out of stock034571280134
CDA68014 	HINDEMITH: Violin Sonatas034571280141
CDA68015 	ARENSKY: Piano Trios034571280158
CDA68016 	DEBUSSY: Songs, Vol. 3  Temporarily out of stock034571280165
CDA68017 	GALILEI V: The Well-tempered Lute034571280172
CDA68018 	RUBINSTEIN: Piano Quartets034571280189
CDA68019 	MONTEVERDI: Madrigals of Love and Loss034571280196
CDA68020 	Music for Remembrance034571280202
CDA68021/4 	POULENC: The Complete Songs034571280219
CDA68025 	ISSERLIS: Piano Music034571280257
CDA68026 	TALLIS: Puer natus est nobis & other sacred music  Temporarily out of stock034571280264
CDA68027 	DUSSEK: Piano Concertos034571280271
CDA68028 	TCHAIKOVSKY: The seasons034571280288
CDA68029 	MOZART: Piano Sonatas034571280295
CDA68030 	SCHUMANN/JANÁCEK: Waldszenen & other piano works034571280301
CDA68031/2 	BACH: Christmas Oratorio034571280318
CDA68033 	DOHNÁNYI: The Complete Solo Piano Music, Vol. 3034571280332
CDA68034 	SCHUBERT: Winterreise  Temporarily out of stock034571280349
CDA68035 	A French Baroque Diva034571280356
CDA68036 	PIERNÉ/VIERNE: Piano Quintet & String Quartet  Temporarily out of stock034571280363
CDA68037 	PROKOFIEV/SHOSTAKOVICH: Cello Concertos034571280370
CDA68038 	BYRD: The Three Masses034571280387
CDA68039 	LEIGHTON: Crucifixus & other choral music034571280394
CDA68040 	KREISLER: Violin Music034571280400
CDA68041/2 	HANDEL: The Eight Great Suites034571280417
CDA68043 	The Romantic Piano Concerto, Vol. 63 – Godard034571280431
CDA68044 	The Romantic Violin Concerto, Vol. 16 – Busoni & Strauss034571280448
CDA68045 	BACH/HANDEL/SCARLATTI: Gamba Sonatas034571280455
CDA68046 	FRANCK: Symphonic Organ Works034571280462
CDA68047 	Hymns to Saint Cecilia034571280479
CDA68048 	FELDMAN: For Bunita Marcus034571280486
CDA68049 	MOZART: Piano Concertos Nos. 22 & 24  Temporarily out of stock034571280493
CDA68050 	The Romantic Violin Concerto, Vol. 17 – Bruch 3034571280509
CDA68051/2 	BACH: Mass in B minor  Temporarily out of stock034571280516
CDA68053 	Amorosi pensieri034571280530
CDA68054 	DOHNÁNYI: The Complete Solo Piano Music, Vol. 4034571280547
CDA68055 	The Romantic Violin Concerto, Vol. 21 – Bruch 2034571280554
CDA68056 	PÄRT: Choral Music  Temporarily out of stock034571280561
CDA68057 	REGER: Songs034571280578
CDA68058 	Canticles from St Paul's034571280585
CDA68059 	MENDELSSOHN: The Complete Solo Piano Music, Vol. 2034571280592
CDA68060 	The Romantic Violin Concerto, Vol. 19 – Bruch 1034571280608
CDA68061 	FRANCK/DEBUSSY: Piano Quintet & String Quartet034571280615
CDA68062 	SMETANA: Czech Dances & On the seashore034571280622
CDA68063 	The Romantic Cello Concerto, Vol. 7 – Fitzenhagen034571280639
CDA68064 	LASSUS: Missa super Dixit Joseph & motets034571280646
CDA68065 	BRUMEL: Missa de beata virgine & motets  Temporarily out of stock034571280653
CDA68066 	The Romantic Piano Concerto, Vol. 67 – Rozycki034571280660
CDA68067 	LISZT: Piano Sonatas & Sonnets034571280677
CDA68068 	BACH: Violin Concertos034571280684
CDA68069 	COMPÈRE: Magnificat, motets & chansons034571280691
CDA68070 	GRIEG: Lyric Pieces  Temporarily out of stock034571280707
CDA68071/2 	RAMEAU: Pièces de clavecin034571280714
CDA68073 	BEETHOVEN: Piano Sonatas Opp. 90, 101 & 106034571280738
CDA68074 	STRAUSS R: The Complete Songs, Vol. 7  Temporarily out of stock034571280745
CDA68075 	DEBUSSY: Songs, Vol. 4034571280752
CDA68076 	TALLIS: Ave, rosa sine spinis & other sacred music  Temporarily out of stock034571280769
CDA68077 	ELGAR/WALTON: Cello Concertos034571280776
CDA68078 	Arias for Benucci034571280783
CDA68079 	MENDELSSOHN/GRIEG/HOUGH: Cello Sonatas034571280790
CDA68080 	DEBUSSY/BARTÓK/PROKOFIEV: Études034571280806
CDA68081/2 	SCHOENBERG: Gurre-Lieder034571280813
CDA68083 	ESENVALDS: Northern Lights & other choral works  Temporarily out of stock034571280837
CDA68084 	ORNSTEIN: Piano Quintet & String Quartet No. 2034571280844
CDA68085 	SZYMANSKI/MYKIETYN: Music for string quartet034571280851
CDA68086 	BEETHOVEN: Piano Sonatas, Opp. 2/2, 10/1, 78 & 110034571280868
CDA68087 	Yulefest!034571280875
CDA68088 	JACQUET OF MANTUA: Missa Surge Petre & motets  Temporarily out of stock034571280882
CDA68089 	PARRY: I was glad & other choral works034571280899
CDA68090 	MOZART/HAYDN: Concertos & Sinfonia concertante034571280905
CDA68091 	MOZART: Violin Sonatas, K301 304 379 & 481034571280912
CDA68092 	MOZART: Violin Sonatas, K305, 376 & 402034571280929
CDA68093 	COUPERIN: L'Apothéose de Lully & Leçons de ténèbres034571280936
CDA68094 	Herrmann, Gershwin, Waxman & Copland034571280943
CDA68095 	TALLIS: Ave, Dei patris filia & other sacred music034571280950
CDA68096 	VAUGHAN WILLIAMS/HOUGH: Dona nobis pacem & Missa Mirabilis  Temporarily out of stock034571280967
CDA68097 	MOZART: Horn Concertos  Temporarily out of stock034571280974
CDA68098 	MENDELSSOHN: The Complete Solo Piano Music, Vol. 3034571280981
CDA68099 	SCHUMANN/DVORÁK: Piano Concertos034571280998
CDA68100 	The Romantic Piano Concerto, Vol. 66 – Herz 2034571281001
CDA68101 	ELGAR: Enigma Variations & other orchestral works034571281018
CDA68102 	The Romantic Violin Concerto, Vol. 20 – Stojowski & Wieniawski  Temporarily out of stock034571281025
CDA68103 	MACHAUT: A burning heart  Temporarily out of stock034571281032
CDA68104 	STEIBELT: Piano Concertos034571281049
CDA68105 	HOWELLS: Collegium Regale & other choral music034571281056
CDA68106 	LOBO: Lamentations & other sacred music  Temporarily out of stock034571281063
CDA68107 	SCHUBERT: Impromptus, Piano Pieces & Variations034571281070
CDA68108 	FELDMAN/CRUMB: Palais de Mari & A Little Suite for Christmas034571281087
CDA68109 	The Romantic Piano Concerto, Vol. 68034571281094
CDA68110 	CLAUSEN/PAULUS: Calm on the listening ear & other choral work034571281100
CDA68111 	BACH: Cantatas Nos 54, 82 & 170034571281117
CDA68112 	BACH C P E: Cello Concertos034571281124
CDA68113 	LALO: Piano Trios034571281131
CDA68114 	Brazilian Adventures034571281148
CDA68115 	Conductus, Vol. 3034571281155
CDA68116 	BRAHMS: The Final Piano Pieces034571281162
CDA68117 	LISZT: The Complete Songs, Vol. 4034571281179
CDA68118 	BORTKIEWICZ: Piano Sonata No. 2 & other works034571281186
CDA68119 	REUBKE: Sonatas034571281193
CDA68120 	BRUCH: Piano Quintet & other works034571281209
CDA68121 	TALLIS: Lamentations & other sacred music034571281216
CDA68122 	HAYDN: String Quartets, Op. 50  Temporarily out of stock034571281223
CDA68123 	BARTÓK: Mikrokosmos 6 & other piano music034571281230
CDA68124 	ROZYCKI/FRIEDMAN: Piano Quintets034571281247
CDA68125 	MENDELSSOHN: The Complete Solo Piano Music, Vol. 4034571281254
CDA68126 	MOZART F/CLEMENTI: Piano Concertos034571281261
CDA68128 	FRANZ: Songs034571281285
CDA68129 	Power of Life034571281292
CDA68130 	The Romantic Piano Concerto, Vol. 70 – Beach, Howell & Chaminade034571281308
CDA68131 	BEETHOVEN: Piano Sonatas, Op. 14/1, 31/1, 49/1&2 & 81a034571281315
CDA68132 	Beneath the northern star – The rise of English polyphony, 1270-1430034571281322
CDA68133 	BARTÓK: Mikrokosmos 5 & other piano music034571281339
CDA68134 	MACHAUT: Sovereign Beauty034571281346
CDA68135 	The Romantic Piano Concerto, Vol. 69 – Hill & Boyle034571281353
CDA68136 	Rostropovich Encores034571281360
CDA68137 	CHOPIN: Mazurkas034571281377
CDA68138 	The Romantic Piano Concerto, Vol. 71 – Czerny034571281384
CDA68139 	DEBUSSY: Piano Music034571281391
CDA68140 	English Romantic Madrigals034571281407
CDA68141 	RIBERA: Magnificats & Motets034571281414
CDA68141D 	RIBERA: Magnificat quartus tonus I034571100975
CDA68142 	DVORÁK: String Quartet & String Quintet034571281421
CDA68143 	MOZART: Violin Sonatas, K296, 306, 454 & 547  Temporarily out of stock034571281438
CDA68144 	ROTH: A Time to Dance & other choral works034571281445
CDA68145 	MEDTNER/RACHMANINOV: Piano Concertos034571281452
CDA68146 	BACH: Goldberg Variations  Temporarily out of stock034571281469
CDA68147 	TAVERNER: Mater Christi sanctissima & Western Wynde034571281476
CDA68148 	RAVEL/FALLA: Piano Concertos034571281483
CDA68149 	BLOW: An Ode on the Death of Mr Henry Purcell034571281490
CDA68150 	LA RUE: Missa Nuncqua fue pena & Missa Inviolata  Temporarily out of stock034571281506
CDA68151 	The Romantic Piano Concerto, Vol. 72 – Potter034571281513
CDA68152 	HANDEL: Finest Arias for Base Voice, Vol. 2034571281520
CDA68153 	BARTÓK: Sonata for two pianos & percussion034571281537
CDA68154 	KOZELUCH: Piano Concertos Nos. 1, 5 & 6034571281544
CDA68155 	BLOCH/LIGETI/DALLAPICCOLA: Solo Cello Suites034571281551
CDA68156 	TALLIS: Spem in alium & other sacred music034571281568
CDA68157 	BACH: Magnificats034571281575
CDA68158 	KRENEK: Reisebuch aus den österreichischen Alpen034571281582
CDA68159 	TANEYEV/RIMSKY KORSAKOV: Piano Trios  Temporarily out of stock034571281599
CDA68160 	HAYDN: String Quartets, Op. 54 & 55034571281605
CDA68161 	DEBUSSY: Piano Music034571281612
CDA68162 	HAYDN/BACH C P E: Cello Concertos  Temporarily out of stock034571281629
CDA68163 	Piers Lane goes to town again034571281636
CDA68164 	MOZART: Violin Sonatas, K303, 377, 378 & 403  Temporarily out of stock034571281643
CDA68165 	Fin de siècle  Temporarily out of stock034571281650
CDA68166 	BORODIN: Piano Quintet & String Quartet No. 2034571281667
CDA68167 	FINZI/BAX/IRELAND: Choral Music034571281674
CDA68168 	BRUCH: String Quintets & Octet034571281681
CDA68169 	SCHUBERT: 21 Songs034571281698
CDA68170 	Music for the Hundred Years' War  Temporarily out of stock034571281704
CDA68171 	CHARPENTIER: Leçons de ténèbres, Litanies & Magnificat034571281711
CDA68172 	SWANN: Songs  Temporarily out of stock034571281728
CDA68173 	The Romantic Piano Concerto, Vol. 73 – Coke034571281735
CDA68174 	STANFORD: Choral Music034571281742
CDA68175 	MOZART: Violin Sonatas, K302, 380 & 526  Temporarily out of stock034571281759
CDA68176 	Stephen Hough's Dream Album034571281766
CDA68177 	FALLA: Fantasia Baetica & other piano music034571281773
CDA68178 	The Romantic Piano Concerto, Vol. 74 – Bennett 1-3034571281780
CDA68179 	LISZT: The Complete Songs, Vol. 5  Temporarily out of stock034571281797
CDA68180 	GUYOT: Te Deum laudamus & motets034571281803
CDA68181/2 	BACH: Mass in B minor  Temporarily out of stock034571281810
CDA68183 	STANFORD: Preludes034571281834
CDA68184 	SCARLATTI: Sonatas, Vol. 2  Temporarily out of stock034571281841
CDA68185 	STRAUSS R: The Complete Songs, Vol. 8034571281858
CDA68186 	SCHUMANN: Davidsbündlertänze, Humoreske & Blumenstück034571281865
CDA68187 	SHEPPARD: Media vita & other sacred choral music034571281872
CDA68188 	RACHMANINOV: Études-tableaux034571281889
CDA68189 	STRAVINSKY: Music for two pianos four hands034571281896
CDA68190 	VAUGHAN WILLIAMS: A London Symphony & other works034571281902
CDA68191 	PARK: Choral works034571281919
CDA68192 	LUDFORD: Missa Videte miraculum & Ave Maria, ancilla034571281926
CDA68193 	BERLIOZ: Harold in Italy & other orchestral works  Temporarily out of stock034571281933
CDA68194 	CHOPIN: Préludes, Piano Sonata No. 2 & Scherzo No. 2034571281940
CDA68195 	MACHAUT: Fortune's Child034571281957
CDA68196 	MacMILLAN: String Quartets034571281964
CDA68197 	SCHUBERT: Winterreise034571281971
CDA68198 	SUK: Piano Music  Temporarily out of stock034571281988
CDA68199 	BEETHOVEN: Piano Sonatas, Op. 27/1, 31/2, 79 & 109034571281995
CDA68200 	BRAHMS: Violin Sonatas034571282008
CDA68201 	SAINT-SAËNS: Symphony No. 3 & other works034571282015
CDA68202 	LISZT: Années de pèlerinage, troisième année  Temporarily out of stock034571282022
CDA68203 	TIPPETT: Symphonies Nos. 1 & 2034571282039
CDA68204 	VIERNE/FRANCK: Violin Sonatas034571282046
CDA68205 	NENOV: Piano Concerto & Ballade No. 2034571282053
CDA68206 	MACHAUT: The gentle physician  Temporarily out of stock034571282060
CDA68207 	PIXIS: Piano Trios034571282077
CDA68208 	CHISHOLM: Violin Concerto & Dance Suite034571282084
CDA68209 	FAURÉ: Requiem & other sacred music034571282091
CDA68210 	PALESTRINA: Missa Confitebor tibi Domine & other works034571282107
CDA68211 	DUSSEK: Piano Concertos, Op. 3, 14 & 49034571282114
CDA68212 	SAINT-SAËNS: Symphony No. 2, Danse macabre & Urbs Roma034571282121
CDA68213 	SCHUBERT: Piano Sonata & Impromptus034571282138
CDA68214 	Organ Fireworks World Tour034571282145
CDA68215 	DOHNÁNYI: String Quartet, Serenade & Sextet034571282152
CDA68216 	OBRECHT: Missa Grecorum & motets034571282169
CDA68217 	The Romantic Piano Concerto, Vol. 75 – Ries034571282176
CDA68219 	BEETHOVEN: Piano Sonatas, Opp. 109, 110 & 111034571282190
CDA68220 	BEETHOVEN: Piano Sonatas, Opp. 2/1, 14/2, 53 & 54034571282206
CDA68221 	HAYDN: String Quartets, Op. 64034571282213
CDA68222 	FINZI: Choral works034571282220
CDA68223 	SAINT-SAËNS: Symphony No. 1 & Carnival of the animals034571282237
CDA68224 	COUPERIN: Dances from the Bauyn Manuscript034571282244
CDA68225 	The Romantic Piano Concerto, Vol. 76 – Rheinberger & Scholz034571282251
CDA68226 	BRAHMS: Late Piano Works034571282268
CDA68227 	CHOPIN/SCHUBERT: Cello & Arpeggione Sonatas034571282275
CDA68228 	The Lily & the Rose034571282282
CDA68229 	The Romantic Piano Concerto, Vol. 77 – Bronsart & Urspruch034571282299
CDA68230 	HAYDN: String Quartets, Op. 71 & 74034571282305
CDA68231/2 	TIPPETT: Symphonies Nos. 3, 4 & B flat  Temporarily out of stock034571282312
CDA68233 	FEINBERG: Piano Sonatas Nos. 1-6034571282336
CDA68234 	MOZART: The Jupiter Project  Temporarily out of stock034571282343
CDA68235 	LISZT: The Complete Songs, Vol. 6034571282350
CDA68236 	DUFAY: Lament for Constantinople & other songs034571282367
CDA68237 	BEETHOVEN: Moonlight Sonata & other piano music034571282374
CDA68238 	DOHNÁNYI: Piano Quintets & String Quartet No. 2034571282381
CDA68239 	SHOSTAKOVICH/KABALEVSKY: Cello Sonatas034571282398
CDA68240 	The Romantic Piano Concerto, Vol. 78 – Clara Schumann, Kalkbrenner, Herz & Hiller034571282404
CDA68241 	CLEVE: Missa Rex Babylonis & other works034571282411
CDA68242 	BRAHMS: Ein deutsches Requiem034571282428
CDA68243 	PARRY: Piano Trios Nos. 1 & 3034571282435
CDA68244 	BACH: The Toccatas034571282442
CDA68245 	VAUGHAN WILLIAMS: A Sea Symphony034571282459
CDA68246 	TAVENER: No longer mourn for me & other cello music034571282466
CDA68247 	LISZT: New Discoveries, Vol. 4  Temporarily out of stock034571282473
CDA68248 	SIBELIUS: Kullervo034571282480
CDA68249 	The Passinge mesures  Temporarily out of stock034571282497
CDA68250 	TALLIS: The Votive Antiphons034571282503
CDA68251 	McDOWALL: Sacred choral music034571282510
CDA68252 	CARDOSO: Requiem, Lamentations, Magnificat & motets034571282527
CDA68253 	BRIDGE/CLARKE: Cello Sonatas  Temporarily out of stock034571282534
CDA68254 	ELGAR: Caractacus034571282541
CDA68255 	TAVENER: Angels & other choral works034571282558
CDA68256 	English Motets  Temporarily out of stock034571282565
CDA68257 	VIVANCO: Missa Assumpsit Jesus & motets034571282572
CDA68258 	The Romantic Piano Concerto, Vol. 79 – Pfitzner & Braunfels034571282589
CDA68259 	BAIRSTOW/HARRIS/STANFORD: Choral works034571282596
CDA68260 	Vida breve034571282602
CDA68261/2 	BACH: The Cello Suites034571282619
CDA68263 	STRAUSS R/BEETHOVEN/GLINKA: The Princess & the Bear034571282633
CDA68264 	The Romantic Piano Concerto, Vol. 80 – Dupont & Benoit034571282640
CDA68265 	FÉVIN: Missa Ave Maria & Missa Salve sancta parens034571282657
CDA68266 	MÄNTYJÄRVI: Choral music034571282664
CDA68267 	SHOSTAKOVICH: Piano Sonatas & Preludes034571282671
CDA68268 	The Romantic Violin Concerto, Vol. 22 – Lassen, Philipp Scharwenka & Langgaard034571282688
CDA68269 	NICODÉ: Ein Liebesleben & other piano works034571282695
CDA68270 	CRAMER: Piano Concertos Nos. 4 & 5034571282701
CDA68271/2 	BACH: The Six Partitas (2018 recording)  Temporarily out of stock034571282718
CDA68273 	CHOPIN: Impromptus, waltzes & mazurkas034571282732
CDA68274 	Music for Saint Katherine of Alexandria034571282749
CDA68275 	BACH: Cantatas Nos. 106 & 182034571282756
CDA68276 	PARRY: Piano Trio No. 2 & Piano Quartet034571282763
CDA68277 	MACHAUT: The single rose  Temporarily out of stock034571282770
CDA68279 	Amarae morti034571282794
CDA68280 	VAUGHAN WILLIAMS: Symphonies Nos. 3 & 4034571282800
CDA68281 	Christmas at St George's Windsor034571282817
CDA68282 	JANÁCEK: Diary of one who disappeared & other songs034571282824
CDA68283 	STANFORD: A Song of Agincourt & other works  Temporarily out of stock034571282831
CDA68284 	PALESTRINA: Lamentations  Temporarily out of stock034571282848
CDA68285 	Fading034571282855
CDA68286 	LIGETI: The 18 Études034571282862
CDA68287 	Musique?034571282879
CDA68288 	SCHUBERT/BRAHMS: Schwanengesang & Vier ernste Gesänge  Temporarily out of stock034571282886
CDA68289 	The Early Horn034571282893
CDA68290 	KORNGOLD/BARTÓK: Piano Quintets034571282909
CDA68291/3 	BEETHOVEN: The Piano Concertos034571282916
CDA68294 	HOWELLS: Missa Sabrinensis & Michael Fanfare034571282947
CDA68295 	ELGAR/BEACH: Piano Quintets034571282954
CDA68296 	DUNHILL/ERLANGER: Piano Quintets034571282961
CDA68297 	The Romantic Piano Concerto, Vol. 81 – Rubbra & Bliss034571282978
CDA68298 	PROKOFIEV: Piano Sonatas Nos. 6, 7 & 8034571282985
CDA68299 	Christmas034571282992
CDA68301 	PARRY: Songs of farewell & wks by Stanford/Gray/Wood034571283012
CDA68302 	CRAMER: Piano Concertos Nos. 1, 3 & 6034571283029
CDA68303 	BOWEN: Fragments from Hans Andersen & Studies034571283036
CDA68304 	HELLINCK/LUPI: Missa Surrexit pastor, Te Deum & motets034571283043
CDA68305 	LITOLFF: Piano Trios034571283050
CDA68306 	LOBO: Masses, Responsories & motets034571283067
CDA68307 	MENDELSSOHN F/SCHUMANN C: Piano Trios & String Quartet034571283074
CDA68308 	HAMELIN: New Piano Works034571283081
CDA68309 	RACHMANINOV: Songs034571283098
CDA68310 	Homage to Godowsky034571283104
CDA68311/2 	BACH: The Six Partitas034571283111
CDA68313 	SHOSTAKOVICH: Violin Concertos034571283135
CDA68314 	New England Choirworks034571283142
CDA68315 	SCHÜTZ: The Christmas story & other works034571283159
CDA68316 	MESSIAEN: Des canyons aux étoiles ...034571283166
CDA68317 	MacMILLAN: Symphony No. 4 & Viola Concerto034571283173
CDA68318 	MACHAUT: The lion of nobility034571283180
CDA68319 	The Romantic Piano Concerto, Vol. 82 – Elmas034571283197
CDA68320 	LISZT/THALBERG: Opera transcriptions & fantasies034571283203
CDA68321 	JOSQUIN: Motets & Mass movements  Temporarily out of stock034571283210
CDA68322 	MENDELSSOHN: Violin Sonatas034571283227
CDA68323 	The Romantic Piano Concerto, Vol. 83 – Gablenz & Paderewski034571283234
CDA68324 	BERLIOZ: Symphonie fantastique & other works034571283241
CDA68325 	VAUGHAN WILLIAMS: Symphony No. 5 & The Pilgrim's Progress034571283258
CDA68326 	ESQUIVEL: Missa Hortus conclusus, Magnificat & motets034571283265
CDA68327 	VLADIGEROV: Exotic preludes & Impressions  Temporarily out of stock034571283272
CDA68328 	JANCEVSKIS: Choral works034571283289
CDA68329 	French duets034571283296
CDA68330 	MENDELSSOHN/MENDELSSOHN: String Quartets034571283302
CDA68331/2 	FAURÉ: Nocturnes & Barcarolles034571283319
CDA68333 	Music for the King of Scots034571283333
CDA68334 	BRAHMS: Piano Sonatas & Rhapsodies034571283340
CDA68335 	HAYDN: String Quartets, Op. 76034571283357
CDA68336 	BACH: Italian Concerto & French Overture034571283364
CDA68337 	ISAAC: Missa Wohlauff gut Gsell & other works  Temporarily out of stock034571283371
CDA68338 	BACH: Goldberg Variations034571283388
CDA68339 	The Romantic Piano Concerto, Vol. 85 – Reinecke034571283395
CDA68340 	SHOSTAKOVICH: Cello Concertos  Temporarily out of stock034571283401
CDA68341 	Love songs  Temporarily out of stock034571283418
CDA68342 	BARGIEL: Piano Trios Nos. 1 & 2034571283425
CDA68343 	BRUCH: Piano Trio & other chamber music034571283432
CDA68344 	MENDELSSOHN: The Complete Solo Piano Music, Vol. 5034571283449
CDA68345 	The Romantic Piano Concerto, Vol. 86 – Tellefsen034571283456
CDA68346 	BEETHOVEN: Variations034571283463
CDA68347 	GUERRERO: Magnificat, Lamentations & Canciones034571283470
CDA68348 	GESUALDO: Tenebrae Responsories for Maundy Thursday  Temporarily out of stock034571283487
CDA68349 	The Florentine Renaissance034571283494
CDA68350 	DOVE/WEIR/MARTIN: Choral works034571283500
CDA68351/2 	CHOPIN: Nocturnes034571283517
CDA68354 	SCHUMANN: Violin Sonatas034571283548
CDA68355 	SCRIABIN: Mazurkas034571283555
CDA68357 	VIVALDI/PIAZZOLLA: The mandolin seasons034571283579
CDA68358 	Sacred treasures of Christmas034571283586
CDA68359 	Sacred treasures of Spain034571283593
CDA68361 	BENDA: Piano Concertos034571283616
CDA68362 	MOMPOU: Música callada034571283623
CDA68363 	SCHUMANN: Arabeske, Kreisleriana & Fantasie034571283630
CDA68364 	HAYDN: String Quartets, Op. 42, 77 & 103034571283647
CDA68365 	RACHMANINOV: Piano Sonata No. 1 & Moments musicaux034571283654
CDA68366 	PAGANINI: 24 Caprices  Temporarily out of stock034571283661
CDA68367 	MOZART: The complete multipiano concertos034571283678
CDA68368 	MENDELSSOHN: The Complete Solo Piano Music, Vol. 6034571283685
CDA68369 	REGNART: Missa Christ ist erstanden & other works034571283692
CDA68370 	SCHUBERT: Piano Sonatas, D664, 769a & 894034571283708
CDA68371/2 	Voyage of a sea-god034571283715
CDA68373 	British solo cello music034571283739
CDA68374 	BEETHOVEN: Piano Sonatas, Op. 106 & 111034571283746
CDA68375 	BACH: Cantatas Nos 35 & 169034571283753
CDA68376 	Northern Lights  Temporarily out of stock034571283760
CDA68377 	SCHUBERT: Die schöne Müllerin  Temporarily out of stock034571283777
CDA68378 	VAUGHAN WILLIAMS: On Wenlock Edge & other songs034571283784
CDA68379 	Josquin's legacy034571283791
CDA68380 	RIES: Piano Trio & Sextets034571283807
CDA68381/2 	BACH C P E: Sonatas & Rondos034571283814
CDA68383 	HAHN: Poèmes & Valses034571283838
CDA68384 	TELEMANN: Fantasias for solo violin034571283845
CDA68385 	MOUTON: Missa Faulte d'argent & Motets034571283852
CDA68387 	BACH: Notebooks for Anna Magdalena034571283876
CDA68388 	Lux aeterna  Temporarily out of stock034571283883
CDA68389 	The Romantic Piano Concerto, Vol. 84 – Schmitt034571283890
CDA68390 	DEBUSSY: Early and late piano pieces034571283906
CDA68391/2 	BOLCOM: The complete rags034571283913
CDA68393 	CRISTO: Magnificat, Antiphons & Missa Salve regina034571283937
CDA68394 	A Golden Cello Decade, 1878-1888034571283944
CDA68396 	VAUGHAN WILLIAMS: Symphonies Nos. 6 & 8034571283968
CDA68397 	MARTINU/KRÁSA/KALABIS: Harpsichord Concertos034571283975
CDA68398 	SCHUBERT: Piano Sonatas D537 & 959034571283982
CDA68399 	MACHAUT: Songs from Remede de Fortune034571283999
CDA68400 	HOUGH/DUTILLEUX/RAVEL: String Quartets034571284002
CDA68401/2 	BACH: The French Suites034571284019
CDA68403 	MAGALHÃES: Missa Veni Domine & Missa Vere Dominus est034571284033
CDA68404 	Morning star034571284040
CDA68405 	VAUGHAN WILLIAMS: Sinfonia antartica & Symphony No. 9034571284057
CDA68406 	TCHAIKOVSKY/KORNGOLD: String Sextets034571284064
CDA68407 	PADOVANO: Missa A la dolc' ombra & Domine a lingua034571284071
CDA68408 	GUERRERO: Missa Ecce sacerdos, Magnificat & motets034571284088
CDA68409 	DEBUSSY: Études & Pour le piano034571284095
CDA68410 	HAYDN: String Quartets, Op. 42 & 77 & Last Words034571284101
CDA68411/2 	MOZART: Piano Sonatas, K279-284 & K309  Temporarily out of stock034571284118
CDA68413 	DVORÁK/COLERIDGE-TAYLOR: String Quartet & Fantasiestücke034571284132
CDA68414 	DASER: Missa Pater noster & other works034571284149
CDA68415 	MORALES: Missa Mille regretz & Missa Desilde al cavall034571284156
CDA68416 	BYRD: Mass for five voices & other works  Temporarily out of stock034571284163
CDA68417 	MACHAUT: The fount of grace034571284170
CDA68418 	STANFORD: Requiem034571284187
CDA68419 	Phantasy in blue034571284194
CDA68420 	VAUGHAN WILLIAMS/MACMILLAN/TAVENER: Choral works034571284200
CDA68421/2 	MOZART: Piano Sonatas, K310-311 & 330-333  Temporarily out of stock034571284217
CDA68423 	SCHUBERT: String Quartets D112 & 887034571284231
CDA68424 	GRIEG: Holberg Suite, Ballade & Lyric Pieces034571284248
CDA68425 	ANTOGNINI: Come to me in the silence of the night034571284255
CDA68426 	Credo034571284262
CDA68427 	Sacred treasures of Venice034571284279
CDA68428 	Russian Variations034571284286
CDA68429 	The Romantic Piano Concerto, Vol. 87 – Reinecke 3 & Sauer 2034571284293
CDA68430 	MACHAUT: A lover's death034571284309
CDA68431/2 	MOZART: Piano Sonatas, K457, 533, 545, 570 & 576  NEW034571284316
CDA68433 	DVORÁK/PRICE: Piano Quintets034571284330
CDA68434 	Anthems, Vol. 1034571284347
CDA68435 	Sacred treasures of Rome  July 2025 release034571284354
CDA68436 	DURUFLÉ/POULENC: Requiem & Lenten Motets034571284361
CDA68437 	SCHUBERT: Piano Sonata & Moments musicaux  July 2025 release034571284378
CDA68439 	LA HÈLE: Missa Praeter rerum seriem034571284392
CDA68440 	BRIGGS: Hail, gladdening Light & other works034571284408
CDA68441 	Honey-coloured cow034571284415
CDA68444 	BOCCHERINI: Cello Concertos, Sonatas & Quintets034571284446
CDA68445 	Reformation – Keyboard words by Byrd, Gibbons & Bull  Temporarily out of stock034571284453
CDA68447 	A monk's life034571284477
CDA68448 	BACH: Preludes, Inventions & Sinfonias034571284484
CDA68450 	FAURÉ: La bonne chanson & other songs034571284507
CDA68451/2 	BACH: The Well-tempered Clavier I  September 2025 release034571284514
CDA68453 	Queen of Hearts034571284538
CDA68455 	HOUGH: Piano Concerto, Sonatina & Partita  Temporarily out of stock034571284552
CDA68456 	BEETHOVEN: Hammerklavier034571284569
CDA68458 	Rare Italian Piano Concertos034571284583
CDA68459 	Unplayed Stories … in 40 Fingers034571284590
CDA68460 	OBRECHT: Scaramella  Temporarily out of stock034571284606
CDA68463 	DEBUSSY: String Quartet & Sonatas034571284637
CDA68464 	BRIAN: Agamemnon & Symphonies Nos. 6 & 12034571284644
CDA68465 	Radiant Dawn  August 2025 release034571284651
CDA68466 	WEIR/BEACH: In the Land of Uz & The Canticle of the Sun  NEW034571284668
CDA68467 	MORALES: Requiem a 5 & Officium defunctorum  September 2025 release034571284675
CDA68468D 	NGWENYAMA: Flow034571284682
CDA68474 	KALABIS: Duettina, Chamber music & Diptych034571284743
CDA68475 	Swans  August 2025 release034571284750
CDA68479 	CHOPIN: The Complete Waltzes  Temporarily out of stockPreviously issued on CDA67849034571284798
CDD22001 	BACH: Brandenburg ConcertosPreviously issued on CDA66711/2034571120010
CDD22002 	BACH: Four Orchestral SuitesPreviously issued on CDA66701/2034571120027
CDD22003 	BARTÓK: Complete String QuartetsPreviously issued on CDA66581/2034571120034
CDD22004 	BEETHOVEN: Complete Cello MusicPreviously issued on CDA66281, CDA66282034571120041
CDD22005 	MOZART: String Quintets  Temporarily out of stockPreviously issued on CDA66431, CDA66432034571120058
CDD22006 	REICHA: Wind QuintetsPreviously issued on CDA66268, CDA66379034571120065
CDD22007 	RUBINSTEIN: Complete Piano SonatasPreviously issued on CDA66017, CDA66105034571120072
CDD22008 	Hummel, Schubert & Schumann  DeletedPreviously issued on CDH88010, CDA66657034571120089
CDD22009 	BACH: Sonatas & Partitas for solo violin034571120096
CDD22010 	SCHUBERT: The Songmakers' Almanac SchubertiadePreviously issued on A66131/2034571120102
CDD22011 	CORELLI: Concerti Grossi, Op. 6  Superseded by CDA66741/2034571120119
CDD22013 	CHOPIN: Nocturnes  Superseded by CDA66341/2034571120133
CDD22014 	SPOHR: Four Double QuartetsPreviously issued on CDA66141, CDA66142034571120140
CDD22015 	STRAUSS R: Complete Music for Winds  Superseded by CDA66731/2034571120157
CDD22017 	The Clarinet in ConcertPreviously issued on CDA66022, CDA66300034571120171
CDD22018 	BRAHMS: String Quartets & Piano QuintetPreviously issued on CDA66651, CDA66652034571120188
CDD22019 	HANDEL: Messiah  Superseded by CDA66251/2034571120195
CDD22020 	MENDELSSOHN: Songs without wordsPreviously issued on CDA66221/2034571120201
CDD22021 	SHEPPARD: Cantate Mass  Superseded by CDS44401/10034571120218
CDD22022 	SHEPPARD: Western Wynde Mass  Superseded by CDS44401/10034571120225
CDD22023 	RUBINSTEIN: Solo Piano Music034571120232
CDD22024 	Nikolai Demidenko LivePreviously issued on CDA66781/2034571120249
CDD22025 	BACH: Sonatas for violin & harpsichord034571120256
CDD22026 	War's Embers  Superseded by CDA66261/2034571120263
CDD22027 	English Music for ClarinetPreviously issued on CDA66014, CDA66044034571120270
CDD22028 	MONTEVERDI: Vespers  Superseded by CDA66311/2034571120287
CDD22029 	MENDELSSOHN: Music for OrganPreviously issued on CDA66491/2034571120294
CDD22030 	BALAKIREV: Symphonies & Symphonic PoemsPreviously issued on CDA66691/2034571120300
CDD22038 	HOWELLS: St Paul's Service & other music  Superseded by CDA66260034571120386
CDD22039 	MARTINU: Chamber MusicPreviously issued on CDA66084, 66133, 66473034571120393
CDD22040 	BOUGHTON: The Immortal HourPreviously issued on CDA66101/2034571120409
CDD22041 	BACH: Wedding Cantata & Hunt CantataPreviously issued on CDA66036034571120416
CDD22042 	BRITTEN: Complete Folk Song Arrangements  Superseded by CDA66941/2034571120423
CDD22043 	BERWALD: Symphonies & OverturesPreviously issued on CDA67081/2034571120430
CDD22044 	A Shropshire LadPreviously issued on CDA66471/2034571120447
CDD22045 	HANDEL: Harpsichord SuitesPreviously issued on CDA66931/2034571120454
CDD22046 	SCHARWENKA: Complete Chamber Music034571120461
CDD22047 	CORELLI: Twelve Violin SonatasPreviously issued on CDA66381/2034571120478
CDD22048 	ALBINONI: Sonate & Trattenimenti  Temporarily out of stockPreviously issued on CDA66831/2034571120485
CDD22049 	VAUGHAN WILLIAMS: Hugh the Drover  Temporarily out of stockPreviously issued on CDA66901/2034571120492
CDD22050 	HANDEL: The Triumph of Time & TruthPreviously issued on CDA66071/2034571120508
CDD22051 	BACH: Mass in B minorPreviously issued on CDA67201/2034571120515
CDD22052 	HANDEL: Organ Concertos  Superseded by CDA67291/2034571120522
CDD22053 	BERWALD: Chamber MusicPreviously issued on CDA66834, CDA66835034571120539
CDD22054 	BORTKIEWICZ: Piano MusicPreviously issued on CDA66933, CDA67094034571120546
CDD22055 	BLOW: AnthemsPreviously issued on CDA67031/2034571120553
CDD22056 	LASSUS: Penitential PsalmsPreviously issued on CDA67271/2034571120560
CDD22057 	LOCATELLI: Sonatas, Op. 8Previously issued on CDA67021/2034571120577
CDD22058 	BRITTEN: Complete Purcell RealizationsPreviously issued on CDA67061/2034571120584
CDD22059 	DUPRÉ: Organ MusicPreviously issued on CDA66205, CDA67047034571120591
CDD22060 	AVISON: Concerti Grossi after ScarlattiPreviously issued on CDA66891/2034571120607
CDD22061 	TARTINI: The Devil's Trill & other violin sonatasPreviously issued on CDA66430, CDA66485034571120614
CDD22062 	BACH: Great Fantasias, Preludes & FuguesPreviously issued on CDA66791/2034571120621
CDD22063 	BOYCE: Trio SonatasPreviously issued on CDA67151/2034571120638
CDD22064 	LOCATELLI: Sonatas, Op. 4Previously issued on CDA67041/2034571120645
CDD22065 	VIVALDI: The Complete Cello SonatasPreviously issued on CDA66881/2034571120652
CDD22066 	LOCATELLI: Concerti Grossi, Op. 1Previously issued on CDA66981/2034571120669
CDD22067 	BERLIOZ: L'Enfance du ChristPreviously issued on CDA66991/2034571120676
CDD22068 	MAGNARD: The Four SymphoniesPreviously issued on CDA67030, CDA67040034571120683
CDD22069 	BEETHOVEN: The Complete String Trios  Superseded by CDA67253034571120690
CDD22070 	FINZI: Earth & Air & RainPreviously issued on CDA66161/2034571120706
CDD22071 	BRIDGE: SongsPreviously issued on CDA67181/2034571120713
CDD22072 	Lo SposalizioPreviously issued on CDA67048034571120720
CDD22073 	ARNE: Artaxerxes  Superseded by CDA67051/2034571120737
CDD22076 	WEBER: Complete Piano SonatasPreviously issued on Arabesque034571120768
CDD22077 	BACH: The Complete Flute Sonatas  Superseded by CDA67264/5034571120775
CDD22082 	BRAHMS: The Complete Trios  Superseded by CDA67251/2034571120829
CDGIM001 	PALESTRINA: Missa Benedicta es755138100121
CDGIM002 	Russian Orthodox Music755138100220
CDGIM003 	PALESTRINA: Missa Nigra sum755138100329
CDGIM004 	TAVERNER: Missa Gloria Tibi Trinitas755138100428
CDGIM005 	TAVENER: Ikon of Light, Funeral Ikos & The Lamb755138100527
CDGIM006 	TALLIS: Spem in alium755138100626
CDGIM007 	TALLIS: The Complete English Anthems755138100725
CDGIM008 	PALESTRINA: Missa Brevis755138100824
CDGIM009 	JOSQUIN: Missa Pange lingua & Missa La sol fa re mi755138100923
CDGIM010 	Christmas Carols & Motets: 755138101029
CDGIM011 	BYRD: Great Service755138101128
CDGIM012 	VICTORIA: Requiem755138101227
CDGIM013 	CLEMENS: Pastores quidnam vidistis755138101326
CDGIM014 	CORNYSH: Stabat mater755138101425
CDGIM015 	GESUALDO: Tenebrae Responsories755138101524
CDGIM016 	SHEPPARD: Media vita755138101623
CDGIM017 	Sarum Chant: 755138101722
CDGIM018 	LASSUS: Missa Osculetur me755138101821
CDGIM019 	JOSQUIN: L'homme armé Masses755138101920
CDGIM020 	PALESTRINA: Missa Assumpta est Maria & Missa Sicut lilium755138102026
CDGIM021 	CARDOSO: Requiem755138102125
CDGIM022 	VICTORIA: Tenebrae Responsories755138102224
CDGIM023 	ISAAC: Missa de Apostolis755138102323
CDGIM024 	TOMKINS: The Great Service755138102422
CDGIM025 	TALLIS: Lamentations of Jeremiah755138102521
CDGIM026 	BRUMEL: Earthquake Mass755138102620
CDGIM027 	Western Wind Masses: 755138102729
CDGIM028 	LÔBO D: Requiem755138102828
CDGIM029 	RORE: Missa Praeter rerum seriem755138102927
CDGIM030 	WHITE: Tudor Church Music755138103023
CDGIM031 	LOBO A: Missa Maria Magdalene755138103122
CDGIM032 	OBRECHT: Missa Maria Zart755138103221
CDGIM033 	MORALES: Missa Si bona suscepimus755138103320
CDGIM034 	TALLIS: The Christmas Mass755138103429
CDGIM035 	OCKEGHEM: Masses755138103528
CDGIM036 	BROWNE: Music from the Eton Choir Book755138103627
CDGIM037 	GOMBERT: Magnificats 1-4755138103726
CDGIM038 	GOMBERT: Magnificats 5-8755138103825
CDGIM039 	JOSQUIN: The Canonic Masses755138103924
CDGIM040 	GUERRERO: Missa Surge propera755138104020
CDGIM041 	ALLEGRI/PALESTRINA: Miserere/Papae Marcelli755138104129
CDGIM042 	JOSQUIN: Malheur me bat & Fortuna desperata755138104228
CDGIM043 	VICTORIA: Lamentations755138104327
CDGIM044 	JOSQUIN: De beata virgine & Ave maris stella755138104426
CDGIM045 	TAVERNER: Missa Gloria tibi Trinitas & Magnificats755138104525
CDGIM046 	TAVERNER: Missa Corona spinea & Dum transissets755138104624
CDGIM047 	MOUTON: Missa Dictes moy toutes voz pensées755138104723
CDGIM048 	JOSQUIN: Di dadi & Une mousse de Biscaye755138104822
CDGIM049 	PÄRT: Tintinnabuli755138104921
CDGIM050 	JOSQUIN: Missa Gaudeamus & Missa L'ami Baudichon755138105027
CDGIM051 	JOSQUIN: Missa Hercules Dux Ferrarie & other works755138105126
CDGIM052 	JOSQUIN/BAULDEWEYN: Missa Mater Patris & Missa Da pacem755138105225
CDGIM053 	SHEPPARD: Missa Cantate & other sacred music755138105324
CDGIM054 	FAYRFAX: Maria plena virtute & other votive antiphons755138105423
CDGIM201 	Essential Tallis Scholars: 755138120129
CDGIM202 	Christmas with The Tallis Scholars: 755138120228
CDGIM203 	TALLIS: Tallis Scholars sing Tallis755138120327
CDGIM204 	PALESTRINA: Tallis Scholars sing Palestrina755138120426
CDGIM205 	Requiem: The Tallis Scholars: 755138120525
CDGIM206 	JOSQUIN: Tallis Scholars sing JosquinPreviously issued on CDGIM019755138120624
CDGIM207 	TALLIS SCHOLARS: Renaissance Giants755138120723
CDGIM208 	BYRD: The Tallis Scholars sing William Byrd755138120822
CDGIM209 	TALLIS SCHOLARS: Tudor Church Music, Vol. 1755138120921
CDGIM210 	TALLIS SCHOLARS: Tudor Church Music, Vol. 2755138121027
CDGIM211 	TALLIS SCHOLARS: Flemish Masters755138121126
CDGIM212 	TALLIS SCHOLARS: Renaissance Radio755138121225
CDGIM213 	TALLIS SCHOLARS: Perfect Polyphony755138121324
CDGIM345 	BYRD: The Three Masses755138134522
CDGIM639 	ALLEGRI: Miserere755138163928
CDGIM802 	WHITACRE: Sainte-Chapelle755138180222
CDGIM992 	BYRD: Playing Elizabeth's Tune755138199224
CDGIM994 	The Tallis Scholars Live in Rome755138199422
CDGIM996 	Lamenta: 755138199620
CDGIM998 	Tallis Scholars Live in Oxford: 755138199828
CDH55001 	Favourite ClassicsPreviously issued on CDH88030034571150017
CDH55002 	Favourite Encores for String QuartetPreviously issued on CDH88038034571150024
CDH55003 	Music for Organ & BrassPreviously issued on CDH88005, CDH88017034571150031
CDH55004 	VAUGHAN WILLIAMS: Mystical Songs & Tudor Portraits  Superseded by CDA66306034571150048
CDH55005 	Concertos for the Kingdom of the Two SiciliesPreviously issued on CDH88025034571150055
CDH55006 	GERSHWIN: Fascinating Rhythm  Temporarily out of stockPreviously issued on CDH88045034571150062
CDH55007 	HAYDN: ConcertosPreviously issued on CDH88037034571150079
CDH55008 	Music for OboePreviously issued on A66206034571150086
CDH55009 	English Choral & Organ MusicPreviously issued on CDA66078034571150093
CDH55010 	PURCELL: Ayres for the TheatrePreviously issued on CDA66212034571150109
CDH55011 	SCHUMANN: Kerner Lieder & LiederkreisPreviously issued on CDA66596034571150116
CDH55012 	STRAUSS R/VERDI: String QuartetsPreviously issued on CDA66317034571150123
CDH55013 	How the world wagsPreviously issued on CDA66008034571150130
CDH55014 	DEBUSSY: The complete music for two pianos  Superseded by CDA66468034571150147
CDH55015 	Oboe QuintetsPreviously issued on CDA66143034571150154
CDH55016 	VIVALDI: Recorder ConcertosPreviously issued on CDA66328034571150161
CDH55017 	RAFF: Symphonies Nos. 3 & 4Previously issued on CDA66628034571150178
CDH55018 	From the Steeples & MountainsPreviously issued on CDA66517034571150185
CDH55019 	BOUGHTON: Symphony No. 3 & Oboe Concerto No. 1Previously issued on CDA66343034571150192
CDH55020 	Favourite Baroque ClassicsPreviously issued on CDA66600034571150208
CDH55021/8 	BEETHOVEN: Complete String QuartetsPreviously issued on CDA66401/8034571150215
CDH55029 	BRIAN: Symphony No. 3Previously issued on CDA66334034571150291
CDH55030 	FAURÉ: Violin SonatasPreviously issued on CDA66277034571150307
CDH55031 	CRUSELL: Clarinet QuartetsPreviously issued on CDA66077034571150314
CDH55032 	PROKOFIEV: String QuartetsPreviously issued on CDA66573034571150321
CDH55033 	VANHAL: Six Quartette Concertante034571150338
CDH55034 	Five Italian Oboe ConcertosPreviously issued on CDH88014034571150345
CDH55035 	The Concerto in EuropePreviously issued on CDH88015034571150352
CDH55036 	Praise to the LordPreviously issued on CDH88036034571150369
CDH55037 	The Classical Harmonie034571150376
CDH55038 	MONDONVILLE: De Profundis & Venite, exsultemus  Superseded by CDA66269034571150383
CDH55039 	SCHUMANN: Album for the YoungPreviously issued on CDH88039034571150390
CDH55040 	HAHN: Chansons Grises & other songsPreviously issued on CDA66045034571150406
CDH55041 	BIBER: Sonatae tam aris, quam aulisPreviously issued on CDA66145034571150413
CDH55042 	HOLST: SavitriPreviously issued on CDA66099034571150420
CDH55043 	BARGIEL/MENDELSSOHN: OctetsPreviously issued on CDA66356034571150437
CDH55044 	VIERNE: Symphony No. 2 & Les AngélusPreviously issued on CDA66284034571150444
CDH55045 	DYSON/HOWELLS: Rhapsodies & In Gloucestershire  Superseded by CDA66139034571150451
CDH55046 	DYSON: Hierusalem & other choral worksPreviously issued on CDA66150034571150468
CDH55047 	BYRD: GradualiaPreviously issued on CDA66451034571150475
CDH55048 	Baroque Christmas MusicPreviously issued on CDH88028034571150482
CDH55049 	MARTUCCI/RESPIGHI: La Canzone dei Ricordi & Il Tramonto  Superseded by CDA66290034571150499
CDH55050 	Lie strewn the white flocks  Temporarily out of stockPreviously issued on CDA66175034571150505
CDH55051 	TAVERNER: Missa Corona Spinea  Superseded by CDA66360034571150512
CDH55052 	TAVERNER: Missa Gloria tibi Trinitas  Last few remainingPreviously issued on CDA66134034571150529
CDH55053 	TAVERNER: Missa Mater Christi sanctissimaPreviously issued on CDA66639034571150536
CDH55054 	TAVERNER: Missa O Michael  Superseded by CDA66325034571150543
CDH55055 	TAVERNER: Missa Sancti Wilhelmi  Superseded by CDA66427034571150550
CDH55056 	TAVERNER: Western Wynde Mass  Temporarily out of stockPreviously issued on CDA66507034571150567
CDH55057 	VILLA-LOBOS: Music for FlutePreviously issued on CDA66295034571150574
CDH55059 	Il Ballarino  Temporarily out of stockPreviously issued on CDA66244034571150598
CDH55060 	English Clarinet Concertos, Vol. 2Previously issued on CDA66634034571150604
CDH55061 	PARRY/STANFORD: Nonet & Serenade  Superseded by CDA66291034571150611
CDH55062 	FIORILLO/VIOTTI: Violin Concertos  Superseded by CDA66210034571150628
CDH55063 	BRIDGE: Piano Trios & Piano QuartetPreviously issued on CDA66279034571150635
CDH55064 	MENDELSSOHN: Complete Music for CelloPreviously issued on CDA66478034571150642
CDH55065 	PURCELL: Songs & DialoguesPreviously issued on CDA66056034571150659
CDH55066 	TOMKINS: Cathedral Music  Superseded by CDA66345034571150666
CDH55067 	BRITTEN: Winter WordsPreviously issued on CDA66209034571150673
CDH55068 	Clarinet Concertos  Superseded by CDA66215034571150680
CDH55069 	English Clarinet Concertos, Vol. 1  Superseded by CDA66031034571150697
CDH55070 	English Music for BrassPreviously issued on CDH88013034571150703
CDH55071 	ARNOLD: Chamber Music, Vol. 1  Temporarily out of stockPreviously issued on CDA66171034571150710
CDH55072 	ARNOLD: Chamber Music, Vol. 2  Temporarily out of stockPreviously issued on CDA66172034571150727
CDH55073 	ARNOLD: Chamber Music, Vol. 3  Superseded by CDA66173034571150734
CDH55074 	CZERNY: Music for horn & fortepiano034571150741
CDH55075 	HANDEL: Six Concerti Grossi, Op. 3Previously issued on CDA66633034571150758
CDH55076 	Clarinet Quintets  Superseded by CDA66479034571150765
CDH55077 	HANDEL: Aminta e FillidePreviously issued on CDA66118034571150772
CDH55078 	MENDELSSOHN/SCHUMANN: Piano Trios  Superseded by CDA66331034571150789
CDH55079 	TYE: Missa Euge bone  Superseded by CDA66424034571150796
CDH55080 	KROMMER/MOZART: Oboe ConcertosPreviously issued on CDA66411034571150802
CDH55081 	SZYMANOWSKI: Piano Music  Temporarily out of stockPreviously issued on CDA66409034571150819
CDH55082 	BEETHOVEN: Diabelli VariationsPreviously issued on CDA66763034571150826
CDH55083 	BEETHOVEN: The Last Three Piano Sonatas034571150833
CDH55084 	Songs by Finzi & his friends  Temporarily out of stockPreviously issued on CDA66015034571150840
CDH55085 	English Music for ViolaPreviously issued on CDA66687034571150857
CDH55086 	MUNDY: Sacred Choral Music  Superseded by CDS44401/10Previously issued on CDA66319034571150864
CDH55087 	BRAHMS: The Three Violin Sonatas  Temporarily out of stockPreviously issued on CDA66465034571150871
CDH55088 	Victorian Concert OverturesPreviously issued on CDA66515034571150888
CDH55089 	SOMERVELL: Maud & A Shropshire LadPreviously issued on CDA66187034571150895
CDH55091 	TELEMANN: Recorder ConcertosPreviously issued on CDA66413034571150918
CDH55092 	MOZART: Wind Serenades & Overtures  Superseded by CDA66887034571150925
CDH55093 	MOZART: Serenade in B flat 'Gran Partita'Previously issued on CDA66285034571150932
CDH55094 	MOZART: String Quartets, K499 & K589  Superseded by CDA66458034571150949
CDH55095 	PALESTRINA: The Song of Songs  Superseded by CDA66733034571150956
CDH55096 	Flute Music of the 16th & 17th centuriesPreviously issued on CDA66298034571150963
CDH55097 	From a Spanish Palace SongbookPreviously issued on CDA66454034571150970
CDH55098 	Spanish Music of the Golden AgePreviously issued on CDA66327034571150987
CDH55099 	Three English Ballet Suites  Superseded by CDA66436034571150994
CDH55100 	PANUFNIK/SESSIONS: Symphony No. 8 & Concerto  Temporarily out of stockPreviously issued on CDA66050034571151007
CDH55101 	FINZI/STANFORD: Clarinet ConcertosPreviously issued on CDA66001034571151014
CDH55102 	VIVALDI: La Pastorella  Temporarily out of stockPreviously issued on CDA66309034571151021
CDH55103 	ENESCU: Violin SonatasPreviously issued on CDA66484034571151038
CDH55104 	HOLST: Choral SymphonyPreviously issued on CDA66660034571151045
CDH55105 	English Clarinet QuintetsPreviously issued on CDA66428034571151052
CDH55106 	ZELENKA: Lamentations of Jeremiah  Superseded by CDA66426034571151069
CDH55107 	KOECHLIN: Music for flute  Superseded by CDA66414034571151076
CDH55108 	TELEMANN: Chamber MusicPreviously issued on CDA66195034571151083
CDH55109 	Rare Piano EncoresPreviously issued on CDA66090034571151090
CDH55110 	JACOB/SOMERVELL: Clarinet Quintets034571151106
CDH55111 	HAYDN: Symphonies Nos. 1, 2, 3, 4 & 5Previously issued on CDA66524034571151113
CDH55112 	HAYDN: Symphonies Nos. 6, 7 & 8Previously issued on CDA66523034571151120
CDH55113 	HAYDN: Symphonies Nos. 9, 10, 11 & 12Previously issued on CDA66529034571151137
CDH55114 	HAYDN: Symphonies Nos. 13, 14, 15 & 16Previously issued on CDA66534034571151144
CDH55115 	HAYDN: Symphonies Nos. 17, 18, 19, 20 & 21  Temporarily out of stockPreviously issued on CDA66533034571151151
CDH55116 	HAYDN: Symphonies Nos. 22, 23, 24 & 25Previously issued on CDA66536034571151168
CDH55117 	HAYDN: Symphonies Nos. 42, 43 & 44Previously issued on CDA66530034571151175
CDH55118 	HAYDN: Symphonies Nos. 45, 46 & 47Previously issued on CDA66522034571151182
CDH55119 	HAYDN: Symphonies Nos. 48, 49 & 50Previously issued on CDA66531034571151199
CDH55120 	HAYDN: Symphonies Nos. 70, 71 & 72Previously issued on CDA66526034571151205
CDH55121 	HAYDN: Symphonies Nos. 73, 74 & 75Previously issued on CDA66520034571151212
CDH55122 	HAYDN: Symphonies Nos. 76, 77 & 78Previously issued on CDA66525034571151229
CDH55123 	HAYDN: Symphonies Nos. 82, 83 & 84  Superseded by CDA66527034571151236
CDH55124 	HAYDN: Symphonies Nos. 85, 86 & 87Previously issued on CDA66535034571151243
CDH55125 	HAYDN: Symphonies Nos. 90, 91 & 92Previously issued on CDA66521034571151250
CDH55126 	HAYDN: Symphonies Nos. 93, 94 & 95Previously issued on CDA66532034571151267
CDH55127 	HAYDN: Symphonies Nos. 101 & 102Previously issued on CDA66528034571151274
CDH55128 	Echoes of a WaterfallPreviously issued on CDA66038034571151281
CDH55129 	ArabesquePreviously issued on CDA66116034571151298
CDH55130 	Caprices & FantasiesPreviously issued on CDA66340034571151304
CDH55131 	SCHARWENKA: Piano Music, Vol. 1Previously issued on Collins13252034571151311
CDH55132 	SCHARWENKA: Piano Music, Vol. 2Previously issued on Collins13522034571151328
CDH55133 	SCHARWENKA: Piano Music, Vol. 3Previously issued on Collins13652034571151335
CDH55134 	SCHARWENKA: Piano Music, Vol. 4Previously issued on Collins14742034571151342
CDH55135 	BERKELEY: A Centenary TributePreviously issued on A66086034571151359
CDH55136 	HANDEL: Il Duello AmorosoPreviously issued on A66155034571151366
CDH55137 	RIMSKY-KORSAKOV: Antar  Superseded by CDA66399034571151373
CDH55138 	LÔBO/MAGALHÃES: Requiem & Missa dilectus meusPreviously issued on CDA66218034571151380
CDH55139 	HOWELLS: Music for violin & piano  Temporarily out of stockPreviously issued on CDA66665034571151397
CDH55140 	ROTT: Symphony in E majorPreviously issued on CDA66366034571151403
CDH55141 	MOSZKOWSKI: Piano Music, Vol. 1Previously issued on Collins14122034571151410
CDH55142 	MOSZKOWSKI: Piano Music, Vol. 2Previously issued on Collins14732034571151427
CDH55143 	MOSZKOWSKI: Piano Music, Vol. 3Previously issued on Collins15192034571151434
CDH55144 	WIDOR: Symphony No. 5  Temporarily out of stockPreviously issued on CDA66181034571151441
CDH55145 	MONTEVERDI: MassesPreviously issued on CDA66214034571151458
CDH55146 	Ancient Airs & Dances  Superseded by CDA66228034571151465
CDH55147 	ELGAR: Cathedral MusicPreviously issued on CDA66313034571151472
CDH55148 	Sacred and Secular Music from six centuriesPreviously issued on CDA66370034571151489
CDH55149 	BARTÓK: Sonata, Contrasts & RhapsodiesPreviously issued on CDA66415034571151496
CDH55150 	MENDELSSOHN: On wings of songPreviously issued on CDA66666034571151502
CDH55151 	Gabriel's GreetingPreviously issued on CDA66685034571151519
CDH55152 	HOWELLS: Howells' & Lambert's ClavichordPreviously issued on CDA66689034571151526
CDH55153 	BOULANGER: Clairières dans le ciel  Superseded by CDA66726034571151533
CDH55154 	BRITTEN: Music for Oboe & Music for PianoPreviously issued on CDA66776034571151540
CDH55155 	WASSENAER: Concerti ArmoniciPreviously issued on CDA66670034571151557
CDH55156 	Bird Songs at EventidePreviously issued on CDA66818034571151564
CDH55157 	Violin Concertos  Superseded by CDA66840034571151571
CDH55158 	BRAHMS: Clarinet SonatasPreviously issued on CDA66202034571151588
CDH55159 	In praise of womanPreviously issued on CDA66709034571151595
CDH55160 	MAHLER: Songs of YouthPreviously issued on CDA66100034571151601
CDH55161 	Joy to the WorldPreviously issued on CDH88031034571151618
CDH55162 	Harp music of the Italian RenaissancePreviously issued on CDA66229034571151625
CDH55163 	KOECHLIN: Le cortège d'Amphitrite  Superseded by CDA66243034571151632
CDH55164 	IRELAND: The complete music for violin & piano  Superseded by CDA66853034571151649
CDH55165 	MONTEVERDI: BalliPreviously issued on CDA66475034571151656
CDH55166 	HUMMEL: String QuartetsPreviously issued on CDA66568034571151663
CDH55167 	POULENC/HAHN: Aubade, Sinfonietta & Bal de Béatrice d'EstePreviously issued on CDA66347034571151670
CDH55168 	MILHAUD: Le Carnaval d'Aix & other worksPreviously issued on CDA66594034571151687
CDH55169 	THOMSON: Louisiana Story  Temporarily out of stockPreviously issued on CDA66576034571151694
CDH55170 	HOLST: The Evening Watch  Superseded by CDA66329034571151700
CDH55171 	HOLST: This have I done for my true love  Superseded by CDA66705034571151717
CDH55172 	SCARLATTI D: Stabat materPreviously issued on CDA66182034571151724
CDH55173 	GLINKA/RIMSKY-KORSAKOV: Grand Sextet & QuintetPreviously issued on CDA66163034571151731
CDH55174 	BOUGHTON: String Quartets & Oboe Quartet No. 1  Superseded by CDA66936034571151748
CDH55175 	SATIE: Piano MusicPreviously issued on CDA66344034571151755
CDH55176 	SATIE: Parade & other theatre musicPreviously issued on CDA66365034571151762
CDH55177 	PROKOFIEV: Peter & the WolfPreviously issued on CDA66499034571151779
CDH55178 	VIVALDI: Viola d'amore concertos  Superseded by CDA66795034571151786
CDH55179 	POULENC: Secular Choral Music  Superseded by CDA66798034571151793
CDH55180 	CHOPIN: Piano ConcertosPreviously issued on CDA66647034571151809
CDH55181 	CHOPIN: The Four ScherziPreviously issued on CDA66514034571151816
CDH55182 	CHOPIN: Ballades & Sonata No. 3Previously issued on CDA66577034571151823
CDH55183 	CHOPIN: Demidenko plays Chopin  Superseded by CDA66597034571151830
CDH55184 	LISZT: Sonata  Superseded by CDA66616034571151847
CDH55185 	MARTINU: Cello SonatasPreviously issued on CDA66296034571151854
CDH55186 	The Courts of LovePreviously issued on CDA66367034571151861
CDH55187 	GURNEY/VAUGHAN WILLIAMS: A Shropshire LadPreviously issued on CDA66385034571151878
CDH55188 	TAUSCH: Double Clarinet ConcertosPreviously issued on CDA66504034571151885
CDH55189 	BEETHOVEN: Septet & Sextet  Superseded by CDA66513034571151892
CDH55190 	VIVALDI: Cantatas, Concertos & MagnificatPreviously issued on CDA66247034571151908
CDH55191 	MUFFAT: Armonico TributoPreviously issued on CDA66032034571151915
CDH55192 	Italian Baroque Trumpet Music  Superseded by CDA66255034571151922
CDH55193 	CAVALLI: Messa ConcertataPreviously issued on CDA66970034571151939
CDH55194 	For Children  Superseded by CDA66185034571151946
CDH55195 	LEIGHTON: Sacred Choral MusicPreviously issued on CDA66489034571151953
CDH55196 	BEETHOVEN: The Creatures of PrometheusPreviously issued on CDA66748034571151960
CDH55197 	CHAMINADE: Piano Music, Vol. 1  Superseded by CDA66584034571151977
CDH55198 	CHAMINADE: Piano Music, Vol. 2  Superseded by CDA66706034571151984
CDH55199 	CHAMINADE: Piano Music, Vol. 3  Superseded by CDA66846034571151991
CDH55200 	ROSSINI: The String SonatasPreviously issued on CDA66595034571152004
CDH55201 	BEETHOVEN/BRAHMS: VariationsPreviously issued on EL 1021-2034571152011
CDH55202 	STRAUSS R: Songs  Superseded by CDA66659034571152028
CDH55203 	CRUSELL: Clarinet ConcertosPreviously issued on CDA66708034571152035
CDH55204 	Land of Heart's Desire  Temporarily out of stockPreviously issued on CDA66988034571152042
CDH55205 	HOWELLS: Concertos & DancesPreviously issued on CDA66610034571152059
CDH55206 	GODOWSKY: Piano MusicPreviously issued on CDA66496034571152066
CDH55207 	Bella Domna  Superseded by CDA66283034571152073
CDH55208 	HAYDN: Harmoniemesse & Little Organ MassPreviously issued on CDA66508034571152080
CDH55209 	RACHMANINOV: Music for two pianosPreviously issued on CDA66375034571152097
CDH55210 	The last rose of summerPreviously issued on CDA66627034571152103
CDH55211 	RHEINBERGER: Music for organ, violin & celloPreviously issued on CDA66883034571152110
CDH55212 	LASSUS: Missa Bell' Amfitrit' altera  Superseded by CDA66688034571152127
CDH55213 	ANERIO: RequiemPreviously issued on CDA66417034571152134
CDH55214 	HUMMEL: SeptetsPreviously issued on CDA66396034571152141
CDH55215 	TCHAIKOVSKY: Piano Sonatas  Superseded by CDA66939034571152158
CDH55216 	O magnum misterium  Superseded by CDA66925034571152165
CDH55217 	Souvenirs de Venise  Superseded by CDA66112034571152172
CDH55218 	Bridge, Elgar & Walton  Temporarily out of stockPreviously issued on CDA66718034571152189
CDH55219 	BOCCHERINI: Cello Sonatas  Temporarily out of stockPreviously issued on CDA66719034571152196
CDH55220 	HOWELLS/VAUGHAN WILLIAMS: Requiem & MassPreviously issued on CDA66076034571152202
CDH55221 	GLAZUNOV: The Complete Solo Piano Music, Vol. 1Previously issued on CDA66833034571152219
CDH55222 	GLAZUNOV: The Complete Solo Piano Music, Vol. 2Previously issued on CDA66844034571152226
CDH55223 	GLAZUNOV: The Complete Solo Piano Music, Vol. 3Previously issued on CDA66855034571152233
CDH55224 	GLAZUNOV: The Complete Solo Piano Music, Vol. 4Previously issued on CDA66866034571152240
CDH55225 	BRITTEN: PhaedraPreviously issued on CDA66845034571152257
CDH55226 	YSAYE: Violin MusicPreviously issued on CDA66940034571152264
CDH55227 	CLEMENTI: Demidenko plays Clementi  Superseded by CDA66808034571152271
CDH55228 	GIBBONS: Anthems & Verse AnthemsPreviously issued on CDA67116034571152288
CDH55229 	Masterpieces of Portuguese PolyphonyPreviously issued on CDA66512034571152295
CDH55230 	German 17th-Century Church MusicPreviously issued on CDA67079034571152301
CDH55231 	VIVALDI: La FoliaPreviously issued on CDA66193034571152318
CDH55232 	BACH C P E: La FoliaPreviously issued on CDA66239034571152325
CDH55233 	SCARLATTI A: La FoliaPreviously issued on CDA66254034571152332
CDH55234 	GEMINIANI: La FoliaPreviously issued on CDA66264034571152349
CDH55235 	MARAIS: La FoliaPreviously issued on CDA66310034571152356
CDH55236 	GRAINGER/GRIEG: At TwilightPreviously issued on CDA66793034571152363
CDH55237 	War's Embers034571152370
CDH55238 	Strauss Waltz Transcriptions  Temporarily out of stockPreviously issued on CDA66785034571152387
CDH55239 	RACHMANINOV: Demidenko plays RachmaninovPreviously issued on CDA66713034571152394
CDH55240 	CORELLI: La Folia & other sonatasPreviously issued on CDA66226034571152400
CDH55241 	Awake, sweet lovePreviously issued on CDA66447034571152417
CDH55242 	SCRIABIN: The Complete ÉtudesPreviously issued on CDA66607034571152424
CDH55243 	All in the April eveningPreviously issued on CDA67076034571152431
CDH55244 	BRITTEN: Five Canticles  Superseded by CDA66498034571152448
CDH55245 	JONES: The Geisha  Superseded by CDA67006034571152455
CDH55246 	FRASER-SIMSON: The Maid of the MountainsPreviously issued on CDA67190034571152462
CDH55247 	GOMBERT: Credo & other sacred music  Superseded by CDA66828034571152479
CDH55248 	Mortuus est Philippus RexPreviously issued on CDA67046034571152486
CDH55249 	English Lute SongsPreviously issued on CDA67126034571152493
CDH55250 	LOCKE: Anthems, Motets & Ceremonial MusicPreviously issued on CDA66373034571152509
CDH55251 	ARNE: Six Favourite ConcertosPreviously issued on CDA66509034571152516
CDH55252 	CROFT: Te Deum & Burial Service  Superseded by CDA66606034571152523
CDH55253 	LINLEY: Ode on the Fairies of ShakespearePreviously issued on CDA66613034571152530
CDH55254 	PHILIPS: MotetsPreviously issued on CDA66643034571152547
CDH55255 	LOCKE: The Broken ConsortPreviously issued on CDA66727034571152554
CDH55256 	LINLEY: Cantatas & Theatre Music  Superseded by CDA66767034571152561
CDH55257 	BLOW/DRAGHI: Odes for St Cecilia  Temporarily out of stockPreviously issued on CDA66770034571152578
CDH55258 	Sound the TrumpetPreviously issued on CDA66817034571152585
CDH55259 	WEELKES: AnthemsPreviously issued on CDA66477034571152592
CDH55260 	English Classical Violin ConcertosPreviously issued on CDA66865034571152608
CDH55261 	English Classical Clarinet ConcertosPreviously issued on CDA66896034571152615
CDH55262 	HANDEL: Italian Duets  Superseded by CDA66440034571152622
CDH55263 	BEETHOVEN: Mass in C majorPreviously issued on CDA66830034571152639
CDH55264 	The Harp of LuduvicoPreviously issued on CDA66518034571152646
CDH55265 	GABRIELI A: Missa Pater peccaviPreviously issued on CDA67167034571152653
CDH55266 	PARRY: Violin SonatasPreviously issued on CDA66157034571152660
CDH55267 	BARTÓK: 44 Duos for two violins  Superseded by CDA66453034571152677
CDH55268 	MENDELSSOHN: Choral MusicPreviously issued on CDA66359034571152684
CDH55269 	BACH/TELEMANN: Oboe & Oboe d'amore ConcertosPreviously issued on CDA66267034571152691
CDH55270 	CHOPIN: Polish Songs  Superseded by CDA67125034571152707
CDH55271 	DUFAY: Music for St Anthony of PaduaPreviously issued on CDA66854034571152714
CDH55272 	DUFAY: Music for St James the GreaterPreviously issued on CDA66997034571152721
CDH55273 	The Marriage of Heaven & HellPreviously issued on CDA66423034571152738
CDH55274 	The Castle of Fair WelcomePreviously issued on CDA66194034571152745
CDH55275 	SCHUMANN C: SongsPreviously issued on CDA67249034571152752
CDH55276 	MORALES: Missa Queramus cum pastoribusPreviously issued on CDA66635034571152769
CDH55277 	BRUCKNER: Mass in E minorPreviously issued on CDA66177034571152776
CDH55278 	TELEMANN: Musique de TablePreviously issued on CDA66278034571152783
CDH55279 	VIVALDI: Opera Arias & SinfoniasPreviously issued on CDA66745034571152790
CDH55280 	HANDEL: Trio Sonatas  Superseded by CDA67083034571152806
CDH55281 	The Spirits of England & France, Vol. 1Previously issued on CDA66739034571152813
CDH55282 	The Spirits of England & France, Vol. 2  Superseded by CDA66773034571152820
CDH55283 	The Spirits of England & France, Vol. 3Previously issued on CDA66783034571152837
CDH55284 	The Spirits of England & France, Vol. 4Previously issued on CDA66857034571152844
CDH55285 	The Spirits of England & France, Vol. 5Previously issued on CDA66919034571152851
CDH55286 	SCRIABIN: The Early ScriabinPreviously issued on CDA67149034571152868
CDH55287 	ASTORGA/BOCCHERINI: Stabat materPreviously issued on CDA67108034571152875
CDH55288 	BUSNOIS/DOMARTO: Missa L'homme arméPreviously issued on CDA67319034571152882
CDH55289 	The Garden of ZephirusPreviously issued on CDA66144034571152899
CDH55290 	The Service of Venus & MarsPreviously issued on CDA66238034571152905
CDH55291 	A Song for FrancescaPreviously issued on CDA66286034571152912
CDH55292 	Music for the Lion-Hearted King  Superseded by CDA66336034571152929
CDH55293 	The Medieval RomanticsPreviously issued on CDA66463034571152936
CDH55294 	Lancaster and ValoisPreviously issued on CDA66588034571152943
CDH55295 	The Study of LovePreviously issued on CDA66619034571152950
CDH55296 	LA RUE: Missa De Feria & Missa Sancta Dei genitrixPreviously issued on CDA67010034571152967
CDH55297 	The Earliest Songbook in EnglandPreviously issued on CDA67177034571152974
CDH55298 	The Voice in the Garden  Superseded by CDA66653034571152981
CDH55299 	GRIEG: String Quartets Nos. 1 & 2Previously issued on CDA67117034571152998
CDH55300 	SCHUMANN: Piano Sonatas  Superseded by CDA66864034571153001
CDH55301 	ELGAR: Quintet & Violin SonataPreviously issued on CDA66645034571153018
CDH55302 	LINLEY: The Song of Moses & Let God arisePreviously issued on CDA67038034571153025
CDH55303 	PURCELL: Mr Henry Purcell's Most Admirable ComposuresPreviously issued on CDA66288034571153032
CDH55304 	SCRIABIN/TCHAIKOVSKY: Piano ConcertosPreviously issued on CDA66680034571153049
CDH55305 	SCHUBERT: String Quintet & String TrioPreviously issued on CDA66724034571153056
CDH55306 	MUSORGSKY/PROKOFIEV: Pictures from an Exhibition/Romeo & JulietPreviously issued on CDA67018034571153063
CDH55307 	BRITTEN: A Boy was BornPreviously issued on CDA66126034571153070
CDH55309 	LIADOV: Solo Piano MusicPreviously issued on CDA66986034571153094
CDH55310 	SCHÜTZ/GABRIELI: The Christmas Story & MotetsPreviously issued on CDA66398034571153100
CDH55311 	ARENSKY: Piano MusicPreviously issued on CDA67066034571153117
CDH55312 	BACH: Cantatas Nos. 54, 169 & 170  Superseded by CDA66326034571153124
CDH55313 	GUERRERO: Missa Sancta et immaculata  Temporarily out of stockPreviously issued on CDA66910034571153131
CDH55314 	MOZART: Epistle SonatasPreviously issued on CDA66377034571153148
CDH55315 	MEDTNER: Demidenko plays MedtnerPreviously issued on CDA66636034571153155
CDH55316 	VILLA-LOBOS: Bachianas brasileiras Nos. 1 & 5Previously issued on CDA66257034571153162
CDH55317 	Masterpieces of Mexican PolyphonyPreviously issued on CDA66330034571153179
CDH55318 	RACHMANINOV: The Divine Liturgy of St John ChrysostomPreviously issued on CDA66703034571153186
CDH55319 	DAQUIN: Douze Noëls  Superseded by CDA66816034571153193
CDH55320 	CASTELLO/PICCHI: The Floating City  Superseded by CDA67013034571153209
CDH55321 	MARTINU/SCHULHOFF: String Sextets  Superseded by CDA66516034571153216
CDH55322 	GLINKA/TCHAIKOVSKY: Piano TriosPreviously issued on CDA67216034571153223
CDH55323 	GOMBERT: Missa Tempore paschali & Motets  Superseded by CDA66943034571153230
CDH55324 	HANDEL: Handel in Hamburg  Superseded by CDA67053034571153247
CDH55325 	While shepherds watchedPreviously issued on CDA66924034571153254
CDH55326 	PEÑALOSA: MassesPreviously issued on CDA66629034571153261
CDH55327 	PURCELL: Hail! bright Cecilia & Who can from joy?Previously issued on CDA66349034571153278
CDH55328 	LÉONIN: Magister Leoninus, Vol. 1  Superseded by CDA66944034571153285
CDH55329 	PIZZETTI: Orchestral MusicPreviously issued on CDA67084034571153292
CDH55331 	TCHAIKOVSKY: Songs  Temporarily out of stockPreviously issued on CDA66617034571153315
CDH55332 	BRUCKNER: Mass in F minorPreviously issued on CDA66599034571153322
CDH55333 	MOZART: Piano Concertos Nos. 11, 12 & 13Previously issued on CDA67358034571153339
CDH55334 	TARTINI: Violin Concertos  Superseded by CDA67345034571153346
CDH55335 	PALESTRINA: O rex gloriae & Viri GalilaeiPreviously issued on CDA66316034571153353
CDH55336 	Songs of ScotlandPreviously issued on CDA67106034571153360
CDH55337 	MEDTNER/RACHMANINOV: Music for two pianosPreviously issued on CDA66654034571153377
CDH55338 	LÉONIN: Magister Leoninus, Vol. 2Previously issued on CDA67289034571153384
CDH55339 	DOWLAND: LachrimaePreviously issued on CDA66637034571153391
CDH55340 	GUERRERO: Missa De la batalla escoutez & other worksPreviously issued on CDA67075034571153407
CDH55341 	English 18th-century Keyboard ConcertosPreviously issued on CDA66700034571153414
CDH55342 	SAINT-SAËNS: Cello SonatasPreviously issued on CDA67095034571153421
CDH55343 	MACKENZIE: Violin Concerto & Pibroch  Superseded by CDA66975034571153438
CDH55344 	His Majestys Sagbutts & Cornetts Grand TourPreviously issued on CDA66847034571153445
CDH55345 	MONTEVERDI: Sacred Vocal Music  Superseded by CDA66021034571153452
CDH55346 	BRAHMS: MotetsPreviously issued on CDA66389034571153469
CDH55347 	BACH: Violin ConcertosPreviously issued on CDA66380034571153476
CDH55348 	BYRD: Mass for five voicesPreviously issued on CDA66837034571153483
CDH55349 	ALBINONI/VIVALDI: Oboe ConcertosPreviously issued on CDA66383034571153490
CDH55350 	HOLST/MATTHEWS: Planets/PlutoPreviously issued on CDA67270034571153506
CDH55351 	PADEREWSKI: Symphony 'Polonia'  Superseded by CDA67056034571153513
CDH55352 	GRECHANINOV: VespersPreviously issued on CDA67080034571153520
CDH55353 	SAINT-SAËNS/YSAYE: Rare transcriptions for violin & piano  Temporarily out of stockPreviously issued on CDA67285034571153537
CDH55354 	SCARLATTI/HASSE: Salve regina, Cantatas & MotetsPreviously issued on CDA66875034571153544
CDH55355 	HAYDN: SongsPreviously issued on CDA67174034571153551
CDH55356 	BRUCKNER: Mass in D minor & Te Deum  Superseded by CDS44071/3034571153568
CDH55357 	PEÑALOSA: The Complete Motets  Superseded by CDA66574034571153575
CDH55358 	VICTORIA: Missa Vidi speciosam & motetsPreviously issued on CDA66129034571153582
CDH55359 	Music for St Paul'sPreviously issued on CDA67009034571153599
CDH55360 	MENDELSSOHN: SongsPreviously issued on CDA67110034571153605
CDH55361 	STANLEY: 6 Concertos in 7 parts, Op. 2  Temporarily out of stockPreviously issued on CDA66338034571153612
CDH55362 	STANFORD: Music for violin & piano  Superseded by CDA67024034571153629
CDH55364 	Masters of the RollsPreviously issued on CDA67098034571153643
CDH55365 	DVORÁK: Music for violin & pianoPreviously issued on CDA66934034571153650
CDH55366 	POULENC: Voyage à ParisPreviously issued on CDA66147034571153667
CDH55367 	PALESTRINA: Missa Hodie Christus natus estPreviously issued on CDA67396034571153674
CDH55368 	PALESTRINA: Missa Aeterna Christi munera & Motets  Superseded by CDA66490034571153681
CDH55369 	BRAHMS: String QuintetsPreviously issued on CDA66804034571153698
CDH55370 	HANDEL: James Bowman sings Heroic AriasPreviously issued on CDA66483034571153704
CDH55371 	MOZART: SongsPreviously issued on CDA66989034571153711
CDH55372 	BRUCKNER/STRAUSS R: Quintet & Capriccio  Superseded by CDA66704034571153728
CDH55373 	SCHELLE: Sacred Music  Superseded by CDA67260034571153735
CDH55374 	JOSQUIN: Missa Pange lingua & Vultum tuumPreviously issued on CDA66614034571153742
CDH55375 	HANDEL: Fireworks Music & Water Music034571153759
CDH55376 	VICTORIA: Missa Trahe me post te & MotetsPreviously issued on CDA66738034571153766
CDH55377 	MENDELSSOHN: String QuintetsPreviously issued on CDA66993034571153773
CDH55378 	BRITTEN: St Nicolas & Hymn to St Cecilia  Temporarily out of stockPreviously issued on CDA66333034571153780
CDH55379 	HAHN: Chamber MusicPreviously issued on CDA67391034571153797
CDH55380 	CHOPIN: The Complete Études034571153803
CDH55381 	CHOPIN: The Complete Waltzes034571153810
CDH55382 	CHOPIN: The Great Polonaises034571153827
CDH55383 	CHOPIN: Preludes & Impromptus034571153834
CDH55384 	CHOPIN: Chamber Music034571153841
CDH55385 	WOLF: Italienisches LiederbuchPreviously issued on CDA66760034571153858
CDH55386 	L'Album des SixPreviously issued on CDA67204034571153865
CDH55387 	MOSCHELES: Complete Concert StudiesPreviously issued on CDA67394034571153872
CDH55388 	LAMBERT: Summer's Last Will & TestamentPreviously issued on CDA66565034571153889
CDH55389 	WOLF: Lieder nach Heine & LenauPreviously issued on CDA67343034571153896
CDH55390 	MOZART: Oboe Quartet, Horn Quintet & other worksPreviously issued on CDA67277034571153902
CDH55391 	CHOPIN: The Complete Mazurkas, Vol. 1034571153919
CDH55392 	CHOPIN: The Complete Mazurkas, Vol. 2034571153926
CDH55393 	KNÜPFER: Sacred Music  Superseded by CDA67160034571153933
CDH55394 	KUHNAU: Sacred MusicPreviously issued on CDA67059034571153940
CDH55395 	MACKENZIE: Orchestral MusicPreviously issued on CDA66764034571153957
CDH55396 	Rare French works for violin & orchestraPreviously issued on CDA67294034571153964
CDH55397 	LAMBERT: Piano Concerto & other worksPreviously issued on CDA66754034571153971
CDH55398 	JANÁCEK: Choral MusicPreviously issued on CDA66893034571153988
CDH55399 	GRECHANINOV: Piano TriosPreviously issued on CDA67295034571153995
CDH55400 	TALLIS: Missa Salve intemerata & Antiphons  Superseded by CDA67207034571154008
CDH55401 	My soul doth magnify the LordPreviously issued on CDA66249034571154015
CDH55402 	My spirit hath rejoicedPreviously issued on CDA66305034571154022
CDH55403 	RACHMANINOV: Études-tableauxPreviously issued on CDA66091034571154039
CDH55404 	VIVALDI: Six Violin Sonatas, Op. 2Previously issued on CDA67467034571154046
CDH55405 	DVORÁK: String Quintet & String SextetPreviously issued on CDA66308034571154053
CDH55406 	For His Majestys Sagbutts & CornettsPreviously issued on CDA66894034571154060
CDH55407 	PALESTRINA: Missa Ecce ego Johannes & other sacred music  Superseded by CDA67099034571154077
CDH55408 	PÄRT: Berliner Messe & Magnificat  Superseded by CDA66960034571154084
CDH55410 	The Maiden's Prayer  Temporarily out of stockPreviously issued on CDA67379034571154107
CDH55411 	ALBERT: Solo Piano Music  Temporarily out of stockPreviously issued on CDA66945034571154114
CDH55412 	DOHNÁNYI: Piano Quintets & Serenade  Superseded by CDA66786034571154121
CDH55413 	HINDEMITH: Ludus Tonalis & Suite 1922Previously issued on CDA66824034571154138
CDH55414 	TAVENER: Sacred Music  Superseded by CDA66464034571154145
CDH55416 	SUK: Piano Quintet & Piano Quartet  Superseded by CDA67448034571154169
CDH55417 	BACH: The Six Motets  Superseded by CDA66369034571154176
CDH55419 	HANDEL: English Arias  Superseded by CDA66797034571154190
CDH55420 	PALESTRINA: Missa De beata virgine & Missa Ave MariaPreviously issued on CDA66364034571154206
CDH55421 	BURGON: Choral Music  Superseded by CDA67567034571154213
CDH55422 	Blah blah blah & other trifles  Temporarily out of stockPreviously issued on CDA66289034571154220
CDH55423 	DUFAY: Missa Puisque je vis & other worksPreviously issued on CDA67368034571154237
CDH55424 	ZELENKA: Sacred Music  Superseded by CDA67350034571154244
CDH55425 	CATOIRE: Piano Music  Superseded by CDA67090034571154251
CDH55426 	ARENSKY/TCHAIKOVSKY: String Quartet & SouvenirPreviously issued on CDA66648034571154268
CDH55427 	HUMMEL/SCHUBERT: Piano QuintetsPreviously issued on CDH88010034571154275
CDH55428 	CHABRIER: BriséïsPreviously issued on CDA66803034571154282
CDH55429 	BYRD: Consort SongsPreviously issued on CDA67397034571154299
CDH55430 	Treasures of the Spanish RenaissancePreviously issued on CDA66168034571154305
CDH55431 	RACHMANINOV: Piano TriosPreviously issued on CDA67178034571154312
CDH55432 	FINZI: Intimations of Immortality & Dies natalisPreviously issued on CDA66876034571154329
CDH55433 	GRAINGER: Jungle Book & other choral worksPreviously issued on CDA66863034571154336
CDH55434 	STANFORD: Piano Quintet & String Quintet No. 1Previously issued on CDA67505034571154343
CDH55435 	WOLF: Eichendorff-LiederPreviously issued on CDA66909034571154350
CDH55436 	Passiontide at St Paul's  Superseded by CDA66916034571154367
CDH55437 	TCHAIKOVSKY: Liturgy of St John ChrysostomPreviously issued on CDA66948034571154374
CDH55438 	BRITTEN: Sacred and Profane & other choral works  Superseded by CDA67140034571154381
CDH55439 	VIVALDI: Concerti con molti istromenti  Superseded by CDA67073034571154398
CDH55440 	PROKOFIEV: Piano Concertos Nos. 2 & 3Previously issued on CDA66858034571154404
CDH55442 	WARLOCK: SongsPreviously issued on CDA66736034571154428
CDH55443 	Epiphany at St Paul'sPreviously issued on CDA67269034571154435
CDH55444 	LANGLAIS: Missa Salve regina & Messe solennellePreviously issued on CDA66270034571154442
CDH55445 	Hear my prayerPreviously issued on CDA66439034571154459
CDH55446 	PRAETORIUS: Christmas Music  Superseded by CDA66200034571154466
CDH55447 	BLOW/PURCELL: Countertenor DuetsPreviously issued on CDA66253034571154473
CDH55448 	POULENC: Mass & MotetsPreviously issued on CDA66664034571154480
CDH55449 	PALESTRINA: Missa Dum complerentur & other sacred musicPreviously issued on CDA67353034571154497
CDH55450 	SCRIABIN: The Complete Préludes, Vol. 1 – Opp. 2-16Previously issued on CDA67057/8034571154503
CDH55451 	SCRIABIN: The Complete Preludes, Vol. 2 – Opp. 17-74Previously issued on CDA67057/8034571154510
CDH55452 	VICTORIA: Missa Dum complerentur, Hymns & SequencesPreviously issued on CDA66886034571154527
CDH55454 	GRAINGER: Rambles & ReflectionsPreviously issued on CDA67279034571154541
CDH55455 	COUPERIN F: Leçons de TénèbresPreviously issued on CDA66474034571154558
CDH55456 	HOWELLS: Choral MusicPreviously issued on CDA67494034571154565
CDH55457 	CHAUSSON/INDY: String QuartetsPreviously issued on CDA67097034571154572
CDH55458 	RACHMANINOV: The TranscriptionsPreviously issued on CDA66486034571154589
CDH55459 	STANFORD: String Quartets  Temporarily out of stockPreviously issued on CDA67434034571154596
CDH55460 	SCHUBERT: OctetPreviously issued on CDA67339034571154602
CDH55461 	WALLACE: Symphonic PoemsPreviously issued on CDA66848034571154619
CDH55462 	Time stands stillPreviously issued on CDA66186034571154626
CDH55463 	Advent at St Paul's  Superseded by CDA66994034571154633
CDH55464 	COLES: Music from Behind the lines  Superseded by CDA67293034571154640
CDH55465 	WALLACE: Creation Symphony & other works  Superseded by CDA66987034571154657
CDH55466 	KORNGOLD/SCHOENBERG: Sextet & Verklärte NachtPreviously issued on CDA66425034571154664
CDH55467 	STRAVINSKY: Les Noces & other choral musicPreviously issued on CDA66410034571154671
CDH55470 	VILLA-LOBOS: Missa São Sebastião & other sacred music  Superseded by CDA66638034571154701
CDH55471 	SIBELIUS: Songs  Temporarily out of stockPreviously issued on CDA67318034571154718
CDH55472 	DVORÁK: Piano Quintet & String QuintetPreviously issued on CDA66796034571154725
CDH55474 	BRUCKNER: Symphony No. 3Previously issued on CDA67200034571154749
CDH55475 	DURUFLÉ: The Complete Organ MusicPreviously issued on CDA66368034571154756
CDH55477 	European Light Music ClassicsPreviously issued on CDA66998034571154770
CDH55478 	BACH C P E: Die Auferstehung und Himmelfahrt JesuPreviously issued on CDA67364034571154787
CDH55479 	BEETHOVEN: Early CantatasPreviously issued on CDA66880034571154794
CDH88005 	Music for Organ and Brass Band  Superseded by CDH55003034571180052
CDH88006 	Service high & anthems clear034571180069
CDH88008 	All in the April evening034571180083
CDH88009 	Creole Belles034571180090
CDH88010 	SCHUBERT/HUMMEL: Trout Quintet/Quintet in E flat  Superseded by CDH55427034571180106
CDH88011 	DOWLAND/CAMPION: It fell on a summer's day034571180113
CDH88012 	VIVALDI: The Four Seasons034571180120
CDH88013 	English music for brass  Superseded by CDH55070034571180137
CDH88014 	Oboe Concertos  Superseded by CDH55034034571180144
CDH88015 	The Concerto in Europe  Superseded by CDH55035034571180151
CDH88016 	BARBER: Piano Music034571180168
CDH88017 	MUSSORGSKY: Pictures at an Exhibition  Superseded by CDH55003034571180175
CDH88018 	DEBUSSY/RAVEL: String Quartets  Rights no longer controlled by Hyperion034571180182
CDH88019 	SMETANA: Dreams & PolkasPreviously issued on BVR312034571180199
CDH88020 	SCHUMANN: Spring Symphony034571180205
CDH88021 	SHAKESPEARE: The Sonnets, Vol. 1034571180212
CDH88022 	SHAKESPEARE: The Sonnets, Vol. 2034571180229
CDH88023 	My Lagan Love034571180236
CDH88024 	Songs of the Hebrides034571180243
CDH88025 	Concertos for the Kingdom of the Two Sicilies  Superseded by CDH55005034571180250
CDH88026 	Variations, Passacaglias & Chaconnes034571180267
CDH88027 	Classical Folk Guitar034571180274
CDH88028 	Baroque Christmas Music  Superseded by CDH55048034571180281
CDH88029 	TCHAIKOVSKY: 18 Piano Pieces, Op. 72034571180298
CDH88030 	Favourite Classics  Superseded by CDH55001034571180304
CDH88031 	Joy to the World  Superseded by CDH55161034571180311
CDH88032 	BEETHOVEN: String Quartets, Op. 74 & 95034571180328
CDH88033 	BACH C P E: Flute Concerto & Sonatas034571180335
CDH88034 	SCHUBERT: Impromptus034571180342
CDH88035 	L'Après-midi d'un dinosaur034571180359
CDH88036 	Praise to the Lord  Superseded by CDH55036034571180366
CDH88037 	HAYDN: Concertos  Superseded by CDH55007034571180373
CDH88038 	Favourite Encores  Superseded by CDH55002034571180380
CDH88039 	SCHUMANN: Album for the Young  Superseded by CDH55039034571180397
CDH88045 	GERSHWIN: Piano Music  Superseded by CDH55006034571180458
CDHLD7510 	VAUGHAN WILLIAMS: The Wasps5065001341106
CDHLD7511 	SHOSTAKOVICH: Symphonies Nos. 5 & 105065001341113
CDHLD7520 	ELGAR: The Dream of Gerontius5065001341199
CDHLD7525 	WAGNER: Götterdämmerung5065001341236
CDHLD7526 	ELGAR: The Kingdom5065001341250
CDHLD7527 	DEBUSSY/MATTHEWS: Préludes5065001341267
CDHLD7531 	WAGNER: Die Walküre5065001341373
CDHLD7534 	ELGAR: The Apostles5065001341380
CDHLD7539 	WAGNER: Parsifal5065001341458
CDHLD7541 	MAHLER: Symphony No. 95065001341472
CDHLD7546 	BRAHMS: Piano Concertos5065001341526
CDHLD7549 	WAGNER: Das Rheingold5065001341540
CDHLD7551 	WAGNER: Siegfried5065001341601
CDHLD7557 	VAUGHAN WILLIAMS: The Complete Symphonies5065001341823
CDHLD7558 	VAUGHAN WILLIAMS: Sinfonia antartica & Symphony No. 95065001341816
CDHLD7564 	ELGAR: Symphonies Nos. 1 & 25065001341946
CDHLD7565 	BRITTEN: The Prince of the Pagodas5065001341953
CDHLL7500 	ELGAR: Symphony No. 1 & In the South5065001341007
CDHLL7501 	ELGAR: Enigma Variations & other works5065001341014
CDHLL7502 	NIELSEN: Symphony No. 5 & Flute Concerto5065001341021
CDHLL7503 	DELIUS/BUTTERWORTH: English Rhapsody5065001341038
CDHLL7504 	Christmas Classics5065001341045
CDHLL7505 	ELGAR: Falstaff & other works5065001341052
CDHLL7506 	SHOSTAKOVICH: Symphonies Nos. 1 & 65065001341069
CDHLL7507 	ELGAR: Symphony No. 2 & Introduction and Allegro5065001341076
CDHLL7508 	STRAUSS: Don Juan, Macbeth & Lieder5065001341083
CDHLL7509 	ELGAR: A self-portrait5065001341090
CDHLL7512 	English landscapes5065001341120
CDHLL7513 	DEBUSSY: La mer & Préludes5065001341132
CDHLL7514 	SIBELIUS: Symphonies Nos. 1 & 35065001341144
CDHLL7515 	MATTHEWS C: Alphabicycle Order & Horn Concerto5065001341151
CDHLL7516 	SIBELIUS: Symphony No. 2, Oceanides & Pohjola5065001341168
CDHLL7517 	WAGNER: Opera Preludes5065001341175
CDHLL7518 	DEBUSSY: Jeux & Préludes5065001341182
CDHLL7521 	ELGAR: Violin Concerto5065001341229
CDHLL7523 	IRELAND: Mai-Dun & other orchestral works5065001341205
CDHLL7524 	BRUCKNER: Symphony No. 95065001341212
CDHLL7528 	English Spring5065001341328
CDHLL7529 	VAUGHAN WILLIAMS: A London Symphony & Oboe Concerto5065001341359
CDHLL7533 	VAUGHAN WILLIAMS: Symphonies Nos. 5 & 85065001341397
CDHLL7535 	HOLST/DELIUS: The Hymn of Jesus, Sea Drift & Cynara5065001341403
CDHLL7536 	ELGAR: Sea Pictures, Pomp and Circumstance & Polonia5065001341410
CDHLL7537 	SHOSTAKOVICH: Symphony No. 75065001341427
CDHLL7538 	MATTHEWS C: No man's land, Crossing the alps & Aftertones5065001341441
CDHLL7540 	VAUGHAN WILLIAMS: Pastoral Symphony & other works5065001341434
CDHLL7542 	VAUGHAN WILLIAMS: A Sea Symphony5065001341489
CDHLL7543 	SIBELIUS: Symphonies Nos. 5 & 75065001341496
CDHLL7544 	ELGAR/BAX: For the fallen5065001341519
CDHLL7545 	A Christmas Celebration5065001341502
CDHLL7547 	VAUGHAN WILLIAMS: Symphonies Nos. 4 & 65065001341533
CDHLL7548 	ELGAR: The Wand of Youth suites & other works5065001341557
CDHLL7550 	SHOSTAKOVICH: Symphony No. 5 & Pushkin Romances5065001341564
CDHLL7552 	DEBUSSY: Nocturnes & other orchestral works5065001341663
CDHLL7553 	SIBELIUS: Symphonies Nos 4 & 65065001341717
CDHLL7554 	DEBUSSY: Images & other orchestral works5065001341724
CDHLL7556 	VAUGHAN WILLIAMS: Job & Songs of travel5065001341779
CDHLL7559 	A Shropshire Lad5065001341854
CDHLL7560 	STRAVINSKY: The soldier's tale5065001341908
CDHLL7562 	TABAKOVA: Orpheus' Comet, Earth Suite & Concertos5065001341939
CDHLL7567 	ADÈS/LEITH/MARSEY: Shanty & other new works  July 2025 release5065001341977
CDJ33001 	SCHUBERT: The Hyperion Schubert Edition, Vol. 01 – Goethe & Schiller Settings034571130019
CDJ33002 	SCHUBERT: The Hyperion Schubert Edition, Vol. 02 – Schubert's Water Songs034571130026
CDJ33003 	SCHUBERT: The Hyperion Schubert Edition, Vol. 03 – Schubert & his Friends I034571130033
CDJ33004 	SCHUBERT: The Hyperion Schubert Edition, Vol. 04 – Schubert & his Friends II034571130040
CDJ33005 	SCHUBERT: The Hyperion Schubert Edition, Vol. 05 – Schubert & the Countryside034571130057
CDJ33006 	SCHUBERT: The Hyperion Schubert Edition, Vol. 06 – Schubert & the Nocturne I034571130064
CDJ33007 	SCHUBERT: The Hyperion Schubert Edition, Vol. 07 – Schubert in 1815 I034571130071
CDJ33008 	SCHUBERT: The Hyperion Schubert Edition, Vol. 08 – Schubert & the Nocturne II034571130088
CDJ33009 	SCHUBERT: The Hyperion Schubert Edition, Vol. 09 – Schubert & the Theatre034571130095
CDJ33010 	SCHUBERT: The Hyperion Schubert Edition, Vol. 10 – Schubert in 1815 II  Temporarily out of stock034571130101
CDJ33011 	SCHUBERT: The Hyperion Schubert Edition, Vol. 11 – Schubert & Death034571130118
CDJ33012 	SCHUBERT: The Hyperion Schubert Edition, Vol. 12 – The Young Schubert I034571130125
CDJ33013 	SCHUBERT: The Hyperion Schubert Edition, Vol. 13 – Lieder Sacred & Profane034571130132
CDJ33014 	SCHUBERT: The Hyperion Schubert Edition, Vol. 14 – Schubert & the Classics034571130149
CDJ33015 	SCHUBERT: The Hyperion Schubert Edition, Vol. 15 – Schubert & the Nocturne III034571130156
CDJ33016 	SCHUBERT: The Hyperion Schubert Edition, Vol. 16 – Schiller Settings  Temporarily out of stock034571130163
CDJ33017 	SCHUBERT: The Hyperion Schubert Edition, Vol. 17 – Schubert in 1816034571130170
CDJ33018 	SCHUBERT: The Hyperion Schubert Edition, Vol. 18 – Schubert & the Strophic Song034571130187
CDJ33019 	SCHUBERT: The Hyperion Schubert Edition, Vol. 19 – Songs about flowers & nature034571130194
CDJ33020 	SCHUBERT: The Hyperion Schubert Edition, Vol. 20 – An 1815 Schubertiad I034571130200
CDJ33021 	SCHUBERT: The Hyperion Schubert Edition, Vol. 21 – Schubert in 1817 & 1818034571130217
CDJ33022 	SCHUBERT: The Hyperion Schubert Edition, Vol. 22 – An 1815 Schubertiad II  Temporarily out of stock034571130224
CDJ33023 	SCHUBERT: The Hyperion Schubert Edition, Vol. 23 – Songs of 1816034571130231
CDJ33024 	SCHUBERT: The Hyperion Schubert Edition, Vol. 24 – A Goethe Schubertiad034571130248
CDJ33025 	SCHUBERT: The Hyperion Schubert Edition, Vol. 25 – Die schöne Müllerin  Superseded by CDA30020034571130255
CDJ33026 	SCHUBERT: The Hyperion Schubert Edition, Vol. 26 – An 1826 Schubertiad034571130262
CDJ33027 	SCHUBERT: The Hyperion Schubert Edition, Vol. 27 – Schubert & the Schlegels034571130279
CDJ33028 	SCHUBERT: The Hyperion Schubert Edition, Vol. 28 – An 1822 Schubertiad034571130286
CDJ33029 	SCHUBERT: The Hyperion Schubert Edition, Vol. 29 – Schubert in 1819 & 1820034571130293
CDJ33030 	SCHUBERT: The Hyperion Schubert Edition, Vol. 30 – Winterreise  Superseded by CDA30021034571130309
CDJ33031 	SCHUBERT: The Hyperion Schubert Edition, Vol. 31 – Schubert & Religion034571130316
CDJ33032 	SCHUBERT: The Hyperion Schubert Edition, Vol. 32 – An 1816 Schubertiad034571130323
CDJ33033 	SCHUBERT: The Hyperion Schubert Edition, Vol. 33 – The Young Schubert034571130330
CDJ33034 	SCHUBERT: The Hyperion Schubert Edition, Vol. 34 – Schubert 1817-1821034571130347
CDJ33035 	SCHUBERT: The Hyperion Schubert Edition, Vol. 35 – Schubert 1822-1825034571130354
CDJ33036 	SCHUBERT: The Hyperion Schubert Edition, Vol. 36 – Schubert in 1827034571130361
CDJ33037 	SCHUBERT: The Hyperion Schubert Edition, Vol. 37 – The Final Year034571130378
CDJ33051/3 	Songs by Schubert's contemporaries034571130514
CDJ33101 	SCHUMANN: The Songs of Robert Schumann, Vol. 01 – Christine Schäfer034571131016
CDJ33102 	SCHUMANN: The Songs of Robert Schumann, Vol. 02 – Simon Keenlyside034571131023
CDJ33103 	SCHUMANN: The Songs of Robert Schumann, Vol. 03 – Juliane Banse034571131030
CDJ33104 	SCHUMANN: The Songs of Robert Schumann, Vol. 04 – Oliver Widmer & Stella Doufexis034571131047
CDJ33105 	SCHUMANN: The Songs of Robert Schumann, Vol. 05 – Christopher Maltman034571131054
CDJ33106 	SCHUMANN: The Songs of Robert Schumann, Vol. 06 – McGreevy, Doufexis, Thompson & Loges034571131061
CDJ33107 	SCHUMANN: The Songs of Robert Schumann, Vol. 07 – Dorothea Röschmann & Ian Bostridge034571131078
CDJ33108 	SCHUMANN: The Songs of Robert Schumann, Vol. 08 – Maltman, Lemalu & Padmore  Temporarily out of stock034571131085
CDJ33109 	SCHUMANN: The Songs of Robert Schumann, Vol. 09 – Ann Murray & Felicity Lott034571131092
CDJ33110 	SCHUMANN: The Songs of Robert Schumann, Vol. 10 – Kate Royal034571131108
CDJ33111 	SCHUMANN: The Songs of Robert Schumann, Vol. 11 – Hanno Müller-Brachmann034571131115
CDJ33121 	BRAHMS: The Complete Songs, Vol. 1 – Angelika Kirchschlager034571131214
CDJ33122 	BRAHMS: The Complete Songs, Vol. 2 – Christine Schäfer  Temporarily out of stock034571131221
CDJ33123 	BRAHMS: The Complete Songs, Vol. 3 – Simon Bode034571131238
CDJ33124 	BRAHMS: The Complete Songs, Vol. 4 – Robert Holl034571131245
CDJ33125 	BRAHMS: The Complete Songs, Vol. 5 – Christopher Maltman034571131252
CDJ33126 	BRAHMS: The Complete Songs, Vol. 6 – Ian Bostridge034571131269
CDJ33127 	BRAHMS: The Complete Songs, Vol. 7 – Benjamin Appl034571131276
CDJ33128 	BRAHMS: The Complete Songs, Vol. 8 – Harriet Burns034571131283
CDJ33129 	BRAHMS: The Complete Songs, Vol. 9 – Robin Tritschler034571131290
CDJ33130 	BRAHMS: The Complete Songs, Vol. 10 – Sophie Rennert034571131306
CDP11001 	Psalms from St Paul's, Vol. 01034571110011
CDP11002 	Psalms from St Paul's, Vol. 02034571110028
CDP11003 	Psalms from St Paul's, Vol. 03034571110035
CDP11004 	Psalms from St Paul's, Vol. 04034571110042
CDP11005 	Psalms from St Paul's, Vol. 05034571110059
CDP11006 	Psalms from St Paul's, Vol. 06034571110066
CDP11007 	Psalms from St Paul's, Vol. 07034571110073
CDP11008 	Psalms from St Paul's, Vol. 08034571110080
CDP11009 	Psalms from St Paul's, Vol. 09034571110097
CDP11010 	Psalms from St Paul's, Vol. 10034571110103
CDP11011 	Psalms from St Paul's, Vol. 11034571110110
CDP11012 	Psalms from St Paul's, Vol. 12034571110127
CDP12101 	The English Hymn, Vol. 1 – Christ Triumphant034571121017
CDP12102 	The English Hymn, Vol. 2 – Jerusalem the Golden  Temporarily out of stock034571121024
CDP12103 	The English Hymn, Vol. 3 – Hills of the north, rejoice  Temporarily out of stock034571121031
CDP12104 	The English Hymn, Vol. 4 – All things bright and beautiful034571121048
CDP12105 	The English Hymn, Vol. 5 – Lead, kindly Light034571121055
CDS44001/3 	MOZART: The Six 'Haydn' String QuartetsPreviously issued on CDA66170, 66188,66234034571140018
CDS44011/3 	MOZART: Complete Music for FlutePreviously issued on CDA66391, 66392, 66393034571140117
CDS44021/3 	MOZART: Six Piano TriosPreviously issued on CDA66093, 66125, 66148034571140216
CDS44031/8 	PURCELL: The Complete Odes & Welcome SongsPreviously issued on 314,349,412, 456,587,598034571140315
CDS44041/8 	RACHMANINOV: The Complete Solo Piano Music034571140414
CDS44051/3 	MENDELSSOHN: Complete String QuartetsPreviously issued on CDA66397, 66579 / 615034571140513
CDS44061/3 	DEBUSSY: Piano MusicPreviously issued on CDA66416, 66487; 66495034571140612
CDS44071/3 	BRUCKNER: The Masses  Temporarily out of stockPreviously issued on CDA66177, 66599, 66650034571140711
CDS44081/3 	MENDELSSOHN: Twelve String SymphoniesPreviously issued on CDA66561/3034571140810
CDS44091/6 	SHOSTAKOVICH: The complete String QuartetsPreviously issued on CDA67153/8034571140919
CDS44101/12 	The Psalms of David034571141015
CDS44121/36 	BACH: The Complete Organ Music034571141213
CDS44141/51 	PURCELL: The Complete Sacred Music034571141411
CDS44161/3 	PURCELL: The complete secular solo songs034571141619
CDS44171/81 	VIVALDI: The Complete Sacred Music034571141718
CDS44191/7 	SIMPSON: The Complete Symphonies034571141916
CDS44201/40 	SCHUBERT: The Complete Songs034571142012
CDS44241/3 	VERACINI: Sonate accademichePreviously issued on CDA66871/3034571142418
CDS44251/3 	Gothic Voices Award WinnersPreviously issued on CDA66039, 66238, 66286034571142517
CDS44261/4 	British Light Music Classics034571142616
CDS44271/3 	HANDEL: Opera AriasPreviously issued on CDA66860, 67128, 66950034571142715
CDS44281/6 	BANTOCK: Orchestral MusicPreviously issued on CDA67250, CDA67395034571142814
CDS44291/4 	BACH: The Well-tempered Clavier  Superseded by CDA67301/2034571142913
CDS44301/5 	BEETHOVEN: Symphonies034571143019
CDS44311/3 	STANFORD: Sacred Choral MusicPreviously issued on CDA66964/5, CDA66974034571143118
CDS44321/4 	VAUGHAN WILLIAMS: Choral Works034571143217
CDS44331/42 	BRAHMS: The Complete Chamber Music034571143316
CDS44351/66 	CHOPIN: The Complete WorksPreviously issued on Arabesque034571143514
CDS44371/4 	HAYDN: The London Symphonies  Temporarily out of stock034571143712
CDS44381/3 	PURCELL: The Complete Ayres for the TheatrePreviously issued on CDA67001/3034571143811
CDS44391/3 	LOCATELLI: L'Arte del ViolinoPreviously issued on CDA66721/3034571143910
CDS44401/10 	The Sixteen & The Golden Age of PolyphonyPreviously issued on 66073, 55086, 51-6,22021-2034571144016
CDS44411/3 	HANDEL: 20 Sonatas, Op. 1Previously issued on CDA66921/3034571144115
CDS44421/35 	BACH: Angela Hewitt plays Bach (2010 collection)034571144214
CDS44441/50 	SCHUMANN: The Complete Songs034571144412
CDS44451/8 	GOTTSCHALK: The Complete Solo Piano Music034571144511
CDS44461/7 	BYRD: The Complete Keyboard MusicPreviously issued on CDA66551/7034571144610
CDS44471/4 	BEETHOVEN: The Complete Music for Piano Trio034571144719
CDS44501/98 	LISZT: The Complete Piano Music034571145013
CDS44511/3 	HANDEL: OttonePreviously issued on CDA66751/3034571145112
CDS44601/4 	FAURÉ: The Complete Music for PianoPreviously issued on CDA66911/4034571146010
CDS44611/4 	MARTINU: The complete music for violin & orchestra  Temporarily out of stockPreviously issued on CDA67671, 2, 3 & 4034571146119
COLCD106 	Christmas Night – Carols of the Nativity  Superseded by CSCD526Previously issued on 29/09/2020040888010623
COLCD107 	Faire is the Heaven – Music of the English Church040888010722
COLCD113 	Hail, gladdening Light – Music of the English Church040888011323
COLCD124 	Images of Christ040888012429
COLCD125 	Illumina040888012528
COLCD126 	Sing, ye Heavens – Hymns for all time040888012627
COLCD127 	Blessed spirit – Music of the soul's journey040888012726
COLCD129 	RUTTER: Mass of the Children & other sacred music040888012924
COLCD130 	O'REGAN: Voices040888013020
COLCD131 	Lighten our Darkness – Music for the close of day incuding Compline040888013129
COLCD132 	HANDEL: Messiah040888013228
COLCD133 	A Christmas Festival040888013327
COLCD134 	The Sacred Flame – European Sacred Music040888013426
COLCD135 	RUTTER: A Song in Season – Sacred music by John Rutter040888013525
COLCD136 	This is the day – Music on royal occasions040888013624
COLCD138 	RUTTER: The Gift of Life & other sacred music040888013822
COLCD139 	RUTTER: Visions & Requiem040888013921
COLV603 	RUTTER: I sing of a maiden & other carols040888060383
COLV604 	RUTTER: Lead, kindly Light040888060482
CSCD502 	Stillness and Sweet Harmony040888050223
CSCD503 	Christmas Star – Carols for the Christmas Season040888050322
CSCD504 	RUTTER: Requiem & Magnificat040888050421
CSCD505 	There is sweet music – English Choral Songs, 1890-1950040888050520
CSCD506 	POULENC: Gloria & other sacred music040888050629
CSCD507 	BYRD: Ave verum corpus & other works040888050728
CSCD508 	Hail! Queen of Heaven – Music in honour of the Virgin Mary040888050827
CSCD509 	Cambridge Singers A Cappella040888050926
CSCD510 	RUTTER: The John Rutter Christmas Album040888051022
CSCD511 	Flora gave me fairest flowers040888051121
CSCD512 	The Cambridge Singers Christmas Album040888051220
CSCD513 	RUTTER: Three Musical Fables040888051329
CSCD514 	RUTTER: Be thou my vision & other sacred music040888051428
CSCD515 	RUTTER: Gloria & other sacred music040888051527
CSCD516 	RUTTER: Fancies & other works040888051626
CSCD517 	The Sprig of Thyme040888051725
CSCD519 	HANDEL: Messiah (Highlights)040888051923
CSCD520 	FAURÉ: Requiem & other sacred music040888052029
CSCD521 	BENNETT: Sea Change & other choral music040888052128
CSCD522 	RUTTER: O praise the Lord of heaven040888052227
CSCD523 	RUTTER: Feel the Spirit & Birthday Madrigals040888052326
CSCD524 	Stanford and Howells Remembered040888052425
CSCD525 	A banquet of voices040888052524
CSCD526 	Christmas Night – Carols of the NativityPreviously issued on COLCD106040888052623
CSCDS402 	Classical Tranquillity040888040224
DVDA68000 	HAMELIN: It's all about the music  Deleted034571880006
DVDA68001 	HEWITT: Bach Performance on the Piano  Deleted034571880013
GAW21017 	MARTIN/PIZZETTI: Mass & Messa di Requiem  Superseded by CDA67017034571110172
GAW21055 	BEETHOVEN: Songs  Superseded by CDA67055034571110554
GAW21238 	The Service of Venus & Mars  Superseded by CDH55290034571112381
GAW21286 	A Song for Francesca  Superseded by CDH55291034571112862
GAW21299 	SIMPSON: Symphony No. 9  Superseded by CDA66299034571112992
GAW21580 	The Romantic Piano Concerto, Vol. 02 – Medtner 2 & 3  Superseded by CDA66580034571115801
GAW21790 	The Romantic Piano Concerto, Vol. 11 – Sauer & Scharwenka  Superseded by CDA66790034571117904
GIMBD641 	ALLEGRI: Miserere  Deleted755138164109
GIMBX301 	THE TALLIS SCHOLARS: Finest Recordings, Vol. 1 - 1980-1989755138130128
GIMBX302 	THE TALLIS SCHOLARS: Finest Recordings, Vol. 2 - 1990-1999755138130227
GIMBX303 	THE TALLIS SCHOLARS: Finest Recordings, Vol. 3 - 2000-2009755138130326
GIMDN902 	BYRD: Playing Elizabeth's Tune  Deleted755138190207
GIMDP901 	BYRD: Playing Elizabeth's Tune  Deleted755138190108
GIMDP903 	PALESTRINA: The Tallis Scholars Live in Rome  Deleted755138190306
GIMSA540 	GUERRERO: Missa Surge propera  Deleted755138154001
GIMSA592 	BYRD: Playing Elizabeth's Tune  Deleted755138159204
GIMSE401 	ALLEGRI: Miserere755138140127
GIMSE403 	TALLIS SCHOLARS: English Madrigals755138140325
HOUGH1 	The Stephen Hough Piano Collection034571100319
HYP12 	The Essential Hyperion  Deleted034571100128
HYP20 	The Essential Hyperion 2  Deleted034571100234
HYP200 	An Intro to The Hyperion Schubert Edition  Deleted034571100197
HYP30 	A Treasury of English Song  Deleted034571100302
HYP41 	Dreamland034571100418
HYP650 	BRUCKNER: Mass in D minor & Te Deum  Superseded by CDH55356034571100258
KGS0001 	Nine Lessons & Carols822231700128
KGS0002 	MOZART: Requiem realisations822231700227
KGS0003 	BRITTEN: Saint Nicolas & other choral works822231700326
KGS0004 	English Hymn Anthems822231700425
KGS0005 	FAURÉ: Requiem & other works822231700524
KGS0006 	After hours822231700623
KGS0007 	Favourite Carols from King's822231700722
KGS0010 	LISZT/REUBKE/MENDELSSOHN: Organ works822231701026
KGS0011 	Evensong Live 2015822231701125
KGS0012 	GABRIELI G: 1615 Gabrieli in Venice822231701224
KGS0014 	Hymns from King's822231701422
KGS0015 	Evensong Live 2016822231701521
KGS0016 	DURUFLÉ: Requiem & other choral works822231701620
KGS0017 	Twelve Days of Christmas822231701729
KGS0018 	BACH: St John Passion822231701828
KGS0020 	The King of Instruments - A Voice Reborn822231702023
KGS0021 	BERNSTEIN/VAUGHAN WILLIAMS: Chichester Psalms & Dona nobis pacem822231702160
KGS0023-D 	Love from King's822231702368
KGS0024-D 	BYRD: Motets822231702467
KGS0025-D 	MESSIAEN: La Nativité du Seigneur822231702566
KGS0026 	Tecchler's Cello - From Cambridge to Rome822231702627
KGS0032-D 	HOWELLS: An English Mass, Cello Concerto & other works822231703266
KGS0033-D 	100 Years of Nine Lessons & Carols822231703365
KGS0034-D 	The music of King's – Choral favourites from Cambridge822231703464
KGS0035-D 	BRUCKNER: Mass in E minor & motets822231703563
KGS0036-D 	A Festival of Nine Lessons & Carols – The Centenary Service822231703662
KGS0037-D 	BACH: St Matthew Passion822231703761
KGS0038-D 	Evensong Live 2019822231703860
KGS0049-D 	BACH: Goldberg Variations822231704966
KGS0050-D 	WALLEN: Peace on Earth & other choral works822231705055
KGS0052-D 	Proud Songsters – English solo song822231705260
KGS0053-D 	DURUFLÉ: Complete organ works822231705369
KGS0060-D 	In the bleak midwinter822231706069
KGS0065-D 	Now the green blade riseth – Choral music for Easter822231706564
KGS0066-D 	MUHLY/GOODMAN: The Street822231706663
KGS0067-D 	My soul, what fear you?822231706762
KGS0069-D 	RUTTER: Orchestral carols822231706960
KGS0071-D 	RUTTER: Visions822231707165
KING2 	Essential Purcell034571100159
KING3 	The James Bowman Collection034571100180
KING4 	The King's Consort Baroque Collection  Deleted034571100203
KING5 	Essential Bach  Deleted034571100241
KING6 	Essential Handel034571100289
KING7 	The King's Consort Collection  Deleted034571100296
LISZT1 	LISZT: Piano Music – An introduction to the complete recording  Deleted034571100227
LPA66039 	HILDEGARD: A feather on the breath of God (Vinyl Edition  Deleted034571996042
LPA67331 	SAINT-SAËNS: The complete works for piano & orch (Vinyl Ed034571995847
LPA67425 	SHOSTAKOVICH: Piano Concertos (Vinyl Edition)  Deleted034571996011
LPA67795 	MENDELSSOHN: Violin Concertos (Vinyl Edition)  Deleted034571996035
LPA67849 	CHOPIN: The Complete Waltzes (Vinyl Edition)  Temporarily out of stock034571996059
LPA68077 	ELGAR/WALTON: Cello Concertos (Vinyl Edition)034571995830
LPA68146 	BACH: Goldberg Variations (Vinyl Edition)034571996028
LPA68161 	DEBUSSY: Images, Estampes & Children's (Vinyl Edition)034571995823
LPA68256 	English Motets (Vinyl Edition)  Temporarily out of stock034571995861
LPA68330 	MENDELSSOHN/MENDELSSOHN F: String Quartets (Vinyl Edition)034571995854
LPA68455 	HOUGH: Piano Concerto, Sonatina & Pa (Vinyl Edition)034571995816
LSO0001 	DVORÁK: Symphony No. 9822231100126
LSO0007 	BERLIOZ: Symphonie fantastique822231100720
LSO0029 	HOLST: The Planets822231102922
LSO0245 	BEETHOVEN: Piano Concerto No. 2822231124528
LSO0267 	MAXWELL DAVIES: Symphony No. 10822231126720
LSO0363-D 	PROKOFIEV: Symphony No. 1822231136354
LSO0366-D 	VAUGHAN WILLIAMS: Fantasia on a theme by Thomas Tallis822231136651
LSO0379-D 	PROKOFIEV: Symphony No. 5822231137955
LSO0390-D 	PROKOFIEV: Symphony No. 6822231139058
LSO0391-D 	PROKOFIEV: Symphony No. 3822231139157
LSO0516 	SMETANA: Ma vlást822231101628
LSO0550 	SHOSTAKOVICH: Symphony No. 5822231105022
LSO0570-D 	BRAHMS: Symphonies Nos. 1-4822231157069
LSO0571-D 	DVORÁK: Symphonies Nos. 6-9822231157168
LSO0572-D 	ELGAR: Symphonies Nos. 1-3 & other works822231157267
LSO0578 	BEETHOVEN: Symphony No. 7 & Triple Concerto822231157823
LSO0580 	BEETHOVEN: Symphony No. 3 & Leonore Overture No. 2822231158028
LSO0582 	BEETHOVEN: Symphonies Nos. 2 & 6822231158226
LSO0587 	BEETHOVEN: Symphonies Nos. 4 & 8822231158721
LSO0590 	BEETHOVEN: Symphonies Nos. 1 & 5822231159025
LSO0592 	BEETHOVEN: Symphony No. 9822231159223
LSO0607 	HANDEL: Messiah822231160724
LSO0609 	ELGAR: Engima Variations & other works822231160922
LSO0627 	MOZART: Requiem822231162728
LSO0660 	MAHLER: Symphony No. 3822231166023
LSO0661 	MAHLER: Symphony No. 6822231166122
LSO0662 	MAHLER: Symphony No. 4822231166221
LSO0663 	MAHLER: Symphony No. 1822231166320
LSO0664 	MAHLER: Symphony No. 5822231166429
LSO0665 	MAHLER: Symphony No. 7822231166528
LSO0666 	MAHLER: Symphonies Nos. 2 & 10822231166627
LSO0668 	MAHLER: Symphony No. 9822231166825
LSO0669 	MAHLER: Symphony No. 8822231166924
LSO0675 	SIBELIUS: Symphonies Nos. 1-7822231167525
LSO0677 	RACHMANINOV: Symphony No. 2822231167723
LSO0682 	PROKOFIEV: Romeo & Juliet822231168225
LSO0683 	VERDI: Requiem822231168324
LSO0688 	RACHMANINOV/STRAVINSKY: Symphonic Dances & Symphony822231168829
LSO0692 	DEBUSSY: La mer, Jeux & Prélude822231169222
LSO0693 	RAVEL: Daphis et Chloé, Pavane & Boléro822231169321
LSO0694 	NIELSEN: Symphonies Nos. 4 & 5822231169420
LSO0701 	STRAUSS: Elektra822231170129
LSO0702 	HAYDN: Symphonies Nos. 92, 93 & 97-99822231170228
LSO0708 	HAYDN: Die Jahreszeiten822231170822
LSO0710 	TCHAIKOVSKY: Symphonies Nos. 1-3822231171027
LSO0715 	NIELSEN: Symphonies Nos. 1 & 6822231171522
LSO0716 	BRUCKNER: Symphony No. 4822231171621
LSO0719 	BRITTEN: War Requiem822231171928
LSO0720 	TIOMKIN: Greatest Film Scores822231172024
LSO0722 	NIELSEN: Symphonies Nos. 2 & 3822231172222
LSO0726 	WEBER: Der Freischütz822231172628
LSO0728 	FAURÉ/BACH: Requiem & Partitas822231172826
LSO0729 	BERLIOZ: Grand Messe des morts822231172925
LSO0731 	SZYMANOWSKI: Symphonies Nos. 1 & 2822231173120
LSO0733 	BRAHMS: Symphonies Nos. 1 & 2 & other works822231173328
LSO0737 	BRAHMS: Symphonies Nos. 3 & 4822231173724
LSO0739 	SZYMANOWSKI: Symphonies Nos. 3 & 4 & Stabat mater822231173922
LSO0744 	TURNAGE: Speranza & From the Wreckage822231174424
LSO0745-D 	BEETHOVEN: Piano Concerto No. 2 & Triple Concerto822231174561
LSO0746 	BRUCKNER: Symphony No. 9822231174622
LSO0749 	BRITTEN: The Turn of the Screw822231174929
LSO0751 	STRAVINSKY: Oedipus Rex & Apollon musagète822231175124
LSO0752 	TCHAIKOVSKY/BARTÓK: Serenade for strings & Divertimento822231175223
LSO0757 	BERLIOZ: Symphonie fantastique & Waverley Overture822231175728
LSO0760 	BERLIOZ: Harold en Italie822231176022
LSO0762 	BERLIOZ: Roméo et Juliette822231176220
LSO0765 	MENDELSSOHN/SCHUMANN: Symphony No. 3 & Piano Concerto822231176527
LSO0767 	MAXWELL DAVIES/PANUFNIK: Symphonies No. 10822231176725
LSO0769 	MENDELSSOHN: Symphonies Nos. 1 & 4822231176923
LSO0770 	SCRIABIN: Symphonies Nos. 1 & 2822231177029
LSO0771 	SCRIABIN: Symphonies Nos. 3 & 4822231177128
LSO0775 	MENDELSSOHN: Symphony No. 5 & Overtures822231177524
LSO0779 	RACHMANINOV/BALAKIREV: Symphony No. 3 & Russia822231177920
LSO0781 	RACHMANINOV: Vespers822231178125
LSO0782 	SCHUMANN: Die Paradies und die Peri822231178224
LSO0784 	RACHMANINOV/BALAKIREV: Symphony No. 1 & Tamara822231178422
LSO0786 	SCHUBERT/SHOSTAKOVICH: Death and the Maiden & Chamber Symphony822231178620
LSO0790 	DEBUSSY: Pelléas et Mélisande822231179023
LSO0792 	ELGAR/VAUGHAN WILLIAMS/BRITTEN: Tallis Fantasia & Bridge Variations822231179221
LSO0795 	MENDELSSOHN: A Midsummer Night's Dream822231179528
LSO0798 	ADÈS: Asyla, Tevot & Polaris822231179825
LSO0800 	VERDI: Requiem822231180029
LSO0802-D 	SHOSTAKOVICH: Symphonies Nos. 1 & 5822231180265
LSO0803 	MENDELSSOHN: Symphony No. 2 'Lobgesang'822231180364
LSO0804-D 	MOZART: Violin Concertos Nos. 1, 2 & 3822231180463
LSO0807-D 	MOZART: Violin Concertos Nos. 4 & 5822231180760
LSO0808-D 	HAYDN: An Imaginary Orchestral Journey822231180869
LSO0809-D 	BERLIOZ: La damnation de Faust822231180968
LSO0810-D 	TCHAIKOVSKY/MUSORGSKY: Symphony No. 4/Pictures from an exhibition822231181064
LSO0813-D 	BERNSTEIN: Wonderful Town822231181361
LSO0816-D 	RACHMANINOV: Symphonies Nos. 1-3 & Symphonic Dances822231181668
LSO0818-D 	SCHUMANN: Symphonies Nos. 2 & 4822231181866
LSO0821-D 	DEBUSSY/RAVEL: La mer & Rapsodie espagnole822231182160
LSO0822-D 	SHOSTAKOVICH: Symphony No. 8822231182269
LSO0826-D 	MENDELSSOHN: Symphonies & Overtures822231182665
LSO0827-D 	BERLIOZ: Odyssey - The Complete Colin Davis Recordings822231182764
LSO0828-D 	SHOSTAKOVICH: Symphonies Nos. 9 & 10822231182863
LSO0830-D 	BRITTEN: Spring Symphony & other works822231183068
LSO0832-D 	SHOSTAKOVICH: Symphony No. 4822231183266
LSO0833-D 	STRAUSS R/DEBUSSY: Also sprach Zarathustra & Jeux822231183365
LSO0834-D 	BERNSTEIN: Candide822231183464
LSO0836-D 	BERNSTEIN/STRAVINSKY/GOLIJOV: Nazareno822231183662
LSO0842-D 	BRUCKNER: Symphony No. 6822231184263
LSO0844-D 	SCHUMANN: Symphonies Nos. 1 & 3822231184461
LSO0850-D 	JANÁCEK: The cunning little vixen & Sinfonietta822231185062
LSO0851-D 	RACHMANINOV: Symphony No. 2822231185161
LSO0855-D 	MOZART: Wind Concertos822231185567
LSO0858-D 	TCHAIKOVSKY/RIMSKY-KORSAKOV: Symphony No. 5 & Kitezh Suite822231185864
LSO0859-D 	SHOSTAKOVICH: Symphony No. 7822231185963
LSO0862-D 	BEETHOVEN: Christ on the Mount of Olives822231186267
LSO0867-D 	VAUGHAN WILLIAMS: Symphonies Nos. 4 & 6822231186762
LSO0875-D 	BRUCKNER: Symphony No. 4822231187561
LSO0878-D 	SHOSTAKOVICH: Symphonies Nos. 6 & 15822231187868
LSO0880-D 	WEILL: The Seven Deadly Sins & other works822231188063
LSO0886-D 	RÓZSA/BARTÓK: Violin Concertos822231188667
LSO0887-D 	BRUCKNER: Symphony No. 7822231188766
LSO0888-D 	SHOSTOKOVICH: Symphony No. 11822231188865
LSO0889-D 	JANÁCEK: Katya kabanova822231188964
LSO0894-D 	MEYERBEER: Le Prophète822231189466
LSO0897-D 	JANÁCEK: Jenůfa822231189763
LSO0898-D 	MENDELSSOHN: Elijah822231189862
LSO0899-D 	RAVEL: Daphne et Chloé822231189961
LSO5061 	The Panufnik Legacies, Vol. 1822231506126
LSO5070 	The Panufnik Legacies, Vol. 2822231507024
LSO5073 	REICH: Clapping Music & other works822231507321
LSO5074-D 	STRAVINSKY: The soldier's tale822231507468
LSO5076 	STRAVINSKY/BARTÓK: The Firebird & Piano Concerto No. 3822231507628
LSO5083-D 	PAGANINI: 24 Caprices822231508366
LSO5090-D 	REICH/SIMCOCK: Percussion Quartet & Quintet822231509066
LSO5092-D 	The Panufnik Legacies, Vol. 3822231509264
LSO5094-D 	BEETHOVEN: Violin Concerto822231509462
LSO5096-D 	STRAVINSKY: Ballets822231509660
LSO5122-D 	WITTER-JOHNSON: Ocean Floor822231512264
LSO5129-D 	RISSMANN: Wonderland822231512967
LSO5135-D 	The Panufnik Legacies, Vol. 4822231513568
NOEL1 	Christmas through the ages034571100265
NOEL2 	A Christmas Present from Polyphony034571100272
NSO0001-D 	DVORÁK/COPLAND: Symphony No. 9 & Billy the Kid810038860169
NSO0002-D 	WALKER G: Sinfonia No. 1810038860268
NSO0005-D 	WALKER G: Sinfonia No. 4810038860565
NSO0007-D 	WALKER G: Five Sinfonias810038860763
NSO0008-D 	BEETHOVEN: Symphonies Nos. 1 & 3810038860862
NSO0009-D 	BEETHOVEN: Symphonies Nos. 4 & 5810038860961
NSO0010-D 	BEETHOVEN: Symphonies Nos. 6 & 8810038861067
NSO0011-D 	BEETHOVEN: Symphonies Nos. 2 & 7810038861166
NSO0012-D 	BEETHOVEN: Symphony No. 9810038861265
NSO0014-D 	SIMON (C): Tales810038861463
NSO0018-D 	SIMON (C): Symphonic works810038861869
SACDA67108 	ASTORGA/BOCCHERINI: Stabat Mater (SACD)  Deleted034571571089
SACDA67114 	Three French Piano Trios (SACD)  Deleted034571571140
SACDA67270 	HOLST/MATTHEWS: The Planets & Pluto (SACD)  Deleted034571572703
SACDA67286 	The Coronation of King George II (SACD)  Deleted034571572864
SACDA67307 	BACH: The Keyboard Concertos, Vol. 1 (SACD)  Deleted034571573076
SACDA67308 	BACH: The Keyboard Concertos, Vol. 2 (SACD)  Deleted034571573083
SACDA67371/2 	CHOPIN: Nocturnes & Impromptus (SACD)  Deleted034571573717
SACDA67375 	PÄRT: Triodion & other choral works (SACD)  Deleted034571573755
SACDA67425 	SHOSTAKOVICH/SHCHEDRIN: Piano Concertos (SACD)  Deleted034571574257
SACDA67428 	MONTEVERDI: The Sacred Music, Vol. 1 (SACD)  Deleted034571574288
SACDA67438 	MONTEVERDI: The Sacred Music, Vol. 2 (SACD)  Deleted034571574387
SACDA67449 	LAURIDSEN: Lux aeterna (SACD)  Deleted034571574493
SACDA67451/2 	BACH: The English Suites (SACD)  Deleted034571574516
SACDA67460 	MACMILLAN: Seven Last Words from the Cross (SACD)034571574608
SACDA67463 	HANDEL: St Cecilia's Day Ode (SACD)  Deleted034571574639
SACDA67475 	TAVENER: Choral Works (SACD)034571574752
SACDA67479 	VICTORIA: Ave Regina caelorum (SACD)  Deleted034571574790
SACDA67480 	COUPERIN F: Keyboard Music, Vol. 2 (SACD)  Deleted034571574806
SACDA67487 	MONTEVERDI: The Sacred Music, Vol. 3 (SACD)  Deleted034571574875
SACDA67499 	BACH: Fantasia, Aria & other works (SACD)  Deleted034571574998
SACDA67501/2 	RACHMANINOV: Piano Concertos (SACD)  Deleted034571575018
SACDA67508 	The Romantic Piano Concerto, Vol. 38 – Rubinstein & Scharwenka (SACD)  Deleted034571575087
SACDA67515 	CHABRIER: Piano Music (SACD)  Deleted034571575155
SACDA67517 	JANÁCEK: Orchestral Music (SACD)  Deleted034571575179
SACDA67518 	BEETHOVEN: Piano Sonatas, Vol. 1 (SACD)  Deleted034571575186
SACDA67519 	MONTEVERDI: The Sacred Music, Vol. 4 (SACD)  Deleted034571575193
SACDA67524 	Moon, sun & all things (SACD)  Deleted034571575247
SACDA67525 	IVES: Symphonies Nos. 2 & 3 (SACD)  Deleted034571575254
SACDA67531/2 	MONTEVERDI: Vespers (SACD)  Deleted034571575315
SACDA67540 	IVES: Symphonies Nos. 1 & 4 (SACD)  Deleted034571575407
SACDA67550 	BRAHMS: Piano Concerto No. 2 (SACD)  Deleted034571575506
SACDA67597 	RAMEAU: Keyboard Suites (SACD)  Deleted034571575971
SACDA67600 	Fire burning in snow (SACD)  Deleted034571576008
SACDA67605 	BEETHOVEN: Piano Sonatas, Vol. 2 (SACD)  Deleted034571576053
SACDA67618 	SCHUMANN: Humoreske & Sonata, Op. 11 (SACD)  Deleted034571576183
SDG101 	BACH: Cantatas, Vol. 1843183010127
SDG104 	BACH: Cantatas, Vol. 8843183010424
SDG107 	BACH: Cantatas, Vol. 24843183010721
SDG110 	BACH: Cantatas, Vol. 10843183011025
SDG113 	BACH: Cantatas, Vol. 14843183011322
SDG114 	BACH: Alles mit Gott843183011421
SDG115 	BACH: Cantatas, Vol. 19843183011520
SDG118 	BACH: Cantatas, Vol. 21843183011827
SDG121 	BACH: Cantatas, Vol. 26843183012121
SDG124 	BACH: Cantatas, Vol. 7843183012428
SDG127 	BACH: Cantatas, Vol. 15843183012725
SDG128 	BACH: Cantatas, Vol. 22843183012824
SDG131 	BACH: Cantatas, Vol. 23843183013128
SDG134 	BACH: Cantatas, Vol. 6843183013425
SDG137 	BACH: Cantatas, Vol. 16843183013722
SDG138 	BACH: Cantatas, Vol. 27843183013821
SDG141 	BACH: Cantatas, Vol. 3843183014125
SDG144 	BACH: Cantatas, Vol. 25843183014422
SDG147 	BACH: Cantatas, Vol. 5843183014729
SDG150 	BACH: Cantatas, Vol. 17843183015023
SDG153 	BACH: Cantatas, Vol. 20843183015320
SDG156 	BACH: Cantatas, Vol. 4843183015627
SDG159 	BACH: Cantatas, Vol. 9843183015924
SDG162 	BACH: Cantatas, Vol. 13843183016228
SDG165 	BACH: Cantatas, Vol. 2843183016525
SDG168 	BACH: Cantatas, Vol. 11843183016822
SDG171 	BACH: Cantatas, Vol. 12843183017126
SDG174 	BACH: Cantatas, Vol. 18843183017423
SDG177 	BACH: Eternal fire843183017720
SDG178 	BACH: Cantatas for Christmas843183017829
SDG185 	BACH: Cantatas, Vol. 28843183018529
SDG502 	BACH/HANDEL/SCARLATTI: Live at Milton Court843183050222
SDG701 	Pilgrimage to Santiago843183070121
SDG702 	BRAHMS: Symphony No. 1 & Schicksalslied843183070220
SDG703 	BRAHMS: Symphony No. 2 & Alto Rhapsody843183070329
SDG704 	BRAHMS: Symphony No. 3 & other works843183070428
SDG705 	BRAHMS: Symphony No. 4 & other works843183070527
SDG706 	BRAHMS: Ein deutsches Requiem843183070626
SDG707 	BACH: Brandenburg Concertos843183070725
SDG710 	Santiago a cappella843183071029
SDG711 	MOZART: Symphonies Nos. 39 & 41843183071128
SDG712 	BACH: St John Passion843183071227
SDG715 	BACH J C: Welt, gute Nacht843183071524
SDG716 	BACH: Motets843183071623
SDG717 	BEETHOVEN: Symphonies Nos. 5 & 7843183071722
SDG718 	BEETHOVEN: Missa solemnis843183071821
SDG719 	BACH: Easter Oratorio & Actus tragicus843183071920
SDG720 	Vigilate!843183072026
SDG721 	BEETHOVEN: Symphonies Nos. 2 & 8843183072125
SDG722 	BACH: Mass in B minor843183072224
SDG725 	BACH: St Matthew Passion843183072521
SDG728 	BACH: Magnificat & Missa in F843183072828
SDG729 	SCHUBERT/BRAHMS: Symphony No. 5 & Serenade No. 2843183072927
SDG730 	MONTEVERDI: Il ritorno d'Ulisse in patria843183073023
SDG731 	Love is come again843183073122
SDG732 	BACH: Violin Concertos843183073221
SDG733 	HANDEL: Semele843183073320
SIGCD001 	TALLIS: The Complete Works, Vol. 1635212000120
SIGCD002 	TALLIS: The Complete Works, Vol. 2635212000229
SIGCD003 	TALLIS: The Complete Works, Vol. 3635212000328
SIGCD010 	TALLIS: The Complete Works, Vol. 4635212001028
SIGCD012 	BACH: The Six Partitas635212001226
SIGCD014 	VIVALDI: 12 Sonatas for violin and continuo, Op. 2635212001424
SIGCD016 	TALLIS: The Complete Works, Vol. 5635212001622
SIGCD017 	GUERRERO: Requiem & Vespers for All Saints635212001721
SIGCD022 	TALLIS: The Complete Works, Vol. 6635212002223
SIGCD024 	BACH: Sonatas for Viola da Gamba & Harpsichord635212002421
SIGCD027 	BACH: Die Kunst der Fuge635212002728
SIGCD029 	TALLIS: The Complete Works, Vol. 7635212002926
SIGCD030 	BACH: Italian Concerto & French Overture635212003022
SIGCD034 	BACH: Music for Oboe and Harpsichord635212003428
SIGCD036 	TALLIS: The Complete Works, Vol. 8635212003626
SIGCD045 	CLEMENS NON PAPA: Missa Ecce quam bonum635212004524
SIGCD051 	SHOSTAKOVICH: Hypothetically Murdered & other works635212005125
SIGCD059 	Anthems for the 21st century635212005927
SIGCD062 	POTT: Christus635212006221
SIGCD063 	VIERNE: Symphonies pour orgue635212006320
SIGCD064 	REICH: Different Trains, Triple Quartet & Duet635212006429
SIGCD065 	Sacred Bridges635212006528
SIGCD066 	TIPPETT/PURCELL: Remember your lovers & other songs635212006627
SIGCD070 	All the ends of the earth635212007020
SIGCD072 	The exquisite hour635212007228
SIGCD073 	CHARPENTIER: Music for the Virgin Mary635212007327
SIGCD074 	HANDEL/MOZART: Messiah635212007426
SIGCD076 	LASSUS: Lamentations & Requiem635212007624
SIGCD078 	TALBOT: Path of Miracles635212007822
SIGCD079 	The Hymns Album635212007921
SIGCD080 	POTT: Meditations & Remembrances635212008027
SIGCD081 	MOZART: Piano Trios635212008126
SIGCD082 	The Triumphs of Oriana635212008225
SIGCD083 	TODD: Mass in Blue & other choral works635212008324
SIGCD084 	Royal Albert Hall Organ Restored635212008423
SIGCD085 	ALLEGRI: Miserere635212008522
SIGCD086 	TELEMANN: The Virtuoso Godfather635212008621
SIGCD087 	WEIR: On buying a horse & other songs635212008720
SIGCD088 	Ghost stories635212008829
SIGCD089 	The organ of Westminster Cathedral635212008928
SIGCD090 	Landscape & Time635212009024
SIGCD091 	BACH: Cello Suites635212009123
SIGCD092 	TIPPETT: Choral images635212009222
SIGCD093 	The Oxford Psalms635212009321
SIGCD094 	Music for the Coronation of James II, 1685635212009420
SIGCD095 	JAMES (J): Wanderer Fantasies after Schubert & Schumann635212009529
SIGCD096 	SCOTT (FG): Moonstruck & other songs635212009628
SIGCD097 	HAYDN: Piano Sonatas635212009727
SIGCD099 	Scenes of spirits635212009925
SIGCD100 	CHILCOTT: Man I sing & other choral works635212010026
SIGCD101 	Songs from the Pleasure Garden635212010129
SIGCD102 	GOTTWALD: Choral arrangements by Clytus Gottwald635212010228
SIGCD103 	METCALF: In Time of Daffodils635212010327
SIGCD104 	Beauty and the beatbox635212010426
SIGCD105 	POTT: The Cloud of Unknowing635212010525
SIGCD106 	HUGHES: A Purse of Gold – Irish Songs by Herbert Hughes635212010624
SIGCD107 	The Swingle Singers ... unwrapped635212010723
SIGCD108 	The Carols Album635212010822
SIGCD109 	MONTEVERDI: Vespers635212010921
SIGCD110 	DVORÁK: Symphonies Nos. 8 & 9635212011027
SIGCD111 	Fiddlesticks635212011126
SIGCD112 	VAUGHAN WILLIAMS/GURNEY/VENABLES: On Wenlock Edge & other songs635212011225
SIGCD113 	BACH: The Well-tempered Clavier I635212011324
SIGCD114 	The Organ of Buckingham Palace Ballroom635212011423
SIGCD115 	Hear my words635212011522
SIGCD116 	ELGAR/MYASKOVSKY: Cello Concertos635212011621
SIGCD117 	GLASS: Complete String Quartets635212011720
SIGCD118 	ELGAR/PAYNE: Symphony No. 3 & Pomp and Circumstance No. 6635212011829
SIGCD119 	The Golden Age635212011928
SIGCD121 	Simple Gifts635212012123
SIGCD122 	BRITTEN: Britten Abroad635212012222
SIGCD123 	BACH: The Well-tempered Clavier II635212012321
SIGCD124 	ROTH: Songs in time of war635212012420
SIGCD125 	The Division Flute635212012529
SIGCD126 	MESSIAEN: Chamber Works635212012628
SIGCD127 	O sacrum convivium635212012727
SIGCD128 	Songs of Innocence635212012826
SIGCD129 	Espressia – Armenian Metamorphoses635212012925
SIGCD130 	Naji Hakim – The organ of Glenalmond College635212013021
SIGCD131 	WERT: Vox in rama - Il secondo libro de motetti635212013125
SIGCD132 	BRAHMS: Symphony No. 2635212013229
SIGCD133 	SCHUBERT: Symphony No. 9635212013328
SIGCD134 	WHITE: Sacred Music635212013427
SIGCD135 	SHOSTAKOVICH: Symphony No. 5 Festive Overture635212013526
SIGCD137 	BRITTEN/SHOSTAKOVICH: Cello Concerto & Cello Symphony635212013724
SIGCD138 	KNOWLES: Poetry Serenade635212013823
SIGCD139 	BEETHOVEN: Lieder und Gesänge635212013922
SIGCD140 	Espressia – Tangos & Fantasies635212014028
SIGCD141 	Emilia635212014127
SIGCD142 	CHILCOTT: Making waves635212014226
SIGCD143 	REICH/KRAFTWERK: Electric Counterpoint & other works635212014325
SIGCD144 	BINGHAM: Remoter Worlds - Choral Music635212014424
SIGCD145 	BEETHOVEN: Lieder und Gesänge635212014523
SIGCD146 	GRANADOS: Goyescas635212014622
SIGCD147 	Romance du soir635212014721
SIGCD148 	STRAUSS: Till Eulenspiegel & Ein Heldenleben635212014820
SIGCD150 	The King's Singers Live at the BBC Proms635212015025
SIGCD151 	HOWELLS: I love all beauteous things & other works635212015124
SIGCD152 	Spanish Heroines635212015223
SIGCD153 	Razor blades, little pills and big pianos635212015322
SIGCD154 	CARLSON: Anna Karenina635212015421
SIGCD155 	LISZT: Songs635212015520
SIGCD156 	Bach Transcribed635212015629
SIGCD157 	TORELLI: The original Brandenburg Concertos635212015728
SIGCD158 	Façades - Contemporary works for saxophone635212015827
SIGCD160 	KORNGOLD: Sonnett für Wien & other songs635212016022
SIGCD161 	The Frostbound Wood & other British songs635212016121
SIGCD162 	HAWES: Song of Songs635212016220
SIGCD163 	DURUFLÉ: Requiem635212016329
SIGCD164 	RACHMANINOV: Violin Sonata & other works635212016428
SIGCD165 	STRAVINSKY: L'oiseau de feu635212016527
SIGCD166 	Yanomami - Music for choir and guitar635212016626
SIGCD167 	The Organ of St Sulpice, Paris635212016725
SIGCD168 	ELGAR: Enigma Variations635212016824
SIGCD169 	BEETHOVEN: Symphonies Nos. 3 & 5635212016923
SIGCD170 	ROSSINI: Mezzo - Scenes & Arias635212017029
SIGCD171 	Dance of the three-legged elephants635212017128
SIGCD172 	RACHMANINOV/GRIEG: Cello Sonatas635212017227
SIGCD173 	SCHOENBERG: Gurrelieder635212017326
SIGCD174 	Don't talk - just listen!635212017425
SIGCD175 	LCO Live - Haydn, Mozart & Beethoven635212017524
SIGCD176 	STAINER: The Crucifixion635212017623
SIGCD178 	HAWES: Fair Albion - Visions of England635212017821
SIGCD179 	ELGAR: Symphonies Nos. 1 & 2635212017920
SIGCD180 	Naked Byrd635212018026
SIGCD181 	HALLGRÍMSSON: Mini Stories635212018125
SIGCD182 	What sweeter music635212018224
SIGCD183 	DVORÁK: Symphonies Nos. 7 & 8635212018323
SIGCD184 	VERDI: Requiem635212018422
SIGCD185 	BACH/BUSONI/BEETHOVEN: now would all freudians please stand aside635212018521
SIGCD186 	KERNIS: Goblin Market635212018620
SIGCD188 	MAHLER: Symphony No. 9635212018828
SIGCD189 	MOZART/GLUCK/BERLIOZ: Arias635212018927
SIGCD190 	HOWELLS: Choral Music635212019023
SIGCD191 	BRAHMS: Sinfonia in B635212019122
SIGCD192 	Swimming over London635212019221
SIGCD193 	BERLIOZ: Symphonie fantastique635212019320
SIGCD194 	SHOSTAKOVICH: Symphony No. 7 'Leningrad'635212019429
SIGCD195 	STRAVINSKY/LIADOV: Petrushka, The enchanted lake & other works635212019528
SIGCD197 	POULENC: Figure humaine635212019726
SIGCD198 	PACHELBEL: Vespers635212019825
SIGCD199 	Deep in My Soul635212019924
SIGCD200 	LCO Live - Beethoven & Mendelssohn635212020029
SIGCD201 	LCO Live - Mozart, Beethoven & Rossini635212020128
SIGCD202 	A Family Christmas635212020227
SIGCD203 	METCALF: Paths of Song635212020326
SIGCD2033 	Stokowski Philadelphia raritiesPreviously issued on CalaCACD0501635212203316
SIGCD204 	VENABLES: At Midnight635212020425
SIGCD205 	STRAVINSKY/POULENC: The Rite of Spring & Les biches635212020524
SIGCD206 	LANGLAIS: Messe solennelle635212020623
SIGCD207 	METCALFE: Constant Filter & other works635212020722
SIGCD2071 	SIBELIUS: Symphonies Nos. 1 & 2Previously issued on CalaCACD0541635212207116
SIGCD208 	BERKELEY: For You635212020821
SIGCD209 	BACH: St John Passion635212020920
SIGCD2092 	DEBUSSY: Engulfed CathedralPreviously issued on Cala 1024635212209219
SIGCD2093 	DEBUSSY: Evening in GranadaPreviously issued on Cala 1025635212209318
SIGCD2094 	BORODIN: Requiem & other worksPreviously issued on Cala 1029635212209417
SIGCD2095 	MUSORGSKY: Pictures from an exhibition & from CrimeaPreviously issued on Cala 1030635212209516
SIGCD210 	Dialogues of Sorrow635212021026
SIGCD211 	LCO Live - Ravel, Fauré, Poulenc & Ibert635212021125
SIGCD212 	LEVINE: Prayers for Mankind635212021224
SIGCD213 	BACH: Motets635212021323
SIGCD214 	PROKOFIEV: Suites from Cinderella and Romeo & Juliet635212021422
SIGCD215 	BACH: Christmas Oratorio635212021521
SIGCD2159 	RAVEL: Valley of the bells & other orchestral worksPreviously issued on Cala635212215913
SIGCD216 	DEBUSSY/GLIÈRE/MOZART: Harp Concertos635212021620
SIGCD2160 	RAVEL: Five o'clock foxtrot & other orchestral worksPreviously issued on Cala635212216019
SIGCD2161 	RESPIGHI: Ballad of the gnomes & other worksPreviously issued on Cala635212216118
SIGCD2162 	SAINT-SAËNS: Africa & other orchestral worksPreviously issued on Cala 4031635212216217
SIGCD2163 	SAINT-SAËNS: Requiem & Organ SymphonyPreviously issued on Cala 4032635212216316
SIGCD2164 	GRAINGER: The warriors & other worksPreviously issued on Cala 4033635212216415
SIGCD217 	Songs of cricket635212021729
SIGCD218 	BACH: Mass in B minor635212021828
SIGCD219 	MAHLER: Symphony No. 4635212021927
SIGCD220 	SHOSTAKOVICH/WALTON: Cello Concertos635212022023
SIGCD222 	HAKIM: Hakim plays Hakim - Danish Radio organ635212022221
SIGCD223 	English Organ Music from the Temple Church635212022320
SIGCD224 	Romantic novelties for violin and orchestra635212022429
SIGCD225 	The Majesty of thy Glory635212022528
SIGCD226 	MUSORGSKY: Pictures at an exhibition635212022627
SIGCD227 	Flux635212022726
SIGCD228 	BRITTEN/POSTON: A Ceremony of Carols & An English Day-Book635212022825
SIGCD229 	TCHAIKOVSKY/RACHMANINOV: Swan Lake & Symphonic Dances635212022924
SIGCD230 	RACHMANINOV: Music for piano635212023020
SIGCD231 	VIVALDI/PIAZZOLLA: The Eight Seasons635212023129
SIGCD232 	SHEPPARD M: The soul rests eternal635212023228
SIGCD233 	These visions635212023327
SIGCD234 	HERMANN: Psycho Suite635212023426
SIGCD235 	Naked Byrd Two635212023525
SIGCD236 	Dance635212023624
SIGCD237 	MONTEVERDI: Vespers635212023723
SIGCD239 	An Irish Songbook635212023921
SIGCD244 	RODRIGO: Works for guitar and orchestra635212024423
SIGCD245 	HAKIM: Chamber music and organ works635212024522
SIGCD246 	HANDEL: Messiah635212024621
SIGCD247 	POULENC: The Complete Songs, Vol. 1635212024720
SIGCD248 	VICTORIA: Requiem635212024829
SIGCD249 	Concerti Curiosi635212024928
SIGCD250 	BRAHMS: Symphonies Nos. 1 & 3635212025024
SIGCD251 	MOZART: An Italian Journey635212025123
SIGCD252 	CHOPIN/SAINT-SAËNS: Cello Sonatas635212025222
SIGCD253 	TCHAIKOVSKY: Symphony No. 6635212025321
SIGCD254 	BEETHOVEN: Symphony No. 9635212025420
SIGCD256 	BRUCKNER: Symphony No. 4635212025628
SIGCD257 	A Choral Christmas635212025727
SIGCD258 	FROST/KARLSEN: Parapraxis & Bassoon Concertos635212025826
SIGCD259 	MAHLER: Lieder eines fahrenden Gesellen635212025925
SIGCD260 	TALBOT: Tide Harmonic635212026021
SIGCD261 	BACH: Organ Music635212026120
SIGCD262 	High Flight635212026229
SIGCD263 	POULENC: The Complete Songs, Vol. 2635212026328
SIGCD264 	RACHMANINOV: Preludes & Melodies635212026427
SIGCD265 	BACH: Mass in B minor635212026526
SIGCD266 	ELGAR: Organ Music635212026625
SIGCD267 	PARRY: Songs of Farewell635212026724
SIGCD268 	Joy to the World635212026823
SIGCD269 	Journey into light – Music for Advent & Christmas635212026922
SIGCD270 	ROTH: Shared Ground635212027028
SIGCD272 	POULENC: The Complete Songs, Vol. 3635212027226
SIGCD273 	ANDRIESSEN: Anaïs Nin & De staat635212027325
SIGCD274 	SHOSTAKOVICH/BRITTEN/PROKOFIEV: Cello Sonatas635212027424
SIGCD275 	MAHLER: Symphony No. 6635212027523
SIGCD276 	The ancient question - Jewish songs635212027622
SIGCD278 	RAMEAU: Music for keyboard635212027820
SIGCD279 	A Festival of Psalms635212027929
SIGCD280 	BERLIOZ: Grande Messe des Morts635212028025
SIGCD281 	A Song of Farewell635212028124
SIGCD282 	HAWES: Lazarus Requiem635212028223
SIGCD283 	A choral tapestry635212028322
SIGCD284 	HAKIM: Hakim plays Hakim - Dudelange organ , Vol. 1635212028421
SIGCD285 	DOVE: There was a child635212028520
SIGCD286 	The glittering plain – New works for saxophone and ensemble635212028629
SIGCD287 	A New Venetian Coronation, 1595635212028728
SIGCD288 	A tribute to Benny Goodman635212028827
SIGCD289 	Let the bright seraphim635212028926
SIGCD290 	LISZT: Excerpts from Années de pèlerinage - Italie635212029022
SIGCD291 	Voces 8 Christmas635212029121
SIGCD292 	WIDOR: Complete Organ Symphonies, Vol. 1635212029220
SIGCD293 	BENNETT: My dancing day & other choral works635212029329
SIGCD294 	A Doll's House & other works for percussion635212029428
SIGCD295 	BYRD/MONTE: The Word Unspoken635212029527
SIGCD296 	HAKIM: Works for organ and chamber ensemble635212029626
SIGCD298 	TODD: The Call of Wisdom635212029824
SIGCD300 	MENDELSSOHN: Elijah635212030028
SIGCD306 	In Recital at Tulle Cathedral635212030622
SIGCD307 	Royal Rhymes and Rounds635212030721
SIGCD308 	Jimmy - James Rhodes Live in Brighton635212030820
SIGCD309 	BRAHMS: Alessio Bax plays Brahms635212030929
SIGCD311 	CHILCOTT: The seeds of stars635212031124
SIGCD312 	KHACHATURIAN/LYAPUNOV: Works for violin & orchestra635212031223
SIGCD313 	24 lies per second635212031322
SIGCD314 	VAUGHAN WILLIAMS/FINZI/QUILTER: English Songs635212031421
SIGCD315 	ELGAR: Go, song of mine & other choral songs635212031520
SIGCD316 	LEVINE: The Divine Liturgy of St John Chrysostom635212031629
SIGCD317 	BRITTEN: The Canticles635212031728
SIGCD318 	Around Britten635212031827
SIGCD319 	WIDOR: Complete Organ Symphonies, Vol. 2635212031926
SIGCD320 	RIMSKY-KORSAKOV: Sheherazade & The Invisible City of Kitezh635212032022
SIGCD321 	MOZART: Piano Concertos Nos. 24 & 27635212032121
SIGCD322 	DVORÁK/SCHUMANN: Cello Concertos635212032220
SIGCD323 	POULENC: The Complete Songs, Vol. 4635212032329
SIGCD324 	RACHMANINOV: Transcriptions and arrangements for organ635212032428
SIGCD325 	BENNETT: Letters to Lindbergh & other choral works635212032527
SIGCD326 	RICHAFORT: Requiem – A Tribute to Josquin Desprez635212032626
SIGCD327 	TALBOT: Alice's Adventures & Fool's Paradise635212032725
SIGCD329 	REGER: Organ Works635212032923
SIGCD330 	RAVEL/STRAVINSKY: Mother Goose & The Rite of Spring635212033029
SIGCD333 	POULENC: Songs, Vol. 5635212033326
SIGCD334 	WIDOR: Complete Organ Symphonies, Vol. 3635212033425
SIGCD335 	BEDNALL: Welcome all wonders635212033524
SIGCD336 	BRITTEN: Cello Suites635212033623
SIGCD337 	WIDOR: Complete Organ Symphonies, Vol. 4635212033722
SIGCD338 	Libera nos - The cry of the oppressed635212033821
SIGCD339 	LASSUS: Lagrime di San Petro635212033920
SIGCD340 	BRITTEN: War Requiem635212034026
SIGCD341 	Great American Songbook635212034125
SIGCD342 	MENDELSSOHN: Violin Concertos635212034224
SIGCD343 	MOZART: Die Schuldigkeit des ersten Gebots635212034323
SIGCD344 	VICTORIA: Tenebrae Responsories635212034422
SIGCD345 	MOZART: Horn Concertos635212034521
SIGCD346 	Incarnation635212034620
SIGCD347 	WIDOR: Complete Organ Symphonies, Vol. 5635212034729
SIGCD348 	BRITTEN: Peter Grimes635212034828
SIGCD349 	SAINT-SAËNS/GOSS/FRANCK: Piano Concertos635212034927
SIGCD350 	BERKELEY/MCCABE/WILLIAMS: Quartets635212035023
SIGCD360 	MAHLER: Symphonies Nos. 1, 2 & 3635212036020
SIGCD361 	MAHLER: Symphonies Nos. 4, 5 & 6635212036129
SIGCD362 	MAHLER: Symphonies Nos. 7, 8 & 9635212036228
SIGCD363 	MAHLER: The Complete Symphonies635212036327
SIGCD364 	COOPER: Continuum & other works635212036419
SIGCD365 	STRAVINSKY/BRAHMS/PIAZZOLLA: Piano Duos635212036525
SIGCD366 	MEALOR/BRITTEN: The flowers have their angels635212036624
SIGCD367 	TAVENER: The Veil of the Temple635212036723
SIGCD368 	BIRTWISTLE: The Moth Requiem635212036822
SIGCD369 	WOLF/BRAHMS: Lieder635212036921
SIGCD370 	My Beloved's Voice635212037027
SIGCD371 	James Rhodes 5635212037126
SIGCD372 	BARTÓK: Duke Bluebeard's Castle635212037225
SIGCD373 	MOZART: The A-Z of Mozart Opera635212037324
SIGCD374 	Jewels of the Bel Canto635212037423
SIGCD375 	PURCELL: A Purcell Collection635212037522
SIGCD376 	1917 - Works for violin & piano635212037621
SIGCD377 	VIVALDI: The Four Seasons635212037720
SIGCD380 	PANUFNIK: Dreamscape - Songs and Trios635212038024
SIGCD381 	JACKSON G: Airplane Cantata & other choral works635212038123
SIGCD382 	DOWLAND: Mister Dowland's Midnight635212038222
SIGCD383 	Avanti l'Opera – An A-Z of Italian Baroque Overtures635212038321
SIGCD384 	Debussy, Françaix, Glinka, Milhaud, Prokofiev635212038420
SIGCD385 	BACH: St Matthew Passion635212038529
SIGCD386 	On Christmas night635212038628
SIGCD387 	Christmas carols from village green to church635212038727
SIGCD388 	WAGNER: Wagner without words635212038826
SIGCD389 	HAKIM: Hakim plays Hakim - Bilbao, Vol. 1635212038925
SIGCD390 	NIELSEN/MOZART: Clarinet Concertos635212039021
SIGCD391 	MARCELLO: Psalms635212039120
SIGCD392 	HANDEL: L'Allegro, il Penseroso ed il Moderato635212039229
SIGCD393 	Postcards - The King's Singers635212039328
SIGCD394 	TODD: Lux et veritas635212039427
SIGCD395 	BACH C P E: Symphonies635212039526
SIGCD396 	SHOSTAKOVICH: 24 Preludes & Fugues, Op 87635212039625
SIGCD397 	BEETHOVEN: Piano Sonatas635212039724
SIGCD398 	The Captive Nightingale635212039823
SIGCD399 	VAUGHAN WILLIAMS/ELGAR: The Lark Ascending635212039922
SIGCD400 	MOZART: Mitridate, re di Ponto635212040027
SIGCD401 	No Exceptions No Exemptions635212040126
SIGCD402 	RAMEAU: Anacréon635212040225
SIGCD403 	Psalm – Contemporary British Trumpet Concertos635212040324
SIGCD404 	Homages - A Musical Dedication635212040423
SIGCD405 	Sounds of Spain & the Americas635212040522
SIGCD406 	The Cole Porter Songbook635212040621
SIGCD407 	GLAZUNOV/PROKOFIEV/TCHAIKOVSKY: Variations on a Rococo theme & other works635212040720
SIGCD408 	In the Midst of Life – Music from the Baldwin Partbooks I635212040829
SIGCD409 	Out of darkness – Music from Lent to Trinity635212040928
SIGCD410 	A Knight's Progress635212041024
SIGCD411 	DAVIS O: Flight635212041123
SIGCD412 	CHILCOTT: St John Passion635212041222
SIGCD413 	ADÈS: The twenty-fifth hour & other chamber music635212041321
SIGCD414 	Il Trionfo di Dori635212041420
SIGCD415 	BIRD: The Oriental Miscellany635212041529
SIGCD416 	Soli - Bartók, Kurtág, Benjamin, Penderecki635212041628
SIGCD417 	PURCELL: Dido & Aeneas635212041727
SIGCD418 	SHOSTAKOVICH: String Quartets Nos. 4, 8 & 11635212041826
SIGCD419 	Surrender - Voices of Persephone635212041925
SIGCD420 	TODD: Alice's Adventures in Wonderland635212042021
SIGCD421 	WEIR: Storm & other choral works635212042120
SIGCD422 	CHILCOTT: The Angry Planet & other choral works635212042229
SIGCD423 	HANDEL: Handel in Italy, Vol. 1635212042328
SIGCD424 	VENABLES: The Song of the Severn & other songs635212042427
SIGCD425 	Inside tracks - the James Rhodes mix tape635212042526
SIGCD426 	SCRIABIN/MUSORGSKY: Piano Sonata No. 3 & Pictures635212042625
SIGCD427 	FAURÉ: Songs, Vol. 1635212042724
SIGCD428 	HANDEL: Handel at Vauxhall, Vol. 1635212042823
SIGCD429 	The shepherd on the rock635212042922
SIGCD430 	BRAHMS/BRUCKNER: Motets635212043028
SIGCD431 	BRUCKNER: Symphony No. 9635212043127
SIGCD432 	SZYMANOWSKI/HAHN: Violin Sonatas635212043226
SIGCD433 	MOZART: Il re pastore635212043325
SIGCD434 	HAYDN: Symphonies Nos. 52, 53 & 59635212043424
SIGCD435 	BACH/HANDEL/MOZART: Aksel! – Arias by Bach, Handel & Mozart635212043523
SIGCD436 	Invisible Stars – Choral works of Ireland & Scotland635212043622
SIGCD437 	DAVIS O/VIVALDI: Seaons635212043721
SIGCD438 	WIDOR: Solo organ works635212043820
SIGCD439 	Lullabies for Mila635212043929
SIGCD440 	Only a Singing Bird635212044025
SIGCD441 	TCHAIKOVSKY: Piano Concerto No. 1 & Nutcracker Suite635212044124
SIGCD442 	TAVENER: Missa Wellensis & other sacred choral music635212044223
SIGCD443 	Songs to the moon635212044322
SIGCD444 	PALOMO/RODRIGO: Nocturnos de Andalucía635212044421
SIGCD445 	Time and its Passing635212044520
SIGCD446 	The Evening Hour635212044629
SIGCD447 	Greensleeves635212044728
SIGCD448 	BRAHMS/BRUCE: Clarinet Quintet & Gumboots635212044827
SIGCD449 	Winchester Cathedral 50th Anniversary EP635212044926
SIGCD450 	PALESTRINA: How fair thou art635212045022
SIGCD451 	HUGHES B: I am the song & other choral works635212045121
SIGCD452 	DOVE: For an unknown soldier & An airmail letter635212045220
SIGCD453 	GOUGH: The world encompassed635212045329
SIGCD454 	L'ESTRANGE: On eagles' wings & other choral works635212045428
SIGCD455 	POULENC: Works for Piano Solo and Duo635212045527
SIGCD456 	HARVEY: Choral music635212045626
SIGCD457 	Where'er you walk - Handel's favourite tenor635212045725
SIGCD458 	Christmas with St John's635212045824
SIGCD459 	The King's Singers Christmas Songbook635212045923
SIGCD460 	Adeste fideles635212046029
SIGCD461 	SCHUBERT: Symphony No. 9635212046128
SIGCD462 	HANDEL: Handel in Italy, Vol. 2635212046227
SIGCD463 	HAKIM: Hakim plays Hakim - Bilbao, Vol. 2635212046326
SIGCD464 	Queen Mary's Big Belly – Prayers for an heir in Catholic England635212046425
SIGCD465 	Anthem – Great British Hymns & Choral Works635212046524
SIGCD466 	BARTÓK: The Miraculous Mandarin & other works635212046623
SIGCD467 	MOZART/NIELSEN: Flute Concertos635212046722
SIGCD468 	ADAMS/HARRIS: Violin Concertos635212046821
SIGCD469 	DAVIS O: Dance635212046920
SIGCD470 	DURUFLÉ/VIERNE/BRIGGS: Midnight at St Etienne du Mont635212047026
SIGCD471 	PARK/TALBOT: Footsteps & Path of Miracles635212047125
SIGCD472 	FAURÉ: Songs, Vol. 2635212047224
SIGCD473 	MOZART: Zaide635212047323
SIGCD474 	Virgin and Child – Music from the Baldwin Partbooks II635212047422
SIGCD475 	A New Heaven635212047521
SIGCD476 	REGER: Fantasias & Fugues635212047620
SIGCD477 	NIELSEN: Flute & Clarinet Concertos635212047729
SIGCD478 	HANDEL: Handel in Ireland, Vol. 1635212047828
SIGCD479 	HANDEL: Handel at Vauxhall, Vol. 2635212047927
SIGCD480 	HAYDN: The Seasons635212048023
SIGCD481 	BYRD/BRITTEN: Choral works635212048122
SIGCD482 	CHOPIN: Preludes635212048221
SIGCD483 	FAURÉ: The Complete Songs, Vol. 3635212048320
SIGCD484 	RACHMANINOV: Symphony No. 1635212048429
SIGCD485 	Perfido! – Opera arias635212048528
SIGCD486 	GRIEG/VAUGHAN WILLIAMS: Subito - Violin Sonata & The lark ascending635212048627
SIGCD487 	DOVE: In Damascus & other works635212048726
SIGCD488 	BACH: The complete solo soprano cantatas, Vol. 1635212048825
SIGCD489 	POULENC/KODÁLY/JANÁCEK: Kyrie635212048924
SIGCD490 	Silence & Music635212049020
SIGCD491 	The House of the Mind635212049123
SIGCD492 	BERNSTEIN/STRAVINSKY/SCHOENBERG: Symphonic Psalms & Prayers635212049228
SIGCD493 	SHOSTAKOVICH: Piano Concertos & Sonatas635212049327
SIGCD494 	Fire On All Sides635212049426
SIGCD495 	McCARTHY/TODD: Codebreaker & Ode to a Nightingale635212049525
SIGCD496 	WALEY-COHEN: Permutations635212049624
SIGCD497 	The King's Singers Christmas Presence635212049723
SIGCD498 	HAKIM: Phèdre, Caprice, Diptyque & Concerto635212049822
SIGCD499 	MOZART: Il sogno di Scipione635212049921
SIGCD500 	The King's Singers Gold635212050026
SIGCD501 	TAVENER: Mother and Child635212050125
SIGCD502 	Christmas with The King's Singers635212050224
SIGCD506 	NYMAN: Music for two pianos635212050620
SIGCD509 	Voyages635212050927
SIGCD510 	DVORÁK/JANÁCEK/SUK: Bohemia - Violin Sonatas635212051023
SIGCD511 	GIBBONS: In chains of gold635212051122
SIGCD512 	CHILCOTT: In winter's arms635212051221
SIGCD513 	The Art of Dancing – Concertos for trumpet, piano & strings635212051320
SIGCD514 	Great Cathedral Anthems635212051429
SIGCD515 	DVORÁK/SIBELIUS: Symphony No. 9 & Finlandia635212051528
SIGCD516 	WILKINSON: The sunlight on the garden & other songs635212051627
SIGCD517 	WILLIAMS R: Sacred choral works635212051726
SIGCD518 	FITKIN: String Quartets635212051825
SIGCD519 	TAVENER/PANUFNIK: 99 Words & other choral works635212051924
SIGCD520 	LASSUS/TYMOCZKO: Sibylla635212052020
SIGCD521 	LUKASZEWSKI: Daylight declines & other choral works635212052129
SIGCD522 	DAVIS O: Liberty635212052228
SIGCD523 	BEETHOVEN/MENDELSSOHN: Concertos635212052327
SIGCD524 	KERNIS: Dreamsongs & other concertos635212052426
SIGCD525 	BEETHOVEN: Piano Concerto No. 5 & works for solo piano635212052525
SIGCD526 	Light Divine635212052624
SIGCD527 	BEETHOVEN: Beethoven Unbound635212052723
SIGCD528 	JENKINS: Complete Four-Part Consort Music635212052822
SIGCD529 	WRIGHT L: Duets635212052921
SIGCD530 	RACHMANINOV: Symphony No. 2635212053027
SIGCD531 	SCHUBERT: Winter Journey635212053126
SIGCD532 	White Light - the space between635212053225
SIGCD533 	LISZT: Piano music635212053324
SIGCD534 	Mozart in London635212053423
SIGCD535 	Advent Live, Vol. 1635212053522
SIGCD536 	A Rose Magnificat635212053621
SIGCD537 	HANDEL/VIVALDI: Silete venti/Nulla in mundo635212053720
SIGCD538 	Tanguero – Music from South America635212053829
SIGCD539 	BLACKFORD: Niobe635212053928
SIGCD540 	RACHMANINOV: Symphony No. 3 & Symphonic Dances635212054024
SIGCD541 	VAUGHAN WILLIAMS: Mass in G minor & other choral works635212054123
SIGCD542 	TCHAIKOVSKY/DUCHEN: The Nutcracker and I, by Alexandra Dariescu635212054222
SIGCD543 	PANUFNIK R: Celestial Bird & other choral works635212054321
SIGCD544 	TELEMANN: Solo Fantasias635212054420
SIGCD545 	Praise my soul – Favourite hymns from Jesus College Cambridge635212054529
SIGCD546 	The Organ of St Bavo, Haarlem635212054628
SIGCD547 	MOZART: Grabmusik & Bastien und Bastienne635212054717
SIGCD548 	RACHMANINOV/SIBELIUS: Piano Concerto No. 3 & Symphony No. 2635212054826
SIGCD549 	Concerti by Telemann, Tartini & others635212054925
SIGCD550 	SCHUBERT: Swansong635212055021
SIGCD551 	Resilience635212055120
SIGCD552 	MOZART/WEBER: Clarinet Quintets635212055229
SIGCD553 	DOWLAND: First Booke of Songes or Ayres635212055328
SIGCD554 	SCHUMANN/KILPINEN/BRAHMS: Nature's solace635212055427
SIGCD555 	DVORÁK: String Quartets Nos. 5 & 12635212055519
SIGCD556 	The romantic horn635212055618
SIGCD557 	A walk with Ivor Gurney & other choral works635212055724
SIGCD558 	Perpetual twilight635212055816
SIGCD559 	SHOSTAKOVICH: String Quartets Nos. 1, 2 & 7635212055915
SIGCD560 	TALLIS/STRIGGIO: Supersize polyphony635212056011
SIGCD561 	BRUNNING: Swansongs635212056127
SIGCD562 	Lest we forget635212056226
SIGCD563 	TODD: Passion Music & Jazz Missa Brevis635212056325
SIGCD564 	PANUFNIK (R): Love abide & other choral works635212056417
SIGCD565 	Love songs635212056516
SIGCD566 	MUSORGSKY/RAVEL/MESSIAEN: Pictures/Miroirs/Cantéyodjayâ635212056615
SIGCD567 	Locus iste635212056714
SIGCD568 	BLACKFORD: Kalon635212056813
SIGCD569 	An English Coronation 1902-1953635212056912
SIGCD570 	TAVERNER: Missa Gloria tibi Trinitas & other works635212057018
SIGCD571 	DURUFLÉ: Complete Choral Works635212057117
SIGCD572 	The Hymns Album II635212057216
SIGCD573 	BACH C P E: Complete Original Works for Violin & Keyboard635212057315
SIGCD574 	From the ground up - The chaconne635212057414
SIGCD575 	MACMILLAN: One equal music & other choral works635212057513
SIGCD576 	In nomine II635212057612
SIGCD577 	MOZART: Apollo et Hyacinthus635212057711
SIGCD578 	PHIBBS/MOZART: Clarinet Concertos635212057810
SIGCD579 	Handel's Queens635212057919
SIGCD580 	GUNNING: Flute Concertino, Clarinet & Guitar Concertos635212058015
SIGCD584 	PROKOFIEV G: Saxophone Concerto & Bass Drum Concerto635212058411
SIGCD585 	TAVENER: The protecting veil & readings635212058510
SIGCD586 	NYMAN/PURCELL: If & other songs635212058619
SIGCD587 	Song's first cycle635212058718
SIGCD588 	Magnificat, Vol. 1635212058817
SIGCD589 	PURCELL: King Arthur635212058916
SIGCD590 	DAVIS O: Arcadia635212059012
SIGCD591 	TODD: Noodles & other works635212059111
SIGCD592 	The Soldier - From Severn to Somme635212059210
SIGCD593 	GUNNING: Symphonies Nos. 2, 10 & 12635212059319
SIGCD594 	TCHAIKOVSKY: Solo piano works635212059418
SIGCD595 	Now may we singen635212059517
SIGCD596 	WIDOR: The Complete Organ Works635212059616
SIGCD597 	DVORÁK: String Quartets Nos. 8 & 10635212059715
SIGCD598 	The last rose of summer635212059814
SIGCD599 	BRUCE: The north wind was a woman & other chamber wo635212059913
SIGCD600 	JANÁCEK: Solo piano635212060018
SIGCD601 	The King's Singers - The Library, Vol. 1635212060117
SIGCD602 	The Godfather635212060216
SIGCD603 	ESENVALDS: There will come soft rains & other works635212060315
SIGCD604 	Cantos sagrados635212060414
SIGCD605 	Ash Wednesday635212060513
SIGCD606 	HAYDN/SCHUBERT/WOLF: The divine muse635212060612
SIGCD607 	Finding harmony635212060711
SIGCD608 	VICTORIA/GUERRERO/MORALES: Salve Salve Salve – Josquin's Spanish legacy635212060810
SIGCD609 	In chains of gold, Vol. 2635212060919
SIGCD610 	HANDEL: Messiah … Refreshed!635212061015
SIGCD611 	Italian inspirations635212061114
SIGCD612 	DÍAZ-JEREZ: Maghek – 7 symphonic poems about the Canary Islands635212061213
SIGCD613 	MEALOR: Blessing & other choral works635212061312
SIGCD614 	BEETHOVEN: Piano Concertos Nos. 1 & 2635212061411
SIGCD615 	PURCELL: The Fairy Queen635212061510
SIGCD616 	BEETHOVEN: Symphonies Nos 1-3635212061619
SIGCD617 	VENABLES: Love lives beyond the tomb & other songs635212061718
SIGCD618 	BEETHOVEN: Violin Sonatas Nos. 1, 5 & 8635212061817
SIGCD619 	Sturm und Drang, Vol. 1635212061916
SIGCD620 	BEETHOVEN: Piano Concertos Nos. 3 & 4635212062012
SIGCD621 	GUNNING: Violin Concerto, Cello Concerto & Birdflight635212062111
SIGCD622 	COUPERIN/GESUALDO: Leçons de ténèbres & Tenebrae Responsories635212062210
SIGCD624 	FINNISSY: Pious Anthems & Voluntaries635212062418
SIGCD625 	WHITACRE: Marimba Quartets635212062517
SIGCD626 	Journeys to the New World635212062616
SIGCD627 	A Ceremony of Carols635212062715
SIGCD628 	PROKOFIEV: Concerto for turntables No 1 & Cello Concerto635212062814
SIGCD629 	PARRY (B): The Hours635212062913
SIGCD630 	WHITACRE: The Sacred Veil635212063019
SIGCD631 	HANCOCK: Choral & organ music635212063118
SIGCD632 	YOUNG: Beowulf635212063217
SIGCD633 	The Sweetest Songs – Music from the Baldwin Partbooks III635212063316
SIGCD634 	WRIGHT: The colour of intention635212063415
SIGCD635 	The King's Singers - The Library, Vol. 2635212063514
SIGCD636 	Sturm und Drang, Vol. 2635212063613
SIGCD637 	BEETHOVEN: Piano Concerto No. 5 & Triple Concerto635212063712
SIGCD638 	VAUGHAN WILLIAMS/SUK/DVORÁK: Tallis Fantasia & String Serenades635212063811
SIGCD639 	BEETHOVEN: Symphonies Nos 4-6635212063910
SIGCD641 	Extra time635212064115
SIGCD642 	All things are quite silent635212064214
SIGCD643 	Be all merry635212064313
SIGCD644 	MARSH: Flare & other works635212064412
SIGCD645 	SCHUBERT: A Schubert Journey635212064511
SIGCD646 	A winter's night635212064610
SIGCD647 	MATTHEWS D: A vision of the sea635212064719
SIGCD648 	TCHAIKOVSKY: Swan Lake (excerpts)635212064818
SIGCD649 	BRITTEN: A Ceremony of Carols & Saint Nicolas635212064917
SIGCD650 	SCHUMANN/SHAW/SHOSTAKOVICH: Babel635212065013
SIGCD651 	GERSHWIN: I got rhythm635212065112
SIGCD652 	Between the clouds635212065211
SIGCD653 	Music from the ghetto635212065310
SIGCD654 	STRAUSS R/COPLAND: Duet Concertino & Clarinet Concerto635212065419
SIGCD655 	GUNNING: Symphonies Nos. 6 & 7635212065518
SIGCD656 	Rediscovered - British clarinet concertos635212065617
SIGCD658 	HANDEL: Handelian Pyrotechnics635212065815
SIGCD659 	BEETHOVEN: Symphonies Nos 7-9635212065914
SIGCD660 	CHAPMAN CAMPBELL: For the love of life & other works635212066010
SIGCD661 	Advent Live, Vol. 2635212066119
SIGCD662 	Timelapse635212066218
SIGCD663 	Settecento635212066317
SIGCD664 	RUIZ: Behold the stars635212066416
SIGCD665 	Spira, spera – Bach transcriptions635212066515
SIGCD666 	BRAHMS: Piano Concerto No. 1 & Waltzes635212066614
SIGCD667 	Magnificat, Vol. 2635212066713
SIGCD668 	DAVIS O: Solace635212066812
SIGCD669 	PROKOFIEV: Symphony No. 5635212066911
SIGCD670 	MARTIN M: Lim Fantasy of Companionship635212067017
SIGCD671 	BRAHMS: Clarinet Sonatas & Ernste Gesänge635212067116
SIGCD672 	ARNE: ArtaxerxesPreviously issued on Linn CKD358635212067215
SIGCD673 	PANUFNIK R: Heartfelt & other works635212067314
SIGCD674 	BRAHMS: Piano Concerto No 2, Capriccios & Intermezzos635212067413
SIGCD675 	GRIEG/RACHMANINOV: Piano Concertos635212067512
SIGCD676 	GUNNING: Symphony No. 5 & String Quartet No. 1635212067611
SIGCD677 	MACKEY/WHITACRE/TICHELI: Asphalt cocktail/October/Blue shades635212067710
SIGCD678 	The King's Singers - The Library, Vol. 3635212067819
SIGCD679 	HANDEL: Eight Great Harpsichord Suites635212067918
SIGCD680 	An Elizabethan Christmas635212068014
SIGCD681 	FAURÉ: The Complete Songs, Vol. 4635212068113
SIGCD682 	IVES (G): Requiem635212068212
SIGCD683 	Christmas Carols with The King's Singers635212068311
SIGCD684 	Lamento635212068410
SIGCD685 	Australian Thais – New music for saxophone and piano635212068519
SIGCD686 	Manifesto635212068618
SIGCD688 	Images635212068816
SIGCD689 	LEHRER: The Queen's Six murder the songs of ...635212068915
SIGCD690 	In winter's house – Christmas with Tenebrae635212069011
SIGCD691 	The tree635212069110
SIGCD692 	JOMMELLI: Il Vologeso635212069219
SIGCD693 	BRESCIANELLO: Concerti & Sinphonie, Op. 1 Libro Primo635212069318
SIGCD694 	Labyrinths635212069417
SIGCD695 	BARRY: Alice's adventures under ground635212069516
SIGCD696 	LOCKE: The Flat Consort635212069615
SIGCD697 	SCHUBERT: Die schöne Müllerin635212069714
SIGCD698 	From Windsor with love635212069813
SIGCD699 	VIVALDI: Vivaldi's women635212069912
SIGCD700 	CHOPIN: Piano Concertos635212070017
SIGCD701 	BARLEY: Light Stories635212070116
SIGCD702 	PUCCINI: La bohème635212070215
SIGCD703 	CHILCOTT: Circlesong & other choral works635212070314
SIGCD704 	BEETHOVEN: Violin Concerto & Romances635212070413
SIGCD705 	Forza azzurri!635212070512
SIGCD706 	SCHUBERT: Violin Sonata, Fantasie & Rondo635212070611
SIGCD707 	Eastertide Evensong635212070710
SIGCD708 	When sleep comes635212070819
SIGCD709 	DAVIS (O): Air635212070918
SIGCD710 	BACH: Harpsichord Concertos Nos 1, 3, 4 & 7635212071014
SIGCD711 	SCHUBERT: The fair maid of the mill635212071113
SIGCD712 	BERG/WEBERN/SCHOENBERG: String Quartets635212071212
SIGCD713 	HANDEL: Caio Fabbricio635212071311
SIGCD714 	Celestial Dawn635212071410
SIGCD715 	DUPARC: The complete songs635212071519
SIGCD716 	LUPO: Fantasia635212071618
SIGCD717 	HILDEGARD: Sacred chants635212071717
SIGCD718 	The King's Singers - The Library, Vol. 4635212071816
SIGCD719 	The Crown - Virtuosic arias635212071915
SIGCD720 	STRAUSS (R): Santtu conducts Strauss635212072011
SIGCD721 	The Psalms635212072110
SIGCD722 	A percussionist's songbook635212072219
SIGCD723 	Into the Light635212072318
SIGCD724 	A Pembroke Christmas635212072417
SIGCD725 	Divine Music635212072516
SIGCD726 	HAYDN: Keyboard Works, Vol. 1635212072615
SIGCD727 	WALTON/SHOSTAKOVICH: String Quartets635212072714
SIGCD728 	LOCKE: The Little Consort635212072813
SIGCD729 	CHILCOTT: Canticles of Light635212072912
SIGCD730 	FALKENBERG: The Moons Symphony635212073018
SIGCD731 	WEELKES/BYRD: Tom & Will635212073117
SIGCD732 	Echoes635212073216
SIGCD733 	BEETHOVEN: The late quartets635212073315
SIGCD734 	VAUGHAN WILLIAMS/GRIEG: Violin Sonatas635212073414
SIGCD735 	Visions illuminées635212073513
SIGCD736 	Lovesick635212073612
SIGCD737 	A Most Marvellous Party635212073711
SIGCD738 	SILVERMAN: Piano Trios635212073810
SIGCD739 	Wonderland635212073919
SIGCD740 	SCARLATTI (F): Dixit Dominus & Messa a 16 voci635212074015
SIGCD741 	MAHLER: Rückert-Lieder635212074114
SIGCD742 	Magnificat, Vol. 3635212074213
SIGCD743 	DAVIS (O): Blue635212074312
SIGCD744 	BACH: Clavier-Übung III635212074411
SIGCD746 	Vidi speciosam635212074619
SIGCD747 	Après un rêve635212074718
SIGCD749 	McDOWALL: Da Vinci Requiem & Seventy degrees below zero635212074916
SIGCD750 	New Millennium635212075012
SIGCD751 	An Englishman Abroad635212075111
SIGCD752 	HAWES: The Nativity635212075210
SIGCD753 	ROTH: The Traveller & Earth and Sky635212075319
SIGCD754 	Noël635212075418
SIGCD755 	Nova! Nova! Joy to the world!635212075517
SIGCD756 	SCHUMANN: Piano Works635212075616
SIGCD757 	FERRABOSCO JR.: Music to hear ...635212075715
SIGCD758 	READE: A Celebration635212075814
SIGCD759 	Sturm und Drang, Vol. 3635212075913
SIGCD760 	MAHLER: Symphony No. 2635212076019
SIGCD761 	Pastoral 21635212076118
SIGCD762 	The Christmas album635212076217
SIGCD763 	HOWELL: Orchestral works635212076316
SIGCD764 	BACH: Harpsichord Concertos Nos. 2, 5 & 6635212076415
SIGCD765 	Rhapsody635212076514
SIGCD766 	Palimpsest – New Works from Old for saxophone and choir635212076613
SIGCD767 	BRESCIANELLO: Concerti & Sinphonie Op 1 Libro Secondo635212076712
SIGCD768 	Advent Live, Vol. 3635212076811
SIGCD769 	Infinite refrain – Music of love's refuge635212076910
SIGCD770 	SCHUBERT: Schubert in English635212077016
SIGCD771 	HAKIM: Hakim plays Hakim - Dudelange organ , Vol. 2635212077115
SIGCD772 	HAKIM: Anne Warthmann sings Naji Hakim635212077214
SIGCD773 	BACH/MACMILLAN: Motets & Sacred Songs635212077313
SIGCD774 	Songs for Peter Pears635212077412
SIGCD775 	TANEYEV/SCHUMANN: Piano Quintets635212077511
SIGCD776 	BYRD: Sacred Works635212077610
SIGCD777 	Magnificat, Vol. 4635212077719
SIGCD778 	PUCCINI: Orchestral transcriptions635212077818
SIGCD779 	JENKINS K: The Armed Man635212077917
SIGCD780 	PUCCINI: A te, Puccini635212078013
SIGCD781 	TARTINI: Violin Sonatas635212078112
SIGCD782 	SCHUMANN: Schumann in English, Vol. 1635212078211
SIGCD783 	ROSEINGRAVE: Harpsichord Suites635212078310
SIGCD785 	ELGAR: The Dream of Gerontius635212078518
SIGCD786 	SHOSTAKOVICH: String Quartets Nos. 9 & 15635212078617
SIGCD787 	DEBUSSY/RAVEL: Debussy and Ravel for two635212078716
SIGCD788 	ELIAS: Music for strings635212078815
SIGCD789 	Earthcycle635212078914
SIGCD790 	FORBES L'ESTRANGE: Heaven to Earth635212079010
SIGCD791 	PIAZZOLLA/LINTENEN: Four Seasons & Cello Concerto635212079119
SIGCD792 	FITKIN: Loosening & other works635212079218
SIGCD793 	DOVE: On the streets and in the sky & other works635212079317
SIGCD794 	BEETHOVEN: Violin Sonatas Nos. 1, 6 & 8635212079416
SIGCD796 	ELIAS: Music for wind635212079614
SIGCD797 	Beauty for ashes635212079713
SIGCD798 	LISZT: Piano Works635212079812
SIGCD799 	GRIEG & SCHUMANN (C): Piano Concertos635212079911
SIGCD800 	BACH: The Complete Organ Works, Vol. 1635212080023
SIGCD802 	BACH: The Complete Organ Works, Vol. 2635212080221
SIGCD803 	BACH: The Complete Organ Works, Vol. 3635212080320
SIGCD804 	BACH: The Complete Organ Works, Vol. 4635212080429
SIGCD805 	BACH: The Complete Organ Works, Vol. 5635212080528
SIGCD806 	BACH: The Complete Organ Works, Vol. 6635212080627
SIGCD807 	BACH: The Complete Organ Works, Vol. 7635212080726
SIGCD808 	BACH: The Complete Organ Works, Vol. 8635212080825
SIGCD809 	BACH: The Complete Organ Works, Vol. 9635212080924
SIGCD810 	BACH: The Complete Organ Works, Vol. 10635212081013
SIGCD811 	BACH: The Complete Organ Works, Vol. 11635212081112
SIGCD812 	BACH: The Complete Organ Works, Vol. 12635212081211
SIGCD813 	BACH: The Complete Organ Works, Vol. 13635212081310
SIGCD814 	BACH: The Complete Organ Works, Vol. 14635212081419
SIGCD816 	CHAPMAN CAMPBELL: Contemplations635212081617
SIGCD819 	The Covid-19 sessions635212181997
SIGCD821 	HEWITT JONES: Christmas Party635212082126
SIGCD824 	SCHUBERT/CHOPIN: Cello Sonatas635212082423
SIGCD826 	The Silken Tent635212082614
SIGCD831 	SCHUBERT: Piano Music, Vol. 1635212083116
SIGCD832 	SCHUBERT: Piano Music, Vol. 2635212083215
SIGCD833 	SCHUBERT: Piano Music, Vol. 3635212083314
SIGCD834 	SCHUBERT: Piano Music, Vol. 4635212083413
SIGCD835 	SCHUBERT: Piano Music, Vol. 5635212083512
SIGCD836 	SCHUBERT: Piano Music, Vol. 6635212083611
SIGCD837 	SCHUBERT: Piano Music, Vol. 7635212083710
SIGCD838 	SCHUBERT: Piano Music, Vol. 8635212083819
SIGCD845 	Church bells beyond the stars635212084519
SIGCD846 	Electric635212084618
SIGCD847 	COOPER: Oculus635212084717
SIGCD851 	CHOPIN/BACH: Vitamin C635212085110
SIGCD856 	STRAVINSKY: The Firebird & Petrushka Suites635212085615
SIGCD861 	CHOPIN/SPACHT: Chopin at midnight635212086117
SIGCD863 	Ireland you're my home635212086315
SIGCD864 	JOYCE: Chamber Music, Vol. 1635212086414
SIGCD866 	DALE (R): Night Seasons & other works635212086612
SIGCD867 	Fields of wonder  July 2025 release635212086711
SIGCD869 	BACH: Cantatas Nos 4, 55 & 82.2635212086919
SIGCD870 	RAVEL: The complete songs635212087015
SIGCD872 	BEETHOVEN: The middle quartets635212087213
SIGCD873 	FORBES L'ESTRANGE: Winter light635212087312
SIGCD875 	ELMS: Visions of St Anne & other orchestral works635212087510
SIGCD876 	RUIZ: Venus & Adonis635212087619
SIGCD877 	SHOSTAKOVICH: Symphonies Nos. 6 & 9635212087718
SIGCD879 	ARLEN: The Song of Songs & The Poet in Exile635212087916
SIGCD880 	A prayer for deliverance  June 2025 release635212088012
SIGCD881 	SCARLATTI F: Il Daniele nel lago de' leoni635212088111
SIGCD882 	Fantasies635212088210
SIGCD883 	BEETHOVEN: The early quartets635212088319
SIGCD885 	Sun moon stars rain635212088517
SIGCD886 	VIVALDI: Opus 8, Vol. 1 – The Four Seasons & other concertos635212088616
SIGCD887 	Such stuff as dreams are made on635212088715
SIGCD888 	SCHUMANN/SCHUMANN (C): Music for clarinet & piano635212088814
SIGCD889 	SHOSTAKOVICH: Symphony No. 10635212088913
SIGCD890 	DAVIS O: Life635212089019
SIGCD891 	TODD: All will be well635212089118
SIGCD892 	Attende Domine635212089217
SIGCD893 	Lament & Liberation635212089316
SIGCD896 	ELGAR: The Kingdom635212089613
SIGCD897 	MUHLY/GIBBONS: My Days & Fantasias635212089712
SIGCD899 	MOZART: Organ works  July 2025 release635212089910
SIGCD900 	Russian Treasures635212090022
SIGCD901 	Plainchant & Tallis Lamentations635212090121
SIGCD902 	A Very English Christmas635212090220
SIGCD903 	CHILCOTT: Sun, Moon, Sea & Stars635212090329
SIGCD904 	Partsongs635212090428
SIGCD905 	BONONCINI: How are the mighty fallen635212090510
SIGCD906 	BEETHOVEN: The Final Sonatas635212090619
SIGCD907 	TEN HOLT: Canto ostinato635212090718
SIGCD908 	VIVALDI: Vivaldi x2 squared635212090817
SIGCD909 	Christmas with The Bevan Family Consort635212090916
SIGCD910 	Forgotten Dances635212091012
SIGCD911 	DEBUSSY: Préludes635212091111
SIGCD912 	The King's Singers Close Harmony635212091210
SIGCD914 	Harmonies of Devotion635212091418
SIGCD915 	Light and Shadow  June 2025 release635212091517
SIGCD916 	BRAHMS: Early and Late Piano Works635212091616
SIGCD917 	LEIGHTON/VAUGHAN WILLIAMS: That sweet city635212091715
SIGCD918 	Crossing borders  June 2025 release635212091814
SIGCD924 	Alone together635212092415
SIGCD929 	MARSH J: A Plastic Theatre & other choral works635212092910
SIGCD931 	In chains of gold, Vol. 3635212093115
SIGCD932 	BLOCH: Schelomo & Suite for viola  July 2025 release635212093214
SIGCD933 	STRAVINSKY: The Rite of Spring635212093313
SIGCD935 	Manía635212093511
SIGCD936 	BRAHMS/ENESCU: Violin Concerto & Ballade  August 2025 release635212093610
SIGCD937 	SCHUMANN/FARRENC/DUROSOIR: Resonance  August 2025 release635212093719
SIGCD945 	HAMPTON: The music of Calvin Hampton635212094518
SIGCD951 	O'HALLORAN: Trade & Mary Motorhead  August 2025 release635212095119
SPCC2000 	The Music of St Paul's Cathedral034571120003
WCC100 	The Music of Westminster Cathedral034571100210
    
    """
    
    codes = extract_catalogue_codes(full_text_data)
    
    OUTPUT_FILE = "catalogue_codes.json"
    
    print(f"\nSuccessfully extracted {len(codes)} codes.")
    
    # Save the clean list to a JSON file
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(codes, f, indent=4)
        
    print(f"Clean list of codes saved to '{OUTPUT_FILE}'")
    
    # Show a small sample of the results
    print("\nSample of extracted codes:")
    print(codes[:10])