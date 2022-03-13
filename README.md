# wordle-cli


Forked from [klipspringr/wordle-cli](https://github.com/klipspringr/wordle-cli), which is a command-line clone of Josh Wardle's [Wordle](https://www.powerlanguage.co.uk/wordle/), inspired by [Paul Battley's Ruby version](https://github.com/threedaymonk/wordle). Features:

## Download and run

Requires **Python 3.6** or later, and a **modern terminal app**.

To download the code and run it:

```bash
git clone https://github.com/shantonusen/wordle-cli.git && cd wordle-cli
python3 distribution.py
python3 doubles.py
python3 offbyone.py
```

## `distribution.py`

```
LETTER COUNT PERCENT  OCCURSIN PERCWORDS
E       1230   10.7% 1053/2309     45.6%
A        975    8.4%  906/2309     39.2%
R        897    7.8%  835/2309     36.2%
O        753    6.5%  672/2309     29.1%
T        729    6.3%  667/2309     28.9%
L        716    6.2%  645/2309     27.9%
I        670    5.8%  646/2309     28.0%
S        668    5.8%  617/2309     26.7%
N        573    5.0%  548/2309     23.7%
C        475    4.1%  446/2309     19.3%
U        466    4.0%  456/2309     19.7%
Y        424    3.7%  416/2309     18.0%
D        393    3.4%  370/2309     16.0%
H        387    3.4%  377/2309     16.3%
P        365    3.2%  345/2309     14.9%
M        316    2.7%  298/2309     12.9%
G        310    2.7%  299/2309     12.9%
B        280    2.4%  266/2309     11.5%
F        229    2.0%  206/2309      8.9%
K        210    1.8%  202/2309      8.7%
W        194    1.7%  193/2309      8.4%
V        152    1.3%  148/2309      6.4%
Z         40    0.3%   35/2309      1.5%
X         37    0.3%   37/2309      1.6%
Q         29    0.3%   29/2309      1.3%
J         27    0.2%   27/2309      1.2%
```

## `doubles.py`

```
Answers with a triple repeating letters, and a double repeating letter: 1/2309
  MAMMA
Answers with triple repeating letters: 19/2309
  BOBBY
  DADDY
  EERIE
  EMCEE
  ERROR
  FLUFF
  GEESE
  MAMMY
  MELEE
  MUMMY
  NANNY
  NINNY
  POPPY
  PUPPY
  RARER
  SASSY
  SISSY
  TATTY
  TEPEE
Answers with double-double repeating letters: 38/2309
  ALLAY
  AMASS
  ARRAY
  ASSAY
  BELLE
  BOOBY
  CACAO
  CIVIC
  COCOA
  FEMME
  FREER
  GAMMA
  KAPPA
  KAYAK
  LEVEL
  LLAMA
  MADAM
  MAGMA
  MIMIC
  MINIM
  MOTTO
  ONION
  PAPAL
  PENNE
  QUEUE
  RADAR
  REFER
  ROTOR
  SALSA
  SENSE
  SHUSH
  SLYLY
  TEETH
  TENET
  TOOTH
  TWEET
  VERVE
  VIVID
Answers with double repeating letters: 689/2309
  <not printed>
```

## `offbyone.py`

```
XIGHT has 9 potential solutions:
  EIGHT
  FIGHT
  LIGHT
  MIGHT
  NIGHT
  RIGHT
  SIGHT
  TIGHT
  WIGHT
XOUND has 8 potential solutions:
  BOUND
  FOUND
  HOUND
  MOUND
  POUND
  ROUND
  SOUND
  WOUND
XOWER has 7 potential solutions:
  COWER
  LOWER
  MOWER
  POWER
  ROWER
  SOWER
  TOWER
XATCH has 7 potential solutions:
  BATCH
  CATCH
  HATCH
  LATCH
  MATCH
  PATCH
  WATCH
SHAXE has 7 potential solutions:
  SHADE
  SHAKE
  SHALE
  SHAME
  SHAPE
  SHARE
  SHAVE
GRAXE has 6 potential solutions:
  GRACE
  GRADE
  GRAPE
  GRATE
  GRAVE
  GRAZE
XATTY has 6 potential solutions:
  BATTY
  CATTY
  FATTY
  PATTY
  RATTY
  TATTY
XAUNT has 6 potential solutions:
  DAUNT
  GAUNT
  HAUNT
  JAUNT
  TAUNT
  VAUNT
SXORE has 6 potential solutions:
  SCORE
  SHORE
  SNORE
  SPORE
  STORE
  SWORE
XASTE has 6 potential solutions:
  BASTE
  CASTE
  HASTE
  PASTE
  TASTE
  WASTE
STAXE has 6 potential solutions:
  STAGE
  STAKE
  STALE
  STARE
  STATE
  STAVE
XILLY has 6 potential solutions:
  BILLY
  DILLY
  FILLY
  HILLY
  SILLY
  WILLY
SPIXE has 5 potential solutions:
  SPICE
  SPIKE
  SPINE
  SPIRE
  SPITE
SXOUT has 5 potential solutions:
  SCOUT
  SHOUT
  SNOUT
  SPOUT
  STOUT
XUSTY has 5 potential solutions:
  DUSTY
  GUSTY
  LUSTY
  MUSTY
  RUSTY
XYING has 5 potential solutions:
  DYING
  EYING
  LYING
  TYING
  VYING
STOXE has 5 potential solutions:
  STOKE
  STOLE
  STONE
  STORE
  STOVE
XEACH has 5 potential solutions:
  BEACH
  LEACH
  PEACH
  REACH
  TEACH
XATER has 5 potential solutions:
  CATER
  EATER
  HATER
  LATER
  WATER
SXARE has 5 potential solutions:
  SCARE
  SHARE
  SNARE
  SPARE
  STARE
XULLY has 5 potential solutions:
  BULLY
  DULLY
  FULLY
  GULLY
  SULLY
XOUGH has 5 potential solutions:
  BOUGH
  COUGH
  DOUGH
  ROUGH
  TOUGH
XANDY has 5 potential solutions:
  CANDY
  DANDY
  HANDY
  RANDY
  SANDY
XOLLY has 5 potential solutions:
  DOLLY
  FOLLY
  GOLLY
  HOLLY
  JOLLY
XOVER has 5 potential solutions:
  COVER
  HOVER
  LOVER
  MOVER
  ROVER
XUNCH has 5 potential solutions:
  BUNCH
  HUNCH
  LUNCH
  MUNCH
  PUNCH
SXACK has 5 potential solutions:
  SHACK
  SLACK
  SMACK
  SNACK
  STACK
XROWN has 5 potential solutions:
  BROWN
  CROWN
  DROWN
  FROWN
  GROWN
XRIED has 5 potential solutions:
  CRIED
  DRIED
  FRIED
  PRIED
  TRIED
SXOOP has 5 potential solutions:
  SCOOP
  SLOOP
  SNOOP
  STOOP
  SWOOP
XLUSH has 4 potential solutions:
  BLUSH
  FLUSH
  PLUSH
  SLUSH
BEXCH has 4 potential solutions:
  BEACH
  BEECH
  BELCH
  BENCH
XARRY has 4 potential solutions:
  CARRY
  HARRY
  MARRY
  PARRY
PRIXE has 4 potential solutions:
  PRICE
  PRIDE
  PRIME
  PRIZE
PAXER has 4 potential solutions:
  PALER
  PAPER
  PARER
  PAYER
XRAWL has 4 potential solutions:
  BRAWL
  CRAWL
  DRAWL
  TRAWL
CRAXE has 4 potential solutions:
  CRANE
  CRATE
  CRAVE
  CRAZE
CLXCK has 4 potential solutions:
  CLACK
  CLICK
  CLOCK
  CLUCK
XEEDY has 4 potential solutions:
  NEEDY
  REEDY
  SEEDY
  WEEDY
XRAIN has 4 potential solutions:
  BRAIN
  DRAIN
  GRAIN
  TRAIN
FLXCK has 4 potential solutions:
  FLACK
  FLECK
  FLICK
  FLOCK
BASIX has 4 potential solutions:
  BASIC
  BASIL
  BASIN
  BASIS
STEEX has 4 potential solutions:
  STEED
  STEEL
  STEEP
  STEER
XOAST has 4 potential solutions:
  BOAST
  COAST
  ROAST
  TOAST
FIXER has 4 potential solutions:
  FIBER
  FILER
  FINER
  FIXER
XINER has 4 potential solutions:
  DINER
  FINER
  LINER
  MINER
STORX has 4 potential solutions:
  STORE
  STORK
  STORM
  STORY
XROVE has 4 potential solutions:
  DROVE
  GROVE
  PROVE
  TROVE
PROXE has 4 potential solutions:
  PROBE
  PRONE
  PROSE
  PROVE
BRINX has 4 potential solutions:
  BRINE
  BRING
  BRINK
  BRINY
XREAK has 4 potential solutions:
  BREAK
  CREAK
  FREAK
  WREAK
XONIC has 4 potential solutions:
  CONIC
  IONIC
  SONIC
  TONIC
XRANK has 4 potential solutions:
  CRANK
  DRANK
  FRANK
  PRANK
XRICK has 4 potential solutions:
  BRICK
  CRICK
  PRICK
  TRICK
XOIST has 4 potential solutions:
  FOIST
  HOIST
  JOIST
  MOIST
SHARX has 4 potential solutions:
  SHARD
  SHARE
  SHARK
  SHARP
SXILL has 4 potential solutions:
  SKILL
  SPILL
  STILL
  SWILL
XASTY has 4 potential solutions:
  HASTY
  NASTY
  PASTY
  TASTY
XLACK has 4 potential solutions:
  BLACK
  CLACK
  FLACK
  SLACK
XOUCH has 4 potential solutions:
  COUCH
  POUCH
  TOUCH
  VOUCH
XOOSE has 4 potential solutions:
  GOOSE
  LOOSE
  MOOSE
  NOOSE
XEVER has 4 potential solutions:
  FEVER
  LEVER
  NEVER
  SEVER
STEAX has 4 potential solutions:
  STEAD
  STEAK
  STEAL
  STEAM
STAXK has 4 potential solutions:
  STACK
  STALK
  STANK
  STARK
BLXND has 4 potential solutions:
  BLAND
  BLEND
  BLIND
  BLOND
XIVER has 4 potential solutions:
  DIVER
  GIVER
  LIVER
  RIVER
TRIXE has 4 potential solutions:
  TRIBE
  TRICE
  TRIPE
  TRITE
XINCH has 4 potential solutions:
  CINCH
  FINCH
  PINCH
  WINCH
SXEAR has 4 potential solutions:
  SHEAR
  SMEAR
  SPEAR
  SWEAR
STXCK has 4 potential solutions:
  STACK
  STICK
  STOCK
  STUCK
XAINT has 4 potential solutions:
  FAINT
  PAINT
  SAINT
  TAINT
SCALX has 4 potential solutions:
  SCALD
  SCALE
  SCALP
  SCALY
SXING has 4 potential solutions:
  SLING
  STING
  SUING
  SWING
SXELL has 4 potential solutions:
  SHELL
  SMELL
  SPELL
  SWELL
XOUSE has 4 potential solutions:
  HOUSE
  LOUSE
  MOUSE
  ROUSE
COVEX has 4 potential solutions:
  COVEN
  COVER
  COVET
  COVEY
MANGX has 4 potential solutions:
  MANGA
  MANGE
  MANGO
  MANGY
SHEEX has 4 potential solutions:
  SHEEN
  SHEEP
  SHEER
  SHEET
SXEEP has 4 potential solutions:
  SHEEP
  SLEEP
  STEEP
  SWEEP
XOWEL has 4 potential solutions:
  BOWEL
  DOWEL
  TOWEL
  VOWEL
XITTY has 4 potential solutions:
  BITTY
  DITTY
  KITTY
  WITTY
XUDGE has 4 potential solutions:
  BUDGE
  FUDGE
  JUDGE
  NUDGE
XALLY has 4 potential solutions:
  DALLY
  RALLY
  SALLY
  TALLY
DXLLY has 4 potential solutions:
  DALLY
  DILLY
  DOLLY
  DULLY
XIDER has 4 potential solutions:
  AIDER
  CIDER
  RIDER
  WIDER
RIXER has 4 potential solutions:
  RIDER
  RIPER
  RISER
  RIVER
XREED has 4 potential solutions:
  BREED
  CREED
  FREED
  GREED
CHXCK has 4 potential solutions:
  CHECK
  CHICK
  CHOCK
  CHUCK
XITCH has 4 potential solutions:
  DITCH
  HITCH
  PITCH
  WITCH
XLANK has 4 potential solutions:
  BLANK
  CLANK
  FLANK
  PLANK
SXASH has 4 potential solutions:
  SLASH
  SMASH
  STASH
  SWASH
WAXER has 4 potential solutions:
  WAFER
  WAGER
  WATER
  WAVER
XEAST has 4 potential solutions:
  BEAST
  FEAST
  LEAST
  YEAST
BLAXE has 4 potential solutions:
  BLADE
  BLAME
  BLARE
  BLAZE
SXUNK has 4 potential solutions:
  SKUNK
  SLUNK
  SPUNK
  STUNK
XRILL has 4 potential solutions:
  DRILL
  FRILL
  GRILL
  KRILL
SPOOX has 4 potential solutions:
  SPOOF
  SPOOK
  SPOOL
  SPOON
```
