
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



    Num HSDirs:         2763
    Num Authorities     10
    Total relays:       6777
    Running relays:     6777

             Versions    |         Count    |         Release date
    --------------------------------------------------------------------------------
             0.2.4.19    |             1    |    Wed Dec 11 23:55:03 2013 -0500
             0.2.4.20    |            58    |    Mon Dec 23 01:41:16 2013 -0500
             0.2.4.21    |            32    |    Sat Mar 1 04:03:22 2014 -0500
             0.2.4.22    |            57    |    Fri May 16 11:12:13 2014 -0400
             0.2.4.23    |           462    |    Mon Jul 28 15:53:27 2014 -0400
             0.2.4.24    |            62    |    Mon Sep 22 21:04:36 2014 -0400
             0.2.4.25    |             4    |    Mon Oct 20 10:01:35 2014 -0400
             0.2.4.26    |            15    |    Tue Mar 17 09:45:07 2015 -0400
             0.2.4.27    |          1079    |    Mon Apr 6 10:29:47 2015 -0400
    0.2.5.1-alpha-dev    |             1    |              Unknown
    0.2.5.3-alpha-dev    |             1    |              Unknown
        0.2.5.5-alpha    |            10    |    Wed Jun 18 14:22:18 2014 -0400
        0.2.5.6-alpha    |             4    |    Mon Jul 28 15:55:43 2014 -0400
           0.2.5.7-rc    |             3    |    Thu Sep 11 21:22:33 2014 -0400
           0.2.5.8-rc    |            19    |    Mon Sep 22 21:50:04 2014 -0400
           0.2.5.9-rc    |             2    |    Mon Oct 20 10:02:07 2014 -0400
             0.2.5.10    |           212    |    Fri Oct 24 09:09:55 2014 -0400
             0.2.5.11    |            39    |    Tue Mar 17 09:46:42 2015 -0400
             0.2.5.12    |           935    |    Mon Apr 6 10:30:15 2015 -0400
    0.2.6.0-alpha-dev    |             7    |              Unknown
    0.2.6.1-alpha-dev    |             2    |              Unknown
        0.2.6.2-alpha    |             4    |    Wed Dec 31 13:09:12 2014 -0500
        0.2.6.3-alpha    |             1    |    Thu Feb 19 17:15:20 2015 -0500
       0.2.6.4-rc-dev    |             1    |              Unknown
           0.2.6.5-rc    |             2    |    Wed Mar 18 15:50:43 2015 -0400
              0.2.6.6    |             8    |    Tue Mar 24 14:17:29 2015 -0400
          0.2.6.6-dev    |             1    |              Unknown
              0.2.6.7    |            72    |    Mon Apr 6 10:30:44 2015 -0400
              0.2.6.8    |           120    |    Wed May 20 13:27:50 2015 -0400
              0.2.6.9    |           244    |    Thu Jun 11 12:54:40 2015 -0400
             0.2.6.10    |          2657    |    Sun Jul 12 16:20:34 2015 -0400
         0.2.6.10-dev    |             1    |              Unknown
    0.2.7.0-alpha-dev    |             1    |              Unknown
        0.2.7.1-alpha    |             6    |    Tue May 12 11:31:47 2015 -0400
    0.2.7.1-alpha-dev    |             3    |              Unknown
        0.2.7.2-alpha    |            21    |    Mon Jul 27 13:14:19 2015 -0400
    0.2.7.2-alpha-dev    |             8    |              Unknown
           0.2.7.3-rc    |            31    |    Fri Sep 25 09:20:46 2015 -0400
           0.2.7.4-rc    |           125    |    Wed Oct 21 15:25:06 2015 -0400
              0.2.7.5    |           441    |    Fri Nov 20 10:15:21 2015 -0500
    0.2.8.0-alpha-dev    |            25    |              Unknown



Note: Release dates were generated using:

    git for-each-ref --sort=taggerdate --format '%(refname) %(taggerdate)' refs/tag


