==============
YARD Stick One
==============

YARD Stick One is a sub-1 GHz wireless transceiver IC on a USB dongle. It is based on the Texas Instruments CC1111.

Features
~~~~~~~~

* half-duplex transmit and receive
* official operating frequencies: 300-348 MHz, 391-464 MHz, and 782-928 MHz
* unofficial operating frequencies: 281-361 MHz, 378-481 MHz, and 749-962 MHz
* modulations: ASK, OOK, GFSK, 2-FSK, 4-FSK, MSK
* data rates up to 500 kbps
* Full-Speed USB 2.0
* SMA female antenna connector (50 ohms)
* software-controlled antenna port power (max 50 mA at 3.3 V)
* low pass filter for elimination of harmonics when operating in the 800 and 900 MHz bands
* GoodFET-compatible expansion and programming header
* GIMME-compatible programming test points
* open source

The official operating frequencies are those supported by Texas Instruments.  Our testing has found the unofficial range to be reliable.



SMA, not RP-SMA
~~~~~~~~~~~~~~~

Some connectors that appear to be SMA are actually RP-SMA.  If you connect an RP-SMA antenna to YARD Stick One, it will seem to connect snugly but won't function at all because neither the male nor female side has a center pin.  RP-SMA connectors are most common on 2.4 GHz antennas and are popular on Wi-Fi equipment.  Adapters are available.



Expansion Interface
~~~~~~~~~~~~~~~~~~~

Header P1 is available as an expansion interface.  See the schematic for the pinout.  It can also be used for firmware programming if the USB bootloader is insufficient for some reason.  You can connect a GoodFET to P1 (with a ribbon cable, for example) for programming.



Project Home
~~~~~~~~~~~~

The project home page, including purchasing information can be found `here <http://greatscottgadgets.com/yardstickone/>`__.
