from fastapi import FastAPI, HTTPException
from modelos import EntradaOperacao
from controlador import executar_operacao

app = FastAPI(title="Calculadora API")

@app.post("/calcular/{operacao}")
def calcular(operacao: str, entrada: EntradaOperacao):
    try:
        resultado = executar_operacao(operacao.lower(), entrada.a, entrada.b)
        return {"resultado": resultado}
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))
    except Exception:
        raise HTTPException(status_code=500, detail="Erro interno ao executar a operação.")
