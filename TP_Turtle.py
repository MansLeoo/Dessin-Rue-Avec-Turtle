# -*- coding: utf-8 -*-

"""
Title : TP_Turtle
author: Mans léo
Version 1.0
"""
from turtle import *
from random import randint
#Initialisation
fenetre=Screen()
fenetre.clear()
liste_couleur=["red","orange","green","blue","navy","yellow",
"gold","tan","brown","sienna","wheat","cyan","pink","salmon","violet","purple"]
#Initialisation du programme 
stylo=Pen()
stylo.penup()
stylo.setposition(x=-300,y=-100)
x_deb,y_deb=stylo.position()
stylo.speed(10)
def maison():
    #variable random
    nb_etage=randint(1,5)
    type_toit=randint(1,3)
    position_porte=randint(1,3)
    couleur_batiment=randint(0,15)
    couleur_porte=randint(0,15)
    while couleur_porte==couleur_batiment:
        couleur_porte=randint(0,15)
    #Création des étage
    stylo.color("grey")
    stylo.pensize(1)
    stylo.fillcolor(liste_couleur[couleur_batiment])
    x,y=stylo.position()
    for i in range(nb_etage):
        stylo.setposition(x,y)
        stylo.setheading(0)
        stylo.begin_fill()
        stylo.pendown()
        stylo.forward(140)
        stylo.left(90)
        stylo.forward(60)
        stylo.left(90)
        stylo.forward(140)
        stylo.left(90)
        stylo.forward(60)
        stylo.left(90)
        y=y+60
        stylo.end_fill()
        
    #Gestion du toit
    stylo.pensize(1)
    if type_toit==1 or type_toit==2 :
        stylo.penup()
        stylo.fillcolor("black")
        x=x-10
        stylo.setposition(x,y)
        stylo.pendown()
        stylo.begin_fill()
        stylo.forward(160)
        stylo.left(160)
        stylo.forward(85)
        stylo.left(40)
        stylo.forward(85)
        stylo.end_fill()
    if type_toit==3:
        stylo.penup()
        stylo.begin_fill()
        stylo.fillcolor("black")
        stylo.setposition(x,y)
        stylo.pendown()
        stylo.begin_fill()
        stylo.forward(140)
        stylo.circle(5,180)
        stylo.forward(140)
        stylo.circle(5,180)
        stylo.end_fill()
    def fenetre(x:float,y:float,balcon=False):
        type_fenetre=randint(1,5)
        stylo.pensize(1)
        if balcon==False or type_fenetre!=5:
            stylo.penup()
            stylo.color('white')
            stylo.fillcolor('white')
            stylo.setposition(x,y)
            stylo.setheading(0)
            stylo.pendown()
            stylo.begin_fill()
            stylo.forward(30)
            stylo.left(90)
            stylo.forward(30)
            stylo.left(90) 
            stylo.forward(30)
            stylo.left(90) 
            stylo.forward(30)
            stylo.left(90)
            stylo.end_fill()
        if balcon==True and type_fenetre==5:
            stylo.penup()
            stylo.color('white')
            stylo.fillcolor('white')
            stylo.setposition(x,y-15)
            stylo.setheading(0)
            stylo.pendown()
            stylo.begin_fill()
            stylo.forward(30)
            stylo.left(90)
            stylo.forward(45)
            stylo.left(90)
            stylo.forward(30)
            stylo.left(90)
            stylo.forward(45)
            stylo.end_fill()
            stylo.penup()
            stylo.setposition(x-8,y-20)
            stylo.setheading(0)
            stylo.color('black')
            stylo.pensize(5)
            stylo.pendown()
            stylo.forward(46)
            stylo.left(90)
            stylo.forward(25)
            stylo.left(90)
            stylo.forward(46)
            stylo.left(90)
            stylo.forward(25)
            stylo.pensize(2)
            stylo.penup()
            x,y=stylo.position()
            for i in range(7):
                x=x+6
                stylo.setposition(x,y)
                stylo.pendown()
                stylo.setheading(0)
                stylo.left(90)
                stylo.forward(25)
                stylo.setheading(0)
                stylo.right(90)
                stylo.forward(25)
    
                
                
            
    
    def porte(x:float,y:float):
        stylo.pensize(1)
        type_porte=randint(1,2)
        stylo.penup()
        stylo.color('grey')
        stylo.fillcolor(liste_couleur[couleur_porte])
        stylo.setposition(x,y)
        stylo.setheading(0)
        stylo.pendown()
        stylo.begin_fill()
        if type_porte==1:
            stylo.forward(30)
            stylo.left(90)
            stylo.forward(50)
            stylo.left(90)
            stylo.forward(30)
            stylo.left(90)
            stylo.forward(50)
            stylo.end_fill()
        if type_porte==2:
            stylo.forward(30)
            stylo.left(90)
            stylo.forward(35)
            stylo.circle(15,180)
            stylo.forward(35)
            stylo.end_fill()
    #Gestion du premier étage
    if position_porte==1:
        porte(x_deb+12.5,y_deb)
        fenetre(x_deb+55,y_deb+20)
        fenetre(x_deb+97.5,y_deb+20)
    if position_porte==2:
        fenetre(x_deb+12.5,y_deb+20)
        porte(x_deb+55,y_deb)
        fenetre(x_deb+97.5,y_deb+20)
    if position_porte==3:
        fenetre(x_deb+12.5,y_deb+20)
        fenetre(x_deb+55,y_deb+20) 
        porte(x_deb+97.5,y_deb)
    #gestion des autres étages 
    et=60
    for i in range(nb_etage-1):
        fenetre(x_deb+12.5,y_deb+20+et,True)
        fenetre(x_deb+55,y_deb+20+et,True) 
        fenetre(x_deb+97.5,y_deb+20+et,True) 
        et=et+60
x=x_deb
for i in range(4):
    maison()
    stylo.penup()
    x_deb=x_deb+190
    y=y_deb
    x=x_deb
    stylo.setposition(x,y)
#ROUTE
stylo.penup()
stylo.pencolor("black")
stylo.setposition(-350,-100)
stylo.pendown()
stylo.setheading(0)
stylo.forward(810)


stylo.clearstamp(stylo.stamp())