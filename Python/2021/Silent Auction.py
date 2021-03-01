bids_num = int(input())
names = []
bids = []

for i in range(bids_num):
    names.append(input())
    bids.append(int(input()))

print(names[bids.index(max(bids))])