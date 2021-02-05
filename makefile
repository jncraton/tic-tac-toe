all: play

play: play.py
	python3 -m doctest play.py
	python3 play.py