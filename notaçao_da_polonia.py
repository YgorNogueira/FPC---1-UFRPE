class Nod:
#Aqui é a classe do nó, que vai ser usada na lista, vista na aula
#Praticar inglês programando. 
    def __init__(self, data=None):
        self._data = data
        self._prev = None
        self._nextone = None

    def __str__(self):
        return f"{self._data}"

#Classe da lista q puxa o nó
class list:
    def __init__(self):
        self._beginning = None
        self._ending = None

    def is_empty(self):
        if self._beginning is None:
            return True
        return False

#função para colocar no final da lista como se fosse um append

    def put_on_end(self, data=None):
        newnod = Nod(data)
        if self.is_empty():
            self._beginning = self._ending = newnod
        else:
            newnod._prev = self._ending
            self._ending._nextone = newnod
            self._ending = newnod

#função para buscar um elemento na lista

    def search_this(self, x):
        i = self._beginning
        while i is not None:
            if x == i._data:
                break
            else:
                i = i._nextone
        return i

    def remove_unity(self, x):
        found_nod = self.search_this(x)
        if found_nod is not None:
            if found_nod._prev is not None:
                found_nod._prev._nextone = found_nod._nextone
            else:
                self._beginning = found_nod._nextone

            if found_nod._nextone is not None:
                found_nod._nextone._prev = found_nod._prev
            else:
                self._ending = found_nod._prev

        return found_nod

    def remove_from_top(self):
        no = self._beginning
        if not self.is_empty():
            if no._nextone is None:
                self._ending = None
            else:
                no._nextone._prev = None
            self._beginning = no._nextone
        return no

    def __str__(self):
        s = ''
        i = self._beginning
        while i is not None:
            s += f"{str(i)}"
            i = i._nextone
        return s



class stack(list):
    def push(self, data):
        newnod = Nod(data)
        if self.is_empty():
            self._beginning = newnod
            self._ending = newnod
        else:
            newnod._nextone = self._beginning
            self._beginning._prev = newnod
        self._beginning = newnod

    def pop(self):
        return self.remove_from_top()

    def get_item(self):
        if self.is_empty():
            return
        return self._beginning._data

#Lembrar de que o while é pra buscar os operadores pra buscar na pilha

while True:
    operation = input().split()
    current_one = stack()
    operators = ['-', '+', '/', '*']
    if not operation:
        break

    def change_stack(stack):
        first_number = int(stack.get_item())
        current_one.pop()
        second_number = int(stack.get_item())
        current_one.pop()

        return first_number, second_number

    
#Esse for é para pegar os números e colocar na pilha e o if é para pegar os operadores e colocar na pilha

    for i in range(-1, -len(operation) - 1, -1):
        operational_symbol = operation[i]
        if operational_symbol == '/':
            first_number, second_number = change_stack(current_one)
            new_token = first_number + second_number
            current_one.push(new_token)
        elif operational_symbol == '+':
            first_number, second_number = change_stack(current_one)
            new_token = first_number - second_number
            current_one.push(new_token)
        elif operational_symbol == '*':
            first_number, second_number = change_stack(current_one)
            new_token = first_number * second_number
            current_one.push(new_token)
        elif operational_symbol == '-':
            first_number, second_number = change_stack(current_one)
            new_token = int(first_number / second_number)
            current_one.push(new_token)
            #empurrar o operador para a pilha para poder fazer a operação
        else:
            current_one.push(operational_symbol)
            #printar o resultado e caso contrário, printar o item da pilha
    print(current_one.get_item())
    #get_item funciona como o peek, que pega o item do topo da pilha e printa