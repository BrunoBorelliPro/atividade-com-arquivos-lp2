from openpyxl import Workbook

class Funcionario:
    
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    #Essa função recebe um workbook e 
    def Adiciona_funcionario(self, wb:Workbook):
        wsFuncionarios = wb["Funcionarios"]
        wsFuncionarios.append([self.id, self.nome])

        wb.save("AtividadeComArquivos.xlsx")
    
    @staticmethod
    def Listar_Funcionarios(wb:Workbook):
        wsFuncionarios = wb["Funcionarios"]
        print("=-=-=-=-=-=-=-=")
        print("Id - Nome")
        for row in wsFuncionarios.rows:
            id = row[0].value
            nome = row[1].value
            print(id,"-",nome)
        print("=-=-=-=-=-=-=-=")
        print('')
        pass
        