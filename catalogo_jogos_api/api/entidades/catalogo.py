class Catalogo():
    def __init__(self, titulo, descricao, data_lancamento, desenvolvedora, genero):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__data_lancamento = data_lancamento
        self.__desenvolvedora = desenvolvedora
        self.__genero = genero

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def data_lancamento(self):
        return self.__data_lancamento

    @data_lancamento.setter
    def data_lancamento(self, data_lancamento):
        self.__data_lancamento = data_lancamento

    @property
    def desenvolvedora(self):
        return self.__desenvolvedora

    @desenvolvedora.setter
    def desenvolvedora(self, desenvolvedora):
        self.__desenvolvedora = desenvolvedora

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero):
        self.__genero = genero
