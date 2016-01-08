#!/env/python

import subprocess
import re
import argparse
import os

## notes
# pause can be done by counting
# how long a song has been playing

FOLDER = "~/Music"

def parse_args():
	parser = argparse.ArgumentParser("vplay")
	
	parser.add_argument(
		"title",
		type=str,
		help="name of a song/album",
		default=None,
		nargs="?"
	)
	
	parser.add_argument(
		"-a",
		help="print albums",
		action="store_true",
		default=False,
		dest="print_albums"
	)
	
	parser.add_argument(
		"-s",
		help="print songs",
		action="store_true",
		default=False,
		dest="print_songs"
	)
	
	parser.add_argument(
		"-x",
		help="stop",
		action="store_true",
		default=False,
		dest="stop"
	)
	
	args = parser.parse_args()

	return args

# run a subprocess
def run(cmd): return subprocess.check_output(cmd, shell=True)

# kill all existing instances of vlc
def kill_vlc():
	try: 
		run("pkill screen")
		run("pkill vlc")
	except: pass

# run VLC, pipe output to null
def run_vlc(args): 
	run("screen -m -d cvlc -Irc " + args + " &")

# Play song/album
def play_vlc(args):
	print("[vplay] Playing: " + args)
	run_vlc('"' + args + '"')

# Return a list of songs
def songs(): return run("ls "+FOLDER+"/*/*")

# Returns a list of FOLDERs
def FOLDERs(): return run("ls "+FOLDER+"/*/").split("\n")[:-1]

# Find a songs absolute path
def get_song(match): return re.sub("\n", "", run('find '+FOLDER+'/* | grep "' + match + '"'))

# Find a FOLDER
def find_FOLDER(match):
	try:    return re.sub("\n","",run('find '+FOLDER+'/*/ | grep -m1 -i ' + match))
	except: return None

# Find a song
def find_song(match):
	try:    return re.sub("\n","",run('find '+FOLDER+'/* -type f -printf "%f\n" | grep -m1 -i ' + match))
	except: return None


def search(match):

	# Stop anything else from playing	
	kill_vlc()
	
	# Check songs.
	name = find_song(match)
	
	# No song? Check albums.
	if name is not None:
		path = get_song(name)
		play_vlc(path)
	else:
		path = find_FOLDER(match)
		if path is not None:
			play_vlc(path)
	

def main():
	args = parse_args()
	
	if args.print_albums:
		print(run("ls "+FOLDER+"/"))
	elif args.print_songs:
		print(run("find "+FOLDER+"/*"))
	elif args.stop:
		kill_vlc()
	else:
		if (args.title is None) or (args.title == ""):
			print("[vplay] no title specified")
		else:
			match = args.title
			kill_vlc()
			search(match)

main()
