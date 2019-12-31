class Perceptron:
    training_nodes = []

    def __init__(self, alpha, weights):
        self.alpha   = alpha
        self.weights = weights


    # Essa funcao recebe os valores do node, e, usando a formula
    # do result, calcula uma resposta. Depois, ele seta o value found
    # para 0 ou 1, dependendo da resposta achada na formula. Esse value
    # found serve para compararmos com o valor-resposta do arquivo.

    # O valor write comeca como False, para o perceptron nao printar
    # a resposta durante os treinos, mas pode ser mudado, como 
    # foi feito no node arbitrario que eu fiz na funcao main
    def predict(self, node, write=False):
        answer = node[-1]
        result = 0

        for i in range(0, len(node)-1):
            result += node[i] * self.weights[i]

        if result >= 0.0:
            value_found = 1.0
            if write:
                print("O ponto eh azul")
        else:
            if write:
                print("O ponto eh vermelho")
            value_found = 0.0

        return value_found


    # Le o arquivo e salva os valores na variavel nodes
    def read(self, filename):
        with open(filename, "r") as f:
            dataset = f.read().splitlines()
            for data in dataset:
                data = [ float(x) for x in data.split(" ") ]
                self.training_nodes.append(data)


    # Aqui, um node eh passado para a funcao predict, e sua resposta eh 
    # comparada com a do arquivo-fonte. Se for diferente, os pesos sao rebalanceados
    def train(self):
        for node in self.training_nodes:
            answer = self.predict(node)
        
            if answer != node[2]:
                self.balance_weights(node, node[2]-answer)

    
    # A funcao de balanceamento so eh chamada se o perceptron errar a resposta
    def balance_weights(self, node, error):
        for i in range(0, len(node)-1):
            self.weights[i] += error * self.alpha * node[i]


def main():
    # O alpha serve como medida para os balanceamentos de peso, e os demais valores
    # sao apenas os valores iniciais dos pesos
    perceptron = Perceptron(0.5, [0.8, 0.3])
    perceptron.read("./arq.txt") # Arquivo-fonte usado para treinar
    perceptron.train()

    # Para verificar os pesos do perceptron
    '''
    print(perceptron.weight1)
    print(perceptron.weight2)
    '''
    
    # Aqui sao valores arbitrarios usados para ver se o perceptron foi
    # treinado bem
    node = [-0.00000007, 100000, 1]
    perceptron.predict(node, write=True)
     

if __name__ == '__main__':
    main()