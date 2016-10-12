My first repository. I am NOT a programmer by any means, these are mere scripts to help me automate some of my work. I would love to be one in the near future, and I figure this is great practice. Please go easy on this lowly squire.

ComparisonStrings.py - Compares string values, very basic -  I use this to put inventory back in their shelve locations. By scanning the SKU location, and the SKU from the product it compares and show a message. Depending if the string values match or not.

refturnsForm.py - Takes user input  that is related to receiving, such as Cust name, E-mail, Order, SKU names and qty etc.. and writes into a CSV file.

color_code.vbs  - Small VBscript that color codes a label with predetermined color swatch folder stored in dropbox. Warning: Lots of ELSIF used.

Label was designed using NiceLabel, with locations G1 through G9 excluding G8. The same goes for H. H1 through H9 excluding H8.

Explanation:
If the label picking box letter is equals to "G" and the label picking box number is equals to a number between 1 and  9 excluding 8 then the result is the color that you stored at that location. In this case the colors are located in dropbox. Again, Same with H. I excluded 8 because we don't have that location available.

Color coding allows replenishing stock at a given location much more accuracy and error reduction(People replenishing stock will not store the wrong item at the wrong location).

![Alt text](https://github.com/propupul/AutomateWarehouse/blob/returnforms_beta/color_g_h.jpg?raw=true "Colors")
