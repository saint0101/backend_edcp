# backend_edcp
Le projet e-DCP a été lancé en vue de digitaliser les services de l’Autorité de protection et de faciliter ainsi les démarches des entreprises et le suivi de la conformité. A cet effet, une équipe projet a été créée ; cette réunion marque le démarrage de ses activités.

Documentation E-DCP ApiRest
*<img src="images/logo.jpg" width="200" height="200">*

## l'architecture se présente comme suit:

<p align="center">
  <img src="images/architecturetdocker.png">
</p>

### **Response codes**

- ##### **Success**
Code | Reason
---- | ------
`200 - Ok` | Request was successful (processing to recover the resource).
`201 - Ok` | Request was successful (processing to create the resource).

- ##### **Error**
Code | Reason
---- | ------
`400 - Bad Request` | Some content in the request was invalid.
`404 - Not Found` |	The requested resource could not be found.
`424 - Not Found` |	The requested resource could not be processed.
`500 - Internal server error` |	Internal server error.


## Description

Bienvenue dans la documentation E-DCP ApiRest. Cette API fournit des services liés à la gestion des utilisateurs, à l'authentification, aux rôles, aux entreprises, etc.

### URL de base
L'URL de base de tous les points de terminaison de l'API est ` {base url}/edcp/api/v0 `

## 1. Description du point de terminaison

### OBTENIR ` /description `

Obtenez des informations sur l’API E-DCP.

#### Réponse

-   **200 OK**

    jsonCopy code

    ```
    {
      "name": "E-DCP ApiRest",
      "version": "v0",
      "Services":
	      {
	        "Liste des utilisateurs disponibles": "{base url}/edcp/api/v0/users",
	        "Recherche d'utilisateur en fonction de l'id": "{base url}/edcp/api/v0/users/<int:user_id>",
	        "Liste des rôles disponibles": "{base url}/edcp/api/v0/roles",
	        "Liste des Entreprises disponibles": "{base url}/edcp/api/v0/entreprises",
	        "Supprimer un utilisateur avec validation de token": "{base url}/edcp/api/v0/users/<int:user_id>",
	        "Créer un utilisateur": "{base url}/edcp/api/v0/users",
	        "Générer le token d'authentification pour un utilisateur": "{base url}/edcp/api/v0/login",
	        "Récupérer le login de l'utilisateur à partir du token": "{base url}/edcp/api/v0/protected"
	      }
    }
    ```
## 2. Authentification

### 2.1 Générer un jeton

#### POST ` /connexion `

Générez un jeton d'authentification avec un identifiant et un mot de passe valides.

#### Demande
-   Type de contenu : application/json jsonCopy code
	 ```
	 {
		 "login": "example_username", "passwd": "example_password"
	 }
	 ```

#### Réponse

- ** 200 OK **
	- code jsonCopy
`{"access_token": "example_access_token"}`

- ** 401 Non autorisé **
	- code jsonCopy
` { "msg": "Mauvais identifiant ou mot de passe"} `

## 3. Gestion des utilisateurs

### 3.1 Créer un utilisateur

#### POST ` /utilisateurs `

Créez un nouvel utilisateur.
#### Demande
-   Type de contenu : application/json jsonCopy code
```
    {
        "login": "new_username",
        "passwd": "new_password",
        "role_id": 1,
        "avatar": "avatar_url",
        "created": "2023-11 -27",
        "nom": "Nom de l'utilisateur",
        "prenoms": "Prénom de l'utilisateur",
        "Organisation": "Organisation de l'utilisateur",
        "email": "user@example.com ",
        "telephone": " 123456789",
        "fonction": "Fonction utilisateur",
        "consentement": true
     }
   ```
#### Réponse
- ** 201 Créé **
	-  code jsonCopy
` {"status_code": 201, "message": "Utilisateur créé avec succès"} `

- ** 500 Erreur interne du serveur **
	-  code jsonCopy
 ` {"status_code": 500,"error ": "Détails de l'erreur interne du serveur"} `

### 3.2 Obtenir tous les utilisateurs

#### OBTENIR ` /utilisateurs `
Obtenez une liste de tous les utilisateurs disponibles.
#### Réponse
- ** 200 OK **
	-  code jsonCopy
 ```
 {
"status_code": 200,
	"datas": [
				{
					"id": 1,
				    "login": "user1",
				    "role_id": 1,
				    "name": "Dernier utilisateur Name",
				    "prenom": "Prénom de l'utilisateur",
				    "organisation": "Organisation de l'utilisateur",
				    "telephone": "123456789",
				    "fonction": "Fonction utilisateur",
				    "dateCreation": "2023-11-27"
			    },
			    // ... objets utilisateur supplémentaires
		 ]
}
```

- ** 500 Erreur interne du serveur **
	- code jsonCopy
			`{ "status_code": 500,"error": "Détails de l'erreur interne du serveur"}`

### 3.3 Obtenir l'utilisateur par ID

#### GET ` /users/<int:user_id> `
Obtenez les détails de l'utilisateur en fonction de l'ID utilisateur fourni.

#### Réponse

- ** 200 OK **
	-   code jsonCopy
```
{
	"status_code": 200,
	"datas":
		[
			{
				"id": 1,
				"login": "user1",
				"role_id": 1,
				"name": "Dernier utilisateur Name",
				"prenom": "Prénom de l'utilisateur",
				"organisation": "Organisation de l'utilisateur",
				"telephone": "123456789",
				"fonction": "Fonction utilisateur",
				"dateCreation": "2023-11-27"
			}
		]
}
```
 - ** 500 Erreur interne du serveur **
	- code jsonCopy
		` {"status_code": 500,       "error": "Détails de l'erreur interne du serveur"} `

### 3.4 Supprimer un utilisateur

#### SUPPRIMER ` /users/<int:user_id> `

Supprimez un utilisateur en fonction de l'ID utilisateur fourni.

#### Réponse

- ** 200 OK **
	- code jsonCopy
```
	{
		"status_code": 200,
		"message": "Utilisateur supprimé avec succès"
	}
```
- ** 500 Erreur interne du serveur **
	-    code jsonCopy
` {"status_code": 500,"error ": "Détails de l'erreur interne du serveur"} `



## 4. Rôles

### 4.1 Obtenir tous les rôles

#### GET ` /rôles `

Obtenez une liste de tous les rôles disponibles.

#### Réponse

- ** 200 OK **
	- code jsonCopy
```
{
	"status_code": 200,"datas":
	 [
		 {
		 "id": 1,"role": "Admin"},
		 // ... objets de rôle supplémentaires
	 ]
 }
 ```

 - ** 500 Erreur interne du serveur **
	 - Code jsonCopy
	` {"status_code": 500,"error": "Détails de l'erreur interne du serveur"} `

## 5. Entreprises

### 5.1 Obtenir toutes les entreprises

#### GET `/entreprises`

Obtenez une liste de toutes les entreprises disponibles.

#### Réponse

- ** 200 OK **
	- code jsonCopy
 ```
 {
  "status_code": 200,
  "datas":
	   [
		    {
		     "id": 1,
		     "typeClient": "Type 1",
		     "nomRaisonSociale": "Société 1",
		     "présentation" : "Description de l'entreprise",
		     "numRccm": "123456789",
		     "domaine": "Domaine de l'entreprise",
		     "telephone": "987654321",
		     "contactEmail": "company@example.com",
		     " pays": "Pays" ,
		     "ville": "Ville",
		     "localisation": "Location",
		     "gmapsLink": "Google Maps Link",
		     "cateDonnees": "Catégorie de données",
		     "effectif": 100
		    },
	     / / ... société objets supplémentaires
	  ]
}
```

- ** 500 Erreur interne du serveur **
	-  code jsonCopy
 ` {"status_code": 500,"error": "Détails de l'erreur interne du serveur"} `


## 6. Sous-finalités

### 6.1 Obtenir toutes les sous-finalités

#### GET ` /sousfinalite `

Obtenez une liste de toutes les sous-finalités disponibles.

#### Réponse

- ** 200 OK **
	- jsonCopy code
```
{
	"status_code": 200,
	"datas": [
			{
				"id": 1,
				"label": "Subfinality 1",
				"sensible": true,
				"ordre": 1,
				"finalite": "Finality 1",
				"id_finalite": 1
			},
	// ... objets de sous-finalité supplémentaires
	]
}
 ```

-  ** 500 Erreur interne du serveur **
	-  code jsonCopy
```
{
	"status_code": 500,
	"error": "Détails de l'erreur interne du serveur"
}
```

## Remarques

-   Assurez-vous de remplacer ` {base url} ` par l'URL de base réelle de votre API.
-   Pour l'authentification, utilisez le jeton obtenu à partir du point de terminaison de connexion dans l'en-tête Authorization pour les routes protégées.
-   Les dates doivent être au format « AAAA-MM-JJ ».
-   Consulter les réponses pour des informations complémentaires en cas d'erreurs.



## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Authors

  **ARTCI** : `https://artci.ci/`

  **DPDP** : `https://www.autoritedeprotection.ci/`

