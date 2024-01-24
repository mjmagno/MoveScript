import pygame

def play_custom_sound(sound_file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        sound = pygame.mixer.Sound(sound_file_path)
        sound.play()
        pygame.time.delay(int(sound.get_length() * 1000))  # Delay to allow sound to finish playing
    except Exception as e:
        print(f"Error playing sound: {e}")
    finally:
        pygame.mixer.quit()
        pygame.quit()