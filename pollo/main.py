import argparse

parser = argparse.ArgumentParser(description='Super Proyecto Demo')
parser.add_argument('--nombre', '-n', help="El nombre de atributo")

def main():
    args = parser.parse_args()
    if args.nombre:
        print(f"Programa especial de Pollo - {args.nombre}")
    else:
        print("Programa especial de Pollo")

if __name__ == '__main__':
    main()
    exit()