import time


class Semaforo():
    estado = "desligado"
    luz_atual = None
    tempo_luz_verde = 5
    tempo_luz_amarela = 2
    tempo_luz_vermelha = 7
    principal = False
    sinal_vinculado = None

    def ligar(self):
        self.estado = "ligado"
        self.luz_atual = "verde"
        pass

    def desligado(self):
        if self.estado == "ligado":
            self.estado = "desligado"
            self.luz_atual = None
        pass

    def mudar_cor(self):
        if self.estado == "ligado":
            self.luz_atual = "amarelo" if self.luz_atual == "verde" else "vermelho" if self.luz_atual == "amarelo" else "verde"
        pass

    # def gerenciar_tempo(self):
    #     if self.estado == "ligado":
    #         if input("Mudar tempo da luz verde? (S/n):")[0].strip().upper() == "S":
    #             self.tempo_luz_verde = int(input())
    #         if input("Mudar tempo da luz amarela? (S/n):")[0].strip().upper() == "S":
    #             self.tempo_luz_amarela = int(input())
    #         if input("Mudar tempo da luz vermelha? (S/n):")[0].strip().upper() == "S":
    #             self.tempo_luz_vermelha = int(input())
    #     pass

    def gerenciar_tempo(self):
        if self.luz_atual == "verde":
            time.sleep(self.tempo_luz_verde)
        elif self.luz_atual == "amarelo":
            time.sleep(self.tempo_luz_amarela)
        elif self.luz_atual == "vermelho":
            time.sleep(self.tempo_luz_vermelha)
        self.mudar_cor()

    def definir_tempo(self, vermelho, amarelo, verde):
        self.tempo_luz_vermelha = vermelho
        self.tempo_luz_amarela = amarelo
        self.tempo_luz_verde = verde

    def definir_principal(self):
        self.principal = True
        pass

    def sinal_secundario(self, s2):
        if s2.principal == False and self.principal == True:
            self.sinal_vinculado = s2
        pass
