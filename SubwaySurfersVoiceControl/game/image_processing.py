import cv2

class ImageProcessing:
    def __init__(self):
        self.player_image = cv2.imread("player_image.jpg")
        self.policeman_image = cv2.imread("policeman_image.jpg")
        self.favorite_person_image = cv2.imread("favorite_person_image.jpg")

    def overlay_images(self, background, foreground, x, y):
        cv2.addWeighted(foreground, 1, background, 1, 0, background)

    def draw_game_environment(self):
        # Load the game environment image
        game_environment = cv2.imread("game_environment.jpg")

        # Overlay the player image
        self.overlay_images(game_environment, self.player_image, 100, 100)

        # Overlay the policeman image
        self.overlay_images(game_environment, self.policeman_image, 200, 200)

        # Overlay the favorite person image
        self.overlay_images(self.policeman_image, self.favorite_person_image, 50, 50)

        # Display the game environment
        cv2.imshow("Game Environment", game_environment)
        cv2.waitKey(0)
        cv2.destroyAllWindows()