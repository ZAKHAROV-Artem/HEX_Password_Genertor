import random
import csv

def main():
    colors={}
    for i in range(int(input("HEX count : "))):
        color = get_hex()
        if color in colors.keys():
            colors[color]+=1
        else:
            colors.update({color:1})

    with open('color.csv', 'w') as color:
        writer = csv.writer(color)
        for i in sorted(colors):
            writer.writerow([i,colors[i]])
        
def get_hex():
    symbols = "0A1B2C3D4E5F6789"
    color = "#"
    for i in range(6):
        color += random.choice(symbols)
    return color

main()