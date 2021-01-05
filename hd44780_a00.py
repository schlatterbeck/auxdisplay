""" Python Character Mapping Codec for Hitachi HD44780 Display with ROM
    character set variant A00
"""

import codecs

class Codec(codecs.Codec):

    def encode(self,input,errors='strict'):
        return codecs.charmap_encode(input,errors,encoding_map)

    def decode(self,input,errors='strict'):
        return codecs.charmap_decode(input,errors,decoding_map)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input,self.errors,encoding_map)[0]

class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_decode(input,self.errors,decoding_map)[0]

class StreamWriter(Codec,codecs.StreamWriter):
    pass

class StreamReader(Codec,codecs.StreamReader):
    pass

### encodings module API

def get_hd44780_a00(name):
    if name == 'hd44780-a00':
        return codecs.CodecInfo(
            name='hd44780-a00',
            encode=Codec().encode,
            decode=Codec().decode,
            incrementalencoder=IncrementalEncoder,
            incrementaldecoder=IncrementalDecoder,
            streamreader=StreamReader,
            streamwriter=StreamWriter,
        )
### Decoding Map
decoding_map = codecs.make_identity_dict(range(128))
decoding_map.update({
    # The whole column 0x1X maps to space
    0x0010: 0x0020,
    0x0011: 0x0020,
    0x0012: 0x0020,
    0x0013: 0x0020,
    0x0014: 0x0020,
    0x0015: 0x0020,
    0x0016: 0x0020,
    0x0017: 0x0020,
    0x0018: 0x0020,
    0x0019: 0x0020,
    0x001a: 0x0020,
    0x001b: 0x0020,
    0x001c: 0x0020,
    0x001d: 0x0020,
    0x001e: 0x0020,
    0x001f: 0x0020,

    0x005c: 0x00a5,     #  YEN SIGN
    0x007e: 0x2192,     #  RIGHTWARDS ARROW
    0x007f: 0x2190,     #  LEFTWARDS ARROW
    # The whole column 0x8X maps to space
    0x0080: 0x0020,
    0x0081: 0x0020,
    0x0082: 0x0020,
    0x0083: 0x0020,
    0x0084: 0x0020,
    0x0085: 0x0020,
    0x0086: 0x0020,
    0x0087: 0x0020,
    0x0088: 0x0020,
    0x0089: 0x0020,
    0x008a: 0x0020,
    0x008b: 0x0020,
    0x008c: 0x0020,
    0x008d: 0x0020,
    0x008e: 0x0020,
    0x008f: 0x0020,
    # The whole column 0x9X maps to space
    0x0090: 0x0020,
    0x0091: 0x0020,
    0x0092: 0x0020,
    0x0093: 0x0020,
    0x0094: 0x0020,
    0x0095: 0x0020,
    0x0096: 0x0020,
    0x0097: 0x0020,
    0x0098: 0x0020,
    0x0099: 0x0020,
    0x009a: 0x0020,
    0x009b: 0x0020,
    0x009c: 0x0020,
    0x009d: 0x0020,
    0x009e: 0x0020,
    0x009f: 0x0020,

    # Special Chars, todo
    0x00a0: 0x0020,
    0x00a5: 0x00b7,     #  MIDDLE DOT
    0x00ae: 0x2203,     #  THERE EXISTS
    0x00b0: 0x002d,     #  HYPHEN-MINUS
    0x00df: 0x00b0,     #  DEGREE SIGN
    0x00e0: 0x03b1,     #  GREEK SMALL LETTER ALPHA
    0x00e1: 0x00e4,     #  LATIN SMALL LETTER A WITH DIAERESIS
    0x00e2: 0x00df,     #  LATIN SMALL LETTER SHARP S
    0x00e3: 0x03b5,     #  GREEK SMALL LETTER EPSILON
    0x00e4: 0x00b5,     #  MICRO SIGN
    0x00e5: 0x03c3,     #  GREEK SMALL LETTER SIGMA
    0x00e6: 0x03c1,     #  GREEK SMALL LETTER RHO
    0x00e8: 0x221a,     #  SQUARE ROOT
    0x00eb: 0x02e3,     #  Superscript CAPITAL LETTER X
    0x00ec: 0x00a2,     #  CENT SIGN
    0x00ed: 0x00a3,     #  POUND SIGN
    0x00ee: 0x00f1,     #  LATIN SMALL LETTER N WITH TILDE
    0x00ef: 0x00f6,     #  LATIN SMALL LETTER O WITH DIAERESIS
    0x00f2: 0x03b8,     #  GREEK SMALL LETTER THETA
    0x00f3: 0x221e,     #  INFINITY
    0x00f4: 0x03a9,     #  GREEK CAPITAL LETTER OMEGA
    0x00f5: 0x00fc,     #  LATIN SMALL LETTER U WITH DIAERESIS
    0x00f6: 0x03a3,     #  GREEK CAPITAL LETTER SIGMA
    0x00f7: 0x03c0,     #  GREEK SMALL LETTER PI
    0x00fd: 0x00f7,     #  DIVISION SIGN
    0x00fe: 0x0020,
    0x00ff: 0x2588,     #  FULL BLOCK

    # characters extending below baseline
    0x00e7: 0x0067,     #  LATIN SMALL LETTER G
    0x00ea: 0x006a,     #  LATIN SMALL LETTER J
    0x00f0: 0x0070,     #  LATIN SMALL LETTER P
    0x00f1: 0x0071,     #  LATIN SMALL LETTER Q
    0x00f9: 0x0079,     #  LATIN SMALL LETTER Y
})

encoding_map = {
    0x0008: 0x0008,     #  Backspace
    0x0009: 0x0009,     #  Tab (mapped to space by display driver)
    0x000a: 0x000a,     #  Newline
    0x000c: 0x000c,     #  Clear Screen
    0x000d: 0x000d,     #  Carriage Return
    0x001b: 0x001b,     #  ESC
    0x0020: 0x0020,     #  SPACE
    0x0021: 0x0021,     #  EXCLAMATION MARK
    0x0022: 0x0022,     #  QUOTATION MARK
    0x0023: 0x0023,     #  NUMBER SIGN
    0x0024: 0x0024,     #  DOLLAR SIGN
    0x0025: 0x0025,     #  PERCENT SIGN
    0x0026: 0x0026,     #  AMPERSAND
    0x0027: 0x0027,     #  APOSTROPHE
    0x0028: 0x0028,     #  LEFT PARENTHESIS
    0x0029: 0x0029,     #  RIGHT PARENTHESIS
    0x002a: 0x002a,     #  ASTERISK
    0x002b: 0x002b,     #  PLUS SIGN
    0x002c: 0x002c,     #  COMMA
    0x002d: 0x002d,     #  HYPHEN-MINUS
    0x002e: 0x002e,     #  FULL STOP
    0x002f: 0x002f,     #  SOLIDUS
    0x0030: 0x0030,     #  DIGIT ZERO
    0x0031: 0x0031,     #  DIGIT ONE
    0x0032: 0x0032,     #  DIGIT TWO
    0x0033: 0x0033,     #  DIGIT THREE
    0x0034: 0x0034,     #  DIGIT FOUR
    0x0035: 0x0035,     #  DIGIT FIVE
    0x0036: 0x0036,     #  DIGIT SIX
    0x0037: 0x0037,     #  DIGIT SEVEN
    0x0038: 0x0038,     #  DIGIT EIGHT
    0x0039: 0x0039,     #  DIGIT NINE
    0x003a: 0x003a,     #  COLON
    0x003b: 0x003b,     #  SEMICOLON
    0x003c: 0x003c,     #  LESS-THAN SIGN
    0x003d: 0x003d,     #  EQUALS SIGN
    0x003e: 0x003e,     #  GREATER-THAN SIGN
    0x003f: 0x003f,     #  QUESTION MARK
    0x0040: 0x0040,     #  COMMERCIAL AT
    0x0041: 0x0041,     #  LATIN CAPITAL LETTER A
    0x0042: 0x0042,     #  LATIN CAPITAL LETTER B
    0x0043: 0x0043,     #  LATIN CAPITAL LETTER C
    0x0044: 0x0044,     #  LATIN CAPITAL LETTER D
    0x0045: 0x0045,     #  LATIN CAPITAL LETTER E
    0x0046: 0x0046,     #  LATIN CAPITAL LETTER F
    0x0047: 0x0047,     #  LATIN CAPITAL LETTER G
    0x0048: 0x0048,     #  LATIN CAPITAL LETTER H
    0x0049: 0x0049,     #  LATIN CAPITAL LETTER I
    0x004a: 0x004a,     #  LATIN CAPITAL LETTER J
    0x004b: 0x004b,     #  LATIN CAPITAL LETTER K
    0x004c: 0x004c,     #  LATIN CAPITAL LETTER L
    0x004d: 0x004d,     #  LATIN CAPITAL LETTER M
    0x004e: 0x004e,     #  LATIN CAPITAL LETTER N
    0x004f: 0x004f,     #  LATIN CAPITAL LETTER O
    0x0050: 0x0050,     #  LATIN CAPITAL LETTER P
    0x0051: 0x0051,     #  LATIN CAPITAL LETTER Q
    0x0052: 0x0052,     #  LATIN CAPITAL LETTER R
    0x0053: 0x0053,     #  LATIN CAPITAL LETTER S
    0x0054: 0x0054,     #  LATIN CAPITAL LETTER T
    0x0055: 0x0055,     #  LATIN CAPITAL LETTER U
    0x0056: 0x0056,     #  LATIN CAPITAL LETTER V
    0x0057: 0x0057,     #  LATIN CAPITAL LETTER W
    0x0058: 0x0058,     #  LATIN CAPITAL LETTER X
    0x0059: 0x0059,     #  LATIN CAPITAL LETTER Y
    0x005a: 0x005a,     #  LATIN CAPITAL LETTER Z
    0x005b: 0x005b,     #  LEFT SQUARE BRACKET
#    0x005c: 0x00cd,     #  REVERSE SOLIDUS ("Backslash")
    0x005c: 0x00a4,     #  REVERSE SOLIDUS ("Backslash")
    0x005d: 0x005d,     #  RIGHT SQUARE BRACKET
    0x005e: 0x005e,     #  CIRCUMFLEX ACCENT
    0x005f: 0x005f,     #  LOW LINE
    0x0060: 0x0060,     #  GRAVE ACCENT
    0x0061: 0x0061,     #  LATIN SMALL LETTER A
    0x0062: 0x0062,     #  LATIN SMALL LETTER B
    0x0063: 0x0063,     #  LATIN SMALL LETTER C
    0x0064: 0x0064,     #  LATIN SMALL LETTER D
    0x0065: 0x0065,     #  LATIN SMALL LETTER E
    0x0066: 0x0066,     #  LATIN SMALL LETTER F
    # Variant extending below baseline, lowest line not displayed
    0x0067: 0x00e7,     #  LATIN SMALL LETTER G
    0x0067: 0x0067,     #  LATIN SMALL LETTER G
    0x0068: 0x0068,     #  LATIN SMALL LETTER H
    0x0069: 0x0069,     #  LATIN SMALL LETTER I
    # Variant extending below baseline, lowest line not displayed
    0x006a: 0x00ea,     #  LATIN SMALL LETTER J
    0x006a: 0x006a,     #  LATIN SMALL LETTER J
    0x006b: 0x006b,     #  LATIN SMALL LETTER K
    0x006c: 0x006c,     #  LATIN SMALL LETTER L
    0x006d: 0x006d,     #  LATIN SMALL LETTER M
    0x006e: 0x006e,     #  LATIN SMALL LETTER N
    0x006f: 0x006f,     #  LATIN SMALL LETTER O
    0x0070: 0x0070,     #  LATIN SMALL LETTER P
    # Variant extending below baseline, still better than without
    0x0070: 0x00f0,     #  LATIN SMALL LETTER P
    0x0071: 0x0071,     #  LATIN SMALL LETTER Q
    # Variant extending below baseline, still better than without
    0x0071: 0x00f1,     #  LATIN SMALL LETTER Q
    0x0072: 0x0072,     #  LATIN SMALL LETTER R
    0x0073: 0x0073,     #  LATIN SMALL LETTER S
    0x0074: 0x0074,     #  LATIN SMALL LETTER T
    0x0075: 0x0075,     #  LATIN SMALL LETTER U
    0x0076: 0x0076,     #  LATIN SMALL LETTER V
    0x0077: 0x0077,     #  LATIN SMALL LETTER W
    0x0078: 0x0078,     #  LATIN SMALL LETTER X
    # Variant extending below baseline, lowest line not displayed
    0x0079: 0x00f9,     #  LATIN SMALL LETTER Y
    0x0079: 0x0079,     #  LATIN SMALL LETTER Y
    0x007a: 0x007a,     #  LATIN SMALL LETTER Z
    0x007b: 0x007b,     #  LEFT CURLY BRACKET
    0x007c: 0x007c,     #  VERTICAL LINE
    0x007d: 0x007d,     #  RIGHT CURLY BRACKET

    0x00a2: 0x00ec,     #  CENT SIGN
    0x00a3: 0x00ed,     #  POUND SIGN
    0x00a5: 0x005c,     #  YEN SIGN
    0x00b0: 0x00df,     #  DEGREE SIGN
    0x00b5: 0x00e4,     #  MICRO SIGN
    0x00b7: 0x00a5,     #  MIDDLE DOT
    0x00df: 0x00e2,     #  LATIN SMALL LETTER SHARP S
    0x00e4: 0x00e1,     #  LATIN SMALL LETTER A WITH DIAERESIS
    0x00f1: 0x00ee,     #  LATIN SMALL LETTER N WITH TILDE
    0x00f6: 0x00ef,     #  LATIN SMALL LETTER O WITH DIAERESIS
    0x00f7: 0x00fd,     #  DIVISION SIGN
    0x00fc: 0x00f5,     #  LATIN SMALL LETTER U WITH DIAERESIS
    0x02e3: 0x00eb,     #  Superscript CAPITAL LETTER X
    0x03a3: 0x00f6,     #  GREEK CAPITAL LETTER SIGMA
    0x03a9: 0x00f4,     #  GREEK CAPITAL LETTER OMEGA
    0x03b1: 0x00e0,     #  GREEK SMALL LETTER ALPHA
    0x03b2: 0x00e2,     #  GREEK SMALL LETTER BETA
    0x03b5: 0x00e3,     #  GREEK SMALL LETTER EPSILON
    0x03b8: 0x00f2,     #  GREEK SMALL LETTER THETA
    0x03bc: 0x00e4,     #  GREEK SMALL LETTER MU
    0x03c0: 0x00f7,     #  GREEK SMALL LETTER PI
    0x03c1: 0x00e6,     #  GREEK SMALL LETTER RHO
    0x03c3: 0x00e5,     #  GREEK SMALL LETTER SIGMA
    0x2190: 0x007f,     #  LEFTWARDS ARROW
    0x2192: 0x007e,     #  RIGHTWARDS ARROW
    0x2203: 0x00ae,     #  THERE EXISTS
    0x221a: 0x00e8,     #  SQUARE ROOT
    0x221d: 0x00e0,     #  PROPORTIONAL TO
    0x221e: 0x00f3,     #  INFINITY
    0x2588: 0x00ff,     #  FULL BLOCK
#Katakana
    0x30a1: 0x00a7,     #  a (kana)
    0x30a2: 0x00b1,     #  A (kana)
    0x30a3: 0x00a8,     #  i (kana)
    0x30a4: 0x00b2,     #  I (kana)
    0x30a5: 0x00a9,     #  u (kana)
    0x30a6: 0x00b3,     #  U (kana)
    0x30a7: 0x00aa,     #  e (kana)
    0x30a8: 0x00b4,     #  E (kana)
    0x30a9: 0x00ab,     #  O (kana)
    0x30aa: 0x00b5,     #  O (kana)
    0x30ab: 0x00b6,     #  Ka (kana)
    0x30ad: 0x00b7,     #  Ki (kana)
    0x30af: 0x00b8,     #  Ku (kana)
    0x30b1: 0x00b9,     #  Ke (kana)
    0x30b3: 0x00ba,     #  Ko (kana)
    0x30b5: 0x00bb,     #  Sa (kana)
    0x30b7: 0x00bc,     #  Shi (kana)
    0x30b9: 0x00bd,     #  Su (kana)
    0x30bb: 0x00be,     #  Se (kana)
    0x30bd: 0x00bf,     #  So (kana)
    0x30bf: 0x00c0,     #  Ta (kana)
    0x30c1: 0x00c1,     #  Chi (kana)
    0x30c3: 0x00af,     #  tsu (kana) Sokuon
    0x30c4: 0x00c2,     #  Tsu (kana)
    0x30c6: 0x00c3,     #  Te (kana)
    0x30c8: 0x00c4,     #  To (kana)
    0x30ca: 0x00c5,     #  Na (kana)
    0x30cb: 0x00c6,     #  Ni (kana)
    0x30cc: 0x00c7,     #  Nu (kana)
    0x30cd: 0x00c8,     #  Ne (kana)
    0x30ce: 0x00c9,     #  No (kana)
    0x30cf: 0x00ca,     #  Ha (kana)
    0x30d2: 0x00cb,     #  Hi (kana)
    0x30d5: 0x00cc,     #  Fu (kana)
    0x30d8: 0x00cd,     #  He (kana)
    0x30db: 0x00ce,     #  Ho (kana)
    0x30de: 0x00cf,     #  Ma (kana)
    0x30df: 0x00d0,     #  Mi (kana)
    0x30e0: 0x00d1,     #  Mu (kana)
    0x30e1: 0x00d2,     #  Me (kana)
    0x30e2: 0x00d3,     #  Mo (kana)
    0x30e4: 0x00d4,     #  Ya (kana)
    0x30e5: 0x00ad,     #  yu (kana)
    0x30e6: 0x00d5,     #  Yu (kana)
    0x30e7: 0x00ae,     #  yo (kana)
    0x30e8: 0x00d6,     #  Yo (kana)
    0x30e9: 0x00d7,     #  Ra (kana)
    0x30ea: 0x00d8,     #  Ri (kana)
    0x30eb: 0x00d9,     #  Ru (kana)
    0x30ec: 0x00da,     #  Re (kana)
    0x30ed: 0x00db,     #  Ro (kana)
    0x30ef: 0x00dc,     #  Wa (kana)
    0x30f3: 0x00dd,     #  N (kana)
    0x30f2: 0x00a6,     #  Wo (kana)
    0x30fc: 0x00b0,
    0x309b: 0x00de,
    0x309c: 0x00df,
}

codecs.register(get_hd44780_a00)
