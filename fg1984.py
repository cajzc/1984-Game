import pygame

# Initialize Pygame
pygame.init()

# Set the window size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Add subtitle font size
small_font= pygame.font.SysFont(None, 20)
small_font_text= small_font.render("Press Q to close",True,(0,0,0))
small_font_rect=small_font_text.get_rect()
small_font_rect.center = (screen_width // 2, screen_height // 2 + 50)

# Set the window title
pygame.display.set_caption("1984 Game")

# Set the background color
background_color = (255, 255, 255)  # white
screen.fill(background_color)

# Set up the winston
winston_size = 24
winston_color = (255,255,0)  # yellow
winston_x = screen_width // 2 - winston_size // 2
winston_y = screen_height // 2 - winston_size // 2
winston_speed = 30

# Set up the borders
border_size = 16
border_color = (0, 0, 0)  # black
border_left = pygame.Rect(0, 0, border_size, screen_height)
border_right = pygame.Rect(screen_width - border_size, 0, border_size, screen_height)
border_top = pygame.Rect(0, 0, screen_width, border_size)
border_bottom = pygame.Rect(0, screen_height - border_size, screen_width, border_size)

book_font = pygame.font.SysFont(None, 24)


# Set up the interactive books
book_size = 12
book_color = (0,0,0)  # black
book_x = [400]
book_y = [200]
write_text = "Press Enter to Write:"
book_text = book_font.render("DOWN WITH BIG BROTHER DOWN WITH BIG BROTHER DOWN WITH BIG BROTHER", True, (0, 0, 0))
book_text_rect = book_text.get_rect(center=(screen_width // 2, screen_height // 2 - 20))
show_book = False

# Set up interactive poster
poster_size = 16
poster_color = (255, 0, 0)  # red
poster_x = [200]
poster_y = [500]
read_text = "Press Enter to Read:"
poster_text=book_font.render("WAR IS PEACE FREEDOM IS SLAVERY IGNORANCE IS STRENGTH",True,(0,0,0))
poster_text_rect=poster_text.get_rect(center=(screen_width // 2, screen_height // 2 - 20))
show_poster=False

# Set up Julia
julia_size = 32
julia_color = (255,0,255)  # pink
julia_x = [700]
julia_y = [120]
read_text = "Press Enter to Interact:"
julia_text=book_font.render("It was something in your face.... As soon as I saw you I knew you were against THEM",True,(0,0,0))
julia_text_rect=julia_text.get_rect(center=(screen_width // 2, screen_height // 2 - 20))
show_julia=False

# Set up O'Brien
obrien_size = 32
obrien_color = (255, 0, 0)  # red
obrien_x = [100]
obrien_y = [120]
read_text = "Press Enter to Interact:"
obrien_text=book_font.render("There is no loyalty but loyalty to the Party. There is no love except love of Big Brother...",True,(0,0,0))
obrien_text_rect=obrien_text.get_rect(center=(screen_width // 2, screen_height // 2 - 20))
show_obrien=False

# Main game loop
running = True

while running:
    # Handle book event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:

            # If Q is pressed, close book prompt
            if show_book and event.key == pygame.K_q:
                show_book = False
            
            # If Q is pressed, close poster prompt
            elif show_poster and event.key == pygame.K_q:
                show_poster = False

            # If Q is pressed, close julia interaction
            elif show_julia and event.key == pygame.K_q:
                show_julia = False

            # If Q is pressed, close obrien interaction
            elif show_obrien and event.key == pygame.K_q:
                show_obrien = False

            # Navigation
            elif event.key == pygame.K_UP:
                winston_y -= winston_speed
            elif event.key == pygame.K_DOWN:
                winston_y += winston_speed
            elif event.key == pygame.K_LEFT:
                winston_x -= winston_speed
            elif event.key == pygame.K_RIGHT:
                winston_x += winston_speed
            
            # If Winstons near the book, show the prompt
            elif not show_book and event.key == pygame.K_RETURN:
                for i in range(len(book_x)):
                    if abs(winston_x - book_x[i]) < winston_size and abs(winston_y - book_y[i]) < winston_size:
                        show_book = True




            # If Winstons near the poster, show the prompt
                for i in range(len(poster_x)):
                    if abs(winston_x - poster_x[i]) < winston_size and abs(winston_y - poster_y[i]) < winston_size:
                        show_poster = True

            # If Winstons near julia, show the interaction
                for i in range(len(poster_x)):
                    if abs(winston_x - julia_x[i]) < winston_size and abs(winston_y - julia_y[i]) < winston_size:
                        show_julia = True

            # If Winstons near obrien, show the interaction
                for i in range(len(poster_x)):
                    if abs(winston_x - obrien_x[i]) < winston_size and abs(winston_y - obrien_y[i]) < winston_size:
                        show_obrien = True


    # Check if the wisnton is near the book
    for i in range(len(book_x)):
        if abs(winston_x - book_x[i]) < winston_size and abs(winston_y - book_y[i]) < winston_size:
            prompt_text = book_font.render(write_text, True, (0, 0, 0))
            prompt_text_rect = prompt_text.get_rect(center=(book_x[i] + book_size // 2, book_y[i] - 20))
            screen.blit(prompt_text, prompt_text_rect)

    # Check if the winston is near the poster
    for i in range(len(poster_x)):
        if abs(winston_x - poster_x[i]) < winston_size and abs(winston_y - poster_y[i]) < winston_size:
            prompt_text = book_font.render(read_text, True, (0, 0, 0))
            prompt_text_rect = prompt_text.get_rect(center=(poster_x[i] + poster_size // 2, poster_y[i] - 20))
            screen.blit(prompt_text, prompt_text_rect)

    # Check if the winston is near julia
    for i in range(len(julia_x)):
        if abs(winston_x - julia_x[i]) < winston_size and abs(winston_y - julia_y[i]) < winston_size:
            prompt_text = book_font.render(read_text, True, (0, 0, 0))
            prompt_text_rect = prompt_text.get_rect(center=(julia_x[i] + julia_size // 2, julia_y[i] - 20))
            screen.blit(prompt_text, prompt_text_rect)

   # Check if the winston is near obrien
    for i in range(len(obrien_x)):
        if abs(winston_x - obrien_x[i]) < winston_size and abs(winston_y - obrien_y[i]) < winston_size:
            prompt_text = book_font.render(read_text, True, (0, 0, 0))
            prompt_text_rect = prompt_text.get_rect(center=(obrien_x[i] + obrien_size // 2, obrien_y[i] - 20))
            screen.blit(prompt_text, prompt_text_rect)

    # Draw the borders
    pygame.draw.rect(screen, border_color, border_left)
    pygame.draw.rect(screen, border_color, border_right)
    pygame.draw.rect(screen, border_color, border_top)
    pygame.draw.rect(screen, border_color, border_bottom)

    # Draw the winston
    pygame.draw.rect(screen, winston_color, (winston_x, winston_y, winston_size, winston_size))

    # Draw the interactive book
    for i in range(len(book_x)):
        # Draw the interactive book
        pygame.draw.rect(screen, book_color, (book_x[i], book_y[i], book_size, book_size))

    # Draw the interactive poster
    for i in range(len(poster_x)):
        # Draw the interactive poster
        pygame.draw.rect(screen, poster_color, (poster_x[i], poster_y[i], poster_size, poster_size))

    # Draw interactive julia
    for i in range(len(julia_x)):
        # Draw the interactive poster
        pygame.draw.rect(screen, julia_color, (julia_x[i], julia_y[i], julia_size, julia_size))

    # Draw interactive obrien
    for i in range(len(obrien_x)):
        # Draw the interactive poster
        pygame.draw.rect(screen, obrien_color, (obrien_x[i], obrien_y[i], obrien_size, obrien_size))

    # Check if you press enter on the book and show message
    if show_book:
        screen.blit(book_text, book_text_rect)
        screen.blit(small_font_text, small_font_rect)

    # Check if you press enter on the poster and show message
    if show_poster:
        screen.blit(poster_text,poster_text_rect)
        screen.blit(small_font_text, small_font_rect)

    # Check if you press enter on the poster and show message
    if show_julia:
        screen.blit(julia_text,julia_text_rect)
        screen.blit(small_font_text, small_font_rect)
     
    # Check if you press enter on the poster and show message
    if show_obrien:
        screen.blit(obrien_text,obrien_text_rect)
        screen.blit(small_font_text, small_font_rect)
     
    # Update the screen
    pygame.display.flip()

    # Clear the screen
    screen.fill(background_color)

# Clean up Pygame
pygame.quit()
