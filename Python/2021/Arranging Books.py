# J4

shelf = input()

num_l, num_m, num_s = shelf.count("L"), shelf.count("M"), shelf.count("S")

l_section = shelf[:num_l]
m_section = shelf[num_l:num_m+num_l]
s_section = shelf[num_m+num_l:]

print(max(l_section.count("M"), m_section.count("L")) + (len(s_section) - s_section.count("S")))
