from main import Compra
import unittest
import unittest.mock
import requests

class TestMain(unittest.TestCase):
# def test_desconto_valor_maior_que_100(self, cadastrar, definir_desconto):
#        compra = compra(-4000, "João", "Bronze", '0')
#        resposta = compra.definir_desconto("Bronze",'-4000')
#        self.assertEqual(resposta, '0')  # O desconto deve ser 15% de 150, que é 15

#    def test_desconto_valor_menor_ou_igual_a_100(self, cadastrar, definir_desconto):
#        compra = compra('800',"Maria", "Bronze", '999999')
#        resposta = cliente.definir_desconto("Bronze",'800')
#        self.assertEqual(resposta, '680')  # Não deve haver desconto para compras menores ou iguais a 100

#    def test_desconto_para_valor_zero(self,cadastrar,definir_desconto):
#        compra = compra(50000,"Carlos", "Ouro", '0.1' )
#        cadastrar("Carlos",'0')
#        resposta = cliente.definir_desconto("Ouro",'50000')
#        self.assertEqual(resposta, '42.500')  # Não deve haver desconto para valor zero

#    def test_desconto_para_valor_negativo(self, cadastrar, definir_desconto):
#        compra = compra('0',"Ana", "",  '0.000000000001')
#        cadastrar("Ana",0.000000000001)
#        resposta = cliente.definir_desconto("Ouro",'0.0000000000')
#        self.assertEqual(resposta, 0.000000000075)  # Não deve haver desconto para valor negativo
    def get_user_data(user_id):
        reponse = requests.get(f"https://api.example.com/users/{user_id}")
        return response.json()
    
'''
    class TesteMock(unittest.TestCase):

        @patch('requests.get')
        def get_user_data(self, mock_get):
            mock_response = Mock()
            response_dict = {'name':'John', 'email': 'john@example.com'}
            mock_response.json.return_value = response_dict

            mock_.get.return_value = mock_response

            user_data = get_user_data(1)
            mock_get.assert_called_with("https://api.example.com/users/1")
            self.assertEqual(user_data, response_dict)
   '''
    
def testar_soma(self):
    comp1 = Compra('5',"Jose","Prata", 0)
    valor1 = comp1.soma(5,5)
    self.assertEqual(valor1,10)
    comp2 = Compra('16',"Wanderley","Bronze", '8000')
    valor2 = comp2.soma('16','16')
    self.assertEqual(valor2, 1616)
    comp3 = Compra('5',"Juan","",'0')
    valor3 = comp3.soma('5',"5")
    self.assertEqual(valor3, 10)
    comp4 = Compra('0',"Zirlan","Ouro",'0')
    valor4 = comp4.soma(0,0.0001)
    self.assertEqual(valor4, 0.0001)
    comp5 = Compra('5',"Obedran","Prata",'8')
    valor5 = comp5.soma("cinco",'8')
    self.assertEqual(valor5, '8')


def testar_entrada(self):
    valor = input(f"Digite o valor do produto: ")
    nome = input(f"Digite o nome do cliente: ")
    tipo = input(f"Digite o tipo de conta do cliente: ")
    saldo = input(f"Digite o saldo do cliente: ")
    self.assertEqual(valor,True)#Esse seria um bom teste para demonstrar que o valor de entrada não é ''?
    self.assertEqual(nome, True)
    self.assertEqual(tipo, True)
    self.assertEqual(saldo, True)
    return(valor,nome,tipo,saldo)

def testar_tipagem(self):
    obj1 = Compra('180',"João","Bronze","0")#como posso criar um teste consistente para ver se o usuário poderá obter mais de um tipo de compra?
    obj2 = Compra('0',"João","Ouro",'0')
    obj3 = Compra('158',"Maria","Prata",'790')
    obj4 = Compra('490',"Maria","Ouro",'1280')
    obj5 = Compra('0',"José","Sem",'0')
    obj6 = Compra('80', "José","Bronze",'80')#supondo que ele acabou de fazer a compra no instante que conheceu o merado
    self.assertEqual(obj1, 'True')
    self.assertEqual(obj2, "True")
    self.assertEqual(obj3, "True")
    self.assertEqual(obj4, "True")
    self.assertEqual(obj5, "True")
    self.assertEqual(obj6, "True")


def teste_transicao(self):
    c1 = Compra('200',"Marcos","Sem",'0')
    self.assertEqual(c1.tipo, "Bronze")#levando em consideração que ele chegou fez o cadastro e depois comprou e patenteou para bronze
    

"""

    def testar_subtracao(self):
        var = main.Compra(5,"João","Ouro",0)
        valor1 = var.subtracao(5,5)
        self.assertEqual(valor1,0)        


    def testar_divisao(self):
        valor1 = main.divisao(1/1)
        self.assertEqual(valor1, 1)
        valor2 = main.divisao('5.000.000'/'999999999')
        self.assertEqual(valor2, 0.005)
        valor3 = main.divisao("21"/3)
        self.assertEqual(valor3, 7)
        valor4 = main.divisao(8/0)
        self.assertEqual(valor4, 0)
    

    def testar_multiplicacao(self):
        valor1 = main.multiplicacao(5,5)
        self.assertEqual(valor1,25)
        valor2 = main.multiplicacao(6,1)
        self.assertEqual(valor2, 6)
        valor3 = main.multiplicacao(6,0)
        self.assertEqual(valor3, 0)
        valor4 = main.multiplicacao(0,6)
        self.assertEqual(valor4, 0)
        valor5 = main.multiplicacao(-8000,1)
        self.assertEqual(valor5, -8000)
"""
if __name__ == '__main__':
    unittest.main()
      