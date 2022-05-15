#
# Gigatron ROMvX0 4x6 font for ASCII codes 32 (SP) to 126 (~).
# Additionally there is a cursor symbol (127) and four dodgey arrow symbols, (128 to 131).
#

def _char4x6(*args):
  """Convert character from easy-readable strings data into ROM bytes"""
  X, Y = len(args[0]), len(args)
  bytes = []
  for y in range(Y):
    byte = 0
    for x in range(X):
      bit = 0 if args[y][x]=='.' else 1
      byte = 2*byte + bit
    bytes.append(byte)
  return bytes

font4x6 = [
  _char4x6(   #' '
    ('....'
     '....'),
    ('....'
     '....'),
    ('....'
     '....')),
  _char4x6(   #'!'
    ('.#..'
     '.#..'),
    ('.#..'
     '....'),
    ('.#..'
     '....')),
  _char4x6(   #'"'
    ('#.#.'
     '#.#.'),
    ('#.#.'
     '....'),
    ('....'
     '....')),
  _char4x6(   #'#'
    ('.#..'
     '###.'),
    ('.#..'
     '###.'),
    ('.#..'
     '....')),
  _char4x6(   #'$'
    ('.##.'
     '#...'),
    ('.#..'
     '..#.'),
    ('##..'
     '....')),
  _char4x6(   #'%'
    ('#...'
     '..#.'),
    ('.#..'
     '#...'),
    ('..#.'
     '....')),
  _char4x6(   #'&'
    ('.#..'
     '#.#.'),
    ('#.#.'
     '##..'),
    ('.##.'
     '....')),
  _char4x6(   #"'"
    ('.#..'
     '.#..'),
    ('#...'
     '....'),
    ('....'
     '....')),
  _char4x6(   #'('
    ('..#.'
     '.#..'),
    ('.#..'
     '.#..'),
    ('..#.'
     '....')),
  _char4x6(   #'),'
    ('#...'
     '.#..'),
    ('.#..'
     '.#..'),
    ('#...'
     '....')),
  _char4x6(   #'*'
    ('....'
     '#.#.'),
    ('.#..'
     '#.#.'),
    ('....'
     '....')),
  _char4x6(   #'+'
    ('....'
     '.#..'),
    ('###.'
     '.#..'),
    ('....'
     '....')),
  _char4x6(   #','
    ('....'
     '....'),
    ('....'
     '....'),
    ('.#..'
     '#...')),
  _char4x6(   #'-'
    ('....'
     '....'),
    ('###.'
     '....'),
    ('....'
     '....')),
  _char4x6(   #'.'
    ('....'
     '....'),
    ('....'
     '....'),
    ('#...'
     '....')),
  _char4x6(   #'/'
    ('....'
     '..#.'),
    ('.#..'
     '#...'),
    ('....'
     '....')),
  _char4x6(   #'0'
    ('###.'
     '#.#.'),
    ('#.#.'
     '#.#.'),
    ('###.'
     '....')),
  _char4x6(   #'1'
    ('.#..'
     '##..'),
    ('.#..'
     '.#..'),
    ('###.'
     '....')),
  _char4x6(   #'2'
    ('###.'
     '..#.'),
    ('###.'
     '#...'),
    ('###.'
     '....')),
  _char4x6(   #'3'
    ('###.'
     '..#.'),
    ('.##.'
     '..#.'),
    ('###.'
     '....')),
  _char4x6(   #'4'
    ('#...'
     '#...'),
    ('##..'
     '###.'),
    ('.#..'
     '....')),
  _char4x6(   #'5'
    ('###.'
     '#...'),
    ('###.'
     '..#.'),
    ('###.'
     '....')),
  _char4x6(   #'6'
    ('###.'
     '#...'),
    ('###.'
     '#.#.'),
    ('###.'
     '....')),
  _char4x6(   #'7'
    ('###.'
     '..#.'),
    ('..#.'
     '..#.'),
    ('..#.'
     '....')),
  _char4x6(   #'8'
    ('###.'
     '#.#.'),
    ('###.'
     '#.#.'),
    ('###.'
     '....')),
  _char4x6(   #'9'
    ('###.'
     '#.#.'),
    ('###.'
     '..#.'),
    ('..#.'
     '....')),
  _char4x6(   #':'
    ('....'
     '.#..'),
    ('....'
     '.#..'),
    ('....'
     '....')),
  _char4x6(   #';'
    ('....'
     '....'),
    ('.#..'
     '....'),
    ('.#..'
     '#...')),
  _char4x6(   #'<'
    ('..#.'
     '.#..'),
    ('#...'
     '.#..'),
    ('..#.'
     '....')),
  _char4x6(   #'='
    ('....'
     '###.'),
    ('....'
     '###.'),
    ('....'
     '....')),
  _char4x6(   #'>'
    ('#...'
     '.#..'),
    ('..#.'
     '.#..'),
    ('#...'
     '....')),
  _char4x6(   #'?'
    ('##..'
     '..#.'),
    ('.##.'
     '....'),
    ('.#..'
     '....')),
  _char4x6(   #'@'
    ('.##.'
     '#.#.'),
    ('###.'
     '#...'),
    ('.##.'
     '....')),
  _char4x6(   #'A'
    ('.#..'
     '#.#.'),
    ('###.'
     '#.#.'),
    ('#.#.'
     '....')),
  _char4x6(   #'B'
    ('##..'
     '#.#.'),
    ('##..'
     '#.#.'),
    ('##..'
     '....')),
  _char4x6(   #'C'
    ('.##.'
     '#...'),
    ('#...'
     '#...'),
    ('.##.'
     '....')),
  _char4x6(   #'D'
    ('##..'
     '#.#.'),
    ('#.#.'
     '#.#.'),
    ('##..'
     '....')),
  _char4x6(   #'E'
    ('###.'
     '#...'),
    ('##..'
     '#...'),
    ('###.'
     '....')),
  _char4x6(   #'F'
    ('###.'
     '#...'),
    ('##..'
     '#...'),
    ('#...'
     '....')),
  _char4x6(   #'G'
    ('.##.'
     '#...'),
    ('#.#.'
     '#.#.'),
    ('.##.'
     '....')),
  _char4x6(   #'H'
    ('#.#.'
     '#.#.'),
    ('###.'
     '#.#.'),
    ('#.#.'
     '....')),
  _char4x6(   #'I'
    ('###.'
     '.#..'),
    ('.#..'
     '.#..'),
    ('###.'
     '....')),
  _char4x6(   #'J'
    ('..#.'
     '..#.'),
    ('..#.'
     '#.#.'),
    ('.#..'
     '....')),
  _char4x6(   #'K'
    ('#.#.'
     '#.#.'),
    ('##..'
     '#.#.'),
    ('#.#.'
     '....')),
  _char4x6(   #'L'
    ('#...'
     '#...'),
    ('#...'
     '#...'),
    ('###.'
     '....')),
  _char4x6(   #'M'
    ('#.#.'
     '###.'),
    ('#.#.'
     '#.#.'),
    ('#.#.'
     '....')),
  _char4x6(   #'N'
    ('###.'
     '#.#.'),
    ('#.#.'
     '#.#.'),
    ('#.#.'
     '....')),
  _char4x6(   #'O'
    ('###.'
     '#.#.'),
    ('#.#.'
     '#.#.'),
    ('###.'
     '....')),
  _char4x6(   #'P'
    ('##..'
     '#.#.'),
    ('##..'
     '#...'),
    ('#...'
     '....')),
  _char4x6(   #'Q'
    ('###.'
     '#.#.'),
    ('#.#.'
     '###.'),
    ('..#.'
     '....')),
  _char4x6(   #'R'
    ('##..'
     '#.#.'),
    ('##..'
     '#.#.'),
    ('#.#.'
     '....')),
  _char4x6(   #'S'
    ('.##.'
     '#...'),
    ('###.'
     '..#.'),
    ('##..'
     '....')),
  _char4x6(   #'T'
    ('###.'
     '.#..'),
    ('.#..'
     '.#..'),
    ('.#..'
     '....')),
  _char4x6(   #'U'
    ('#.#.'
     '#.#.'),
    ('#.#.'
     '#.#.'),
    ('###.'
     '....')),
  _char4x6(   #'V'
    ('#.#.'
     '#.#.'),
    ('#.#.'
     '#.#.'),
    ('.#..'
     '....')),
  _char4x6(   #'W'
    ('#.#.'
     '#.#.'),
    ('#.#.'
     '###.'),
    ('#.#.'
     '....')),
  _char4x6(   #'X'
    ('#.#.'
     '#.#.'),
    ('.#..'
     '#.#.'),
    ('#.#.'
     '....')),
  _char4x6(   #'Y'
    ('#.#.'
     '#.#.'),
    ('#.#.'
     '.#..'),
    ('.#..'
     '....')),
  _char4x6(   #'Z'
    ('###.'
     '..#.'),
    ('.#..'
     '#...'),
    ('###.'
     '....')),
  _char4x6(   #'['
    ('.##.'
     '.#..'),
    ('.#..'
     '.#..'),
    ('.##.'
     '....')),
  _char4x6(   #'\\'
    ('....'
     '#...'),
    ('.#..'
     '..#.'),
    ('....'
     '....')),
  _char4x6(   #']'
    ('.##.'
     '..#.'),
    ('..#.'
     '..#.'),
    ('.##.'
     '....')),
  _char4x6(   #'^'
    ('.#..'
     '#.#.'),
    ('....'
     '....'),
    ('....'
     '....')),
  _char4x6(   #'_'
    ('....'
     '....'),
    ('....'
     '....'),
    ('###.'
     '....')),
  _char4x6(   #'`'
    ('#...'
     '.#..'),
    ('....'
     '....'),
    ('....'
     '....')),
  _char4x6(   #'a'
    ('....'
     '.##.'),
    ('#.#.'
     '#.#.'),
    ('.##.'
     '....')),
  _char4x6(   #'b'
    ('#...'
     '##..'),
    ('#.#.'
     '#.#.'),
    ('##..'
     '....')),
  _char4x6(   #'c'
    ('....'
     '.##.'),
    ('#...'
     '#...'),
    ('.##.'
     '....')),
  _char4x6(   #'d'
    ('..#.'
     '.##.'),
    ('#.#.'
     '#.#.'),
    ('.##.'
     '....')),
  _char4x6(   #'e'
    ('....'
     '.##.'),
    ('#...'
     '##..'),
    ('.##.'
     '....')),
  _char4x6(   #'f'
    ('.##.'
     '.#..'),
    ('###.'
     '.#..'),
    ('.#..'
     '....')),
  _char4x6(   #'g'
    ('....'
     '.##.'),
    ('#.#.'
     '.##.'),
    ('..#.'
     '##..')),
  _char4x6(   #'h'
    ('#...'
     '##..'),
    ('#.#.'
     '#.#.'),
    ('#.#.'
     '....')),
  _char4x6(   #'i'
    ('.#..'
     '....'),
    ('.#..'
     '.#..'),
    ('.#..'
     '....')),
  _char4x6(   #'j'
    ('.#..'
     '....'),
    ('.#..'
     '.#..'),
    ('.#..'
     '##..')),
  _char4x6(   #'k'
    ('#...'
     '#.#.'),
    ('##..'
     '##..'),
    ('#.#.'
     '....')),
  _char4x6(   #'l'
    ('#...'
     '#...'),
    ('#...'
     '#...'),
    ('.#..'
     '....')),
  _char4x6(   #'m'
    ('....'
     '###.'),
    ('###.'
     '#.#.'),
    ('#.#.'
     '....')),
  _char4x6(   #'n'
    ('....'
     '###.'),
    ('#.#.'
     '#.#.'),
    ('#.#.'
     '....')),
  _char4x6(   #'o'
    ('....'
     '###.'),
    ('#.#.'
     '#.#.'),
    ('###.'
     '....')),
  _char4x6(   #'p'
    ('....'
     '##..'),
    ('#.#.'
     '##..'),
    ('#...'
     '#...')),
  _char4x6(   #'q'
    ('....'
     '.##.'),
    ('#.#.'
     '.##.'),
    ('..#.'
     '..#.')),
  _char4x6(   #'r'
    ('....'
     '##..'),
    ('#.#.'
     '#...'),
    ('#...'
     '....')),
  _char4x6(   #'s'
    ('....'
     '###.'),
    ('#...'
     '.##.'),
    ('###.'
     '....')),
  _char4x6(   #'t'
    ('.#..'
     '###.'),
    ('.#..'
     '.#..'),
    ('.##.'
     '....')),
  _char4x6(   #'u'
    ('....'
     '#.#.'),
    ('#.#.'
     '#.#.'),
    ('###.'
     '....')),
  _char4x6(   #'v'
    ('....'
     '#.#.'),
    ('#.#.'
     '#.#.'),
    ('.#..'
     '....')),
  _char4x6(   #'w'
    ('....'
     '#.#.'),
    ('#.#.'
     '###.'),
    ('###.'
     '....')),
  _char4x6(   #'x'
    ('....'
     '#.#.'),
    ('.#..'
     '.#..'),
    ('#.#.'
     '....')),
  _char4x6(   #'y'
    ('....'
     '#.#.'),
    ('#.#.'
     '#.#.'),
    ('.#..'
     '.#..')),
  _char4x6(   #'z'
    ('....'
     '###.'),
    ('..#.'
     '.#..'),
    ('###.'
     '....')),
  _char4x6(   #'{'
    ('.##.'
     '.#..'),
    ('##..'
     '.#..'),
    ('.##.'
     '....')),
  _char4x6(   #'|'
    ('.#..'
     '.#..'),
    ('.#..'
     '.#..'),
    ('.#..'
     '....')),
  _char4x6(   #'}'
    ('##..'
     '.#..'),
    ('.##.'
     '.#..'),
    ('##..'
     '....')),
  _char4x6(   #'~'
    ('....'
     '....'),
    ('###.'
     '....'),
    ('....'
     '....')),
  _char4x6(   #'\x7f'
    ('###.'
     '###.'),
    ('###.'
     '###.'),
    ('###.'
     '....')),
  _char4x6(   #U+2190 Leftwards arrow
    ('....'
     '.#..'),
    ('#...'
     '#...'),
    ('.#..'
     '....')),
  _char4x6(   #U+2191 Upwards arrow
    ('....'
     '.##.'),
    ('#..#'
     '....'),
    ('....'
     '....')),
  _char4x6(   #U+2192 Rightwards arrow
    ('....'
     '..#.'),
    ('...#'
     '...#'),
    ('..#.'
     '....')),
  _char4x6(   #U+2193 Downwards arrow
    ('....'
     '....'),
    ('....'
     '#..#'),
    ('.##.'
     '....')),
]
