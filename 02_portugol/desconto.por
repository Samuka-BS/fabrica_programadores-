programa {
  funcao inicio() {
    real produto, desconto, porcentagem
    // valor do produto = R$ 200,00
    // percentual de desconto = 10%
    // valor do desconto = R$ 20,00
    escreva("informe o valor do produto: ")
    leia (produto)
    escreva("Quanto de desconto tem a vista?: ")
    leia(desconto)
    porcentagem = produto * (desconto / 100)
    escreva("A porcentagem é de: ", porcentagem) 
    
    
  }
}
