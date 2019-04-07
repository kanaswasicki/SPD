Laboratorium 2 Algorytm NEH:
1. Porównanie działania algorytmu brute force, Johnson, NEH:
    W folderze statystyki znajdują się informacje, które wskazują na to, że brute force działa dużo wolniej niż reszta algorytmu ale jesteś pewni, że zwróci optymalne rozwiązanie problemu. Algorytm Johnsona w porównaniu do algorytmu NEH działa szybciej, dla 29 zadań jest to róznica 10^2, ale ze względu na czas wykonywania i milisekundach nie jesteśmy w stanie odczuć tej róznicy (zostało to sprawdzone za pomocą funkcji time.clock(), która liczy czas działania procesora. Początek zlicza został umieszczony przed rozpoczęciem samego algorytmu natomiast zakończenie tuż po a przed wpisanie wartości do tabel porównawczych), jednak w większości przypadku algorytm NEH działa lepiej, gdyż zwraca wartości Cmax mniejsze lub równe wartościom zwróconym przez algorytm Johnsona. 
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
Dla wychlodzenia:

\begin{tabular}{l|l|c|c|c|c|r|r}
wychlodzenie & Cmax &wychlodzenie & Cmax & wychlodzenie & Cmax & wychlodzenie & Cmax\\ \hline
0.8 & 1182.0 & 0.9 & 1172.0 &0.95& 1163.0&0.99& 1163.0\\
0.8 & 1244.0 & 0.9 & 1178.0 &0.95& 1163.0&0.99& 1163.0\\
0.8 & 1195.0 & 0.9 & 1182.0 &0.95& 1163.0&0.99& 1163.0\\
0.8 & 1168.0 & 0.9 & 1176.0 &0.95& 1178.0&0.99& 1168.0\\
0.8 & 1192.0 & 0.9 & 1163.0 &0.95& 1163.0&0.99& 1163.0\\
0.8 & 1168.0 & 0.9 & 1172.0 &0.95& 1163.0&0.99& 1163.0\\
0.8 & 1195.0 & 0.9 & 1163.0 &0.95& 1163.0&0.99& 1168.0\\
0.8 & 1211.0 & 0.9 & 1202.0 &0.95& 1163.0&0.99& 1163.0\\
0.8 & 1211.0 & 0.9 & 1182.0 &0.95& 1172.0&0.99& 1163.0\\
0.8 & 1177.0 & 0.9 & 1168.0 &0.95& 1163.0&0.99& 1168.0\\
\hline
0.8 & 1194.3 & 0.9 & 1175.8 &0.95& 1165.4&0.99& 1164.5\\
\hline\hline
\end{tabular}
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
porownanie insert / swap

\begin{tabular}{l|l|c|c}
Insert & Cmax &Swap & Cmax \\ \hline
--- & 1198.0 & --- & 1168.0\\
--- & 1168.0 & --- & 1168.0\\
--- & 1168.0 & --- & 1168.0\\
--- & 1231.0 & --- & 1163.0\\
--- & 1163.0 & --- & 1173.0\\
--- & 1199.0 & --- & 1168.0\\
--- & 1182.0 & --- & 1163.0\\
--- & 1182.0 & --- & 1168.0\\
--- & 1182.0 & --- & 1168.0\\
--- & 1182.0 & --- & 1204.0\\
--- & 1195.0 & --- & 1173.0\\
--- & 1176.0 & --- & 1182.0\\
--- & 1178.0 & --- & 1178.0\\
--- & 1255.0 & --- & 1163.0\\
--- & 1163.0 & --- & 1168.0\\
--- & 1168.0 & --- & 1163.0\\
--- & 1163.0 & --- & 1168.0\\
--- & 1182.0 & --- & 1168.0\\
--- & 1182.0 & --- & 1163.0\\
--- & 1163.0 & --- & 1182.0\\
--- & 1182.0 & --- & 1256.0\\
--- & 1198.0 & --- & 1168.0\\
--- & 1168.0 & --- & 1168.0\\
--- & 1205.0 & --- & 1165.0\\
--- & 1195.0 & --- & 1176.0\\
--- & 1178.0 & --- & 1168.0\\
--- & 1176.0 & --- & 1168.0\\
--- & 1244.0 & --- & 1242.0\\
--- & 1202.0 & --- & 1163.0\\
--- & 1168.0 & --- & 1163.0\\
\hline
--- & 1186.5333333333333 & --- & 1175.2\\
\hline\hline
\end{tabular}

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$