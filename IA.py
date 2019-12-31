from random import uniform
class Perceptron:
    training_nodes = []

    def __init__(self, alpha, weight1, weight2):
        self.alpha   = alpha
        self.weight1 = weight1
        self.weight2 = weight2


    def predict(self, node, write=False):
        value1 = node[0]
        value2 = node[1]
        answer = node[2]

        result = (value1 * self.weight1) + (value2 * self.weight2)

        if result >= 0.0:
            value_found = 1.0
            if write:
                print("O ponto eh azul")
        else:
            if write:
                print("O ponto eh vermelho")
            value_found = 0.0

        return value_found


    def read(self, filename):
        with open(filename, "r") as f:
            dataset = f.read().splitlines()
            for data in dataset:
                data = [ float(x) for x in data.split(" ") ]
                self.training_nodes.append(data)


    def train(self):
        for node in self.training_nodes:
            answer = self.predict(node)
        
            if answer != node[2]:
                self.balance_weights(node, node[2]-answer)

    
    def balance_weights(self, node, error):
        self.weight1 += error * self.alpha * node[0]
        self.weight2 += error * self.alpha * node[1]
    

def main():
    perceptron = Perceptron(0.5, 0.8, 0.3)
    perceptron.read("./arq.txt")
    perceptron.train()


    print(perceptron.weight1)
    print(perceptron.weight2)
    node = [-0.00000007, 1000, 1]
    perceptron.predict(node, write=True)
     

if __name__ == '__main__':
    main()