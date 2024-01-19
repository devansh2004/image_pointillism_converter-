#Devansh Patel
#101267833

#imports needed
import pygame
import sys
import random

#the scale used to resize the original image to the one being made (works best from 4 to 8 (4 is best though))
scale = 4

#loading the original image given by the user
ogImage = pygame.image.load(sys.argv[1])

#getting the dimensions of the original image
(ogX,ogY) = ogImage.get_size()

#creating the surface for the new image and setting its dimention with the set scale
surface = pygame.display.set_mode((ogX*scale,ogY*scale))

#making the surface background white
surface.fill((255,255,255))

#going through each pixel in the original image
for x in range(0, ogX):
    for y in range(0, ogY):
        
        #getting the rgb value of a single pixel from the original image
        (r, g, b, _) = ogImage.get_at((x, y))

        #getting the lumince of the singular pixel
        lum = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255

        #setting varibles with the same rgb values to be used as the condition for each color loop
        wr =r
        wg =g
        wb =b
        
        #Helps correct the color, as since green recs go on top and red recs and blue recs go on top of both (makes it look better in my opinion).
        cd = 8

        #checks if all red, green, and blue values are 0, and makes the pixel black
        if(r == 0 and g == 0 and b == 0):
            for w in range (300):
                pygame.draw.rect(surface,(0,0,0),(((x*scale) + random.randint(0,scale+1)) ,((y*scale) + random.randint(0,scale+1)),2,2))

            #sets the conditions for the while loops to 0 so the other color recs dont go on top of the balck pixel
            wr =0
            wg =0
            wb =0        
            
        #checks if all red, green, and blue values are 255, and makes the pixel white 
        if(r == 255 and g == 255 and b == 255):
            for w in range (300):
                pygame.draw.rect(surface,(255,255,255),(((x*scale) + random.randint(0,scale+1)) ,((y*scale) + random.randint(0,scale+1)),2,2))

            #sets the conditions for the while loops to 0 so the other color recs dont go on top of the white pixel
            wr =0
            wg =0
            wb =0    

        #adds red rectangles to make up the red value of said pixel
        while(wr>0):
            if(lum > 0.2126):
                pygame.draw.rect(surface,(255,0,0),(((x*scale) + random.randint(0,scale)) ,((y*scale) + random.randint(0,scale)),1,1))

            #condition for how many times the while loop should run    
            wr=wr -cd

        #adds green rectangles to make up the green value of said pixel
        while(wg>0):
            if(lum > 0.7152):
                pygame.draw.rect(surface,(0,255,0),(((x*scale) + random.randint(0,scale)) ,((y*scale) + random.randint(0,scale)),1,1))
                
            #condition for how many times the while loop should run    
            wg = wg -cd*3

        #adds blue rectangles to make up the blue value of said pixel
        while(wb>0):
            if(lum > 0.0722):
                pygame.draw.rect(surface,(0,0,255),(((x*scale) + random.randint(0,scale)) ,((y*scale) + random.randint(0,scale)),1,1))
                
            #condition for how many times the while loop should run    
            wb = wb -cd*4
        
        
        
        #keeps updating image every pixel (Thought it looked cool)
        pygame.display.update()
        
        
            
#updates image for the final time after processing every pixel is done
pygame.display.update()

#closes windows, when user decides to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()