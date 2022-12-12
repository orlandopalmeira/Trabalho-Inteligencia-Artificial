
class InfoCaminho:
    """
    Classe que contém informação sobre o caminho que um algoritmo determinou.
    """
    def __init__(self , caminho_final, caminho_do_algoritmo):
        """
        Construtor da classe InfoCaminho
        :param caminho_final: caminho_final
        :param caminho_do_algoritmo: caminho_do_algoritmo
        """
        self.caminhoFinal = caminho_final
        self.caminhoDoAlgoritmo = caminho_do_algoritmo


    def setCaminhoFinal(self, caminho_final):
        self.caminhoFinal = caminho_final

    def setCaminhoDoAlgoritmo(self, caminho_do_algoritmo):
        self.caminhoDoAlgoritmo = caminho_do_algoritmo

    def getCaminhoFinal(self):
        return self.caminhoFinal

    def getCaminhoDoAlgoritmo(self):
        return self.caminhoDoAlgoritmo
