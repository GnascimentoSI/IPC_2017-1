# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Aracille de Souza Barbosa           1315120206
# Felipe Eduardo Silva de Almeida     1715310031
# Kethelen Tamara Braga               1525212002
# Nayara da Silva Cerdeira da Costa   1715310038
# Vitor Summer Oliveira Pantaleão     1715310042
# Yuri Leandro de Aquino Silva        1615100462
#
# Faça um programa que calcule e mostre a área de um losango.
# Sabe-se que A = (diagonal maior * diagonal menor)/2
# ----------------------------------------------------------

diag_larger = int(input("Informe a diagonal maior (cm): "))
diag_smaller = int(input("Informe a diagonal menor (cm): "))
area = (diag_larger * diag_smaller) / 2
print ("A área do losango é de %0.2f cm." % area)
