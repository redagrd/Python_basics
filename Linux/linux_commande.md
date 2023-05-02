# Commandes utilisateurs

• Donner les droits sudo a un utilisateur : usermod -aG sudo utilisateur

• Afficher quel utilisateur je suis : whoami

• Donne les informations sur l’utilisateur en cours (uid, gid) : id

• Ajouter un utilisateur : adduser utilisateur

• Modifier un utilisateur : usermod -option(s) utilisateur

• Supprimer un utilisateur : deluser utilisateur

• Supprimer un utilisateur avec son répertoire personnel : deluser -r utilisateur

• Ajouter un(des) groupe(s) : addgroup groupe1 groupe2 groupe3

• Supprimer un groupe : delgroup groupe

• Ajouter un utilisateur à un groupe : adduser utilisateur groupe

• Modifier le groupe propriétaire d’un fichier : chgrp groupe fichier

•Modifier le groupe et le propriétaire d’un fichier : chown propriétaire:group fichier

• Modifier le mot de passe d’un utilisateur : passwd utilisateur

• Désactiver / réactiver un compte : passwd -l utilisateur / passwd -u utilisateur

• Information sur les conditions d’expiration du mot de passe : chage -l utilisateur

• Regarder l’expiration d’un mot de passe et s’il a été changé : chage -l utilisateur

• Demander un nouveau mot de passe pour un utilisateur dans 5 jours : chage -M 5 utilisateur