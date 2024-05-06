
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from collections import deque
Builder.load_file("tela.kv")

class Decimal_octal_binario:
    def deciOcta(self, x):
        valortrabalho = x
        Pilha_resto = deque()
        while valortrabalho != 0:
            Pilha_resto.append(valortrabalho % 8)
            valortrabalho = (valortrabalho // 8)
        numero_stri = ""
        for n in reversed(Pilha_resto):
            numero_stri = numero_stri + str(n)
        print(numero_stri)
        return numero_stri
    def deciObina(self, x):
        valortrabalho = x
        Pilha_resto = deque()
        while valortrabalho != 0:
            Pilha_resto.append(valortrabalho % 2)
            valortrabalho = (valortrabalho // 2)
        numero_stri = ""
        for n in reversed(Pilha_resto):
            numero_stri = numero_stri + str(n)
        print(numero_stri)
        return numero_stri
    def deciHexa(self, x):
        valortrabalho = x
        Pilha_resto = deque()
        while valortrabalho != 0:
            resto = valortrabalho % 16
            if resto >= 10:
                switch_case = {
                    10: "A",
                    11: "B",
                    12: "C",
                    13: "D",
                    14: "E",
                    15: "F"
                }
                Pilha_resto.append(switch_case[resto])
            else:
                Pilha_resto.append(resto)
            valortrabalho = valortrabalho // 16
        
        numero_stri = ""
        for n in reversed(Pilha_resto):
            numero_stri += str(n)
        print(numero_stri)
        return numero_stri
#entrada = int(input("Digite o número que deseja converter: "))

#donda = Decimal_octal_binario()
#donda.deciOcta(entrada)

#donda.deciObina(entrada)
#donda.deciHexa(entrada)
class RootWidget(ScreenManager):
    pass
class MainApp(App):
    def buil(self):
        return RootWidget()
    def calcular(self, tipo):
        input_field = self.root.ids.input_field
        resultado_label=self.root.ids.resultado_label
        valor_digitado=input_field.text

        try:
            valor = int(valor_digitado)
        except ValueError:
            resultado_label.text= "Valor inválido"
            return
        donda = Decimal_octal_binario()
        if tipo=='octal':
            resultado= donda.deciOcta(valor)
        elif tipo=='binario':
            resultado= donda.deciObina(valor)
        elif tipo=='hexadecimal':
            resultado= donda.deciHexa(valor)
        resultado_label.text= f"Resultado:{resultado}"
if __name__=="__main__":
    MainApp().run()