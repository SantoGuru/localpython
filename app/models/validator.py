from jsonschema import validate, ValidationError
from flask import jsonify

client_schema = {
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "Loja da Venda": {
        "type": "string",
        "description": "Nome da loja onde a venda foi realizada"
      },
      "Data da Venda": {
        "type": "string",
        "format": "date",
        "description": "Data em que a venda foi realizada"
      },
      "Nome do cliente": {
        "type": "string",
        "description": "Nome do cliente que realizou a compra"
      },
      "Data de cadastro do cliente no sistema": {
        "type": "string",
        "format": "date",
        "description": "Data de cadastro do cliente no sistema"
      },
      "Celular 1": {
        "type": "string",
        "description": "Primeiro número de celular do cliente"
      },
      "Celular 2": {
        "type": "string",
        "description": "Segundo número de celular do cliente"
      },
      "Celular 3": {
        "type": "string",
        "description": "Terceiro número de celular do cliente"
      },
      "Celular 4": {
        "type": "string",
        "description": "Quarto número de celular do cliente (opcional)"
      },
      "ID do vendedor no sistema": {
        "type": "string",
        "description": "Identificação do vendedor no sistema"
      },
      "Nome completo do vendedor": {
        "type": "string",
        "description": "Nome completo do vendedor"
      },
      "Celular do vendedor": {
        "type": "string",
        "description": "Número de celular do vendedor"
      },
      "ID da nota ou venda": {
        "type": "string",
        "description": "Identificação da nota ou venda"
      },
      "Valor da nota ou venda": {
        "type": "string",
        "description": "Valor total da nota ou venda"
      },
      "Produtos da nota ou venda": {
        "type": "array",
        "description": "Lista de produtos incluídos na nota ou venda",
        "items": {
          "type": "object",
          "properties": {
            "ID produto no sistema": {
              "type": "string",
              "description": "Identificação do produto no sistema"
            },
            "Fabricante": {
              "type": "string",
              "description": "Nome do fabricante do produto"
            },
            "Nome do produto ou servico": {
              "type": "string",
              "description": "Nome do produto ou serviço"
            },
            "descricao do produto ou servico": {
              "type": "string",
              "description": "Descrição do produto ou serviço"
            },
            "Valor do produto ou servico": {
              "type": "string",
              "description": "Valor do produto ou serviço"
            },
            "Quantidade vendida": {
              "type": "string",
              "description": "Quantidade de produto ou serviço vendida"
            }
          },
          "required": [
            "ID produto no sistema",
            "Nome do produto ou servico",
            "descricao do produto ou servico",
            "Valor do produto ou servico",
            "Quantidade vendida"
          ]
        }
      }
    },
    "required": [
      "Loja da Venda",
      "Data da Venda",
      "Nome do cliente",
      "Data de cadastro do cliente no sistema",
      "Celular 1",
      "ID do vendedor no sistema",
      "Nome completo do vendedor",
      "Celular do vendedor",
      "ID da nota ou venda",
      "Valor da nota ou venda",
      "Produtos da nota ou venda"
    ]
  }
}

def validar(data):
    try:
        validate(instance=data, schema=client_schema)
    except ValidationError as e:
         return jsonify({"error": e.message}), 400
