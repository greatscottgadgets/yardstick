==========================
Frequently Asked Questions
==========================

**Question:** What is the latest release?

The latest rfcat release may be found here.

**Question:** Why doesn't the LED turn on when I plug in my YARD Stick One?

Yes. This is the expected behavior of RfCat firmware. The LED only illuminates while data is being transferred in transmit or receive mode.

**Question:** My firmware isn't running, how do I enter bootloader mode?

Bootloader mode can be triggered by connecting pins 7 and 9 on the P1 expansion header::


         +---------------------------------------+
         | YARD Stick One      2 4 6 8 10 12 14  |
   +-----+                     1 3 5 7 9  11 13  +-----+
   | SMA                                           USB |
   +-----+                                       +-----+
         |                                       |
         +---------------------------------------+
