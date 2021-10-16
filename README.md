# Bin2Dec-Python
Uma função que converte dígitos binários para o sistema decimal de numeração.

## Como usar
Não se preocupe com o __formato__ ou com __espaços__, a função é capaz de manipular o que foi digitado para que tudo funcione corretamente.
*Atente-se que a função requer parâmetros de palavra-chave (keyword arguments)*.
```bash
bin2dec(binary_digits='1100100')
>>> 100
```

```bash
bin2dec(binary_digits='0110 0100')
>>> 100
```

Além disso, em caso de erros, a função é __bastante prestativa__, pois analisa muitos fatores de erro internamento, facilitando na hora de tratar exceções.
Entenda melhor analisando os exemplos à seguir:
```bash
bin2dec(binary_digits='1234')
>>> ValueError: Only binary digits (0 and 1) are allowed: "1234" entered
```
No exemplo acima, vemos que a função lança uma exceção, o que de imediato quebraria o programa.
Mas testar tudo digitado pelo usuário no seu próprio código seria meio verboso, por isso a função já testa e retorna exceções que o ajudam à informar seu usuário.

## Tratando exceções
Usando o trecho de código abaixo, vamos exemplificar como a função lida com erros e o ajuda à tratá-los.
```python
from bin2dec import bin2dec


try:
  bin_digit = str(input('bin: '))
  print(bin2dec(binary_digits=bin_digit))
except Exception as e:
  print(f'Sorry, something went wrong: {e}')
```
Agora executando este módulo e inserindo `bla bla` na entrada, temos uma saída parecida com:
```bash
>>> Sorry, something went wrong: Only binary digits (0 and 1) are allowed: "blabla" entered
```
## Sucesso
Você viu que esta função pode ser útil quando queremos converter um conjunto de dígitos binários para a notaçao decimal de numeração. Fique à vontade para brincar com esta função, no entanto pesso que releia a licença.
