#!/usr/bin/python3

import codecs
import hd44780_a00

class Display :
    """ Model a HD44780 compatible display on Linux
        The kernel driver for these modules support several escape
        sequences and special character.
        Note that there is a code to switch to a larger font (instead of
        5x8 dots to 5x10 dots) which is not implemented by most
        displays. Likewise there is a double-height version which is
        also not very common.
    """

    # These will be mapped to calls named 'esc_' + name
    #     name sequence
    esc_sequences = dict \
        ( clear           = b'\x1b[2J'
        , home            = b'\x1b[H'
        , display_on      = b'\x1b[LD'
        , display_off     = b'\x1b[Ld'
        , cursor_on       = b'\x1b[LC'
        , cursor_off      = b'\x1b[Lc'
        , blink_on        = b'\x1b[LB'
        , blink_off       = b'\x1b[Lb'
        , backlight_on    = b'\x1b[L+'
        , backlight_off   = b'\x1b[L-'
        , backlight_flash = b'\x1b[L*'
        , font_small      = b'\x1b[Lf'
        , font_large      = b'\x1b[LF'
        , lines_one       = b'\x1b[Ln'
        , lines_two       = b'\x1b[LN'
        , cursor_left     = b'\x1b[Ll'
        , cursor_right    = b'\x1b[Lr'
        , display_left    = b'\x1b[LL'
        , display_right   = b'\x1b[LR'
        , clr_to_eol      = b'\x1b[Lk'
        , reinit          = b'\x1b[LI'
        )

    # Pre-defined RAM characters, indexed by their unicode
    ram_chars = dict \
        ( ( ( '\u00c4' # LATIN CAPITAL LETTER A WITH DIAERESIS
            , ( 0b00010001
              , 0b00000100
              , 0b00001010
              , 0b00010001
              , 0b00011111
              , 0b00010001
              , 0b00010001
              , 0b00000000
              )
            )
          , ( '\u00d6' # LATIN CAPITAL LETTER O WITH DIAERESIS
            , ( 0b00010001
              , 0b00001110
              , 0b00010001
              , 0b00010001
              , 0b00010001
              , 0b00010001
              , 0b00001110
              , 0b00000000
              )
            )
          , ( '\u00dc' # LATIN CAPITAL LETTER U WITH DIAERESIS
            , ( 0b00010001
              , 0b00000000
              , 0b00010001
              , 0b00010001
              , 0b00010001
              , 0b00010001
              , 0b00001110
              , 0b00000000
              )
            )
          )
        )

    def __init__ (self, device = '/dev/lcd', encoding = 'hd44780-a00') :
        self.devname  = device
        self.encoding = encoding
        self.dev      = open (device, 'wb')
    # end def __init__

    def __getattr__ (self, name) :
        if name.startswith ('esc_') :
            try :
                seq = self.esc_sequences [name [4:]]
                def x () :
                    self.write (seq)
                setattr (self, name, x)
                return x
            except KeyError as err :
                raise AttributeError (err)
        raise AttributeError (name)
    # end def __getattr__

    def write (self, s) :
        if isinstance (s, str) :
            s = s.encode (self.encoding)
        self.dev.write (s)
        self.dev.flush ()
    # end def write

    def goto (self, x = None, y = None) :
        """ Position cursor at x, y, zero-based
            Note that positions too high are wrapped
        """
        if x is None and y is None :
            return
        assert x is None or 0 <= x <= 999
        assert y is None or 0 <= y <= 999
        if x is None :
            self.write (b'\x1b[Ly%d;' % y)
        elif y is None :
            self.write (b'\x1b[Lx%d;' % x)
        else :
            self.write (b'\x1b[Lx%dy%d;' % (x, y))
    # end def goto

    def define_glyph (self, code, data) :
        assert 0 <= code <= 7
        print (len (data))
        assert len (data) == 8
        self.write ('\x1b[LG%d' % code)
        for byte in data :
            self.write ("%02x" % byte)
        self.write (';')
    # end def define_glyph

# end class Display

if __name__ == '__main__' :
    import sys
    d = Display ()
    #d.goto (0, 18)
    #d.write (b'\x80')
    d.define_glyph (0, d.ram_chars ['\u00c4'])
    d.define_glyph (1, d.ram_chars ['\u00d6'])
    d.define_glyph (2, d.ram_chars ['\u00dc'])
    d.esc_clear ()
    #d.write (b'\x00A \x01O \x02U ')
    d.write (b'-\xb0')
    if len (sys.argv) > 1 :
        d.write (' '.join (sys.argv [1:]))
    else :
        d.write ('Hello World')
