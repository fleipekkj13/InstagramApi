#APP Ideia

Recive a message, from Instagram or Facebook.
Call the program to response this message.


------------ HOW THE CODE WILL WORKS? ------------


--------- FIRST STEPS ---------

1. Client send a message.
2. Program recive the message.
3. Read the message.
4. If message contains "Qual o valor, quanto custa, quanto esta saindo, valor" -> Code execute. Else, don't execute.

--------- SECOND STEPS ---------

5. If message contains any value in the array then code search the price of product what the client wants to know.

--------- HOW HE ARE SEARCH FOR THAT? ---------

1. Access the website with the "search url".
2. Get the exact or similarity prodcut. If don't find anything like what the clien't want to know. Then, call someone to search in GS.
3. Send the value to client, and if the client don't send anything after 5minutos, end the chat.


--------- ALGORITHMS ---------

1 - Recive message:

    Create a timer to access the website and search for some new message:
        Timer = 5min.
        