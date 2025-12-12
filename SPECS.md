## Règles de sécurité minimales

- JWT (Jetons Web JSON) utilisés pour l'authentification. Chaque requête api nécessitant une authentification doit inclure un JWT valide dans son en-tête d'autorisation.
- Hashing des mots de passe. Les mots de passe ne sont jamais stockés sous forme de texte brut. Ils sont toujours hashés avant d'être stockés dans la base de données.
- CORS (Cross-origin resource sharing) doit être activé pour assurer une gestion correcte des requêtes provenant de différentes origines.
- Utiliser les variables d'environnement pour stocker les informations sensibles (ex. clés API, clés secrètes JWT, informations de connexion à la base de données).
