﻿'Make sure that a value is set for label variables (preview the label before you start writing your script).
'The result of the script must be saved in the 'Result'
'variable. Default script will return value "0"

If [label_picking_box.row] = "G" And [label_picking_box.bay] = "1" Then
 Result = "C:\Dropbox\Path\to\Colors\red.gif"

ElseIf [label_picking_box.row] = "G" And [label_picking_box.bay] = "2" Then
 Result = "C:\Dropbox\Path\to\ColorsColors\green.gif"
 
ElseIf [label_picking_box.row] = "G" And [label_picking_box.bay] = "3" Then
 Result = "C:\Dropbox\Path\to\Colors\Colors\lime.gif"
 
ElseIf [label_picking_box.row] = "G" And [label_picking_box.bay] = "4" Then
 Result = "C:\Dropbox\Path\to\Colors\Colors\orange.gif"
 
ElseIf [label_picking_box.row] = "G" And [label_picking_box.bay] = "5" Then
 Result = "C:\Dropbox\Path\to\Colors\Colors\pink.gif"
 
ElseIf [label_picking_box.row] = "G" And [label_picking_box.bay] = "6" Then
 Result = "C:\Dropbox\Path\to\Colors\Colors\teal.gif"
 
ElseIf [label_picking_box.row] = "G" And [label_picking_box.bay] = "7" Then
 Result = "C:\Dropbox\Path\to\Colors\Colors\lavender.gif"

ElseIf [label_picking_box.row] = "G" And [label_picking_box.bay] = "9" Then
 Result = "C:\Dropbox\Path\to\Colors\Colors\yellow.gif"
 
ElseIf [label_picking_box.row] = "H" And [label_picking_box.bay] = "1" Then
 Result = "C:\Dropbox\Label Printer Files\Colors\yellow.gif"
 
ElseIf [label_picking_box.row] = "H" And [label_picking_box.bay] = "2" Then
 Result = "C:\Dropbox\Label Printer Files\Colors\lavender.gif"
 
ElseIf [label_picking_box.row] = "H" And [label_picking_box.bay] = "3" Then
 Result = "C:\Dropbox\Path\to\Colors\Colors\teal.gif"
 
ElseIf [label_picking_box.row] = "H" And [label_picking_box.bay] = "4" Then
 Result = "C:\Dropbox\Path\to\Colors\Colors\pink.gif"
 
ElseIf [label_picking_box.row] = "H" And [label_picking_box.bay] = "5" Then
 Result = "C:\Dropbox\Path\to\Colors\Colors\orange.gif"

ElseIf [label_picking_box.row] = "H" And [label_picking_box.bay] = "6" Then
 Result = "C:\Dropbox\Path\to\Colors\Colors\lime.gif"
 
ElseIf [label_picking_box.row] = "H" And [label_picking_box.bay] = "7" Then
 Result = "C:\Dropbox\Path\to\Colors\Colors\green.gif"
 
ElseIf [label_picking_box.row] = "H" And [label_picking_box.bay] = "9" Then
 Result = "C:\Dropbox\Path\to\Colors\Colors\red.gif"


 
Else
 Result = ""
 
End If


Result = Result
