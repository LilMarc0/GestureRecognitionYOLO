- Folositi orice python>3,5 doriti, important este sa rualti comanda de mai jos in consola.

		pip install opencv-python numpy 
		
- Pentru a rula, folosim comanda:  

		python Main.py --gest NUME_GEST

- Argumente optionale: ( de preferat, nu le schimbati )

                                    -- show True/False  ---> Daca vreti sa vedeti de inregistrati ( default True )
                                    -- sec nr_sec       ---> Numarul de secunde de inregistrare ( default 20 )
                                    -- fps nr           ---> Numarul de cadre pe secunda ( default 15 )
									
- *NUME_GEST* trebuie ales dintr-o lista pe care ne-o stabilim, pe moment m-am gandit la gesturile basic discutate pana acum:

		palma, ok, like, cadrustanga, cadrudreapta, n(1-5)deget
