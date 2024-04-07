#Quetion 1
from typing import List


class Contract:
    def __init__(self, id: int, debt: int) -> None:
        self.id = id
        self.debt = debt

    def __str__(self) -> str:
        return f"{self.id}, {self.debt}"


class Contracts:
    def get_top_N_open_contracts(
        self, open_contracts: List[Contract], renegotiated_contracts: List[int], top_n: int) -> List[int]:
        """Retorna uma lista contendo, top_n: inteiros referentes aos IDs dos devedores,
           ordenados do maior devedor para o menor.
        Args:
            open_contracts: Lista de contratos em aberto, e cada elemento é uma instância de Contract.
            renegotiated_contracts: Lista dos IDs dos associados que já renegociaram seus débitos.
            top_n: Quantidade de maiores devedores a serem retornados.
        """
        not_renegotiated_contracts = filter(
        lambda contract: contract.id not in renegotiated_contracts, open_contracts
        )
        sorted_contracts = sorted(
        not_renegotiated_contracts, key=lambda contract: contract.debt, reverse=True
        )
        top_n_contracts = [contract.id for contract in sorted_contracts[:top_n]]
        return top_n_contracts

def main() -> None:
    contracts = [
        Contract(1, 1),
        Contract(2, 2),
        Contract(3, 3),
        Contract(4, 4),
        Contract(5, 5)
    ]
    renegotiated = [3]
    top_n = 3

    c_managed = Contracts()
    actual_open_contracts = c_managed.get_top_N_open_contracts(contracts, renegotiated, top_n)

    print("IDs dos devedores:")
    print(actual_open_contracts)
    

if __name__ == "__main__":
    main()
