from sys import exit
import random


class Game(object):

	def __init__(self, start):
		self.start = start

	def play(self):
		next = self.start

		while True:
			print "\n--------"
			room = getattr(self, next)
			next = room()

	def death(self):
		print "Stinky corgi is stinky. \n"
		exit(1)

	def intro(self):
		print "Albert the corgi rolled in something smelly and needs a bath!"
		print "Before your friends come over for dinner, you need to get Albert"
		print "clean without making a huge mess, which is no small task for an"
		print "evasive and wiggly little corgi like Albert. Good luck."
		print ""
		print '"Phew Albert! You are one stinky pooch! You need a bath!" You'
		print "head to the bathroom, grab the shampoo, and begin filling the tub."
		print ""
		print "Albert, fully aware of what's to come, silently disappears into the"
		print 'depths of the house. "Albert!" You call, but nothing stirs. Corgis know'
		print "when it's bathtime."
		print ""
		print "You head to the kitchen and grab some treats. Albert isn't going"
		print "to make this easy, and time is running out. You gotta find him quick"
		print "or there won't be time to bathe the dog and get ready for dinner!"
		print ""
		
		hiding_options = ["A", "B", "C", "D", "E"]

		hiding_place = random.choice(hiding_options)
		print hiding_place

		print "You look... \n"

		print "A. under the bed. \nB. in the closet. \nC. behind the couch."
		print "D. in the kitchen. \nE. in the laundry basket. \n"

		hiding_guess = raw_input("> ")
		guesses = 0

		while hiding_guess != hiding_place and guesses < 2:
			print "Nope, no corgi here. \n"
			guesses += 1
			hiding_guess = raw_input("> ")

		if hiding_guess == hiding_place:
			return 'bathtub'
		
		else:
			print "\n--------"
			print "You hear a splashing sound coming from the bathroom. You think maybe"
			print "Albert has decided to bathe himself, so you head to the bathroom"
			print "to investigate. Upon entering the bathroom you see the tub is"
			print "overflowing! As you shut off the water and start toweling the"
			print "floor, you hear the doorbell ring. Your friends are here, your house is a"
			print "mess, and your stinky corgi is waiting by the door to great your guests"
			print "with his new favorite cologne! Game over."
			return 'death'


	def bathtub(self):
		print '"Albert! There you are! I\'ve got some yummy treats here for ya. Yummy treats'
		print 'for a good little doggy!" You offer Albert a small treat and he happily takes'
		print "it and follows you to the bathroom hoping for more tasty morsels. You... "
		print ""
		print "A. toss a toy into the tub, hoping Albert will jump into the tub on his own."
		print "B. pick up Albert and put him in the tub yourself.\n"

		tub_placement = raw_input("> ")

		if tub_placement == "A":
			print "\n--------"
			print "Albert jumps into the tub after the ball making a huge splash. He"
			print "eagerly snatches up the toy, and now thinking all of this is a great"
			print "game, jumps back out of the tub with the ball in his mouth and goes"
			print "frapping through the house. Now you've got a stinky, wet dog and several"
			print "rooms to clean before your friends arrive. While Albert is doing his"
			print "victory laps around your coffee table and evading your every attempt"
			print "to catch him, the doorbell rings. Your friends are here for dinner!"
			print "Game over."
			return 'death'
		
		elif tub_placement == "B":
			return 'tubtime'
		
		else:
			print "Please select 'A' or 'B' only."
			return 'bathtub'


	def tubtime(self):
		print "You carefully place Albert in the tub and begin soaping him up."
		print "You work up a really good lather in his fur and make a pile of bubbles"
		print "which you carefully place on top of his head. You snap a quick picture of"
		print "Albert to share with your Instagram later. Everyone will think your pup"
		print "is just too darn cute with all those bubbles on his head."
		print ""
		print "Photo opp over, you give Albert a good rinse and shut off the water."
		print "As the tub drains, you reach for the... "
		print ""
		print "A. blow dryer."
		print "B. towels. \n"

		dry_option = raw_input("> ")

		if dry_option == "A":
			print "\n--------"
			print "You turn on the blow dryer and Albert looks at you as if"
			print "you've grown another head just before dashing out of the"
			print "bathroom at corgi warp speed....."
			print "Game over."
			return 'death'

		elif dry_option == "B":
			print "\n--------"
			print "Albert may not love bathtime, but he certainly enjoys the post-bath"
			print "towel rubdown. You begin drying off Albert, then wrap him in a towel"
			print "and pick him up out of the tub. Shaking off the last of the water from"
			print "his fur, Albert takes off for a few frappy laps around the living room."
			print "Mission Clean Corgi accomplished!"
			print ""
			print "\n--------"
			exit(0)

		else:
			print "Please select 'A' or 'B' only."
			return 'tubtime'

corgi_game = Game("intro")
corgi_game.play()


