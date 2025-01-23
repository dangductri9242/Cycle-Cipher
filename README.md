# Cycle-Cipher
An original cipher for encrypting and decrypting files
The coding product will be separated into two parts, which are Cycle Ciphers conducting in $\mathbf{Z}_{26}$ and $\mathbf{Z}_{256}$.
\subsection{Coding product in $\mathbf{Z}_{26}$}
The coding products in $\mathbf{Z}_{26}$ will include a process of encryption, decryption, a key generator, and a program that checking the frequency of the text. In $\mathbf{Z}_{26}$, all plaintexts and ciphertexts just only include capital letters from A to Z. Furthermore, the file to be encrypted and decrypted must end in \textbf{.txt}\\

\textbf{The encryption process}: The program will return a ciphertext file from a file includes the plaintext and the key. The ciphertext file does not need to be created in advance. The complexity of the program should be O(n). The structure of command line will be:
\begin{lstlisting}
python .\Z26_cyclecipher_encryption.py .\plaintext_file.txt 
.\ciphertext_file.txt .\key_file.txt
\end{lstlisting}

\textbf{The decryption process}: The program will return a decrypted text file from a file includes the ciphertext and the key. The decrypted text file does not need to be created in advance. The complexity of the program should be O(n). The structure of command line will be:
\begin{lstlisting}
python .\Z26_cyclecipher_decryption.py .\ciphertext_file.txt
.\decrypted_text_file.txt .\key_file.txt
\end{lstlisting}

\textbf{Key generation}: The program will return a key file with the number of rounds. The file for the key does not need to be created in advance. The structure of command line will be:
\begin{lstlisting}
python .\key_generator.py .\key_file.txt number_of_rounds
\end{lstlisting}


\textbf{The frequency of the text}: The program will return a graphic demonstrate the histogram of the text from a given text file. The structure of command line will be:
\begin{lstlisting}
python .\frequency_ciphertext.py .\text_file.txt 
\end{lstlisting}

\subsection{Coding product in $\mathbf{Z}_{256}$}

\indent \indent The coding products in $\mathbf{Z}_{256}$ will include a process of encryption, decryption, and a key generator. In $\mathbf{Z}_{256}$, the plaintext can be any file to be encrypted to a \textbf{.cyc} file, and the decryption can also turn any \textbf{.cyc} file into the original file. However, the key still need to keep in \textbf{.txt}.

\textbf{The encryption process}: The program will return a ciphertext file from a file includes the plaintext and the key. The ciphertext file does not need to be created in advance. The complexity of the program should be O(n). The structure of command line will be:
\begin{lstlisting}
python .\Z256_cyclecipher_encryption.py .\plaintext_file 
.\ciphertext_file .\key_file.txt
\end{lstlisting}

\textbf{The decryption process}: The program will return a decrypted text file from a file includes the ciphertext and the key. The decrypted text file does not need to be created in advance. The complexity of the program should be O(n). The structure of command line will be:
\begin{lstlisting}
python .\Z256_cyclecipher_decryption.py .\ciphertext_file.txt
.\decrypted_text_file.txt .\key_file.txt
\end{lstlisting}

\textbf{Key generation}: The program will return a key file with the number of rounds. The file for the key does not need to be created in advance. The structure of command line will be:
\begin{lstlisting}
python .\key_generator.py .\key_file.txt number_of_rounds
\end{lstlisting}

There is no frequency check for $\mathbf{Z}_{256}$ because the histogram will be huge and it cannot be indicated through any graphics.
