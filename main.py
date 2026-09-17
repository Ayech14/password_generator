import random
import math

alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%&*"

pass_len = int(input("Enter Password Length"))

alpha_len = pass_len // 2
num_len = math.ceil(pass_len * 30 / 100)
special_len = pass_len - (alpha_len + num_len)

password = []