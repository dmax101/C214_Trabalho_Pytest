class Notas:
    def __init__(self, p1, p2, p3=None):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def is_aprovado(self):

        is_aprovado = False
        need_np3 = False

        media_p1p2 = round((self.p1 + self.p2) / 2)
        print(50 * "-")
        print((self.p1 + self.p2) / 2)
        print(50 * "-")

        _np3 = 0
        if self.p3 != None:
            _np3 = self.p3

        if media_p1p2 < 30:
            is_aprovado = False
            need_np3 = False
            print("Reprovado com média de {} pontos".format(media_p1p2))
        
        elif media_p1p2 >= 60:
            is_aprovado = True
            need_np3 = False
            print("Aprovado com média de {} pontos".format(media_p1p2))
        
        else:
            is_aprovado = False
            need_np3 = True
            print("Fazer NP3. Média NP1 e NP2 de {} pontos".format(media_p1p2))

        if need_np3 and (self.p3 != None):
            if round((media_p1p2 + _np3) / 2) < 50:
                is_aprovado = False
                print("Reprovado com média de {} pontos".format(round((media_p1p2 + _np3) / 2)))

            elif round((media_p1p2 + _np3) / 2) >= 50:
                is_aprovado = True
                print("Aprovado com média de {} pontos".format(round((media_p1p2 + _np3) / 2)))
        else:
            print("Falta nota NP3")
        
        return is_aprovado