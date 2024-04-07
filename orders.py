#Question 2
from typing import List


class Orders:
    def combine_orders(self, requests: List[int], n_max: int) -> int:
        """Calcula o número minimo de viagens de carro-forte das agências.
        Args:
            requests (list[int]): Lista de valores requisitados para cada agência.
            n_max (int): Valor máximo que pode ser transportado em uma viagem.
        Returns: inteiro,  número minimo de viagens necessárias.
        """
        trips = 0
        requests.sort(reverse=True)

        while requests:
            if len(requests) >= 2 and requests[0] + requests[1] <= n_max:
                trips += 1
                requests.pop(0)
                requests.pop(1)
            else:
                trips += 1
                requests.pop(0)
        return trips

def main() -> None:
    orders = [70, 30, 10]
    n_max = 100
    #expected_orders = 2

    how_many = Orders().combine_orders(orders, n_max)
    print(how_many)


if __name__ == "__main__":
    main()
