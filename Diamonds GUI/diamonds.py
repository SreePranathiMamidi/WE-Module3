import pygame
import random
import os

pygame.init()

WIDTH, HEIGHT = 1000, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Diamond Card Game")

# Load card images for hearts and clubs
hearts_images = {i: pygame.image.load(f"images/{i}heart.png") for i in range(2, 15)}
clubs_images = {i: pygame.image.load(f"images/{i}club.png") for i in range(2, 15)}

# Function to draw card
def draw_card(card_value, x, y, suit):
    if suit == "hearts":
        scaled_card = pygame.transform.scale(hearts_images[card_value], (70, 110))
    elif suit == "clubs":
        scaled_card = pygame.transform.scale(clubs_images[card_value], (70, 110))
    else:
        diamond_image = pygame.image.load(f"images/{card_value}diamond.png")
        scaled_card = pygame.transform.scale(diamond_image, (70, 110))
    WINDOW.blit(scaled_card, (x, y))

# Function to draw scores
def draw_scores(user_score, computer_score):
    font = pygame.font.SysFont(None, 36)
    user_text = font.render(f"Your Score: {user_score}", True, (0, 0, 0))
    WINDOW.blit(user_text, (10, 10))
    computer_text = font.render(f"Computer Score: {computer_score}", True, (0, 0, 0))
    WINDOW.blit(computer_text, (WIDTH - computer_text.get_width() - 10, 10))

# Main function to run the game
def main():
    # Game variables
    user_hand = list(range(2, 15))  # User's hand
    computer_hand = list(range(2, 15))  # Computer's hand
    user_score = 0
    computer_score = 0
    diamond_hand = list(range(2,15))
    diamond_card = random.choice(diamond_hand)
    diamond_hand.remove(diamond_card)
    user_bid = None
    computer_bid = None
    bid_count = 0

    # Main game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Handle user bidding (left-click to bid)
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if mouse_x < WIDTH / 2:  # User's hand
                    selected_card = min(max((mouse_y - HEIGHT * 0.2) // (HEIGHT * 0.6 / len(user_hand)), 0), len(user_hand) - 1)
                    user_bid = user_hand.pop(int(selected_card))
                    bid_count += 1
                else:  # Computer's hand
                    if diamond_card >=7:
                        computer_bid = random.choice(computer_hand[:len(computer_hand)//2])
                    else:
                        computer_bid = random.choice(computer_hand[len(computer_hand)//2:])
                    computer_hand.remove(computer_bid)
                    bid_count += 1

        # Draw game elements
        WINDOW.fill((255, 255, 255))

        # Draw scores
        draw_scores(user_score, computer_score)

        # Draw user's hand
        for i, card in enumerate(user_hand):
            draw_card(card, 50, HEIGHT * 0.2 + i * (HEIGHT * 0.6 / len(user_hand)), "hearts")

        # Draw computer's hand
        for i, card in enumerate(computer_hand):
            draw_card(card, WIDTH - 150, HEIGHT * 0.2 + i * (HEIGHT * 0.6 / len(computer_hand)), "clubs")

        # Draw diamond card
        
        # Update scores based on bids
        if user_bid is not None and computer_bid is not None:
            if user_bid > computer_bid:
                user_score += diamond_card
            elif computer_bid > user_bid:
                computer_score += diamond_card
            # Reset bids
            user_bid = None
            computer_bid = None
        if bid_count == 2:
            diamond_card = random.choice(diamond_hand)
            diamond_hand.remove(diamond_card)
            bid_count = 0
        draw_card(diamond_card, WIDTH // 2 - 50, HEIGHT // 2 - 50, "diamond")

        pygame.display.update()

    # Quit Pygame
    pygame.quit()

main()