import requests

def ObtenerPrecioBitcoin():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        precioUSD = data['bpi']['USD']['rate_float'] 
        return precioUSD
    except requests.RequestException as e:
        print(f"Hubo un error al consultar el precio de Bitcoin: {e}")
        return None

def CalcularValorBitcoins(n, precioUSD):
    return n * precioUSD

def main():
    try:
        n = float(input("Ingrese la cantidad de Bitcoins que posee: "))
        precioUSD = ObtenerPrecioBitcoin()

        if precioUSD is not None:
            valor = CalcularValorBitcoins(n, precioUSD)
            print(f"El costo actual de {n} Bitcoins en USD es: ${valor:,.4f}")
        else:
            print("No se encontró el precio de Bitcoin")
    except ValueError:
        print("Por favor, ingrese un número válido")

if __name__ == "__main__":
    main()