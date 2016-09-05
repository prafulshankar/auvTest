auvTest

1) OpenCV task: Followed the instructions on the auv website, using appropriate color spaces to find a good color space. Then refined the masks by eroding and dilating the resulting images. Used Circulr Hough transform to detect circles and find their (x,y,r) Wrote it onto the image and presented the output as jpg "targeted-buoys".

Syntax to use: python buoy.py -iimage/image path eg: python buoy.py -i "buoysf.jpg". 

*note: couldn't use cvmoments but the results seem right regardless*

2) Calculator task: Implemented cmd line interface for a simple calculator that takes in and parses mathematical expressions involving +-*/ and presents the steps converting it to postfix first and then evaluating the result 

Syntax to use: python calc.py

3) Sudoku task: First check for size and shape of board and what numbers are present on it Then each row for uniqueness using helper function Then each column Then each box using numpy reshaping methods 
Syntax to use: python SuDoku.py 
NOTE: Boards passed in as np arrays in the file
