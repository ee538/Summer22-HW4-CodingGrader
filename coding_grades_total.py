from __future__ import print_function
import re


def get_ok_num_perq(tresfile):
    file = open(tresfile,"r")
    cnt = 0
    f = file.read()
    lists = f.split("\n")
    
    for i in lists:
        if i:
            cnt += 1
    
    return cnt

total_coding_score = 0.0;

q_nums = [1, 2]

for q_num in q_nums:
	pass_num = get_ok_num_perq("grades/Q%dres_.txt" % q_num)

	if q_num == 1:
		if pass_num <= 17:
			q1_score = pass_num * 1
		elif pass_num == 18:
			q1_score = 20
		print("Q1:", pass_num, "/", 18, "passed | score:", q1_score)
		total_coding_score += q1_score
	elif q_num == 2:
		if pass_num <= 23:
			q2_score = pass_num * 4
		elif pass_num == 24:
			q2_score = 100
		print("Q2:", pass_num, "/", 24, "passed | score:", q2_score)
		total_coding_score += q2_score
	else:
		raise ValueError('Wrong question number')


print("-----------------------------------------")
print("Your total score of coding section:", total_coding_score)
print("-----------------------------------------")
	

