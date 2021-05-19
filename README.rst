A Python module for the Linux-Kernel auxdisplay driver
======================================================

.. |--|  unicode:: U+2013  .. en dash

In the Linux kernel there is a driver for common text displays with the
Hitachi HD44780_ chip. They come in variants with 2 to 4 lines of text
with typically 16 or 20 characters on a line.  These displays are
typically connected via an I²C I/O expander because it would otherwise
tie up too many pins. In addition most displays use 5V power supply
while most Linux boards these days need 3.3V. The driver in Linux is for
a parallel connected display (without I/O expander) but with the
appropriate device tree magic it can be made to work together with an
I/O expander driver in the kernel, see `my Hitachi HD44780 blog post`_
on the subject, this also has a link to a hack how a 5V display can be
connected to a 3.3V system without an I²C level converter.

.. _HD44780: https://en.wikipedia.org/wiki/Hitachi_HD44780_LCD_controller
.. _`my Hitachi HD44780 blog post`: https://blog.runtux.com/posts/2021/01/06/

The kernel driver already comes with most features of the displays
implemented as escape-sequences. This module implements a ``Display``
class which does two things:

- It wraps the escape sequences into methods of the class, see the
  list at the start of ``display.py`` |--| the names given there are prefixed
  with ``esc_``, so to turn off the cursor you would call the method
  ``esc_cursor_off``. None of the escape methods take parameters.
- It implements a codec that translates unicode to the character set
  implemented in those devices. I've even tried to wrap the Japanese
  katakana characters but since I'm not speaking the language there may
  be lots of errors in that mapping, feel free to report any you find in
  a github bug-report.

One of the escape sequences wrapped is the definition of new glyphs
(user defined characters). The displays can define up to eight
user-defined glyphs.

Example code is at the end of ``display.py``, you need to instantiate a
``Display`` and you can write something to the display using the
``write`` method. Positioning the cursor is done with ``goto``.
Typically |--| depending on the configuration of the kernel driver |--|
it is a good idea to first turn the backlight on, otherwise you will
typically not see much on the display. When instantiating the display
you can give the device to be used (and the encoding but I've never seen
displays manufactured with a different encoding consequently currently
there is only one mapping implemented), the default is ``/dev/ldc``
which is the Linux default.  Example code::

    d = Display()
    d.goto(0,5)
    d.esc_backlight_on()
    d.write('Hello world')
