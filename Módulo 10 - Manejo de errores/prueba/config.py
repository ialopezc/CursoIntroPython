def main():
    try:
        configuration = open('config.txt')
    except OSError as err:
        print(f"ocurrio un erro #{err}")


if __name__ == '__main__':
    main()