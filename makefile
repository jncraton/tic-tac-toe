all: play

test: play.py
	python3 -m doctest play.py

play: play.py test
	python3 play.py