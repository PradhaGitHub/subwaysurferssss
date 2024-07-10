import pygame
from game.game_logic import GameLogic
from game.image_processing import ImageProcessing
from game.voice_commands import VoiceCommands

def main():
    # Initialize Pygame
    pygame.init()

    # Create a game logic object
    game_logic = GameLogic()

    # Create an image processing object
    image_processing = ImageProcessing()

    # Create a voice commands object
    voice_commands = VoiceCommands()

    # Set up the game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get voice commands
        command = voice_commands.get_command()

        # Process the command
        if command == "left":
            game_logic.move_left()
        elif command == "right":
            game_logic.move_right()
        elif command == "jump":
            game_logic.jump()
        elif command == "duck":
            game_logic.duck()

        # Update the game state
        game_logic.update()

       