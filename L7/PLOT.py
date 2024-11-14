from matplotlib import pyplot as plt
import json

def plot_data(seris):
    fig, ax = plt.subplots()
    fig.set_size_inches([20, 10])
    fig.tight_layout(pad=1.5)    
    for ss in data:
        plt.plot(ss)            
    plt.grid()
    plt.savefig("serii.png", bbox_inches='tight', dpi=300)    

data = json.load(open('serii.json', 'r'))
plot_data(data)