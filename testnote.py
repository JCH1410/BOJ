base_rate = 5
base_dmg = 50
total = 180
for i in range(91):
    cri_rate = (base_rate + i) / 100
    cri_dmg = 1 + (base_dmg + (total - 2 * i)) / 100
    cri_avg = 100 * cri_rate * cri_dmg + 100 * (1 - cri_rate)
    print(f'rate : {base_rate + i}%, dmg : {base_dmg + (total - 2 * i)}%, avg : {round(cri_avg, 2)}')

print('helloworld')