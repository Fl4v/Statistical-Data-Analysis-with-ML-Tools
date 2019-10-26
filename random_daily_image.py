from api import NasaApod

if __name__ == "__main__":
    Nasa = NasaApod()
    user_input = input('Would you like to open the image? [y/n]: ')
    if user_input == 'y':
        Nasa.open_daily_image()
    else:
        pass
