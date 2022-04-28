class Position:

    """The class Position is used to store coordinates of an object. It also contains a method "in_position(self, position)" to check if the given position of the mouse-cursor is within the object.

    Attributes:
        x: the x-coordinate of the object
        y: the y-coordinate of the object
        coordinates: combined (x, y)-coordinates
        width: width of the object
        height: height of the object
    """

    def __init__(self, x, y, width, height):

        """The constructor of the class.

        Args:
            x: the x-coordinate
            y: the y-coordinate
            width: the width of the object
            height: the height of the object
        """

        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)

        self.width = width
        self.height = height

    def in_position(self, position):

        """Checks if the mouse-cursor is within the object.

        Args:
            position: gives the position of the mouse-cursor as coordinates. (tuple)

        Returns:
            True: if the position of the mouse-cursor is within the object
            False: if the position of the mouse-cursor is not within the object.
        """
    
        if self.x <= position[0] <= self.x + self.width and self.y <= position[1] <= self.y + self.height:
            return True
        
        return False

class GameboardPositions:

    """ The GameboardPositions class oversees the UI's positioning of most elements. Each element is an instance of the Position class. 
        Most coordinates are given in relation to the display_size or to each other. In this way it is assured that everything looks correct. 
        It is to be noted that player1_hand_cards and player2_hand_cards are elements with a special arrangement since their position varies. These thus have functions to decide the position.
        The same is true for a card that is targeted by a player.

    Attributes:
        Note: As there are so many attributes in this class and lots of them just being repetition or a mirror of another it is unecessary to
              explain each attribute individually. I will take some of them and explain them in greater detail.

            gameboard: An instance of the class Gameboard shared across multiply classes in the architecture as a whole.
            album: An instance of the class Album shared across multiply classes in the architecture as a whole.
            display_size = An  instance of the class DisplaySize
            card_width = The width of a card.
            card_height = The height of a card.

            The rest of the attributes are of one of two types.

            1. Deck/Card: Instances of the class Position. All of these have card_width as the argument for width and card_height as the argument for heihgt.
            2. Button/button_text: Instances of the class Position. All of these have button_width as the argument for width and button_height as the argument for height.

    """

    def __init__(self, gameboard, album, display_size, card_width, card_height):

        """The constructor of the class. This class also holds all of the attributes. Read the notes about the class to get a good understanding of the arguments as well. The rest is very straight forward.
        """

        self.gameboard = gameboard
        self.album = album.images

        # Dimensions
        self.display_size = display_size
        self.card_width = card_width
        self.card_height = card_height

        # Reserve_deck position
        self.reserve_deck = Position(((self.display_size.width/4)-(self.card_height/2)), ((self.display_size.height/2)-(self.card_width/2)), self.card_width, self.card_height)

        # Field_deck position
        self.field_deck = Position(((self.display_size.width/2)-(self.card_width/2)), ((self.display_size.height/2)-(self.card_height/2)), self.card_width, self.card_height)


        # Player1 staged position
        self.player1_staged = Position((self.field_deck.x - self.card_width*0.7), (self.field_deck.y + self.card_height*0.7), self.card_width, self.card_height)

        # Player2 staged position
        self.player2_staged = Position((self.field_deck.x + self.card_width*0.7), (self.field_deck.y - self.card_height*0.7), self.card_width, self.card_height)


        # Player1 endgame first, second, third
        self.player1_endgame_second = Position((self.display_size.width/2-self.card_width/2), (self.player1_staged.y + self.card_height*1.5), self.card_width, self.card_height)
        self.player1_endgame_first = Position((self.player1_endgame_second.x - self.card_width*1.5), (self.player1_endgame_second.y), self.card_width, self.card_height)
        self.player1_endgame_third = Position((self.player1_endgame_second.x + self.card_width*1.5), (self.player1_endgame_second.y), self.card_width, self.card_height)


        # Player2 endgame first, second, third
        self.player2_endgame_second = Position((self.player1_endgame_second.x), (self.player2_staged.y - self.card_height*2), self.card_width, self.card_height)
        self.player2_endgame_first = Position((self.player2_endgame_second.x - self.card_width*1.5), (self.player2_endgame_second.y), self.card_width, self.card_height)
        self.player2_endgame_third = Position((self.player2_endgame_second.x + self.card_width*1.5), (self.player2_endgame_first.y), self.card_width, self.card_height)


        # Player1 final first, second, third
        self.player1_final_first = Position((self.player1_endgame_first.x), (self.player1_endgame_first.y + self.card_height*0.2), self.card_width, self.card_height)
        self.player1_final_second = Position((self.player1_endgame_second.x), (self.player1_final_first.y), self.card_width, self.card_height)
        self.player1_final_third = Position((self.player1_endgame_third.x), (self.player1_final_first.y), self.card_width, self.card_height)


        # Player2 final first, second, third
        self.player2_final_first = Position((self.player2_endgame_first.x), (self.player2_endgame_first.y - self.card_height*0.2), self.card_width, self.card_height)
        self.player2_final_second = Position((self.player2_endgame_second.x), (self.player2_final_first.y), self.card_width, self.card_height)
        self.player2_final_third = Position((self.player2_endgame_third.x), (self.player2_final_first.y), self.card_width, self.card_height)


        # Player hand mid card position
        self.player1_hand_mid_card = Position((self.display_size.width/2), (self.display_size.height-self.card_height*1.1), self.card_width, self.card_height)
        self.player2_hand_mid_card = Position((self.display_size.width/2), (self.card_height*0.1), self.card_width, self.card_height)

        # Gameboard graphics
        self.reserve_deck_frame = Position((self.reserve_deck.x - self.card_height*0.05), (self.reserve_deck.y - self.card_width*0.10), 125, 95)
        self.field_deck_frame = Position((self.field_deck.x - self.card_width*0.10), (self.field_deck.y - self.card_height*0.05), 95, 125)

        self.player1_stage_frame = Position((self.player1_staged.x - self.card_width*0.10), (self.player1_staged.y - self.card_height*0.05), 95, 125)
        self.player2_stage_frame = Position((self.player2_staged.x - self.card_width*0.10), (self.player2_staged.y - self.card_height*0.05), 95, 125)

        self.button_width = self.card_width*1.5
        self.button_height = self.card_height/2.8

        self.playbutton = Position((self.player1_staged.x + self.card_width + 10), (self.player1_staged.y + self.card_width - 10), self.button_width, self.button_height)
        self.playbutton_text = Position((self.playbutton.x + 40), (self.playbutton.y + 10), self.button_width, self.button_height)

        self.exitbutton = Position((self.card_width/3), (self.display_size.height - self.card_width/1.5), self.button_width, self.button_height)
        self.exitbutton_text = Position((self.exitbutton.x + 40), (self.exitbutton.y + 10), self.button_width, self.button_height)

        self.unstagebutton = Position((self.player1_stage_frame.x - self.button_width*1.05), (self.playbutton.y), self.button_width, self.button_height)
        self.unstagebutton_text = Position((self.unstagebutton.x + 10), (self.unstagebutton.y + 10), self.button_width, self.button_height)

        self.sortbutton = Position((self.display_size.width - self.exitbutton.x - self.button_width), (self.exitbutton.y), self.button_width, self.button_height)
        self.sortbutton_text = Position((self.sortbutton.x + 40), (self.sortbutton.y + 10), self.button_width, self.button_height)



    def decide_player1_hand_card_position(self, card, card_index):

        """Decides the position of a card in player1's hand. The position is decided as a relation between the card_index and the total amount of cards in the player's hand.

        Args:
            card: An instance of the class Card. It is used to find the correct image in self.album.
            card_index: gives aditional information on where the card should be positioned,

        Returns:
            tuple: Returns a tuple of the (x,y) coordinates.
        """

        ui_card = self.album[card.name]

        if ui_card.target == False:

            ui_card.x = ((self.player1_hand_mid_card.x) -
                         (len(self.gameboard.player1_hand)/2)*self.card_width)+(100*card_index)
            ui_card.y = (self.player1_hand_mid_card.y)

            return (ui_card.x, ui_card.y)

        return (ui_card.x, ui_card.y)

    def decide_player2_hand_card_position(self, card, card_index):


        """Decides the position of a card in player2's hand. The position is decided as a relation between the card_index and the total amount of cards in the player's hand.

        Args:
            card: An instance of the class Card. It is used to find the correct image in self.album.
            card_index: gives aditional information on where the card should be positioned,

        Returns:
            tuple: Returns a tuple of the (x,y) coordinates.
        """

        ui_card = self.album[card.name]

        if ui_card.target == False:

            x = ((self.player2_hand_mid_card.x) -
                 (len(self.gameboard.player2_hand)/2)*self.card_width)+(100*card_index)
            y = (self.player2_hand_mid_card.y)

            return (x, y)

        return (ui_card.x, ui_card.y)

