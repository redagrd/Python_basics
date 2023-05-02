# TP reseau

connecter deux machines en reseau interne (LAN)
1 = creation d'une nouvelle machine
2 = configurer interface sur virtual box (changer pont en reseau interne)
et nomer LAN 1
ensuite gérer l'adressage, trouver fichier config pour adresser le reseau (192.168.0/24)

```bash
sudo nano /etc/network/interfaces
```

dans le fichier nano il fau ajouter les lignes suivantes

```bash
auto enp0s3
iface enp0s3 inet static
address 192.168.1.5/24
gateway 192.157.1.2
```


et enfin 3e VM qui contient pfsense
