# vplay (WIP)


`vplay` is wrapper for the VLC Media Player CLI, written in python.


It is designed only to work on my personal system with my own configurations, but should be easy to port to other versions of linux.


## behavior


`vplay` is designed to take a song or album title as a parameter, so when you type


`vplay shrine` it will grep your music folder for a song with `shrine` in the title.


When a song is found, `vplay` will play it. (starting `vlc` as a background process)


If a song is not found `vplay` will then search your album titles for the name.


If an album is found, `vplay` will play it.


## usage


`vplay <song/album title>` to start playing a song or album


`vplay -x` to stop playing


`vplay -s` to list all songs in your music folder


`vplay -a` to list all albums in your music folder


## planned features

* cross-platform support

* pause

* skip

* more?

## requirements

**VLC Media Player**


http://www.videolan.org/vlc/index.html


**Screen**


https://help.ubuntu.com/community/Screen


`apt-get install screen` should work on Ubuntu.


## add `vplay` as a bash alias


open up your `~/.bashrc`


append `alias vplay="bash <wherever you installed>/vplay.sh"`


otherwise you'll need to type `python <wherever you installed>/vplay <title>` every time you want to play something.
