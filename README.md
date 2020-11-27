# PriceEstimater

This is a tool that I made for a friend that had some trouble knowing how to price appointments.

The problem:
  She had problem with underpricing and overpricing appointments.

The approach:
  I have come up with an approach that bases the price off of:
  - Special factor: how special is this appointment for the customer Ex: Wedding, graduation, classis photoshoot
  - Hours: how many hours the appointment is supposed to last.
  - Age: Age of the client. The reason behind making that a factor is that photoshoots can be harder with young clients than 
         older clients.
  - Weather: How good the weather is during the appointment. the reason behind making that a factor is that weather conditions
             can affect equipment and the photographer.
  - Editing: Will you be editing the photos/videos. 
  
The results:
  - Estimates Lowest price to offer, recommended price to offer, and the highest price to offer.
  
## Install
1. install requirements
  ```python
  pip install -r requirements.txt
  ```

## Run
  - if you are happy with the preset factors that makes the estimation, you can just run the program by typing
  ```python
  python app.py
  ```


___
I know that this project is still far from perfect, I'm still working on some fixes to make it more effecient and I'd love any kind of help with this project!
