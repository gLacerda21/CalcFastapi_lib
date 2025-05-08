import importlib
from operacoes.base import Operacao

def executar_operacao(nome: str, a: float, b: float) -> float:
    try:
        modulo = importlib.import_module(f"operacoes.{nome}")
        classe = getattr(modulo, nome.capitalize())
        if not issubclass(classe, Operacao):
            raise TypeError("Classe de operação inválida.")
        instancia = classe()
        return instancia.calcular(a, b)
    except ModuleNotFoundError:
        raise ValueError(f"Operação '{nome}' não foi encontrada.")
    except Exception as e:
        raise e
