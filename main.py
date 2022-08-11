from acesso_cep import BuscaEndereco
from cpf_cnpj import Documento
from datas_br import DatasBr
from telefones_br import TelefonesBr

print("Testando formatador de Data")

dia_de_hoje = DatasBr()
print(dia_de_hoje, dia_de_hoje.dia_semana())

print("--------------------------------------------------------")
print("Testando formatador e Validador de CPF e CNPJ")

meu_cpf = "72021464369"
meu_cpf = Documento.cria_documento(meu_cpf)
print(meu_cpf)
meu_cnpj = "85805143000123"
meu_cnpj = Documento.cria_documento(meu_cnpj)
print(meu_cnpj)

print("--------------------------------------------------------")
print("Testando Formatador e Validador de telefones")

meu_telefone = "555581074556"
meu_telefone = TelefonesBr(meu_telefone)
print(meu_telefone)

print("--------------------------------------------------------")
print("Testando Formatador e Buscador de Endereço pelo CEP")

cep = "97105140"
retorna_cep = BuscaEndereco(cep)
busca_endereco = BuscaEndereco.acessa_via_cep(cep)
print(retorna_cep, busca_endereco)