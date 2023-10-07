#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	len_word = 0
	for c in text:
		if c.isalnum() == True:
			len_word += 1
	return len_word

def get_word_length_histogram(text):
	word_lenght = []
	word_count = text.split(" ")
	word_list = []
	# apprendre à utiliser les fonctions déjà créées ou les créer si besoin / découper pb
	for word in word_count:
		word_lenght.append(get_num_letters(word))
	for i in range(max(word_lenght) + 1):
		word_list.append(0)
	for word in word_count:
		if get_num_letters(word) == 0:
			continue
		word_list[get_num_letters(word)] += 1
	return word_list

def format_histogram(histogram):
	ROW_CHAR = "*"
	result = ""
	for i, elem in enumerate(histogram):
		if i == 0:
			continue
		result += f"{i}{ROW_CHAR * elem} \n"
	return result

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"
	for i, elem in enumerate(histogram):
		result = ""
		if i == 0:
			result += "\n" * 3 + '-'
		else:
			result += "\n" * (3 - elem) + "| \n" * elem  + "-"
	return result


if __name__ == "__main__":
	print(get_word_length_histogram("a aa-aa \t aa9  "))

