
# Tor Stats

Very basic script to print out some stats about Tor's infrastructure.

Uses the stem library to output a count of Hidden Services directories, directory authorities, relays, etc.

## Installation

First install the stem library:

`sudo pip install stem`

Then clone this project and cd into the directory:

    git clone https://github.com/mono-man/torstats.git
    cd torstats

## Usage

`python torstats.py`

## Output


    Num HSDirs:         2995
    Num Authorities     10
    Total relays:       6798
    Running relays:     6798

             Versions    |    Count
             ----------------------
             0.2.4.19    |    1
             0.2.4.20    |    58
             0.2.4.21    |    31
             0.2.4.22    |    56
             0.2.4.23    |    474
             0.2.4.24    |    64
             0.2.4.25    |    4
             0.2.4.26    |    17
             0.2.4.27    |    1085
    0.2.5.1-alpha-dev    |    1
    0.2.5.3-alpha-dev    |    1
        0.2.5.5-alpha    |    10
        0.2.5.6-alpha    |    5
           0.2.5.7-rc    |    3
           0.2.5.8-rc    |    19
           0.2.5.9-rc    |    2
             0.2.5.10    |    214
             0.2.5.11    |    38
    0.2.6.0-alpha-dev    |    8
    0.2.6.1-alpha-dev    |    2
        0.2.6.2-alpha    |    4
           0.2.6.5-rc    |    1
              0.2.6.8    |    125
             0.2.6.10    |    3061
                 None    |    2
             0.2.5.12    |    914
       0.2.6.4-rc-dev    |    1
              0.2.6.6    |    8
          0.2.6.6-dev    |    1
              0.2.6.7    |    72
              0.2.6.9    |    248
         0.2.6.10-dev    |    1
    0.2.7.0-alpha-dev    |    1
        0.2.7.1-alpha    |    6
    0.2.7.1-alpha-dev    |    3
        0.2.7.2-alpha    |    23
    0.2.7.2-alpha-dev    |    9
           0.2.7.3-rc    |    33
           0.2.7.4-rc    |    169
              0.2.7.5    |    1
    0.2.8.0-alpha-dev    |    22




